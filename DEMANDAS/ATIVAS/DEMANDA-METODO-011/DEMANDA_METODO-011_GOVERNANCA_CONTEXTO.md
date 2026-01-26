---
demanda_id: DEMANDA-METODO-011
title: Governança de Bancos de Contexto
type: método / governança
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-METODO-011 — Governança de Bancos de Contexto

**Tipo:** Método / Governança  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existe um documento canônico em `/METODO/GOVERNANCA_CONTEXTO.md`
- ✅ O documento define como bancos de contexto são criados, versionados e usados
- ✅ A estrutura de CONTEXTO está definida e governada
- ✅ Qualquer executor consegue criar e versionar um banco de contexto seguindo o contrato

**Resultado esperado do sistema:**

> "Existe um contrato que define como bancos de contexto são criados, versionados e usados por produtos."

---

## 🚫 Regras Canônicas

**Governança de Contexto:**

> "CONTEXTO não é prompt solto. CONTEXTO é artefato versionado com fonte rastreável."

**Rastreabilidade de Fonte:**

> "Todo CONTEXTO DEVE ter fonte (lei, norma, modelo, doutrina). Contexto sem fonte é FAIL estrutural."

**Referência Obrigatória:**

> "Todo OUTPUT gerado DEVE referenciar o CONTEXTO usado. Output sem referência é FAIL estrutural."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Documento `/METODO/GOVERNANCA_CONTEXTO.md` criado
- ✅ Estrutura de CONTEXTO definida:
  - CONTEXTO é versionado
  - CONTEXTO tem fonte rastreável
  - CONTEXTO é referenciado nos outputs
- ✅ Regra explícita: "CONTEXTO ≠ prompt solto"
- ✅ Critérios de PASS/FAIL para criação de contexto definidos
- ✅ Formato de versionamento de contexto definido

### FAIL

- ❌ Documento não existe
- ❌ Estrutura de CONTEXTO não está definida
- ❌ Regra de versionamento não está explícita
- ❌ Fonte não é obrigatória
- ❌ Referência em outputs não é obrigatória

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um contrato formal que defina como bancos de contexto devem ser criados, versionados e usados por produtos. Isso gera:

1. **Falta de rastreabilidade:** Não é possível saber qual contexto foi usado em um output
2. **Inconsistência de fonte:** Contextos podem ser criados sem fonte rastreável
3. **Perda de qualidade:** Outputs podem ser gerados com contextos desatualizados ou incorretos
4. **Impossibilidade de auditoria:** Não é possível auditar a origem de um output

### Impacto

Sem governança de contexto:
- Outputs não são rastreáveis
- Qualidade não é garantida
- Auditoria é impossível
- Versionamento é inconsistente

---

## 🚫 DO / DON'T

### ✅ DO

- **Definir estrutura canônica de CONTEXTO**
- **Estabelecer regra: CONTEXTO tem fonte rastreável**
- **Criar critérios binários de PASS/FAIL**
- **Definir versionamento de CONTEXTO**
- **Especificar formato de referência em outputs**

### ❌ DON'T

- **Criar CONTEXTO sem fonte**
- **Permitir CONTEXTO sem versionamento**
- **Permitir OUTPUT sem referência ao CONTEXTO**
- **Tratar CONTEXTO como prompt solto**
- **Permitir CONTEXTO desatualizado sem marcação**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- Nenhum

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. `/METODO/GOVERNANCA_CONTEXTO.md`
   - Definir estrutura canônica de CONTEXTO
   - Definir regra de fonte rastreável
   - Definir critérios de PASS/FAIL
   - Definir versionamento
   - Definir formato de referência em outputs

### Validações

1. Documento criado e commitado
2. Estrutura de CONTEXTO definida
3. Regra de fonte rastreável explícita
4. Critérios binários definidos
5. Formato de referência definido

---

## ❌ Fora de Escopo

- Criação de bancos de contexto específicos (isso será feito em demandas de produto)
- Implementação de software para gerenciar contextos
- Migração de contextos existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "CONTEXTO sem fonte é prompt solto. CONTEXTO sem versionamento é perda de rastreabilidade. Governança de contexto é condição de passagem para qualquer produto no método END-FIRST."
