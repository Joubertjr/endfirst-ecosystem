# F1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-METODO-017 — Estrutura Canônica de Personas  
**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Executor:** Cursor  
**Papel ativo:** Executor (Cursor)  

---

## 🔒 END — ESTADO FINAL ESPERADO (EXATO)

Existe uma estrutura canônica por persona contendo definição, playbook, regras, gates, checklist e modelos de evidência, permitindo que qualquer agente atue corretamente apenas lendo os artefatos da persona.

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Estrutura canônica criada para as personas: `CEO`, `PRODUTO`, `EXECUTOR`, `AUDITOR`
- ✅ Persona `CEO` com artefatos completos (definição, playbook, regras, gates, checklist, modelos de evidência, README)
- ✅ Regra de governança atualizada para impedir ativação de persona sem diretório canônico
- ✅ `DEMANDA-METODO-014` atualizada para refletir:
  - Referência direta a `/METODO/PERSONAS/<PAPEL>/`
  - Regra: persona = conjunto de artefatos, não prompt
- ✅ Evidência de execução gerada com lista de diretórios, lista de arquivos e PASS/FAIL
- ✅ Commit final realizado com mensagem canônica exigida

### FAIL

- ❌ Qualquer persona obrigatória sem diretório canônico
- ❌ Persona CEO incompleta
- ❌ Governança não atualizada
- ❌ Evidência ausente/insuficiente
- ❌ Commit final não realizado ou mensagem diferente da exigida

---

## 📋 Fases de Execução

### F1.1 — Criar estrutura canônica por persona

**END desta fase:**
Existe um diretório canônico por persona em `/METODO/PERSONAS/<PAPEL>/` com subpastas obrigatórias.

**Artefatos:**
- `/METODO/PERSONAS/CEO/` (estrutura completa)
- `/METODO/PERSONAS/PRODUTO/` (estrutura completa)
- `/METODO/PERSONAS/EXECUTOR/` (estrutura completa)
- `/METODO/PERSONAS/AUDITOR/` (estrutura completa)

**Critérios de PASS:**
- ✅ Cada diretório contém: `DEFINICOES/`, `PLAYBOOKS/`, `REGRAS/`, `GATES/`, `CHECKLISTS/`, `EVIDENCIAS_MODELO/` e `README.md`

**Critérios de FAIL:**
- ❌ Qualquer subpasta ausente

---

### F1.2 — Gerar artefatos completos da persona CEO

**END desta fase:**
A persona `CEO` pode ser executada por qualquer agente apenas lendo seus artefatos canônicos.

**Artefatos:**
- `/METODO/PERSONAS/CEO/DEFINICOES/CEO.md`
- `/METODO/PERSONAS/CEO/PLAYBOOKS/CEO_PLAYBOOK.md`
- `/METODO/PERSONAS/CEO/REGRAS/CEO_REGRAS.md`
- `/METODO/PERSONAS/CEO/GATES/CEO_GATES.md`
- `/METODO/PERSONAS/CEO/CHECKLISTS/CEO_CHECKLIST.md`
- `/METODO/PERSONAS/CEO/EVIDENCIAS_MODELO/modelo_aprovacao_demanda.md`
- `/METODO/PERSONAS/CEO/EVIDENCIAS_MODELO/modelo_aprovacao_f1.md`
- `/METODO/PERSONAS/CEO/EVIDENCIAS_MODELO/modelo_validacao_final.md`
- `/METODO/PERSONAS/CEO/README.md`

**Critérios de PASS:**
- ✅ Todos os arquivos existem
- ✅ Conteúdo contém, no mínimo:
  - Objetivo do papel
  - Autoridade
  - Responsabilidades
  - Limites
  - Perguntas canônicas
  - Critérios de PASS do papel
  - Decisões permitidas
  - Decisões proibidas

**Critérios de FAIL:**
- ❌ Qualquer arquivo ausente
- ❌ Qualquer seção mínima obrigatória ausente

---

### F1.3 — Atualizar governança do método

**END desta fase:**
Existe regra explícita impedindo ativação de persona sem diretório canônico por persona.

**Artefato:**
- Atualização em `/METODO/REGRA_PAPEL_ATIVO_OBRIGATORIO.md`

**Critérios de PASS:**
- ✅ Regra adicionada (texto exato exigido)

**Critérios de FAIL:**
- ❌ Regra ausente ou texto diferente

---

### F1.4 — Atualizar DEMANDA-METODO-014

**END desta fase:**
`DEMANDA-METODO-014` referencia a estrutura canônica por persona e define persona como conjunto de artefatos.

**Artefatos:**
- Atualização em `/DEMANDAS/ATIVAS/DEMANDA-METODO-014/DEMANDA_METODO-014_PERSONAS_OPERACIONAIS.md`
- Atualização em `/DEMANDAS/ATIVAS/DEMANDA-METODO-014/DEMANDA_METODO-014_F1_PLANEJAMENTO.md`

**Critérios de PASS:**
- ✅ Referência direta a `/METODO/PERSONAS/<PAPEL>/` presente
- ✅ Regra “persona = conjunto de artefatos, não prompt” presente

**Critérios de FAIL:**
- ❌ Referência ausente
- ❌ Regra ausente

---

### F1.5 — Gerar evidência de execução

**END desta fase:**
Existe evidência auditável com lista de criação e validação PASS/FAIL.

**Artefato:**
- `/DEMANDAS/ATIVAS/DEMANDA-METODO-017/EVIDENCIAS/execucao_demanda_metodo_017_f1.md`

**Critérios de PASS:**
- ✅ Lista de diretórios criados
- ✅ Lista de arquivos criados
- ✅ Validação PASS/FAIL explícita

**Critérios de FAIL:**
- ❌ Evidência incompleta

---

### F1.6 — Commit final

**END desta fase:**
Existe commit único com mensagem canônica exigida.

**Artefato:**
- Commit no git

**Critérios de PASS:**
- ✅ Mensagem do commit é exatamente:
  - `feat(METODO-017): estrutura canonica de personas + persona CEO completa`

**Critérios de FAIL:**
- ❌ Commit ausente
- ❌ Mensagem diferente

---

## 🔒 Regra Final

Persona sem diretório canônico é improviso. Agente sem persona é FAIL estrutural.
