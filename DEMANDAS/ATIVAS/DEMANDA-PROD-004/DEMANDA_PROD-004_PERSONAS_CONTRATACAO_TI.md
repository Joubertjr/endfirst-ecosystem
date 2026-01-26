---
demanda_id: DEMANDA-PROD-004
title: Personas do Produto (Contratação TI)
type: produto / personas
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-PROD-004 — Personas do Produto (Contratação TI)

**Tipo:** Produto / Personas  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG  
**Repositório:** `endfirst-ecosystem`  
**Diretório:** `/PRODUTOS/contratacao-ti/`

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existem personas configuradas: gestor, jurídico, técnico e controle
- ✅ Cada persona tem papel definido no fluxo
- ✅ Cada persona tem responsabilidades definidas
- ✅ Cada persona tem permissões definidas

**Resultado esperado do sistema:**

> "Existem personas configuradas: gestor, jurídico, técnico e controle."

---

## 🚫 Regras Canônicas

**Personas de Produto:**

> "Persona sem papel é papel sem governança. Papel no fluxo é condição de passagem."

**Separação de Responsabilidades:**

> "Gestor decide. Jurídico valida. Técnico especifica. Controle audita. Mistura de papéis é FAIL estrutural."

**Persona como Artefato:**

> "Persona é artefato de primeira classe. Persona não é usuário genérico."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Personas definidas:
  - **Gestor:** Decide necessidade, aprova ETP
  - **Jurídico:** Valida conformidade legal
  - **Técnico:** Especifica requisitos técnicos
  - **Controle:** Audita conformidade
- ✅ Cada persona tem papel no fluxo
- ✅ Cada persona tem responsabilidades
- ✅ Cada persona tem permissões
- ✅ Documentação de personas existe

### FAIL

- ❌ Personas não estão definidas
- ❌ Persona não tem papel no fluxo
- ❌ Persona não tem responsabilidades
- ❌ Persona não tem permissões
- ❌ Documentação não existe

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existem personas definidas para o produto de contratação pública de TI. Isso gera:

1. **Falta de clareza:** Não está claro quem faz o quê
2. **Mistura de papéis:** Usuários podem tentar fazer tarefas de outras personas
3. **Perda de governança:** Não há critério binário para validar se uma persona está agindo conforme
4. **Inconsistência de responsabilidades:** Cada usuário pode interpretar seu papel de forma diferente

### Impacto

Sem personas de produto:
- Governança é perdida
- Responsabilidades são confusas
- Permissões são inconsistentes
- Qualidade não é garantida

---

## 🚫 DO / DON'T

### ✅ DO

- **Definir personas: gestor, jurídico, técnico, controle**
- **Estabelecer papel de cada persona no fluxo**
- **Definir responsabilidades de cada persona**
- **Definir permissões de cada persona**
- **Documentar personas**

### ❌ DON'T

- **Permitir mistura de papéis**
- **Permitir persona sem papel no fluxo**
- **Permitir persona sem responsabilidades**
- **Permitir persona sem permissões**
- **Permitir persona sem documentação**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- **Depende de:** DEMANDA-METODO-014 (Personas Operacionais)
- **Depende de:** DEMANDA-PROD-001 (Produto 001 — Contratação TI)

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. **Documentação de Personas**
   - `/PRODUTOS/contratacao-ti/PERSONAS.md`
   - Definição de cada persona
   - Papel no fluxo
   - Responsabilidades
   - Permissões

2. **Matriz de Responsabilidades**
   - RACI (Responsible, Accountable, Consulted, Informed)
   - Matriz de permissões

### Validações

1. Personas definidas
2. Papel no fluxo definido
3. Responsabilidades definidas
4. Permissões definidas
5. Documentação existe

---

## ❌ Fora de Escopo

- Criação de personas de outros produtos (isso será feito em demandas futuras)
- Implementação de software para gerenciar personas
- Migração de personas existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Persona sem papel é papel sem governança. Persona sem responsabilidade é papel sem autoridade. Personas de produto são condição de passagem para qualquer produto no método END-FIRST."
