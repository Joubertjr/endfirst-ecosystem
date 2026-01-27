#!/usr/bin/env python3
from __future__ import annotations

import argparse
import atexit
import datetime as _dt
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional


ROOT_DIR = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT_DIR / "METODO" / "PERSONAS"
OUT_ROOT = ROOT_DIR / "Auditoria"
_LOCK_PATH: Optional[Path] = None
TEMPLATE_PATH = ROOT_DIR / "TEMPLATE_AUDITORIA_CANONICA_DE_PERSONA.md"
CONFIG_PATH = ROOT_DIR / "tools" / "auditoria_personas_config.json"


def load_config() -> dict:
    defaults = {
        "critical_terms": [
            "clareza",
            "viabilidade",
            "evidência",
            "risco",
            "improviso estrutural",
            "fase genérica",
            "lacuna",
        ],
        "markdown": {"ignore_fenced_code_blocks": True},
        "rules": {
            "nao_binario_by_section": True,
            "block3_require_headings": True,
            "block3_min_nonempty_lines_after_heading": 2,
        },
        "inventory_min_files": {"GATES": 3, "EVIDENCIAS_MODELO": 3},
    }
    if not CONFIG_PATH.exists():
        return defaults
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return defaults
        # shallow merge
        out = {**defaults, **data}
        out["markdown"] = {**defaults.get("markdown", {}), **data.get("markdown", {})}
        out["rules"] = {**defaults.get("rules", {}), **data.get("rules", {})}
        if not isinstance(out.get("critical_terms"), list):
            out["critical_terms"] = defaults["critical_terms"]
        return out
    except Exception:
        return defaults


CONFIG = load_config()


def iter_markdown_fenced_code_state(line: str, in_code: bool) -> bool:
    # Toggle em fences do tipo ``` ou ~~~
    if re.match(r"^\s*```", line) or re.match(r"^\s*~~~", line):
        return not in_code
    return in_code


def strip_fenced_code_blocks(lines: list[str]) -> list[str]:
    if not CONFIG.get("markdown", {}).get("ignore_fenced_code_blocks", True):
        return lines
    out: list[str] = []
    in_code = False
    for line in lines:
        # Regra: nunca manter linha de fence (abertura/fechamento) no output.
        is_fence = bool(re.match(r"^\s*```", line) or re.match(r"^\s*~~~", line))
        if is_fence:
            in_code = iter_markdown_fenced_code_state(line, in_code)
            continue
        if in_code:
            continue
        out.append(line)
    return out


def detect_nao_binario_by_section(lines: list[str]) -> Optional[tuple[int, str]]:
    """
    Regra robusta:
      - Se existe seção "Critérios de PASS" e NÃO existe seção "Critérios de FAIL" (ou "Critérios de Reprovação"),
        então é NAO_BINARIO (BAIXA).
    """
    if not CONFIG.get("rules", {}).get("nao_binario_by_section", True):
        return None
    clean = strip_fenced_code_blocks(lines)
    pass_heading_re = re.compile(r"^\s*#{1,6}\s+.*\b[Cc]rit(é|e)rios?\s+de\s+PASS\b")
    fail_heading_re = re.compile(r"^\s*#{1,6}\s+.*\b[Cc]rit(é|e)rios?\s+de\s+(FAIL|REPROVA(Ç|C)ÃO)\b", re.IGNORECASE)
    any_heading_re = re.compile(r"^\s*#{1,6}\s+")

    pass_line: Optional[tuple[int, str]] = None
    pass_idx0: Optional[int] = None
    has_fail_section = False
    for idx0, line in enumerate(clean):
        i = idx0 + 1
        if pass_heading_re.match(line) and pass_line is None:
            pass_line = (i, line.strip()[:200])
            pass_idx0 = idx0
        if fail_heading_re.match(line):
            has_fail_section = True

    if pass_line is None:
        return None
    if has_fail_section:
        return None

    # Se não há seção explícita de FAIL, aceitar se a própria seção de PASS contém
    # tokens claros de FAIL (ex.: "❌", "✅/❌", "FAIL").
    section_lines: list[str] = []
    if pass_idx0 is not None:
        for line in clean[pass_idx0 + 1 :]:
            if any_heading_re.match(line):
                break
            section_lines.append(line)
    section_text = "\n".join(section_lines)
    if re.search(r"\bFAIL\b", section_text) or ("❌" in section_text) or re.search(r"✅\s*/\s*❌", section_text):
        return None

    return pass_line


def _normalize_heading_title(s: str) -> str:
    s = re.sub(r"^\s*#{1,6}\s*", "", s).strip()
    # remover emojis e símbolos comuns
    s = re.sub(r"[✅❌🎯🔒🧬📌📍📖📄📁]", "", s)
    # normalizar espaços e pontuação
    s = re.sub(r"[\t ]+", " ", s)
    s = s.strip(" -—:_")
    return s.lower()


def parse_markdown_sections(lines: list[str]) -> dict[str, tuple[int, list[str]]]:
    """
    Retorna dict: heading_normalizado -> (linha_do_heading, linhas_do_conteudo_ate_proximo_heading)
    """
    clean = strip_fenced_code_blocks(lines)
    sections: dict[str, tuple[int, list[str]]] = {}
    current_key: Optional[str] = None
    current_start_line: Optional[int] = None
    current_content: list[str] = []

    def flush() -> None:
        nonlocal current_key, current_start_line, current_content
        if current_key is not None and current_start_line is not None:
            # manter primeira ocorrência (determinístico)
            if current_key not in sections:
                sections[current_key] = (current_start_line, current_content[:])
        current_key = None
        current_start_line = None
        current_content = []

    for idx0, line in enumerate(clean):
        if re.match(r"^\s*#{1,6}\s+", line):
            flush()
            current_key = _normalize_heading_title(line)
            current_start_line = idx0 + 1
            current_content = []
        else:
            if current_key is not None:
                current_content.append(line)
    flush()
    return sections


REQUIRED_ITEMS = [
    ("DEFINICOES/", "dir", "DEFINICOES"),
    ("PLAYBOOKS/", "dir", "PLAYBOOKS"),
    ("REGRAS/", "dir", "REGRAS"),
    ("GATES/", "dir", "GATES"),
    ("CHECKLISTS/", "dir", "CHECKLISTS"),
    ("EVIDENCIAS_MODELO/", "dir", "EVIDENCIAS_MODELO"),
    ("README.md", "file", "README.md"),
]


REQUIRED_FIELDS = [
    # Para o BLOCO 3 canônico, o modo preferencial é por HEADING (seções reais).
    # patterns aqui ficam como fallback quando config permitir.
    ("Objetivo", [r"\b[Oo]bjetivo\b"]),
    ("Autoridade", [r"\b[Aa]utoridade\b"]),
    ("Responsabilidades", [r"\b[Rr]esponsabilidades\b"]),
    ("Limites", [r"\b[Ll]imites\b"]),
    ("Perguntas canônicas", [r"[Pp]erguntas canônicas"]),
    ("Critérios de PASS", [r"[Cc]ritérios de PASS", r"[Cc]ritério de PASS"]),
    ("Decisões permitidas", [r"[Dd]ecisões permitidas", r"[Dd]ecisão permitida"]),
    ("Decisões proibidas", [r"[Dd]ecisões proibidas", r"[Dd]ecisão proibida"]),
    ("Rastreabilidade", [r"[Rr]astreabilidade"]),
    ("Versionamento", [r"[Vv]ersionamento", r"\b[Vv]ersão:", r"\b[Dd]ata:"]),
]


@dataclass(frozen=True)
class Finding:
    id: str
    severidade: str  # BLOQUEIO|ALTA|MEDIA|BAIXA
    tag: str  # PLACEHOLDER|AMBIGUIDADE|CONTRADICAO|NAO_BINARIO|SEM_RASTREABILIDADE|REFERENCIA_AUSENTE|INCONSISTENCIA_CRUZADA
    arquivo: str
    linha: int
    trecho: str
    regra: str
    correcao: str


def _run_git(args: list[str]) -> str:
    try:
        out = subprocess.check_output(["git", *args], cwd=str(ROOT_DIR), stderr=subprocess.STDOUT)
        return out.decode("utf-8", errors="replace").strip()
    except Exception:
        return ""


def next_audit_dir(out_root: Path) -> Path:
    out_root.mkdir(parents=True, exist_ok=True)
    max_n = 0
    for p in out_root.glob("auditoria-*"):
        m = re.match(r"^auditoria-(\d+)$", p.name)
        if m:
            max_n = max(max_n, int(m.group(1)))
    return out_root / f"auditoria-{max_n + 1}"


def _release_lock() -> None:
    global _LOCK_PATH
    if _LOCK_PATH is not None and _LOCK_PATH.exists():
        try:
            _LOCK_PATH.unlink()
        except OSError:
            pass
        _LOCK_PATH = None


def acquire_audit_lock(out_root: Path) -> None:
    """Trava concorrência: apenas uma execução por vez em out_root."""
    global _LOCK_PATH
    out_root.mkdir(parents=True, exist_ok=True)
    lock_path = out_root / ".lock"
    try:
        fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
        os.write(fd, str(os.getpid()).encode("utf-8"))
        os.close(fd)
        _LOCK_PATH = lock_path
        atexit.register(_release_lock)
    except FileExistsError:
        raise SystemExit(
            f"Auditoria já em execução ou lock órfão em {lock_path}. "
            "Remova o arquivo .lock se não houver outra auditoria rodando."
        )


def copy_source_into_original(aud_dir: Path) -> tuple[Path, str]:
    original_root = aud_dir / "_ORIGINAL"
    dst = original_root / "METODO" / "PERSONAS"
    original_root.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE_DIR, dst, dirs_exist_ok=False)
    cmd = f'cp -a "{SOURCE_DIR}" "{dst}"'
    return dst, cmd


def iter_all_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        # incluir dot-dirs também; ordenação determinística
        dirnames.sort()
        filenames.sort()
        for fn in filenames:
            files.append(Path(dirpath) / fn)
    files.sort()
    return files


def detect_symlinks_in_tree(root: Path) -> list[Path]:
    """Retorna todos os paths sob root que são symlinks (política: não permitidos em _ORIGINAL)."""
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        base = Path(dirpath)
        for name in dirnames + filenames:
            p = base / name
            if p.is_symlink():
                found.append(p)
    return sorted(found)


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_checksums(out_path: Path, files: list[Path], rel_root: Path) -> None:
    lines: list[str] = []
    for f in files:
        rel = f.relative_to(rel_root).as_posix()
        lines.append(f"{sha256_file(f)}  {rel}")
    out_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def tree_like(root: Path) -> str:
    # Implementação interna (não depende de `tree`).
    root = root.resolve()

    def walk(dir_path: Path, prefix: str) -> list[str]:
        entries = sorted(dir_path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
        out: list[str] = []
        for idx, p in enumerate(entries):
            last = idx == len(entries) - 1
            branch = "└── " if last else "├── "
            out.append(f"{prefix}{branch}{p.name}")
            if p.is_dir():
                ext = "    " if last else "│   "
                out.extend(walk(p, prefix + ext))
        return out

    lines = [str(root), *walk(root, "")]
    return "\n".join(lines) + "\n"


def is_persona_dir(p: Path) -> bool:
    """Pasta só é considerada pacote de persona se tiver README.md e todos os itens canônicos (REQUIRED_ITEMS)."""
    if not p.is_dir() or not (p / "README.md").is_file():
        return False
    for _label, kind, name in REQUIRED_ITEMS:
        t = p / name
        if kind == "dir" and not t.is_dir():
            return False
        if kind == "file" and not t.is_file():
            return False
    return True


def persona_packages(personas_root: Path) -> list[Path]:
    """Lista pastas que passam em is_persona_dir (evita docs/README, templates/README como persona)."""
    out: list[Path] = []
    for p in sorted(personas_root.iterdir(), key=lambda x: x.name.lower()):
        if is_persona_dir(p):
            out.append(p)
    return out


def block1_structure(personas_root: Path) -> tuple[bool, str]:
    rows: list[str] = []
    ok_all = True
    rows.append("| Persona | Item obrigatório | Presente? (PASS/FAIL) | Evidência (caminho) |")
    rows.append("|---|---|---|---|")

    for persona_dir in persona_packages(personas_root):
        for label, kind, name in REQUIRED_ITEMS:
            target = persona_dir / name
            present = target.is_dir() if kind == "dir" else target.is_file()
            status = "PASS" if present else "FAIL"
            if not present:
                ok_all = False
            evid = target.as_posix()
            rows.append(f"| {persona_dir.name} | {label} | {status} | `{evid}` |")

    return ok_all, "\n".join(rows) + "\n"


def block2_inventory(personas_root: Path) -> tuple[bool, str]:
    rows: list[str] = []
    ok_all = True
    rows.append("| Pasta | Arquivos encontrados | PASS/FAIL |")
    rows.append("|---|---:|---|")
    min_files = CONFIG.get("inventory_min_files", {}) or {}

    for persona_dir in persona_packages(personas_root):
        for label, kind, name in REQUIRED_ITEMS:
            target = persona_dir / name
            if kind == "file":
                count = 1 if target.is_file() else 0
            else:
                if target.is_dir():
                    count = sum(1 for p in target.rglob("*") if p.is_file())
                else:
                    count = 0
            required_min = 1
            if kind == "dir":
                try:
                    required_min = int(min_files.get(name, 1))
                except Exception:
                    required_min = 1
            status = "PASS" if count >= required_min else "FAIL"
            if status == "FAIL":
                ok_all = False
            rows.append(f"| `{(persona_dir / name).as_posix()}` | {count} | {status} |")

    return ok_all, "\n".join(rows) + "\n"


def first_match_evidence(lines: list[str], patterns: list[str]) -> Optional[tuple[int, str]]:
    for i, line in enumerate(lines, start=1):
        for pat in patterns:
            if re.search(pat, line):
                return i, line.strip()[:200]
    return None


def analyze_file_requirements(path: Path, rel_root: Path) -> tuple[bool, list[tuple[str, str, str]]]:
    # returns: ok, rows(requirement, status, evidence)
    rel = path.relative_to(rel_root).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
    except Exception:
        rows = [(name, "FAIL", "Erro ao ler como UTF-8") for (name, _p) in REQUIRED_FIELDS]
        return False, rows

    ok = True
    rows: list[tuple[str, str, str]] = []

    rules_cfg = CONFIG.get("rules", {}) or {}
    require_headings = bool(rules_cfg.get("block3_require_headings", True))
    # Compat: aceitar tanto min_section_lines (novo) quanto block3_min_nonempty_lines_after_heading (antigo)
    min_nonempty = int(rules_cfg.get("min_section_lines", rules_cfg.get("block3_min_nonempty_lines_after_heading", 1)))
    sections = parse_markdown_sections(lines) if require_headings else {}

    def get_section(keys: list[str]) -> Optional[tuple[int, list[str]]]:
        for k in keys:
            if k in sections:
                return sections[k]
        return None

    def count_nonempty(content: list[str]) -> int:
        return sum(1 for x in content if x.strip())

    def fail(req_name: str, reason: str) -> None:
        nonlocal ok
        ok = False
        rows.append((req_name, "FAIL", reason))

    def pass_(req_name: str, ln: int, heading: str) -> None:
        rows.append((req_name, "PASS", f"Linha {ln}: {heading}"))

    for req, pats in REQUIRED_FIELDS:
        if require_headings:
            if req == "Objetivo":
                sec = get_section(["objetivo"])
                if not sec:
                    fail(req, "Seção 'Objetivo' ausente (heading obrigatório)")
                else:
                    ln, content = sec
                    if count_nonempty(content) < min_nonempty:
                        fail(req, f"Linha {ln}: Seção 'Objetivo' vazia/insuficiente (mín. {min_nonempty} linhas não vazias)")
                    else:
                        pass_(req, ln, "## objetivo")
                continue

            if req == "Autoridade":
                sec = get_section(["autoridade"])
                if not sec:
                    fail(req, "Seção 'Autoridade' ausente (heading obrigatório)")
                else:
                    ln, content = sec
                    if count_nonempty(content) < min_nonempty:
                        fail(req, f"Linha {ln}: Seção 'Autoridade' vazia/insuficiente (mín. {min_nonempty} linhas não vazias)")
                    else:
                        pass_(req, ln, "## autoridade")
                continue

            if req == "Responsabilidades":
                sec = get_section(["responsabilidades"])
                if not sec:
                    fail(req, "Seção 'Responsabilidades' ausente (heading obrigatório)")
                else:
                    ln, content = sec
                    if count_nonempty(content) < min_nonempty:
                        fail(req, f"Linha {ln}: Seção 'Responsabilidades' vazia/insuficiente (mín. {min_nonempty} linhas não vazias)")
                    else:
                        pass_(req, ln, "## responsabilidades")
                continue

            if req == "Limites":
                sec = get_section(["limites"])
                if not sec:
                    fail(req, "Seção 'Limites' ausente (heading obrigatório)")
                else:
                    ln, content = sec
                    if count_nonempty(content) < min_nonempty:
                        fail(req, f"Linha {ln}: Seção 'Limites' vazia/insuficiente (mín. {min_nonempty} linhas não vazias)")
                    else:
                        pass_(req, ln, "## limites")
                continue

            if req == "Perguntas canônicas":
                sec = get_section(["perguntas canônicas", "perguntas canonicas"])
                if not sec:
                    fail(req, "Seção 'Perguntas canônicas' ausente (heading obrigatório)")
                else:
                    ln, content = sec
                    if count_nonempty(content) < min_nonempty:
                        fail(req, f"Linha {ln}: Seção 'Perguntas canônicas' vazia/insuficiente (mín. {min_nonempty} linhas não vazias)")
                    else:
                        pass_(req, ln, "## perguntas canônicas")
                continue

            if req == "Critérios de PASS":
                sec = get_section(["critérios de pass", "criterios de pass"])
                if not sec:
                    fail(req, "Seção 'Critérios de PASS' ausente (heading obrigatório)")
                else:
                    ln, content = sec
                    if count_nonempty(content) < min_nonempty:
                        fail(req, f"Linha {ln}: Seção 'Critérios de PASS' vazia/insuficiente (mín. {min_nonempty} linhas não vazias)")
                    else:
                        pass_(req, ln, "## critérios de pass")
                continue

            if req == "Decisões permitidas":
                sec = get_section(["decisões permitidas", "decisoes permitidas"])
                if not sec:
                    fail(req, "Seção 'Decisões permitidas' ausente (heading obrigatório)")
                else:
                    ln, content = sec
                    if count_nonempty(content) < min_nonempty:
                        fail(req, f"Linha {ln}: Seção 'Decisões permitidas' vazia/insuficiente (mín. {min_nonempty} linhas não vazias)")
                    else:
                        pass_(req, ln, "## decisões permitidas")
                continue

            if req == "Decisões proibidas":
                sec = get_section(["decisões proibidas", "decisoes proibidas"])
                if not sec:
                    fail(req, "Seção 'Decisões proibidas' ausente (heading obrigatório)")
                else:
                    ln, content = sec
                    if count_nonempty(content) < min_nonempty:
                        fail(req, f"Linha {ln}: Seção 'Decisões proibidas' vazia/insuficiente (mín. {min_nonempty} linhas não vazias)")
                    else:
                        pass_(req, ln, "## decisões proibidas")
                continue

            if req == "Rastreabilidade":
                sec = get_section(["rastreabilidade"])
                if not sec:
                    fail(req, "Seção 'Rastreabilidade' ausente (heading obrigatório)")
                else:
                    ln, content = sec
                    content_nonempty = [x for x in content if x.strip()]
                    if len(content_nonempty) < min_nonempty:
                        fail(req, f"Linha {ln}: Seção 'Rastreabilidade' vazia/insuficiente (mín. {min_nonempty} linhas não vazias)")
                    else:
                        text_block = "\n".join(content_nonempty)
                        has_item = bool(re.search(r"(^|\n)\s*[-*]\s+\S", text_block)) or bool(
                            re.search(r"\[[^\]]+\]\([^)]+\)", text_block)
                        ) or bool(re.search(r"https?://", text_block))
                        if not has_item:
                            fail(req, f"Linha {ln}: Seção 'Rastreabilidade' sem itens (exigir lista/link/citação)")
                        else:
                            pass_(req, ln, "## rastreabilidade")
                continue

            if req == "Versionamento":
                sec = get_section(["versionamento"])
                if not sec:
                    fail(req, "Seção 'Versionamento' ausente (heading obrigatório)")
                else:
                    ln, content = sec
                    content_nonempty = [x for x in content if x.strip()]
                    if len(content_nonempty) < min_nonempty:
                        fail(req, f"Linha {ln}: Seção 'Versionamento' vazia/insuficiente (mín. {min_nonempty} linhas não vazias)")
                    else:
                        text_block = "\n".join(content_nonempty)
                        version_re = re.compile(r"\b[Vv]ersão:\s*v?\d+(?:\.\d+)+(?:[-+][0-9A-Za-z\.-]+)?\b")
                        date_re = re.compile(r"\b[Dd]ata:\s*(\d{4}-\d{2}-\d{2})\b")
                        has_version = bool(version_re.search(text_block))
                        has_date = False
                        m = date_re.search(text_block)
                        if m:
                            try:
                                _dt.date.fromisoformat(m.group(1))
                                has_date = True
                            except Exception:
                                has_date = False
                        if not has_version or not has_date:
                            fail(req, f"Linha {ln}: Seção 'Versionamento' inválida (exigir 'Versão: vX.Y' e 'Data: YYYY-MM-DD')")
                        else:
                            pass_(req, ln, "## versionamento")
                continue

        # Fallback (modo antigo) — usado apenas se headings não forem exigidos
        ev = first_match_evidence(lines, pats)
        if ev is None:
            rows.append((req, "FAIL", "Não encontrado"))
            ok = False
        else:
            ln, snippet = ev
            rows.append((req, "PASS", f"Linha {ln}: {snippet}"))

    _ = rel
    return ok, rows


def block3_analysis(md_files: list[Path], rel_root: Path) -> tuple[bool, str, int, list[str]]:
    parts: list[str] = []
    ok_all = True
    fail_files: list[str] = []
    for f in md_files:
        rel = f.relative_to(rel_root).as_posix()
        ok, rows = analyze_file_requirements(f, rel_root)
        if not ok:
            ok_all = False
            fail_files.append(rel)
        parts.append(f"## {rel}\n")
        parts.append("| Requisito obrigatório | PASS/FAIL | Evidência (linha/trecho) |")
        parts.append("|---|---|---|")
        for req, st, ev in rows:
            parts.append(f"| {req} | {st} | {ev} |")
        parts.append(f"\n**Resultado do arquivo:** {'PASS' if ok else 'FAIL'}\n")
        parts.append("---\n")

    parts.append(f"\n**Resultado do bloco 3:** {'PASS' if ok_all else 'FAIL'}\n")
    return ok_all, "\n".join(parts), len(fail_files), fail_files


def find_placeholders(text: str) -> bool:
    return re.search(r"\bTODO\b|\bTBD\b|\bPLACEHOLDER\b|\ba definir\b|\bto be defined\b", text, re.IGNORECASE) is not None


def find_ambiguity(text: str) -> bool:
    return re.search(r"\btalvez\b|\bprovavelmente\b|\bpossivelmente\b|\bgeralmente\b|\bnormalmente\b|\bpode ser\b|\bdeveria\b|\bseria bom\b", text, re.IGNORECASE) is not None


def iter_markdown_links(line: str) -> Iterable[str]:
    for m in re.findall(r"\[[^\]]*\]\(([^)]+)\)", line):
        yield m


def block4_scan(all_files: list[Path], rel_root: Path) -> tuple[bool, list[Finding]]:
    findings: list[Finding] = []
    counter = 1

    def add(sev: str, tag: str, arquivo: str, linha: int, trecho: str, regra: str, correcao: str) -> None:
        nonlocal counter
        findings.append(
            Finding(
                id=f"ACHADO-{counter:03d}",
                severidade=sev,
                tag=tag,
                arquivo=arquivo,
                linha=linha,
                trecho=trecho,
                regra=regra,
                correcao=correcao,
            )
        )
        counter += 1

    for f in all_files:
        rel = f.relative_to(rel_root).as_posix()
        try:
            lines = f.read_text(encoding="utf-8", errors="strict").splitlines()
            text = "\n".join(lines)
        except Exception:
            add(
                "ALTA",
                "INCONSISTENCIA_CRUZADA",
                rel,
                0,
                "(arquivo não é texto UTF-8)",
                "Artefatos de auditoria devem ser auditáveis como texto",
                "Remover arquivo binário/ilegível ou convertê-lo para texto auditável",
            )
            continue

        # Varredura linha a linha (com suporte a ignorar blocos de código)
        in_code = False
        for i, line in enumerate(lines, start=1):
            in_code = iter_markdown_fenced_code_state(line, in_code)
            if in_code and CONFIG.get("markdown", {}).get("ignore_fenced_code_blocks", True):
                continue

            # Placeholders
            if re.search(r"\bTODO\b|\bTBD\b|\bPLACEHOLDER\b|\ba definir\b|\bto be defined\b", line, re.IGNORECASE):
                add(
                    "BLOQUEIO",
                    "PLACEHOLDER",
                    rel,
                    i,
                    line.strip()[:200],
                    "Artefatos não podem conter placeholders",
                    "Substituir placeholder por conteúdo real",
                )

            # Ambiguidade
            # Regra: ignorar exemplos negativos/advertências explícitas
            if re.search(r"\b(talvez|provavelmente|possivelmente|geralmente|normalmente|pode ser|deveria|seria bom)\b", line, re.IGNORECASE):
                if re.search(r"\b(não deve|nao deve|evitar|exemplo de erro|exemplo negativo|anti-?exemplo|contra-?exemplo)\b", line, re.IGNORECASE):
                    continue
                add(
                    "MEDIA",
                    "AMBIGUIDADE",
                    rel,
                    i,
                    line.strip()[:200],
                    "Critérios devem ser objetivos e verificáveis",
                    "Substituir termo subjetivo por critério objetivo",
                )

            # Referências ausentes (links locais quebrados)
            for link in iter_markdown_links(line):
                if link.startswith("http") or link.startswith("#"):
                    continue
                # remover âncoras
                link_path = link.split("#", 1)[0]
                if not link_path:
                    continue
                candidate = (f.parent / link_path).resolve()
                try:
                    candidate.relative_to(rel_root.resolve())
                except Exception:
                    # fora do escopo copiado
                    add(
                        "ALTA",
                        "REFERENCIA_AUSENTE",
                        rel,
                        i,
                        f"Link: {link}",
                        "Referências devem apontar para arquivos existentes no pacote auditado",
                        "Corrigir o link para apontar para arquivo existente no pacote auditado",
                    )
                    continue
                if not candidate.exists():
                    add(
                        "ALTA",
                        "REFERENCIA_AUSENTE",
                        rel,
                        i,
                        f"Link: {link}",
                        "Referências devem apontar para arquivos existentes",
                        "Criar o arquivo referenciado ou corrigir a referência",
                    )

        # Não-binariedade (robusta por seção, não por linha)
        if f.suffix.lower() == ".md":
            nb = detect_nao_binario_by_section(lines)
            if nb is not None:
                ln, snippet = nb
                add(
                    "BAIXA",
                    "NAO_BINARIO",
                    rel,
                    ln,
                    snippet,
                    "Critérios devem ser binários (PASS/FAIL) por seção",
                    "Adicionar seção 'Critérios de FAIL' (ou 'Critérios de Reprovação') correspondente",
                )

    any_bloqueio = any(a.severidade == "BLOQUEIO" for a in findings)
    return (not any_bloqueio), findings


def detect_contradictions(md_files: list[Path], rel_root: Path, start_counter: int) -> list[Finding]:
    """
    Regra mínima (eficaz e determinística):
      - Extrair bullets da seção "Decisões permitidas" e "Decisões proibidas"
      - Se uma mesma ação (linha normalizada) aparece em ambos (mesmo ou outro arquivo), registrar CONTRADICAO (ALTA)
    """
    counter = start_counter
    findings: list[Finding] = []

    def norm_action(s: str) -> str:
        s = s.strip()
        s = re.sub(r"^\s*[-*]\s+", "", s)
        s = re.sub(r"^\s*\d+\.\s+", "", s)
        s = re.sub(r"^\s*-\s*\[[ xX]\]\s+", "", s)
        s = s.lower()
        s = re.sub(r"[`*_]", "", s)
        s = re.sub(r"\s+", " ", s).strip()
        return s

    permitted: dict[str, tuple[str, int]] = {}
    prohibited: dict[str, tuple[str, int]] = {}

    for f in md_files:
        rel = f.relative_to(rel_root).as_posix()
        try:
            lines = f.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue
        sections = parse_markdown_sections(lines)
        perm = sections.get("decisões permitidas") or sections.get("decisoes permitidas")
        prohib = sections.get("decisões proibidas") or sections.get("decisoes proibidas")
        for sec, store in [(perm, permitted), (prohib, prohibited)]:
            if not sec:
                continue
            heading_ln, content = sec
            for idx, line in enumerate(content, start=heading_ln + 1):
                if (
                    re.match(r"^\s*[-*]\s+\S", line)
                    or re.match(r"^\s*\d+\.\s+\S", line)
                    or re.match(r"^\s*-\s*\[[ xX]\]\s+\S", line)
                ):
                    k = norm_action(line)
                    if k and k not in store:
                        store[k] = (rel, idx)

    overlaps = sorted(set(permitted.keys()) & set(prohibited.keys()))
    for k in overlaps:
        p_file, p_ln = permitted[k]
        b_file, b_ln = prohibited[k]
        findings.append(
            Finding(
                id=f"ACHADO-{counter:03d}",
                severidade="ALTA",
                tag="CONTRADICAO",
                arquivo=f"{p_file} | {b_file}",
                linha=0,
                trecho=f"Ação conflitante: {k}",
                regra="A mesma ação não pode ser simultaneamente permitida e proibida",
                correcao=f"Remover/ajustar a ação em um dos lados (permitido/proibido) para eliminar a contradição",
            )
        )
        counter += 1

    return findings


def write_findings(out_path: Path, findings: list[Finding]) -> None:
    parts: list[str] = []
    parts.append("BLOCO 4 — VARREDURA DE FALHAS\n")
    if not findings:
        parts.append("Resultado do bloco 4: PASS / FAIL\n")
        out_path.write_text("\n".join(parts), encoding="utf-8")
        return

    for a in findings:
        parts.append(a.id)
        parts.append(f"Severidade: {a.severidade}")
        parts.append(f"Tag: {a.tag}")
        parts.append(f"{a.arquivo}:{a.linha}")
        parts.append(a.trecho)
        parts.append(a.regra)
        parts.append(a.correcao)
        parts.append("")  # blank line

    any_bloqueio = any(a.severidade == "BLOQUEIO" for a in findings)
    parts.append(f"Resultado do bloco 4: {'FAIL' if any_bloqueio else 'PASS'}\n")
    out_path.write_text("\n".join(parts), encoding="utf-8")


def block5_cross(personas_root: Path) -> tuple[bool, str]:
    rows: list[str] = []
    ok_all = True
    rows.append("| Cruzamento | PASS/FAIL | Evidência |")
    rows.append("|---|---|---|")

    termos_criticos = list(CONFIG.get("critical_terms", []))

    # Termos críticos definidos (em qualquer DEFINICOES dentro do pacote)
    definicoes_text = ""
    for p in personas_root.rglob("DEFINICOES"):
        if p.is_dir():
            for f in p.rglob("*.md"):
                try:
                    definicoes_text += f.read_text(encoding="utf-8", errors="ignore").lower() + "\n"
                except Exception:
                    pass

    termos_ok = True
    faltantes = [t for t in termos_criticos if re.search(rf"{re.escape(t)}\s*[:—-]", definicoes_text) is None]
    if faltantes:
        termos_ok = False
        ok_all = False
        rows.append(f"| Termos críticos definidos | FAIL | Faltando definição objetiva: {', '.join(faltantes)} |")
    else:
        rows.append("| Termos críticos definidos | PASS | Definições detectadas para termos críticos |")

    # Templates citados existem fisicamente (somente referência EXPLÍCITA: modelo_<id>)
    # Regra: só auditar referências do padrão `modelo_<id>` (não plural "modelos", não frases genéricas).
    refs_ausentes: list[str] = []
    for f in personas_root.rglob("*.md"):
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        # resolver persona_dir do arquivo (subdir direto contendo README.md)
        persona_dir = None
        for p in f.parents:
            if p.parent == personas_root and (p / "README.md").is_file():
                persona_dir = p
                break
        if persona_dir is None:
            continue
        for m in re.findall(r"\bmodelo_([a-z0-9_]+)\b", content, re.IGNORECASE):
            cand = persona_dir / "EVIDENCIAS_MODELO" / f"modelo_{m}.md"
            if not cand.exists():
                refs_ausentes.append(cand.relative_to(personas_root).as_posix())
    if refs_ausentes:
        ok_all = False
        rows.append(f"| Templates citados existem fisicamente | FAIL | Ausentes: {', '.join(sorted(set(refs_ausentes))[:10])} |")
    else:
        rows.append("| Templates citados existem fisicamente | PASS | Nenhuma referência explícita `modelo_<id>` ausente detectada |")

    # Cruzamentos por persona: checar se links para GATES em PLAYBOOKS/CHECKLISTS existem
    for persona_dir in persona_packages(personas_root):
        # Gates citados por nome de arquivo também devem existir (ex.: CEO_GATES.md)
        gates_dir = persona_dir / "GATES"
        gates_files = set()
        if gates_dir.is_dir():
            for gf in gates_dir.rglob("*.md"):
                gates_files.add(gf.name.lower())

        for kind, dir_name in [("Playbook ↔ Gates", "PLAYBOOKS"), ("Checklist ↔ Gates", "CHECKLISTS")]:
            broken: list[str] = []
            base = persona_dir / dir_name
            if base.is_dir():
                for f in base.rglob("*.md"):
                    try:
                        raw_lines = f.read_text(encoding="utf-8", errors="ignore").splitlines()
                    except Exception:
                        continue
                    lines = strip_fenced_code_blocks(raw_lines)
                    for i, line in enumerate(lines, start=1):
                        # Referência textual a *_GATES.md
                        for m in re.findall(r"\b([A-Z0-9_]+_GATES\.md)\b", line):
                            if m.lower() not in gates_files:
                                broken.append(f"{f.relative_to(personas_root).as_posix()}:{i} -> {m}")
                        for link in iter_markdown_links(line):
                            if "GATES" not in link and "gates" not in link:
                                continue
                            link_path = link.split("#", 1)[0]
                            if not link_path or link_path.startswith("http") or link_path.startswith("#"):
                                continue
                            cand = (f.parent / link_path).resolve()
                            if not cand.exists():
                                broken.append(f"{f.relative_to(personas_root).as_posix()}:{i} -> {link}")
            status = "PASS" if not broken else "FAIL"
            if broken:
                ok_all = False
                rows.append(f"| {persona_dir.name}: {kind} | FAIL | Links quebrados: {broken[0]} |")
            else:
                rows.append(f"| {persona_dir.name}: {kind} | PASS | Sem links locais quebrados para GATES detectados |")

        # Definição ↔ Regras: links para REGRAS em DEFINICOES existem
        broken_def: list[str] = []
        defin_dir = persona_dir / "DEFINICOES"
        if defin_dir.is_dir():
            for f in defin_dir.rglob("*.md"):
                try:
                    raw_lines = f.read_text(encoding="utf-8", errors="ignore").splitlines()
                except Exception:
                    continue
                lines = strip_fenced_code_blocks(raw_lines)
                for i, line in enumerate(lines, start=1):
                    for link in iter_markdown_links(line):
                        if "REGRAS" not in link and "regras" not in link:
                            continue
                        link_path = link.split("#", 1)[0]
                        if not link_path or link_path.startswith("http") or link_path.startswith("#"):
                            continue
                        cand = (f.parent / link_path).resolve()
                        if not cand.exists():
                            broken_def.append(f"{f.relative_to(personas_root).as_posix()}:{i} -> {link}")
        if broken_def:
            ok_all = False
            rows.append(f"| {persona_dir.name}: Definição ↔ Regras | FAIL | Links quebrados: {broken_def[0]} |")
        else:
            rows.append(f"| {persona_dir.name}: Definição ↔ Regras | PASS | Sem links locais quebrados para REGRAS detectados |")

    return ok_all, "\n".join(rows) + "\n"


def write_manifesto(
    out_path: Path,
    when: str,
    auditor: str,
    metodo: str,
    fonte: str,
    commit_repo: str,
    personas: list[str],
    arquivos_md_total: int,
    findings: list[Finding],
    bloco0: bool,
    bloco1: bool,
    bloco2: bool,
    bloco3: bool,
    bloco4: bool,
    bloco5: bool,
    bloco3_fail_count: int,
    bloco3_fail_files: list[str],
) -> None:
    bloqueios = sum(1 for a in findings if a.severidade == "BLOQUEIO")
    altas = sum(1 for a in findings if a.severidade == "ALTA")
    medias = sum(1 for a in findings if a.severidade == "MEDIA")
    baixas = sum(1 for a in findings if a.severidade == "BAIXA")

    final_fail = (not bloco0) or (not bloco1) or (not bloco2) or (not bloco3) or (not bloco5) or (bloqueios > 0)
    status_final = "FAIL" if final_fail else "PASS"
    status_emoji = "❌" if status_final == "FAIL" else "✅"

    parts: list[str] = []
    parts.append("# MANIFESTO DE AUDITORIA — PERSONAS\n\n")
    parts.append(f"**Data:** {when}  \n")
    parts.append(f"**Auditor:** {auditor}  \n")
    parts.append(f"**Método:** {metodo}  \n")
    parts.append(f"**Fonte:** {fonte}  \n")
    parts.append(f"**Commit/Repo:** {commit_repo}  \n\n")
    parts.append("---\n\n")
    parts.append("## VEREDITO FINAL\n\n")
    parts.append(f"**{status_emoji} {status_final}**\n\n")
    parts.append("---\n\n")
    parts.append("## ESTATÍSTICAS\n\n")
    parts.append("| Métrica | Valor |\n")
    parts.append("|---------|-------|\n")
    parts.append(f"| Personas auditadas | {len(personas)} ({', '.join(personas)}) |\n")
    parts.append(f"| Arquivos auditados | {arquivos_md_total} |\n")
    parts.append(f"| Total de achados | {len(findings)} |\n")
    parts.append(f"| **BLOQUEIOS** | **{bloqueios}** |\n")
    parts.append(f"| ALTAS | {altas} |\n")
    parts.append(f"| MÉDIAS | {medias} |\n")
    parts.append(f"| BAIXAS | {baixas} |\n\n")
    parts.append("---\n\n")
    parts.append("## BLOCOS EXECUTADOS\n\n")
    parts.append("| Bloco | Descrição | Resultado |\n")
    parts.append("|-------|-----------|-----------|\n")
    parts.append(f"| BLOCO 0 | Provas de Reprodução | {'✅ PASS' if bloco0 else '❌ FAIL'} |\n")
    parts.append(f"| BLOCO 1 | Estrutura | {'✅ PASS' if bloco1 else '❌ FAIL'} |\n")
    parts.append(f"| BLOCO 2 | Inventário de Arquivos | {'✅ PASS' if bloco2 else '❌ FAIL'} |\n")
    parts.append(f"| BLOCO 3 | Conteúdo por Arquivo | {'✅ PASS' if bloco3 else f'❌ FAIL ({bloco3_fail_count} arquivos FAIL)'} |\n")
    parts.append(f"| BLOCO 4 | Varredura de Falhas | {'✅ PASS' if bloco4 else f'❌ FAIL ({bloqueios} BLOQUEIOS)'} |\n")
    parts.append(f"| BLOCO 5 | Consistência Cruzada | {'✅ PASS' if bloco5 else '❌ FAIL'} |\n")
    parts.append(f"| BLOCO 6 | Veredito Final | {status_emoji} {status_final} |\n")
    parts.append(f"| BLOCO 7 | Templateabilidade | {'❌ NÃO' if status_final == 'FAIL' else '✅ SIM'} |\n")
    parts.append("| BLOCO 8 | Ações | Listadas abaixo |\n\n")
    parts.append("---\n\n")
    parts.append("## PRINCIPAIS BLOQUEIOS\n\n")
    bloqueios_list = [a for a in findings if a.severidade == "BLOQUEIO"][:5]
    if not bloqueios_list:
        parts.append("Nenhum.\n\n")
    else:
        for idx, a in enumerate(bloqueios_list, start=1):
            parts.append(f"{idx}. **{a.id}:** {a.tag} em `{a.arquivo}:{a.linha}`\n")
        parts.append("\n")
    parts.append("---\n\n")
    parts.append("## TOP 5 ACHADOS (POR SEVERIDADE)\n\n")
    order = {"BLOQUEIO": 0, "ALTA": 1, "MEDIA": 2, "BAIXA": 3}
    top = sorted(findings, key=lambda x: (order.get(x.severidade, 99), x.id))[:5]
    if not top:
        parts.append("Nenhum.\n\n")
    else:
        for a in top:
            parts.append(f"- **{a.id}** ({a.severidade}/{a.tag}) — `{a.arquivo}:{a.linha}`\n")
        parts.append("\n")
    parts.append("---\n\n")
    parts.append("## FALHAS PRINCIPAIS\n\n")
    if bloco3_fail_files:
        parts.append("### BLOCO 3 (Conteúdo por Arquivo)\n")
        parts.append(f"- **{bloco3_fail_count} arquivos** sem todos os requisitos obrigatórios\n")
        parts.append("- Arquivos afetados:\n")
        for f in bloco3_fail_files[:20]:
            parts.append(f"  - {f}\n")
        parts.append("\n")
    parts.append("### BLOCO 4 (Varredura de Falhas)\n")
    parts.append(f"- **{bloqueios} BLOQUEIOS**\n")
    parts.append(f"- **{medias} MÉDIAS**\n")
    parts.append(f"- **{baixas} BAIXAS**\n\n")
    parts.append("---\n\n")
    parts.append("## ENTREGÁVEIS\n\n")
    parts.append("Checksums em `01_CHECKSUMS_VERIFICAVEIS.txt` são relativos à raiz da cópia auditada: `_ORIGINAL/METODO/PERSONAS`.\n\n")
    parts.append("✅ 00_MANIFESTO.md  \n")
    parts.append("✅ 01_CHECKSUMS_VERIFICAVEIS.txt  \n")
    parts.append("✅ 02_ESTRUTURA_COMPLETA.txt  \n")
    parts.append("✅ 03_RELATORIO_EXECUTIVO.md  \n")
    parts.append("✅ 04_ANALISE_DETALHADA_POR_ARQUIVO.md  \n")
    parts.append("✅ 05_FALHAS_IDENTIFICADAS.md  \n")
    parts.append("✅ 06_CONSISTENCIA_CRUZADA.md  \n")
    parts.append("✅ 07_RECOMENDACOES_ACAO.md  \n")
    parts.append("✅ 08_AMBIENTE.txt  \n")
    parts.append("✅ _ORIGINAL/ (cópia integral da fonte auditada)  \n\n")
    parts.append("---\n\n")
    parts.append(f"**Status:** {status_emoji} {'REPROVADO' if status_final == 'FAIL' else 'APROVADO'}  \n")
    motivo_parts: list[str] = []
    if bloqueios > 0:
        motivo_parts.append(f"{bloqueios} BLOQUEIOS")
    if not bloco1:
        motivo_parts.append("BLOCO 1 FAIL")
    if not bloco2:
        motivo_parts.append("BLOCO 2 FAIL")
    if not bloco3:
        motivo_parts.append("BLOCO 3 FAIL")
    if not bloco5:
        motivo_parts.append("BLOCO 5 FAIL")
    if motivo_parts:
        parts.append(f"**Motivo:** {' + '.join(motivo_parts)}  \n")
    parts.append("**Próxima ação:** " + ("Corrigir bloqueios e falhas identificadas" if status_final == "FAIL" else "Nenhuma") + "\n")

    out_path.write_text("".join(parts), encoding="utf-8")


def write_executive(
    out_path: Path,
    cmd_copia: str,
    bloco0: bool,
    bloco1: bool,
    bloco2: bool,
    bloco3: bool,
    bloco4: bool,
    bloco5: bool,
    findings: list[Finding],
    aud_dir: Path,
    original_root: Path,
) -> None:
    bloqueios = sum(1 for a in findings if a.severidade == "BLOQUEIO")
    altas = sum(1 for a in findings if a.severidade == "ALTA")
    medias = sum(1 for a in findings if a.severidade == "MEDIA")
    baixas = sum(1 for a in findings if a.severidade == "BAIXA")

    final_fail = (not bloco0) or (not bloco1) or (not bloco2) or (not bloco3) or (not bloco5) or (bloqueios > 0)
    status_final = "FAIL" if final_fail else "PASS"

    parts: list[str] = []

    parts.append("BLOCO 0 — PROVAS DE REPRODUÇÃO (BLOQUEANTE)\n")
    parts.append(f"Comando de captura/cópia da fonte auditada (para _ORIGINAL/):\n\n`{cmd_copia}`\n")
    parts.append(f"Fonte auditada (copiada): `{original_root.relative_to(aud_dir).as_posix()}`\n")
    parts.append(f"Estrutura completa (tree): `02_ESTRUTURA_COMPLETA.txt`\n")
    parts.append(f"Checksums SHA256: `01_CHECKSUMS_VERIFICAVEIS.txt`\n")
    parts.append(f"Resultado do bloco 0: {'PASS' if bloco0 else 'FAIL'}\n")
    parts.append("\n⸻\n")

    parts.append("BLOCO 1 — ESTRUTURA (BINÁRIO)\n\n")
    parts.append("Tabela:\n\n")
    # a tabela detalhada fica em 06? Não. Colocar aqui é ok.
    parts.append("Resultado do bloco 1: " + ("PASS" if bloco1 else "FAIL") + "\n")
    parts.append("\n⸻\n")

    parts.append("BLOCO 2 — INVENTÁRIO DE ARQUIVOS\n\n")
    parts.append("Resultado do bloco 2: " + ("PASS" if bloco2 else "FAIL") + "\n")
    parts.append("\n⸻\n")

    parts.append("BLOCO 3 — CONTEÚDO POR ARQUIVO (LINHA A LINHA)\n\n")
    parts.append("Resultado do bloco 3: " + ("PASS" if bloco3 else "FAIL") + "\n")
    parts.append("\n⸻\n")

    parts.append("BLOCO 4 — VARREDURA DE FALHAS\n\n")
    parts.append("Resultado do bloco 4: " + ("PASS" if bloco4 else "FAIL") + "\n")
    parts.append("\n⸻\n")

    parts.append("BLOCO 5 — CONSISTÊNCIA CRUZADA\n\n")
    parts.append("Resultado do bloco 5: " + ("PASS" if bloco5 else "FAIL") + "\n")
    parts.append("\n⸻\n")

    parts.append("BLOCO 6 — VEREDITO FINAL\n\n")
    parts.append("Reportar:\n")
    parts.append(f"\t•\tQuantidade de BLOQUEIOS: {bloqueios}\n")
    parts.append(f"\t•\tQuantidade de ALTAS: {altas}\n")
    parts.append(f"\t•\tQuantidade de MÉDIAS: {medias}\n")
    parts.append(f"\t•\tQuantidade de BAIXAS: {baixas}\n\n")
    parts.append(f"Status final: {status_final}\n")

    # Top achados (contexto mínimo)
    order = {"BLOQUEIO": 0, "ALTA": 1, "MEDIA": 2, "BAIXA": 3}
    top = sorted(findings, key=lambda x: (order.get(x.severidade, 99), x.id))[:5]
    parts.append("\n⸻\n")
    parts.append("TOP 5 ACHADOS (POR SEVERIDADE)\n")
    if not top:
        parts.append("Nenhum.\n")
    else:
        for a in top:
            parts.append(f"- {a.id} | {a.severidade} | {a.tag} | {a.arquivo}:{a.linha}\n")

    out_path.write_text("".join(parts), encoding="utf-8")


def write_actions(out_path: Path, findings: list[Finding]) -> None:
    actions: list[str] = []
    seen: set[str] = set()
    for f in findings:
        a = f.correcao.strip()
        if a and a not in seen:
            seen.add(a)
            actions.append(a)
    parts: list[str] = []
    parts.append("BLOCO 8 — AÇÕES\n\n")
    parts.append("Listar somente ações objetivas, sem explicação:\n")
    if not actions:
        parts.append("1.\n")
    else:
        for i, a in enumerate(actions, start=1):
            parts.append(f"{i}.\t{a}\n")
    out_path.write_text("".join(parts), encoding="utf-8")


def write_08_ambiente(out_path: Path) -> None:
    """Grava metadata de ambiente para reprodutibilidade: python, uname, git status, git HEAD."""
    lines: list[str] = []
    lines.append("python --version")
    try:
        out = subprocess.check_output(
            [sys.executable, "--version"], stderr=subprocess.STDOUT, timeout=5
        )
        lines.append(out.decode("utf-8", errors="replace").strip())
    except Exception:
        lines.append("(não obtido)")
    lines.append("")
    lines.append("uname -a")
    try:
        u = platform.uname()
        lines.append(f"{u.system} {u.node} {u.release} {u.version} {u.machine}")
    except Exception:
        lines.append("(não obtido)")
    lines.append("")
    lines.append("git rev-parse HEAD")
    lines.append(_run_git(["rev-parse", "HEAD"]) or "(sem git)")
    lines.append("")
    lines.append("git status --porcelain")
    lines.append(_run_git(["status", "--porcelain"]) or "(working tree clean)")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Auditoria canônica de personas (fonte: METODO/PERSONAS/, saída: Auditoria/auditoria-N/)"
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        metavar="DIR",
        help="Pasta onde criar auditoria-N (default: Auditoria/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Só validar e mostrar o que faria, sem escrever arquivos",
    )
    args = parser.parse_args()

    out_root = args.out.resolve() if args.out else OUT_ROOT

    # Fail-fast: prints iniciais
    print(f"ROOT_DIR={ROOT_DIR}")
    print(f"SOURCE_DIR={SOURCE_DIR}")
    print(f"OUT_ROOT={out_root}")

    if not SOURCE_DIR.exists():
        raise SystemExit(
            f"Fonte não encontrada: {SOURCE_DIR}\n"
            "Rode na raiz do repositório: make auditoria"
        )

    aud_dir = next_audit_dir(out_root)
    print(f"auditoria-N={aud_dir.name}")

    if args.dry_run:
        print("[DRY-RUN] Validando persona_packages em METODO/PERSONAS/...")
        # Personas em SOURCE_DIR para dry-run (ainda não copiamos)
        _personas_root = SOURCE_DIR
        _dirs = persona_packages(_personas_root)
        if not _dirs:
            raise SystemExit(
                "Nenhuma persona válida encontrada em METODO/PERSONAS/. "
                "Cada persona deve ter README.md e os itens: DEFINICOES/, PLAYBOOKS/, REGRAS/, GATES/, CHECKLISTS/, EVIDENCIAS_MODELO/."
            )
        print(f"[DRY-RUN] Seriam auditadas {len(_dirs)} personas: {[d.name for d in _dirs]}")
        print(f"[DRY-RUN] Saída em: {aud_dir}")
        return 0

    acquire_audit_lock(out_root)
    try:
        aud_dir.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        _release_lock()
        raise SystemExit(f"Pasta já existe: {aud_dir}")
    (aud_dir / "_ORIGINAL").mkdir(parents=True, exist_ok=True)

    copied_root, cmd = copy_source_into_original(aud_dir)
    personas_root = copied_root

    # 02 estrutura (tree -a equivalente)
    (aud_dir / "02_ESTRUTURA_COMPLETA.txt").write_text(tree_like(copied_root), encoding="utf-8")

    # 01 checksums
    files = iter_all_files(copied_root)
    write_checksums(aud_dir / "01_CHECKSUMS_VERIFICAVEIS.txt", files, copied_root)

    # 08 ambiente (reprodutibilidade)
    write_08_ambiente(aud_dir / "08_AMBIENTE.txt")

    bloco0_pass = True

    # BLOCO 1
    b1_pass, b1_table = block1_structure(personas_root)

    # BLOCO 2
    b2_pass, b2_table = block2_inventory(personas_root)

    # BLOCO 3 (somente arquivos .md dentro dos pacotes de persona)
    persona_dirs = persona_packages(personas_root)
    if not persona_dirs:
        _release_lock()
        raise SystemExit(
            "Nenhuma persona válida encontrada em METODO/PERSONAS/. "
            "Cada persona deve ter README.md e os itens: DEFINICOES/, PLAYBOOKS/, REGRAS/, GATES/, CHECKLISTS/, EVIDENCIAS_MODELO/."
        )
    md_files: list[Path] = []
    for p in files:
        if p.suffix.lower() != ".md":
            continue
        if any(str(p).startswith(str(d) + os.sep) for d in persona_dirs):
            md_files.append(p)
    b3_pass, b3_report, b3_fail_count, b3_fail_files = block3_analysis(md_files, copied_root)
    (aud_dir / "04_ANALISE_DETALHADA_POR_ARQUIVO.md").write_text(b3_report, encoding="utf-8")

    # BLOCO 4
    # Tudo que é "arquivo auditado" usa root = copied_root para caminhos relativos consistentes
    b4_pass, findings = block4_scan(files, copied_root)
    # Contradições mínimas (permitido vs proibido)
    findings.extend(detect_contradictions(md_files, copied_root, start_counter=len(findings) + 1))
    # Symlinks em _ORIGINAL: política de reprodutibilidade (ALTA)
    _next_id = len(findings) + 1
    for sym in detect_symlinks_in_tree(copied_root):
        rel = sym.relative_to(copied_root).as_posix()
        findings.append(
            Finding(
                id=f"ACHADO-{_next_id}",
                severidade="ALTA",
                tag="SYMLINK",
                arquivo=rel,
                linha=0,
                trecho=rel,
                regra="Não deve haver symlinks em _ORIGINAL (reprodutibilidade)",
                correcao="Substituir symlink por cópia real ou remover",
            )
        )
        _next_id += 1
    write_findings(aud_dir / "05_FALHAS_IDENTIFICADAS.md", findings)

    # BLOCO 5
    b5_pass, b5_table = block5_cross(personas_root)
    (aud_dir / "06_CONSISTENCIA_CRUZADA.md").write_text("BLOCO 5 — CONSISTÊNCIA CRUZADA\n\n" + b5_table, encoding="utf-8")

    # 03 executivo (inclui tabelas de bloco 1/2 e status)
    exec_path = aud_dir / "03_RELATORIO_EXECUTIVO.md"
    write_executive(
        exec_path,
        cmd_copia=cmd,
        bloco0=bloco0_pass,
        bloco1=b1_pass,
        bloco2=b2_pass,
        bloco3=b3_pass,
        bloco4=b4_pass,
        bloco5=b5_pass,
        findings=findings,
        aud_dir=aud_dir,
        original_root=copied_root,
    )

    # Injetar tabelas de bloco 1/2 dentro do executivo (sem reescrever lógica)
    exec_txt = exec_path.read_text(encoding="utf-8")
    exec_txt = exec_txt.replace(
        "BLOCO 1 — ESTRUTURA (BINÁRIO)\n\nTabela:\n\nResultado do bloco 1:",
        "BLOCO 1 — ESTRUTURA (BINÁRIO)\n\nTabela:\n\n" + b1_table + "\nResultado do bloco 1:",
    )
    exec_txt = exec_txt.replace(
        "BLOCO 2 — INVENTÁRIO DE ARQUIVOS\n\nResultado do bloco 2:",
        "BLOCO 2 — INVENTÁRIO DE ARQUIVOS\n\nTabela obrigatória:\n\n" + b2_table + "\nResultado do bloco 2:",
    )
    exec_path.write_text(exec_txt, encoding="utf-8")

    # 00 manifesto (formato robusto de auditoria)
    personas = [p.name for p in persona_dirs]
    commit_short = _run_git(["rev-parse", "--short", "HEAD"]) or "(sem git)"
    repo_url = _run_git(["config", "--get", "remote.origin.url"]).strip() or "repo local"
    write_manifesto(
        aud_dir / "00_MANIFESTO.md",
        when=_dt.date.today().isoformat(),
        auditor="AUTOMACAO",
        metodo="END-FIRST",
        fonte="METODO/PERSONAS/ (cópia em _ORIGINAL/)",
        commit_repo=f"{repo_url} @ {commit_short}",
        personas=personas,
        arquivos_md_total=len(md_files),
        findings=findings,
        bloco0=bloco0_pass,
        bloco1=b1_pass,
        bloco2=b2_pass,
        bloco3=b3_pass,
        bloco4=b4_pass,
        bloco5=b5_pass,
        bloco3_fail_count=b3_fail_count,
        bloco3_fail_files=b3_fail_files,
    )

    # 07 ações
    write_actions(aud_dir / "07_RECOMENDACOES_ACAO.md", findings)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

