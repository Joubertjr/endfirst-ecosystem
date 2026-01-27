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

## 🔒 FONTE ÚNICA DE VERDADE (PERSONAS)

> “Persona só é válida se existir em /METODO/PERSONAS//.
> Qualquer definição fora disso é FAIL estrutural.”

**Interpretação canônica:**

- A única fonte válida de persona é o diretório canônico: `/METODO/PERSONAS/<PAPEL>/`
- Diretórios/arquivos legados fora do diretório canônico (ex.: `/METODO/PERSONAS/DEFINICOES/`) **não** são fonte de verdade

---

## 🔒 REGRA: DIRETÓRIO CANÔNICO OBRIGATÓRIO

> “Nenhuma persona pode ser ativada sem diretório próprio em /METODO/PERSONAS// contendo definição, playbook, regras, gates e checklist.”

---

## ✅ CRITÉRIOS DE PASS

Uma fase pode ser executada se:

1. ✅ A persona existe no diretório canônico em `/METODO/PERSONAS/<PAPEL>/`
2. ✅ Existe artefato de definição do papel em `/METODO/PERSONAS/<PAPEL>/DEFINICOES/`
3. ✅ Existe playbook do papel em `/METODO/PERSONAS/<PAPEL>/PLAYBOOKS/`
4. ✅ Existe regras do papel em `/METODO/PERSONAS/<PAPEL>/REGRAS/`
5. ✅ Existe gates do papel em `/METODO/PERSONAS/<PAPEL>/GATES/`
6. ✅ Existe checklist do papel em `/METODO/PERSONAS/<PAPEL>/CHECKLISTS/`
3. ✅ Existe vínculo papel-fase em `/METODO/_PROCESSOS/VINCULOS_PROCESSO/`
4. ✅ O papel ativo está explicitamente declarado no contexto
5. ✅ O papel ativo tem autoridade para executar a fase

---

## ❌ CRITÉRIOS DE FAIL

Uma fase NÃO pode ser executada se:

1. ❌ A persona não existe no diretório canônico `/METODO/PERSONAS/<PAPEL>/`
2. ❌ Existe definição concorrente fora do diretório canônico (duas fontes de verdade)
3. ❌ Não existe definição do papel no diretório canônico
4. ❌ Não existe playbook do papel no diretório canônico
5. ❌ Não existe regras/gates/checklist do papel no diretório canônico
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
1. ✅ Existe `/METODO/PERSONAS/EXECUTOR/DEFINICOES/EXECUTOR.md`?
2. ✅ Existe `/METODO/PERSONAS/EXECUTOR/PLAYBOOKS/EXECUTOR_PLAYBOOK.md`?
3. ✅ Existe vínculo Executor ↔ Execução de Fases em `/METODO/_PROCESSOS/VINCULOS_PROCESSO/PAPEL_FASE.md`?
4. ✅ Executor tem autoridade para executar fases?

**Resultado:** ✅ PASS — Fase pode ser executada

---

### Exemplo 2: Aprovação de Demanda

**Contexto:**
- Fase: Aprovação de DEMANDA-METODO-016
- Papel ativo: Executor

**Validação:**
1. ✅ Existe `/METODO/PERSONAS/EXECUTOR/DEFINICOES/EXECUTOR.md`?
2. ✅ Executor tem autoridade para aprovar demandas?
   - ❌ NÃO — Executor NÃO PODE aprovar demandas (limite do papel)

**Resultado:** ❌ FAIL — Fase não pode ser executada (violação de limite)

---

## 🔗 RASTREABILIDADE

Esta regra é implementada através de:

1. `/METODO/PERSONAS/<PAPEL>/DEFINICOES/` — Definições de papéis (fonte única)
2. `/METODO/PERSONAS/<PAPEL>/PLAYBOOKS/` — Playbooks operacionais (fonte única)
3. `/METODO/PERSONAS/<PAPEL>/REGRAS/` — Regras do papel (fonte única)
4. `/METODO/PERSONAS/<PAPEL>/GATES/` — Gates do papel (fonte única)
5. `/METODO/PERSONAS/<PAPEL>/CHECKLISTS/` — Checklists do papel (fonte única)
6. `/METODO/_PROCESSOS/VINCULOS_PROCESSO/` — Vínculos papel-fase-demanda-produto

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
