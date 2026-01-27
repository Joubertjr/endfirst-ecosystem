# METODO/PERSONAS — Fonte única de personas

Este diretório contém **apenas personas** (papéis) no formato canônico:

- `CEO/`
- `PRODUTO/`
- `EXECUTOR/`
- `AUDITOR/`

## Regra estrutural

- **Tudo que estiver em `METODO/PERSONAS/` deve ser “persona”.**
- Artefatos que **não são persona** (ex.: vínculos/contratos/processos comuns) **não podem** viver aqui, para evitar que auditorias de persona tratem itens comuns como “persona”.

## Processos comuns (não-persona)

Artefatos comuns a todas as personas (ex.: vínculos de processo) ficam em:

- `/METODO/_PROCESSOS/`
  - `/METODO/_PROCESSOS/VINCULOS_PROCESSO/`

## Fonte única de verdade (reforço)

> “Persona só é válida se existir em /METODO/PERSONAS//.
> Qualquer definição fora disso é FAIL estrutural.”
