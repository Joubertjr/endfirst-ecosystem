---
document_id: DEMANDA_METODO-007_F1
type: planning
parent_demand: DEMANDA-METODO-007
status: pending_approval
created_at: 2026-01-20
created_by: Manus (Agent)
approved_by: pending
governed_by: /METODO/END_FIRST_V2.md
version: 1.0
priority: ALTA
---

# F-1 (PLANEJAMENTO CANÔNICO) — DEMANDA-METODO-007

**Versão:** 1.0  
**Data de Criação:** 20 de Janeiro de 2026  
**Criado por:** Manus (Agent)  
**Status:** PENDENTE DE APROVAÇÃO DO CEO  
**Demanda:** DEMANDA-METODO-007 v1.0  
**Tipo:** Método / Governança  
**Prioridade:** ALTA (estruturalmente prioritária sobre METODO-006)

---

## 📋 REFERÊNCIA

**Demanda:** `/DEMANDAS_MANUS/DEMANDA_METODO-007_TDD_CLEAN_CODE_BLOQUEIO_ESTRUTURAL.md` (v1.0)  
**Issue:** Pendente de criação  
**Commit da demanda:** `83f0e09`  

---

## 🎯 OBJETIVO DESTE F-1

Este documento é o **planejamento canônico (F-1)** da DEMANDA-METODO-007 v1.0.

Conforme **OD-012 (Planning is a first-class artifact. Executor only executes.)**:
- Este F-1 define **o que será feito** e **como será feito**
- Nenhuma execução ocorre sem aprovação explícita do CEO
- O executor (Manus) apenas executa o que está planejado aqui

---

## 🔒 END DO F-1

Ao final da execução deste F-1, o método END-FIRST v2 terá:

1. ✅ **Critérios objetivos de Clean Code** definidos e verificáveis
2. ✅ **Governança de TDD e Clean Code** integrada ao END-FIRST v2
3. ✅ **Template de F-1 atualizado** com validação obrigatória de TDD/Clean Code
4. ✅ **`.cursorrules` atualizado** com bloqueios explícitos
5. ✅ **Evidência retroativa** documentada (DEMANDA-PROD-004)
6. ✅ **Regra formal ativa** no método: TDD e Clean Code como bloqueio estrutural

**Resultado observável:**
> "Nenhuma fase pode ser declarada PASS se código foi escrito antes de testes ou se critérios objetivos de Clean Code forem violados."

---

## 🚫 BLOQUEIOS ESTRUTURAIS

- 🔒 **Nenhuma implementação de ferramenta:** Esta demanda é de método, não de código
- 🔒 **Nenhum framework de teste específico:** Não escolher Jest, Vitest, etc.
- 🔒 **Nenhum linter obrigatório:** Não impor ESLint, Prettier, etc.
- 🔒 **Nenhuma automação de validação:** Não criar scripts de verificação
- 🔒 **Governar critérios, não implementações:** Definir o que validar, não como validar

---

## 📊 FASES DE EXECUÇÃO (F1-F6)

### FASE F1 — Definir Critérios Objetivos de Clean Code

**END desta fase:**
> Critérios objetivos de Clean Code existem e são verificáveis (não subjetivos).

**Tempo estimado:** 2-3 horas

**Artefato esperado:**
- `/METODO/CLEAN_CODE_CRITERIA.md`
- Critérios objetivos: tamanho de função, responsabilidade, complexidade ciclomática
- Critérios binários (PASS/FAIL)
- Exemplos de código que passa e que falha
- Marcadores grep-friendly

**Critérios de PASS:**
- ✅ Documento criado e versionado
- ✅ Critérios objetivos definidos (não "código limpo é bom")
- ✅ Critérios são binários e verificáveis
- ✅ Exemplos de PASS/FAIL fornecidos
- ✅ Nenhum framework ou linter específico mencionado

**Exemplo de critério objetivo:**
- Função com mais de 20 linhas = FAIL
- Função com mais de 3 responsabilidades = FAIL
- Complexidade ciclomática > 10 = FAIL

---

### FASE F2 — Adicionar Governança de TDD ao END-FIRST v2

**END desta fase:**
> END-FIRST v2 tem seção explícita "Governança de Qualidade de Código" com TDD e Clean Code como regras formais.

**Tempo estimado:** 2-3 horas

**Artefato esperado:**
- `/METODO/END_FIRST_V2.md` (v1.5 → v1.6)
- Seção "Governança de Qualidade de Código" adicionada
- TDD como regra formal (não recomendação)
- Critérios de Clean Code referenciados
- FAIL automático para violações

**Critérios de PASS:**
- ✅ Seção adicionada ao END_FIRST_V2.md
- ✅ TDD definido como bloqueio estrutural
- ✅ Referência a `/METODO/CLEAN_CODE_CRITERIA.md`
- ✅ Regra explícita: "Fase = FAIL se testes não precederam código"
- ✅ Versão incrementada (v1.5 → v1.6)

---

### FASE F3 — Atualizar Template de F-1

**END desta fase:**
> Template de F-1 exige validação formal de TDD/Clean Code; F-1 inválido sem essa seção preenchida.

**Tempo estimado:** 1-2 horas

**Artefato esperado:**
- `/METODO/TEMPLATE_DEMANDA_CANONICA.md` (v1.1 → v1.2)
- Seção "Validação de TDD e Clean Code" adicionada
- Campos obrigatórios:
  - TDD é obrigatório nesta demanda? (SIM / NÃO)
  - Evidência RED → GREEN → REFACTOR existe? (caminho do artefato)
  - Critérios de Clean Code aplicados? (lista de critérios)

**Critérios de PASS:**
- ✅ Seção adicionada ao template
- ✅ Campos obrigatórios especificados
- ✅ F-1 inválido se seção não for preenchida
- ✅ Versão incrementada (v1.1 → v1.2)

---

### FASE F4 — Atualizar `.cursorrules`

**END desta fase:**
> `.cursorrules` bloqueia execução fora das regras de TDD/Clean Code; Cursor opera sob contrato, não interpretação.

**Tempo estimado:** 1-2 horas

**Artefato esperado:**
- `.cursorrules` (atualizado)
- Regras explícitas:
  - ❌ Não escrever código antes de teste
  - ❌ Não declarar fase PASS sem evidência de TDD
  - ❌ Não criar funções acima do limite definido em CLEAN_CODE_CRITERIA
  - ❌ Não misturar responsabilidades

**Critérios de PASS:**
- ✅ Regras adicionadas ao `.cursorrules`
- ✅ Bloqueios explícitos (não sugestões)
- ✅ Referência a `/METODO/CLEAN_CODE_CRITERIA.md`
- ✅ Cursor não pode "interpretar" qualidade

---

### FASE F5 — Criar Evidência de Aplicação Retroativa

**END desta fase:**
> Análise documentada de DEMANDA-PROD-004 mostra onde o método deixou passar violações de TDD/Clean Code.

**Tempo estimado:** 2-3 horas

**Artefato esperado:**
- `/EVIDENCIAS/aplicacao_retroativa_metodo_007.md`
- Análise de DEMANDA-PROD-004:
  - Onde TDD foi violado
  - Onde Clean Code foi violado
  - Por que o método não bloqueou
- Comparativo método antigo vs novo
- Demonstração de como nova regra teria bloqueado

**Critérios de PASS:**
- ✅ Documento criado e versionado
- ✅ Análise de DEMANDA-PROD-004 documentada
- ✅ Comparativo método antigo vs novo
- ✅ Demonstração de bloqueio com nova regra

---

### FASE F6 — Declarar PASS

**END desta fase:**
> Regra ativa, documentada, verificável e integrada ao método.

**Tempo estimado:** 0.5-1 hora

**Artefato esperado:**
- `/DEMANDAS_MANUS/DEMANDA_METODO-007_F6_CONCLUSAO.md`
- Declaração de PASS
- Resumo de artefatos criados
- Validação de conformidade

**Critérios de PASS:**
- ✅ Todos os artefatos criados e versionados
- ✅ END alcançado
- ✅ Bloqueios estruturais respeitados
- ✅ Método atualizado e integrado

---

## 📊 RESUMO DAS FASES

| Fase | END | Artefato | Tempo |
|------|-----|----------|-------|
| F1 | Critérios objetivos de Clean Code definidos | `/METODO/CLEAN_CODE_CRITERIA.md` | 2-3h |
| F2 | Governança de TDD adicionada ao método | `/METODO/END_FIRST_V2.md` (v1.6) | 2-3h |
| F3 | Template de F-1 atualizado | `/METODO/TEMPLATE_DEMANDA_CANONICA.md` (v1.2) | 1-2h |
| F4 | `.cursorrules` atualizado | `.cursorrules` | 1-2h |
| F5 | Evidência retroativa criada | `/EVIDENCIAS/aplicacao_retroativa_metodo_007.md` | 2-3h |
| F6 | PASS declarado | `/DEMANDAS_MANUS/DEMANDA_METODO-007_F6_CONCLUSAO.md` | 0.5-1h |
| **TOTAL** | | **5 documentos + 1 atualização** | **9-14h** |

---

## 🔗 DEPENDÊNCIAS

**Dependências satisfeitas:**
- ✅ DEMANDA-METODO-007 v1.0 registrada
- ✅ Evidência de violação (DEMANDA-PROD-004) existe
- ✅ END-FIRST v2 (v1.5) existe
- ✅ Template de F-1 (v1.1) existe
- ✅ `.cursorrules` existe

**Nenhuma dependência bloqueante.**

---

## ⚠️ RISCOS E MITIGAÇÕES

### Risco 1: Critérios de Clean Code muito rígidos
**Probabilidade:** Média  
**Impacto:** Alto (bloqueio excessivo)  
**Mitigação:** Definir critérios objetivos mas razoáveis (ex: 20 linhas, não 10)

### Risco 2: Conflito com código existente
**Probabilidade:** Alta  
**Impacto:** Médio  
**Mitigação:** Regra é prospectiva (não retroativa); código existente não é alterado

### Risco 3: TDD obrigatório em todos os casos
**Probabilidade:** Baixa  
**Impacto:** Médio  
**Mitigação:** Template de F-1 permite declarar "TDD não obrigatório" com justificativa

---

## 📋 CRITÉRIOS DE APROVAÇÃO DO F-1

Para o CEO aprovar este F-1, os seguintes critérios devem ser satisfeitos:

1. ✅ **Fases bem definidas:** Cada fase tem END, artefato esperado, tempo estimado e critérios de PASS
2. ✅ **Bloqueios estruturais respeitados:** Nenhuma implementação de ferramenta, nenhum framework específico, nenhuma automação
3. ✅ **Critérios objetivos:** Clean Code tem critérios verificáveis (não subjetivos)
4. ✅ **TDD como bloqueio:** Não como recomendação, mas como regra formal
5. ✅ **Integração ao método:** Fase F2 integra ao END-FIRST v2, F3 atualiza template, F4 atualiza `.cursorrules`
6. ✅ **Tempo realista:** 9-14 horas estimadas (razoável para escopo de método)
7. ✅ **Prioridade estrutural justificada:** Método permite erro grave sem essa demanda

---

## 🧭 PRÓXIMOS PASSOS (APÓS APROVAÇÃO)

1. ✅ CEO aprova F-1
2. ✅ Status muda: F-1 PENDENTE → F-1 APROVADO
3. ✅ Execução começa (F1-F6)
4. ✅ Cada fase é executada sequencialmente
5. ✅ Artefatos são criados, versionados e integrados
6. ✅ DEMANDA-METODO-007 é declarada PASS

---

## 📜 DECLARAÇÃO CANÔNICA

> "Este F-1 governa a execução da DEMANDA-METODO-007. Nenhuma fase é executada sem este planejamento aprovado. Nenhuma decisão é tomada durante execução que não esteja prevista aqui."

> **"Qualidade não é uma expectativa. Qualidade é uma condição de passagem."**

---

**Status:** PENDENTE DE APROVAÇÃO DO CEO  
**Aguardando:** Validação e autorização explícita do CEO para executar

---

## 🔗 Referências

- `/DEMANDAS_MANUS/DEMANDA_METODO-007_TDD_CLEAN_CODE_BLOQUEIO_ESTRUTURAL.md` (v1.0)
- `/METODO/END_FIRST_V2.md` — Método END-FIRST v2 (v1.5)
- `/METODO/TEMPLATE_DEMANDA_CANONICA.md` — Template canônico (v1.1)
- `.cursorrules` — Regras do Cursor
- `/DEMANDAS_MANUS/DEMANDA-PROD-004_*` — Evidência de violação
