---
demanda_id: DEMANDA-PROD-003
title: Fluxo END-FIRST — Edital de TI
type: produto / fluxo
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-PROD-003 — Fluxo END-FIRST: Edital de TI

**Tipo:** Produto / Fluxo  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG  
**Repositório:** `endfirst-ecosystem`  
**Diretório:** `/PRODUTOS/contratacao-ti/planejamento/`

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existe um fluxo governado por END-FIRST que gera um edital completo com evidência
- ✅ O fluxo está documentado em `/PRODUTOS/contratacao-ti/planejamento/`
- ✅ 1 execução do fluxo gera 1 edital completo
- ✅ Evidência é registrada em `/PRODUTOS/contratacao-ti/EVIDENCIAS/`

**Resultado esperado do sistema:**

> "Existe um fluxo governado por END-FIRST que gera um edital completo com evidência."

---

## 🚫 Regras Canônicas

**Fluxo Governado:**

> "Fluxo sem governança é execução sem rastreabilidade. Governança é condição de passagem."

**Evidência Obrigatória:**

> "Fluxo sem evidência não é auditável. Evidência é condição de passagem."

**END como Contrato:**

> "END governa fluxo. Fluxo sem END não é governado."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Fluxo existe em `/PRODUTOS/contratacao-ti/planejamento/`
- ✅ Fluxo gera edital completo:
  - ETP (Estudo Técnico Preliminar)
  - TR (Termo de Referência)
  - Edital
  - Anexos
- ✅ 1 execução do fluxo gera 1 edital completo
- ✅ Evidência é registrada em `/PRODUTOS/contratacao-ti/EVIDENCIAS/`
- ✅ Output referencia CONTEXTO usado
- ✅ Output tem versionamento cruzado

### FAIL

- ❌ Fluxo não existe
- ❌ Fluxo não gera edital completo
- ❌ Execução não gera edital
- ❌ Evidência não é registrada
- ❌ Output não referencia CONTEXTO
- ❌ Output não tem versionamento cruzado

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um fluxo governado por END-FIRST para gerar edital de TI. Isso gera:

1. **Falta de rastreabilidade:** Não é possível rastrear origem do edital
2. **Inconsistência de documentos:** Documentos podem não estar conformes
3. **Impossibilidade de auditoria:** Não é possível auditar conformidade
4. **Perda de qualidade:** Edital pode não estar conforme

### Impacto

Sem fluxo governado:
- Rastreabilidade é perdida
- Documentos são inconsistentes
- Auditoria é impossível
- Qualidade não é garantida

---

## 🚫 DO / DON'T

### ✅ DO

- **Criar fluxo em `/PRODUTOS/contratacao-ti/planejamento/`**
- **Gerar ETP, TR, Edital e anexos**
- **Registrar evidência em `/PRODUTOS/contratacao-ti/EVIDENCIAS/`**
- **Referenciar CONTEXTO nos outputs**
- **Incluir versionamento cruzado nos outputs**

### ❌ DON'T

- **Criar fluxo sem governança**
- **Gerar edital sem evidência**
- **Gerar output sem referência ao CONTEXTO**
- **Gerar output sem versionamento cruzado**
- **Permitir fluxo sem END**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- **Depende de:** DEMANDA-PROD-001 (Produto 001 — Contratação TI)
- **Depende de:** DEMANDA-PROD-002 (Banco de Contexto — Contratação TI)
- **Depende de:** DEMANDA-METODO-012 (Versionamento Cruzado)

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. **Fluxo END-FIRST**
   - Definição do END (Estado Final Esperado)
   - Fases do fluxo
   - Critérios de PASS/FAIL
   - Templates de documentos

2. **Templates**
   - Template de ETP
   - Template de TR
   - Template de Edital
   - Template de anexos

3. **Evidências**
   - Estrutura de evidência
   - Formato de evidência
   - Critérios de evidência

### Validações

1. Fluxo existe e está documentado
2. Fluxo gera edital completo
3. Evidência é registrada
4. Output referencia CONTEXTO
5. Output tem versionamento cruzado

---

## ❌ Fora de Escopo

- Criação de outros fluxos (isso será feito em demandas futuras)
- Implementação de software para executar fluxo
- Migração de fluxos existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Fluxo sem governança é execução sem rastreabilidade. Fluxo sem evidência não é auditável. Fluxo sem END não é governado. Fluxo END-FIRST é condição de passagem para qualquer produto no método END-FIRST."
