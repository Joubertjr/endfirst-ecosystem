---
demanda_id: DEMANDA-METODO-017
title: Estrutura Canônica de Personas (diretório por persona)
type: método / governança
classe: A
altera_funcionalidade: não
exige_f1: sim
status: em_execucao
created_at: 2026-01-26
created_by: CEO
executor: Cursor
---

# DEMANDA-METODO-017 — Estrutura Canônica de Personas

## 🔒 END (Resultado Observável)

### Estado Final Esperado (EXATO)

Existe uma estrutura canônica por persona contendo definição, playbook, regras, gates, checklist e modelos de evidência, permitindo que qualquer agente atue corretamente apenas lendo os artefatos da persona.

---

## 🎯 Objetivo

Formalizar uma estrutura canônica **por persona** dentro de `/METODO/PERSONAS/<PAPEL>/` para eliminar improviso (persona = prompt) e tornar a atuação de agentes governada por artefatos rastreáveis.

---

## 📌 Escopo

### Em escopo

- Criar estrutura canônica por persona em `/METODO/PERSONAS/<PAPEL>/` com subpastas:
  - `DEFINICOES/`
  - `PLAYBOOKS/`
  - `REGRAS/`
  - `GATES/`
  - `CHECKLISTS/`
  - `EVIDENCIAS_MODELO/`
  - `README.md`
- Estrutura obrigatória para as personas:
  - `CEO`
  - `PRODUTO`
  - `EXECUTOR`
  - `AUDITOR`
- Persona **CEO** com artefatos completos (definição, playbook, regras, gates, checklist, modelos de evidência, README).
- Atualizar governança para bloquear ativação de persona sem diretório canônico.
- Atualizar `DEMANDA-METODO-014` para refletir a nova definição: persona = conjunto de artefatos, não prompt.

### Fora de escopo

- Mudanças no motor de ativação dinâmica de papéis.
- Ferramentas/sistema de execução automática de gates por persona.
- Migração/remoção de artefatos antigos fora do diretório canônico (pode ser feito em demanda futura).

---

## 🔒 Regras Canônicas

- **Persona sem diretório canônico é improviso. Agente sem persona é FAIL estrutural.**
- **Persona = conjunto de artefatos, não prompt.**

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Existe `/METODO/PERSONAS/CEO/` com subpastas obrigatórias e `README.md`
- ✅ Existe `/METODO/PERSONAS/PRODUTO/` com subpastas obrigatórias e `README.md`
- ✅ Existe `/METODO/PERSONAS/EXECUTOR/` com subpastas obrigatórias e `README.md`
- ✅ Existe `/METODO/PERSONAS/AUDITOR/` com subpastas obrigatórias e `README.md`
- ✅ Persona CEO completa criada:
  - ✅ `/METODO/PERSONAS/CEO/DEFINICOES/CEO.md`
  - ✅ `/METODO/PERSONAS/CEO/PLAYBOOKS/CEO_PLAYBOOK.md`
  - ✅ `/METODO/PERSONAS/CEO/REGRAS/CEO_REGRAS.md`
  - ✅ `/METODO/PERSONAS/CEO/GATES/CEO_GATES.md`
  - ✅ `/METODO/PERSONAS/CEO/CHECKLISTS/CEO_CHECKLIST.md`
  - ✅ `/METODO/PERSONAS/CEO/EVIDENCIAS_MODELO/modelo_aprovacao_demanda.md`
  - ✅ `/METODO/PERSONAS/CEO/EVIDENCIAS_MODELO/modelo_aprovacao_f1.md`
  - ✅ `/METODO/PERSONAS/CEO/EVIDENCIAS_MODELO/modelo_validacao_final.md`
  - ✅ `/METODO/PERSONAS/CEO/README.md`
- ✅ Regra adicionada em `/METODO/REGRA_PAPEL_ATIVO_OBRIGATORIO.md` para bloquear ativação sem diretório canônico por persona
- ✅ `DEMANDA-METODO-014` atualizada com:
  - ✅ Referência direta a `/METODO/PERSONAS/<PAPEL>/`
  - ✅ Regra: persona = conjunto de artefatos, não prompt
- ✅ Evidência gerada em `/DEMANDAS/ATIVAS/DEMANDA-METODO-017/EVIDENCIAS/execucao_demanda_metodo_017_f1.md` contendo:
  - ✅ Lista de diretórios criados
  - ✅ Lista de arquivos criados
  - ✅ Validação PASS/FAIL

### FAIL

- ❌ Qualquer persona obrigatória sem diretório canônico completo
- ❌ Persona CEO incompleta (faltando qualquer artefato obrigatório)
- ❌ Governança não atualizada para bloquear ativação sem diretório canônico
- ❌ Evidência ausente ou sem validação PASS/FAIL

---

## 🧭 Regra Final

Persona sem diretório canônico é improviso. Agente sem persona é FAIL estrutural.

Existe uma estrutura canônica por persona contendo definição, playbook, regras, gates, checklist e modelos de evidência, permitindo que qualquer agente atue corretamente apenas lendo os artefatos da persona.
