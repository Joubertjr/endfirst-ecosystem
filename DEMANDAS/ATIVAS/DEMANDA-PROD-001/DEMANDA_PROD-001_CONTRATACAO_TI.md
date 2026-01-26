---
demanda_id: DEMANDA-PROD-001
title: Produto 001 — Contratação Pública de TI
type: produto / contratação pública
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-PROD-001 — Produto 001: Contratação Pública de TI

**Tipo:** Produto / Contratação Pública  
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

- ✅ Existe um produto governado pelo método capaz de gerar: ETP, TR, Edital e anexos conforme legislação brasileira
- ✅ O produto está no diretório canônico `/PRODUTOS/contratacao-ti/`
- ✅ 1 fluxo completo gera 1 edital com evidência
- ✅ O produto segue a estrutura canônica de produto

**Resultado esperado do sistema:**

> "Existe um produto governado pelo método capaz de gerar: ETP, TR, Edital e anexos conforme legislação brasileira."

---

## 🚫 Regras Canônicas

**Produto Governado:**

> "Produto sem governança é software sem rastreabilidade. Produto governado é condição de passagem."

**Estrutura Canônica:**

> "Produto DEVE seguir estrutura canônica. Produto fora da estrutura é FAIL estrutural."

**Legislação como Contexto:**

> "Legislação é contexto versionado. Produto sem contexto não é auditável."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Produto existe em `/PRODUTOS/contratacao-ti/`
- ✅ Produto segue estrutura canônica:
  ```
  /PRODUTOS/contratacao-ti/
    README.md
    DEMANDAS/
    planejamento/
    EVIDENCIAS/
    CONTEXTO/
    OUTPUTS/
  ```
- ✅ Produto gera ETP, TR, Edital e anexos
- ✅ 1 fluxo completo gera 1 edital com evidência
- ✅ Legislação brasileira está no CONTEXTO/
- ✅ Outputs referenciam CONTEXTO usado

### FAIL

- ❌ Produto não existe no diretório canônico
- ❌ Produto não segue estrutura canônica
- ❌ Produto não gera todos os documentos
- ❌ Fluxo não gera edital completo
- ❌ Legislação não está no CONTEXTO/
- ❌ Outputs não referenciam CONTEXTO

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um produto governado pelo método capaz de gerar documentos de contratação pública de TI. Isso gera:

1. **Falta de rastreabilidade:** Não é possível rastrear origem dos documentos
2. **Inconsistência de legislação:** Legislação pode estar desatualizada
3. **Impossibilidade de auditoria:** Não é possível auditar conformidade
4. **Perda de qualidade:** Documentos podem não estar conformes

### Impacto

Sem produto governado:
- Rastreabilidade é perdida
- Legislação fica desatualizada
- Auditoria é impossível
- Qualidade não é garantida

---

## 🚫 DO / DON'T

### ✅ DO

- **Criar produto em `/PRODUTOS/contratacao-ti/`**
- **Seguir estrutura canônica de produto**
- **Gerar ETP, TR, Edital e anexos**
- **Incluir legislação brasileira no CONTEXTO/**
- **Referenciar CONTEXTO nos outputs**
- **Gerar evidência de execução**

### ❌ DON'T

- **Criar produto fora do diretório canônico**
- **Criar produto sem estrutura canônica**
- **Gerar documentos sem legislação no CONTEXTO/**
- **Gerar outputs sem referência ao CONTEXTO**
- **Gerar documentos sem evidência**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- **Depende de:** DEMANDA-METODO-010 (Governança de Produtos)
- **Depende de:** DEMANDA-METODO-011 (Governança de Contexto)
- **Depende de:** DEMANDA-METODO-012 (Versionamento Cruzado)

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. **Estrutura de Produto**
   - `/PRODUTOS/contratacao-ti/README.md`
   - `/PRODUTOS/contratacao-ti/DEMANDAS/`
   - `/PRODUTOS/contratacao-ti/planejamento/`
   - `/PRODUTOS/contratacao-ti/EVIDENCIAS/`
   - `/PRODUTOS/contratacao-ti/CONTEXTO/`
   - `/PRODUTOS/contratacao-ti/OUTPUTS/`

2. **Contexto**
   - Legislação brasileira (Lei 14.133/2021, etc.)
   - Acórdãos do TCU
   - Modelos de documentos
   - Doutrina

3. **Fluxo de Geração**
   - Fluxo END-FIRST para gerar edital
   - Templates de ETP, TR, Edital
   - Validação de conformidade

### Validações

1. Produto existe no diretório canônico
2. Estrutura canônica está completa
3. Legislação está no CONTEXTO/
4. Fluxo gera edital completo
5. Outputs referenciam CONTEXTO
6. Evidência é gerada

---

## ❌ Fora de Escopo

- Implementação de features avançadas (isso será feito em demandas futuras)
- Criação de outros produtos (isso será feito em demandas futuras)
- Migração de dados existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Produto sem governança é software sem rastreabilidade. Produto sem contexto não é auditável. Produto sem evidência não é rastreável. Produto governado é condição de passagem para qualquer produto no método END-FIRST."
