# Auditoria Canônica de Personas

A pasta **Auditoria/** é somente saída. A entrada auditada é sempre **METODO/PERSONAS/**.

Esta pasta armazena **execuções** da auditoria canônica de personas. Cada execução gera uma pasta numerada `auditoria-N` com os entregáveis e a cópia da fonte auditada. O objetivo é avaliar de forma reprodutível e binária (PASS/FAIL) a pasta `METODO/PERSONAS/` do repositório.

---

## Como rodar uma auditoria

Na raiz do repositório, execute:

```bash
make auditoria
```

Isso chama [../tools/executar_auditoria.sh](../tools/executar_auditoria.sh), que por sua vez executa [../tools/executar_auditoria_personas.py](../tools/executar_auditoria_personas.py).

- **Fonte auditada:** `METODO/PERSONAS/` (diretório local). O script copia esse diretório para `Auditoria/auditoria-N/_ORIGINAL/METODO/PERSONAS` e trabalha somente sobre essa cópia.
- **Nova execução:** sempre cria a próxima pasta disponível (`auditoria-1`, `auditoria-2`, …). Uma única execução por vez (lock em `Auditoria/.lock`).
- **Opções (script direto):** `python tools/executar_auditoria_personas.py --out <dir>` grava em outra pasta; `--dry-run` só valida e mostra o que faria.

**Não é necessário ZIP.** O processo padrão usa apenas o diretório local `METODO/PERSONAS/`.

---

## O que cada execução contém (pastas `auditoria-N`)

Cada pasta `auditoria-N` contém:

| Arquivo / Pasta | Descrição breve |
|-----------------|------------------|
| `00_MANIFESTO.md` | Cabeçalho da auditoria, veredito final, estatísticas, blocos, principais bloqueios e entregáveis. |
| `01_CHECKSUMS_VERIFICAVEIS.txt` | SHA256 de todos os arquivos da cópia auditada (paths relativos à raiz da cópia). |
| `02_ESTRUTURA_COMPLETA.txt` | Árvore (estilo `tree`) da cópia em `_ORIGINAL/`. |
| `03_RELATORIO_EXECUTIVO.md` | Resumo por bloco (0 a 5), status, comando de cópia e top achados. |
| `04_ANALISE_DETALHADA_POR_ARQUIVO.md` | Bloco 3: requisitos obrigatórios por arquivo (Objetivo, Autoridade, etc.) e PASS/FAIL por seção. |
| `05_FALHAS_IDENTIFICADAS.md` | Bloco 4: achados (BLOQUEIO/ALTA/MEDIA/BAIXA), tag, arquivo:linha, trecho, correção. |
| `06_CONSISTENCIA_CRUZADA.md` | Bloco 5: cruzamentos Playbook↔Gates, Checklist↔Gates, Definição↔Regras, termos críticos, templates. |
| `07_RECOMENDACOES_ACAO.md` | Bloco 8: lista objetiva de ações recomendadas. |
| `08_AMBIENTE.txt` | Reprodutibilidade: python --version, uname, git rev-parse HEAD, git status --porcelain. |
| `_ORIGINAL/` | Cópia integral da fonte auditada (`METODO/PERSONAS/` sob `_ORIGINAL/METODO/PERSONAS`). |

O **veredito** está em `00_MANIFESTO.md`. As **falhas** detalhadas estão em `05_FALHAS_IDENTIFICADAS.md`. Os **checksums** e a **evidência bruta** estão em `01_CHECKSUMS_VERIFICAVEIS.txt` e em `_ORIGINAL/`.

---

## Os blocos em uma frase cada

- **Bloco 0** — Provas de reprodução: comando de cópia, árvore, checksums, existência de `_ORIGINAL/`.
- **Bloco 1** — Estrutura: presença obrigatória de DEFINICOES/, PLAYBOOKS/, REGRAS/, GATES/, CHECKLISTS/, EVIDENCIAS_MODELO/, README.md por persona.
- **Bloco 2** — Inventário: contagem de arquivos por pasta e mínimos configuráveis (ex.: GATES, EVIDENCIAS_MODELO).
- **Bloco 3** — Conteúdo por arquivo: seções/headings obrigatórios e conteúdo mínimo (Objetivo, Critérios de PASS/FAIL, Rastreabilidade, Versionamento, etc.).
- **Bloco 4** — Varredura de falhas: placeholders, ambiguidade, contradições, não-binariedade, rastreabilidade, referências, etc.
- **Bloco 5** — Consistência cruzada: links e termos entre Playbooks, Gates, Checklists, Definições, Regras e modelos.
- **Bloco 6** — Veredito final: FAIL se algum bloco 0–3 ou 5 falhar ou houver BLOQUEIO.
- **Bloco 7** — Templateabilidade: se o conjunto pode virar template.
- **Bloco 8** — Ações: lista de correções/ajustes recomendados.

Para os critérios formais de cada bloco, use a [instrução formal na raiz do repositório](../TEMPLATE_AUDITORIA_CANONICA_DE_PERSONA.md).

---

## Fluxo em resumo

Cópia de `METODO/PERSONAS/` → `_ORIGINAL/` → Blocos 0–8 → entregáveis em `auditoria-N`.

---

## Onde está o motor e a configuração

- **Script:** [../tools/executar_auditoria_personas.py](../tools/executar_auditoria_personas.py)
- **Configuração:** [../tools/auditoria_personas_config.json](../tools/auditoria_personas_config.json) — termos críticos, regras de Bloco 3/4, mínimos de inventário, etc.
- **Instrução formal:** [../TEMPLATE_AUDITORIA_CANONICA_DE_PERSONA.md](../TEMPLATE_AUDITORIA_CANONICA_DE_PERSONA.md) na raiz do repositório.

O comportamento da auditoria vem do script + config + template. O fluxo é sempre por diretório: fonte `METODO/PERSONAS/`, cópia em `_ORIGINAL/`.
