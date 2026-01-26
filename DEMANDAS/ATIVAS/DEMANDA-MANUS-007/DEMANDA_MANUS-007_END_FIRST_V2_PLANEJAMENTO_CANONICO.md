---
demanda_id: DEMANDA_MANUS-007
title: END-FIRST v2 — Planejamento como Artefato Canônico
status: cancelled
created_at: 2026-01-19
created_by: CEO
assigned_to: Manus (Agent)
priority: critical
governed_by: /METODO/PILAR_ENDFIRST.md
version: 1.0
---

# DEMANDA_MANUS-007 — END-FIRST v2: Planejamento como Artefato Canônico

**Versão:** 1.0  
**Data de Criação:** 19 de Janeiro de 2026  
**Solicitado por:** CEO  
**Executor:** Manus (Agent)  
**Status:** CANCELLED

**Motivo do cancelamento:** Conteúdo incorporado ao método. END-FIRST v2 já existe, já foi atualizado (v1.5) e já foi aplicado com sucesso. O que resta não é mais "demanda" crítica, é manutenção editorial que ocorre fora de DOING.

**Decisão:** CEO (2026-01-20)

**Observação:** Planejamento não é mais trabalho crítico, é higiene.  
**Tipo:** Methodology / Governance / END-FIRST

---

## 🎯 END (IMUTÁVEL)

> "Evoluir o método END-FIRST para v2 com novo estágio obrigatório F-1 (Planejamento Canônico BLOQUEANTE), documentado canonicamente no repositório, eliminando retrabalho de validação e interpretação durante execução."

---

## 📋 CONTEXTO (PROBLEMA OBSERVADO)

Durante a execução real de um projeto complexo, foi observado **retrabalho sistemático** entre:
- Arquiteto (humano)
- Executor (Cursor)
- Validações manuais repetidas

**O problema não foi:**
- ❌ Técnico
- ❌ Qualidade de código
- ❌ Execução do Cursor

**A causa raiz foi metodológica:**

O método END-FIRST atual **não trata planejamento como artefato canônico governado**, o que gera:
- Interpretação durante execução
- Endurecimento tardio de regras
- Ciclos repetidos de validação
- Overhead cognitivo e operacional

**Evidência empírica:** Múltiplas iterações planejamento ⇄ execução documentadas.

---

## 🔍 DIAGNÓSTICO (CAUSA RAIZ)

O método END-FIRST atualmente:
- Assume que "planejar" ≈ "executar"
- Não exige aprovação explícita do plano
- Não diferencia planejamento, TODO e execução
- Permite que o executor interprete regras durante a execução

**👉 Isso não escala sob carga real.**

---

## 🔒 PROPOSTA (OBRIGATÓRIA)

Introduzir **evolução canônica do método END-FIRST para v2**.

### F-1 — Planejamento Canônico (BLOQUEANTE)

**Este estágio passa a ser obrigatório antes de qualquer execução.**

#### END (Resultado Esperado)
- ✅ Existe 1 documento único de planejamento canônico
- ✅ Existe 1 TODO canônico derivado do plano
- ✅ Escopo DO / DON'T explícito
- ✅ Ordem de execução explícita
- ✅ Critérios de FAIL explícitos
- ✅ Strings de prova definidas (quando aplicável)

#### DONE WHEN
- ✅ Declaração explícita no relatório: **"F-1 aprovada"**
- ✅ Nenhum comando foi executado
- ✅ Nenhum código foi alterado

#### PROIBIÇÕES (FAIL automático)
- ❌ Executar comandos
- ❌ Criar código
- ❌ Criar automações
- ❌ "Validar rapidamente"
- ❌ Interpretar regras durante execução

---

## 🧱 REGRA GLOBAL (CANÔNICA)

> **"Planejamento é artefato de primeira classe."**

- O executor (Cursor) **apenas executa**
- Arquitetura, governança e escopo **só existem antes da F-1 aprovada**

---

## 📊 IMPACTO ESPERADO

Após END-FIRST v2:
- ✅ Zero retrabalho de validação
- ✅ Zero interpretação durante execução
- ✅ Cursor atua como executor literal
- ✅ Arquitetura e governança ficam estáveis
- ✅ Redução drástica de overhead cognitivo
- ✅ Método passa a escalar para projetos complexos

---

## 📦 ENTREGÁVEIS

**Manus deve entregar:**

1. **Documento canônico END-FIRST v2**
   - Path: `/METODO/END_FIRST_V2.md`
   - Conteúdo: Evolução do método com F-1 obrigatório
   - Estrutura: Contexto, Diagnóstico, Proposta, Regras, Impacto

2. **Atualização de PILAR_ENDFIRST.md**
   - Referência explícita a END-FIRST v2
   - Link para documento canônico

3. **Atualização de ONTOLOGY_DECISIONS.md**
   - Criar OD-012: "Planejamento é artefato de primeira classe"
   - Referência a F-1 como estágio obrigatório

4. **Atualização de CURSOR_INSTRUCTIONS.md**
   - Adicionar regra: "Sem F-1 aprovada, não executar"
   - Bloqueio estrutural para execução sem planejamento

5. **Atualização de APPROVAL_LOG.md**
   - Registrar novos documentos governados
   - Versionar mudanças

6. **Parecer estrutural**
   - Análise de impacto em documentos existentes
   - Validação de conformidade com ODs atuais
   - Decisão final: APROVADO / AJUSTAR / REJEITADO

---

## ✅ CRITÉRIOS DE ACEITAÇÃO

- [ ] Documento END-FIRST v2 criado em `/METODO/END_FIRST_V2.md`
- [ ] PILAR_ENDFIRST.md atualizado com referência a v2
- [ ] ONTOLOGY_DECISIONS.md atualizado com OD-012
- [ ] CURSOR_INSTRUCTIONS.md atualizado com bloqueio F-1
- [ ] APPROVAL_LOG.md atualizado com novos documentos
- [ ] Parecer estrutural entregue
- [ ] Commit criado com "Refs #[ISSUE_NUMBER]"
- [ ] Commit aguardando validação do CEO antes do push

---

## 🚫 RESTRIÇÕES

**Proibido:**
- ❌ Executar sem DEMANDA_MANUS-007
- ❌ Criar código ou automações
- ❌ Mudanças em documentos não listados em entregáveis
- ❌ Exceção estrutural (CEO não autorizou)

**Permitido:**
- ✅ Análise de impacto em documentos existentes
- ✅ Criação de novos documentos canônicos
- ✅ Atualização de documentos governados
- ✅ Versionamento no APPROVAL_LOG

---

## 🧠 PRINCÍPIOS ONTOLÓGICOS APLICADOS

**OD-007:** Single source of truth → END-FIRST v2 será fonte canônica  
**OD-009:** Processo > Disciplina → F-1 bloqueia execução por design  
**OD-010:** RESULT é entidade primária → Planejamento tem END explícito  
**OD-011 (estendida):** Metacognição fora do caminho crítico → Executor não interpreta

**Novo (proposto):**  
**OD-012:** Planejamento é artefato de primeira classe → F-1 obrigatório

---

## 📜 EVIDÊNCIA

Esta proposta nasce de **uso real do método**, com múltiplos ciclos de retrabalho documentados durante:
- Endurecimento tardio de regras
- Redefinição de escopo
- Validações repetidas

**Não é opinião. É evidência empírica.**

---

## 📜 HISTÓRICO DE MUDANÇAS

| Data | Versão | Mudança | Autor |
|------|--------|---------|-------|
| 2026-01-19 | 1.0 | DEMANDA_MANUS-007 criada e movida para DOING | CEO |

---

**Governado por:** `/METODO/PILAR_ENDFIRST.md`  
**Path Canônico:** `/DEMANDAS_MANUS/DEMANDA_MANUS-007_END_FIRST_V2_PLANEJAMENTO_CANONICO.md`
