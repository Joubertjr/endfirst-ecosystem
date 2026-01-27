#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE_PATH="${ROOT_DIR}/TEMPLATE_AUDITORIA_CANONICA_DE_PERSONA.md"
OUT_DIR="${ROOT_DIR}/Auditoria"

if [[ ! -f "${TEMPLATE_PATH}" ]]; then
  echo "ERRO: template não encontrado em: ${TEMPLATE_PATH}" >&2
  exit 1
fi

mkdir -p "${OUT_DIR}"

shopt -s nullglob
max_n=0
for p in "${OUT_DIR}"/auditoria-*; do
  base="$(basename "${p}")"
  if [[ "${base}" =~ ^auditoria-([0-9]+)(\.md)?$ ]]; then
    n="${BASH_REMATCH[1]}"
    if (( n > max_n )); then
      max_n="${n}"
    fi
  fi
done

next_n=$((max_n + 1))
AUD_DIR="${OUT_DIR}/auditoria-${next_n}"

mkdir -p "${AUD_DIR}"
mkdir -p "${AUD_DIR}/_ORIGINAL"

cat > "${AUD_DIR}/00_MANIFESTO.md" <<'EOF'
INSTRUÇÃO FORMAL — AUDITORIA CANÔNICA DE PERSONA (VERSÃO ROBUSTA)

Você DEVE auditar a pasta METODO/PERSONAS/ usando exclusivamente este template.
É proibido interpretar livremente, resumir, pular blocos ou corrigir arquivos.

Regras gerais:
	•	Trabalhar SOMENTE sobre a pasta METODO/PERSONAS/ (fonte auditada local; sem ZIP).
	•	Auditoria do ZERO: é proibido reaproveitar qualquer relatório, checksum, achado, evidência, ou saída de auditorias anteriores (incluindo `auditoria_canonica/`).
	•	Gerar SHA256 de TODOS os arquivos.
	•	Incluir cópia integral do pacote auditado.
	•	Tudo é PASS/FAIL binário.
	•	Qualquer BLOQUEIO ⇒ FAIL final.
	•	Não elogiar. Não explicar método. Apenas auditar.

⸻

CABECALHO (obrigatório)

Preencher:
	•	Data:
	•	Auditor:
	•	Método:
	•	Fonte (diretório local auditado): METODO/PERSONAS/
	•	Commit/Repo (se existir):

⸻

PROIBIDO
	•	Interpretar
	•	Resumir
	•	Corrigir arquivos
	•	Reaproveitar qualquer conteúdo/artefato de auditorias anteriores (incluindo `auditoria_canonica/`)
	•	Explicar método
	•	Suavizar falhas
	•	Ignorar bloco

⸻

PERMITIDO APENAS

AUDITAR → CLASSIFICAR → BLOQUEAR OU APROVAR.
EOF

cat > "${AUD_DIR}/01_CHECKSUMS_VERIFICAVEIS.txt" <<'EOF'
EOF

cat > "${AUD_DIR}/02_ESTRUTURA_COMPLETA.txt" <<'EOF'
EOF

cat > "${AUD_DIR}/03_RELATORIO_EXECUTIVO.md" <<'EOF'
BLOCO 0 — PROVAS DE REPRODUÇÃO (BLOQUEANTE)

Resultado do bloco 0: PASS / FAIL

⸻

BLOCO 1 — ESTRUTURA (BINÁRIO)

Resultado do bloco 1: PASS / FAIL

⸻

BLOCO 2 — INVENTÁRIO DE ARQUIVOS

Resultado do bloco 2: PASS / FAIL

⸻

BLOCO 3 — CONTEÚDO POR ARQUIVO (LINHA A LINHA)

Resultado do bloco 3: PASS / FAIL

⸻

BLOCO 4 — VARREDURA DE FALHAS

Resultado do bloco 4: PASS / FAIL

⸻

BLOCO 5 — CONSISTÊNCIA CRUZADA

Resultado do bloco 5: PASS / FAIL

⸻

BLOCO 6 — VEREDITO FINAL

Reportar:
	•	Quantidade de BLOQUEIOS:
	•	Quantidade de ALTAS:
	•	Quantidade de MÉDIAS:
	•	Quantidade de BAIXAS:

Status final: PASS / FAIL

⸻

BLOCO 7 — TEMPLATEABILIDADE

Pode virar template para outras personas? SIM / NÃO

Se NÃO:
Listar condições faltantes objetivas:
	•	(lista)

⸻

BLOCO 8 — AÇÕES

Listar somente ações objetivas, sem explicação:
	1.
	2.
	3.
EOF

cat > "${AUD_DIR}/04_ANALISE_DETALHADA_POR_ARQUIVO.md" <<'EOF'
BLOCO 3 — CONTEÚDO POR ARQUIVO (LINHA A LINHA)

Para CADA arquivo individualmente:

<caminho_do_arquivo>

Requisito obrigatório	PASS/FAIL	Evidência (linha/trecho)
Objetivo		
Autoridade		
Responsabilidades		
Limites		
Perguntas canônicas		
Critérios de PASS		
Decisões permitidas		
Decisões proibidas		
Rastreabilidade		
Versionamento		

Resultado por arquivo: PASS / FAIL
EOF

cat > "${AUD_DIR}/05_FALHAS_IDENTIFICADAS.md" <<'EOF'
BLOCO 4 — VARREDURA DE FALHAS

ACHADO-XXX
Severidade: BLOQUEIO | ALTA | MEDIA | BAIXA
Tag: PLACEHOLDER | AMBIGUIDADE | CONTRADICAO | NAO_BINARIO | SEM_RASTREABILIDADE | REFERENCIA_AUSENTE | INCONSISTENCIA_CRUZADA
Arquivo:linha
Trecho
Regra violada
Correção mínima

Resultado do bloco 4: PASS / FAIL
EOF

cat > "${AUD_DIR}/06_CONSISTENCIA_CRUZADA.md" <<'EOF'
BLOCO 5 — CONSISTÊNCIA CRUZADA

Tabela:

Cruzamento	PASS/FAIL	Evidência

Resultado do bloco 5: PASS / FAIL
EOF

cat > "${AUD_DIR}/07_RECOMENDACOES_ACAO.md" <<'EOF'
BLOCO 8 — AÇÕES

Listar somente ações objetivas, sem explicação:
	1.
	2.
	3.
EOF

touch "${AUD_DIR}/_ORIGINAL/.gitkeep"

echo "Criado: ${AUD_DIR}"
