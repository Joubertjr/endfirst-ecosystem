# REGRA CANÔNICA: PAPEL ATIVO OBRIGATÓRIO

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Método:** END-FIRST v2

---

## 🔒 REGRA CANÔNICA

> **"Nenhuma fase do método pode ser executada sem papel ativo definido por artefato."**

---

## 📋 DEFINIÇÃO

**Papel ativo:** Papel responsável pela execução de uma fase específica do método, definido formalmente em artefato rastreável.

**Artefato rastreável:** Documento em `/METODO/PERSONAS/` que define:
- Objetivo do papel
- Autoridade do papel
- Responsabilidades do papel
- Limites do papel (o que NÃO pode decidir)
- Evidências exigidas pelo papel

---

## ✅ CRITÉRIOS DE PASS

Uma fase pode ser executada se:

1. ✅ Existe artefato de definição do papel em `/METODO/PERSONAS/DEFINICOES/`
2. ✅ Existe playbook do papel em `/METODO/PERSONAS/PLAYBOOKS/`
3. ✅ Existe vínculo papel-fase em `/METODO/PERSONAS/VINCULOS_PROCESSO/`
4. ✅ O papel ativo está explicitamente declarado no contexto
5. ✅ O papel ativo tem autoridade para executar a fase

---

## ❌ CRITÉRIOS DE FAIL

Uma fase NÃO pode ser executada se:

1. ❌ Não existe artefato de definição do papel
2. ❌ Não existe playbook do papel
3. ❌ Não existe vínculo papel-fase
4. ❌ O papel ativo não está declarado
5. ❌ O papel ativo não tem autoridade para executar a fase
6. ❌ O papel ativo está violando seus limites

---

## 🎯 APLICAÇÃO DA REGRA

### Exemplo 1: Execução de Fase

**Contexto:**
- Fase: F1 de DEMANDA-METODO-010
- Papel ativo: Executor

**Validação:**
1. ✅ Existe `/METODO/PERSONAS/DEFINICOES/EXECUTOR.md`?
2. ✅ Existe `/METODO/PERSONAS/PLAYBOOKS/EXECUTOR_PLAYBOOK.md`?
3. ✅ Existe vínculo Executor ↔ Execução de Fases em `/METODO/PERSONAS/VINCULOS_PROCESSO/PAPEL_FASE.md`?
4. ✅ Executor tem autoridade para executar fases?

**Resultado:** ✅ PASS — Fase pode ser executada

---

### Exemplo 2: Aprovação de Demanda

**Contexto:**
- Fase: Aprovação de DEMANDA-METODO-016
- Papel ativo: Executor

**Validação:**
1. ✅ Existe `/METODO/PERSONAS/DEFINICOES/EXECUTOR.md`?
2. ✅ Executor tem autoridade para aprovar demandas?
   - ❌ NÃO — Executor NÃO PODE aprovar demandas (limite do papel)

**Resultado:** ❌ FAIL — Fase não pode ser executada (violação de limite)

---

## 🔗 RASTREABILIDADE

Esta regra é implementada através de:

1. `/METODO/PERSONAS/DEFINICOES/` — Definições de papéis
2. `/METODO/PERSONAS/PLAYBOOKS/` — Playbooks operacionais
3. `/METODO/PERSONAS/VINCULOS_PROCESSO/` — Vínculos papel-fase-demanda-produto

---

## 🧭 IMPACTO

**Sem esta regra:**
- ❌ Executor pode tentar aprovar demandas
- ❌ CEO pode tentar implementar código
- ❌ Auditor pode aprovar por simpatia
- ❌ Governança é perdida

**Com esta regra:**
- ✅ Papel ativo é sempre conhecido
- ✅ Limites de papel são respeitados
- ✅ Governança é garantida
- ✅ Rastreabilidade é total

---

## 🔒 REGRA FINAL

> "Papel sem artefato é improviso. Fase sem papel ativo é FAIL estrutural."
