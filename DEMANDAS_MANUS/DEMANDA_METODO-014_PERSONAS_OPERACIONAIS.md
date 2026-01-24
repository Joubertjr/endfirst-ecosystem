---
demanda_id: DEMANDA-METODO-014
title: Personas Operacionais do Método
type: método / governança
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-METODO-014 — Personas Operacionais do Método

**Tipo:** Método / Governança  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existe um documento canônico em `/METODO/PERSONAS_OPERACIONAIS.md`
- ✅ O documento define as personas operacionais do método: CEO, Chefe de Produto e Executor
- ✅ Cada persona tem responsabilidade, permissões e papéis no fluxo definidos
- ✅ Qualquer executor consegue identificar qual persona deve executar cada ação

**Resultado esperado do sistema:**

> "Existe definição formal de personas: CEO, Chefe de Produto e Executor (IA / humano), com responsabilidade, permissões e papéis no fluxo."

---

## 🚫 Regras Canônicas

**Personas Operacionais:**

> "Persona sem responsabilidade é papel sem governança. Persona sem permissão é papel sem autoridade."

**Separação de Responsabilidades:**

> "CEO aprova. Chefe de Produto planeja. Executor executa. Mistura de papéis é FAIL estrutural."

**Executor Universal:**

> "Executor pode ser IA ou humano. Método não distingue. Método governa."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Documento `/METODO/PERSONAS_OPERACIONAIS.md` criado
- ✅ Personas definidas:
  - **CEO:** Aprova demandas, aprova F-1s, define prioridades
  - **Chefe de Produto:** Cria demandas, cria F-1s, valida execução
  - **Executor:** Executa F-1s, gera evidências, registra outputs
- ✅ Responsabilidades de cada persona definidas
- ✅ Permissões de cada persona definidas
- ✅ Papéis no fluxo de cada persona definidos
- ✅ Critérios de PASS/FAIL para cada persona definidos

### FAIL

- ❌ Documento não existe
- ❌ Personas não estão definidas
- ❌ Responsabilidades não estão definidas
- ❌ Permissões não estão definidas
- ❌ Papéis no fluxo não estão definidos
- ❌ Critérios de PASS/FAIL não estão definidos

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um contrato formal que defina as personas operacionais do método. Isso gera:

1. **Falta de clareza:** Não está claro quem aprova, quem planeja e quem executa
2. **Mistura de papéis:** Executor pode tentar aprovar demandas
3. **Perda de governança:** Não há critério binário para validar se uma persona está agindo conforme
4. **Inconsistência de responsabilidades:** Cada executor pode interpretar seu papel de forma diferente

### Impacto

Sem personas operacionais:
- Governança é perdida
- Responsabilidades são confusas
- Permissões são inconsistentes
- Qualidade não é garantida

---

## 🚫 DO / DON'T

### ✅ DO

- **Definir personas operacionais: CEO, Chefe de Produto, Executor**
- **Estabelecer responsabilidades de cada persona**
- **Definir permissões de cada persona**
- **Definir papéis no fluxo de cada persona**
- **Criar critérios binários de PASS/FAIL**

### ❌ DON'T

- **Permitir mistura de papéis**
- **Permitir Executor aprovar demandas**
- **Permitir CEO executar F-1s**
- **Permitir Chefe de Produto aprovar demandas sem CEO**
- **Permitir persona sem responsabilidade definida**

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

1. `/METODO/PERSONAS_OPERACIONAIS.md`
   - Definir personas: CEO, Chefe de Produto, Executor
   - Definir responsabilidades de cada persona
   - Definir permissões de cada persona
   - Definir papéis no fluxo de cada persona
   - Criar critérios binários de PASS/FAIL

### Validações

1. Documento criado e commitado
2. Personas definidas
3. Responsabilidades definidas
4. Permissões definidas
5. Papéis no fluxo definidos
6. Critérios binários definidos

---

## ❌ Fora de Escopo

- Implementação de software para gerenciar personas
- Criação de personas específicas de produtos (isso será feito em demandas de produto)
- Migração de personas existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Persona sem responsabilidade é papel sem governança. Persona sem permissão é papel sem autoridade. Personas operacionais são condição de passagem para qualquer execução no método END-FIRST."
