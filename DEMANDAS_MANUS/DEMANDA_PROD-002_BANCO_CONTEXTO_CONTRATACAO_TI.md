---
demanda_id: DEMANDA-PROD-002
title: Banco de Contexto — Contratação TI
type: produto / contexto
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-PROD-002 — Banco de Contexto: Contratação TI

**Tipo:** Produto / Contexto  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG  
**Repositório:** `endfirst-ecosystem`  
**Diretório:** `/PRODUTOS/contratacao-ti/CONTEXTO/`

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existe um banco de contexto versionado contendo: leis (Lei 14.133/2021, etc.), acórdãos, modelos e doutrina
- ✅ O banco de contexto está em `/PRODUTOS/contratacao-ti/CONTEXTO/`
- ✅ Cada contexto tem fonte rastreável
- ✅ Cada contexto é versionado

**Resultado esperado do sistema:**

> "Existe um banco de contexto versionado contendo: leis (14.133 etc.), acórdãos, modelos e doutrina."

---

## 🚫 Regras Canônicas

**Contexto Versionado:**

> "Contexto sem versão é contexto sem rastreabilidade. Versionamento é condição de passagem."

**Fonte Rastreável:**

> "Contexto sem fonte é prompt solto. Fonte rastreável é condição de passagem."

**Contexto como Artefato:**

> "Contexto é artefato de primeira classe. Contexto não é prompt solto."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Banco de contexto existe em `/PRODUTOS/contratacao-ti/CONTEXTO/`
- ✅ Banco contém:
  - Leis (Lei 14.133/2021, Lei 8.666/1993, etc.)
  - Acórdãos do TCU
  - Modelos de documentos
  - Doutrina
- ✅ Cada contexto tem fonte rastreável
- ✅ Cada contexto é versionado
- ✅ Estrutura de contexto segue governança

### FAIL

- ❌ Banco de contexto não existe
- ❌ Banco não contém todas as fontes
- ❌ Contexto não tem fonte rastreável
- ❌ Contexto não é versionado
- ❌ Estrutura não segue governança

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um banco de contexto versionado para contratação pública de TI. Isso gera:

1. **Falta de rastreabilidade:** Não é possível rastrear origem do contexto
2. **Inconsistência de legislação:** Legislação pode estar desatualizada
3. **Impossibilidade de auditoria:** Não é possível auditar conformidade
4. **Perda de qualidade:** Documentos podem não estar conformes

### Impacto

Sem banco de contexto:
- Rastreabilidade é perdida
- Legislação fica desatualizada
- Auditoria é impossível
- Qualidade não é garantida

---

## 🚫 DO / DON'T

### ✅ DO

- **Criar banco de contexto em `/PRODUTOS/contratacao-ti/CONTEXTO/`**
- **Incluir leis, acórdãos, modelos e doutrina**
- **Versionar cada contexto**
- **Incluir fonte rastreável em cada contexto**
- **Seguir estrutura de governança de contexto**

### ❌ DON'T

- **Criar contexto sem fonte**
- **Criar contexto sem versionamento**
- **Criar contexto fora do diretório canônico**
- **Tratar contexto como prompt solto**
- **Permitir contexto desatualizado sem marcação**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- **Depende de:** DEMANDA-METODO-011 (Governança de Contexto)
- **Depende de:** DEMANDA-PROD-001 (Produto 001 — Contratação TI)

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. **Legislação**
   - Lei 14.133/2021 (Nova Lei de Licitações)
   - Lei 8.666/1993 (Lei de Licitações antiga)
   - Decreto 11.462/2023
   - IN SGD/ME nº 1/2019

2. **Acórdãos**
   - Acórdãos do TCU sobre contratação de TI
   - Súmulas do TCU

3. **Modelos**
   - Modelos de ETP
   - Modelos de TR
   - Modelos de Edital

4. **Doutrina**
   - Artigos sobre contratação pública de TI
   - Livros sobre contratação pública

### Validações

1. Banco de contexto existe
2. Todas as fontes estão incluídas
3. Cada contexto tem fonte rastreável
4. Cada contexto é versionado
5. Estrutura segue governança

---

## ❌ Fora de Escopo

- Criação de outros bancos de contexto (isso será feito em demandas futuras)
- Implementação de software para gerenciar contexto
- Migração de contextos existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Contexto sem fonte é prompt solto. Contexto sem versionamento é perda de rastreabilidade. Banco de contexto é condição de passagem para qualquer produto no método END-FIRST."
