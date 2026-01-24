---
demanda_id: DEMANDA-METODO-016
title: Auditor Técnico do Método
type: método / governança
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-24
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-METODO-016 — Auditor Técnico do Método

**Tipo:** Método / Governança  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existe um documento canônico em `/METODO/AUDITOR_TECNICO.md`
- ✅ O documento define o papel "Auditor Técnico do Método" com responsabilidades, permissões e procedimentos
- ✅ O Auditor pode validar F-1s, demandas e artefatos sem acesso ao Git
- ✅ Qualquer executor consegue atuar como Auditor seguindo o contrato

**Resultado esperado do sistema:**

> "Existe definição formal do papel Auditor Técnico do Método, com responsabilidades, permissões, procedimentos de auditoria e critérios binários de validação."

---

## 🚫 Regras Canônicas

**Auditor Técnico:**

> "Auditor valida sem confiar. Auditor não aprova por simpatia. Auditor procura falhas escondidas."

**Auditoria Sem Acesso ao Git:**

> "Auditor valida sem acesso direto ao Git. Executor fornece evidências. Auditor valida evidências."

**Critérios Binários:**

> "Auditor usa critérios binários. PASS ou FAIL. Sem meio-termo."

**Independência do Auditor:**

> "Auditor não implementa. Auditor não decide escopo. Auditor não aprova demandas. Auditor valida."

**Branch Padrão Governado:**

> "O método define um branch padrão (master ou main). Todos os commits de método vão para o branch padrão. Branch padrão é contrato."

**Anti-Placeholder em Artefatos:**

> "Artefatos de método não podem conter TODO, TBD ou PLACEHOLDER. Placeholder em END é FAIL. Placeholder em critérios de fase é permitido se resolvido durante execução."

**Unicidade de Markers no README:**

> "Markers no README.md devem ser únicos. Duplicação de markers é FAIL estrutural."

**Aprovação Explícita de F-1:**

> "Todo F-1 deve ter status explícito (PENDENTE ou APROVADO), data de aprovação e autoridade aprovadora. F-1 sem aprovação explícita não pode ser executado."

**Formato Canônico de Critérios:**

> "Critérios de PASS/FAIL devem usar formato canônico: ### PASS e ### FAIL. Formato diferente é FAIL estrutural."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Documento `/METODO/AUDITOR_TECNICO.md` criado
- ✅ Papel Auditor Técnico definido:
  - Responsabilidades do Auditor
  - Permissões do Auditor
  - Proibições do Auditor
  - Procedimentos de auditoria
  - Critérios binários de validação
- ✅ Procedimento de auditoria de F-1s definido
- ✅ Procedimento de auditoria de demandas definido
- ✅ Procedimento de auditoria de artefatos definido
- ✅ Formato de relatório de auditoria definido
- ✅ Critérios de PASS/FAIL para auditoria definidos
- ✅ Regras canônicas de integridade definidas:
  - Branch padrão governado
  - Anti-placeholder em artefatos
  - Unicidade de markers no README
  - Aprovação explícita de F-1
  - Formato canônico de critérios
- ✅ Gate canônico de integridade definido:
  - Nome do gate
  - Critérios binários do gate
  - Evidências exigidas
  - Condições de bloqueio

### FAIL

- ❌ Documento não existe
- ❌ Papel Auditor não está definido
- ❌ Responsabilidades não estão definidas
- ❌ Permissões não estão definidas
- ❌ Proibições não estão definidas
- ❌ Procedimentos de auditoria não estão definidos
- ❌ Formato de relatório não está definido
- ❌ Critérios de PASS/FAIL não estão definidos
- ❌ Regras canônicas de integridade não estão definidas
- ❌ Gate canônico de integridade não está definido

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um papel formal de "Auditor Técnico do Método". Isso gera:

1. **Falta de validação independente:** Não há validação independente de F-1s e artefatos
2. **Dependência de acesso ao Git:** Validação requer acesso direto ao Git
3. **Falta de procedimentos:** Não há procedimentos formais de auditoria
4. **Inconsistência de validação:** Cada validação pode ser feita de forma diferente

### Impacto

Sem Auditor Técnico:
- Governança é perdida
- Validação é inconsistente
- Qualidade não é garantida
- Rastreabilidade é impossível

---

## 🚫 DO / DON'T

### ✅ DO

- **Definir papel Auditor Técnico**
- **Estabelecer responsabilidades do Auditor**
- **Definir permissões do Auditor**
- **Definir proibições do Auditor**
- **Criar procedimentos de auditoria**
- **Definir formato de relatório de auditoria**
- **Criar critérios binários de validação**

### ❌ DON'T

- **Permitir Auditor implementar**
- **Permitir Auditor decidir escopo**
- **Permitir Auditor aprovar demandas**
- **Permitir auditoria sem critérios binários**
- **Permitir auditoria sem evidências**
- **Permitir aprovação por simpatia**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- **Depende de:** DEMANDA-METODO-014 (Personas Operacionais)
- **Depende de:** DEMANDA-METODO-015 (Mecanismo Dinâmico de Ativação de Papéis)

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. `/METODO/AUDITOR_TECNICO.md`
   - Definir papel Auditor Técnico
   - Definir responsabilidades do Auditor
   - Definir permissões do Auditor
   - Definir proibições do Auditor
   - Criar procedimentos de auditoria de F-1s
   - Criar procedimentos de auditoria de demandas
   - Criar procedimentos de auditoria de artefatos
   - Definir formato de relatório de auditoria
   - Criar critérios binários de validação

### Validações

1. Documento criado e commitado
2. Papel Auditor definido
3. Responsabilidades definidas
4. Permissões definidas
5. Proibições definidas
6. Procedimentos de auditoria definidos
7. Formato de relatório definido
8. Critérios binários definidos

---

## 🔍 RESPONSABILIDADES DO AUDITOR

### O que o Auditor PODE fazer:

- ✅ Solicitar evidências ao Executor
- ✅ Validar F-1s contra critérios binários
- ✅ Validar demandas contra critérios binários
- ✅ Validar artefatos contra critérios binários
- ✅ Procurar falhas escondidas
- ✅ Tentar quebrar o sistema
- ✅ Gerar relatório de auditoria
- ✅ Declarar PASS ou FAIL

### O que o Auditor NÃO PODE fazer:

- ❌ Implementar
- ❌ Decidir escopo
- ❌ Aprovar demandas
- ❌ Aprovar F-1s
- ❌ Modificar método
- ❌ Aprovar por simpatia
- ❌ Validar sem critérios binários

---

## 📊 PROCEDIMENTO DE AUDITORIA DE F-1s

### Inputs:

- Arquivo de F-1
- Arquivo de demanda correspondente

### Outputs:

- Relatório de auditoria
- Status: PASS ou FAIL

### Passos:

1. **Solicitar evidências ao Executor:**
   - Lista de demandas existentes
   - Lista de F-1s existentes
   - END de cada F-1
   - Status de cada F-1

2. **Validar estrutura do F-1:**
   - F-1 tem END explícito?
   - F-1 tem fases bem definidas?
   - F-1 tem critérios de PASS/FAIL?
   - F-1 tem artefatos definidos?

3. **Validar coerência do END:**
   - END do F-1 bate com END da demanda?
   - END é mensurável?
   - END é binário?

4. **Validar qualidade das fases:**
   - Cada fase tem END específico?
   - Cada fase tem artefato definido?
   - Cada fase tem critérios de PASS?

5. **Procurar falhas escondidas:**
   - F-1 tem placeholders?
   - F-1 tem fases genéricas?
   - F-1 tem TODOs ou TBDs?

6. **Gerar relatório:**
   - Listar achados
   - Declarar PASS ou FAIL
   - Recomendar ações

---

## 🔒 GATE CANÔNICO DE INTEGRIDADE DO MÉTODO

### Nome do Gate

**`Z-METHOD-REPO-INTEGRITY`**

### Propósito

Validar a integridade estrutural do repositório do método END-FIRST antes de declarar PASS em qualquer demanda de método.

### Critérios Binários

**PASS:**
- ✅ HEAD == origin/[branch_padrão]
- ✅ Markers README únicos
- ✅ Zero placeholders (TODO/TBD/PLACEHOLDER) em artefatos de método
- ✅ Todas as demandas têm END + PASS/FAIL
- ✅ Branch padrão definido e documentado
- ✅ Todos os F-1s têm status explícito (PENDENTE ou APROVADO)
- ✅ Formato canônico de critérios (### PASS / ### FAIL) em todas as demandas

**FAIL:**
- ❌ HEAD != origin/[branch_padrão]
- ❌ Markers README duplicados
- ❌ Placeholders em artefatos de método
- ❌ Demandas sem END ou PASS/FAIL
- ❌ Branch padrão não definido
- ❌ F-1s sem status explícito
- ❌ Formato de critérios não canônico

### Evidências Exigidas

1. Output de `git log --oneline -n 20`
2. Output de `git status`
3. Lista de markers no README.md
4. Lista de demandas com END e PASS/FAIL
5. Lista de F-1s com status
6. Scan de placeholders em artefatos

### Quando Bloqueia PASS

O gate bloqueia PASS de qualquer demanda de método (DEMANDA-METODO-XXX) se **qualquer critério FAIL** for detectado.

---

## ❌ Fora de Escopo

- Implementação de software para auditoria
- Criação de personas específicas de produtos
- Migração de auditorias existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Auditor sem procedimento é improviso. Auditor sem critério binário é opinião. Auditor sem independência é aprovação por simpatia. Auditor Técnico do Método é condição de passagem para governança de qualidade no método END-FIRST."
