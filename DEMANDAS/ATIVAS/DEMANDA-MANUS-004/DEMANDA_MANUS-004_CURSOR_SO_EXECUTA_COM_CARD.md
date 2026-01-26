---
demanda_id: DEMANDA_MANUS-004
title: Regra: Cursor só executa com Card
status: backlog
created_at: 2026-01-11
created_by: CEO
assigned_to: Manus (Agent)
priority: high
governed_by: /METODO/PILAR_ENDFIRST.md
version: 1.0
---

# DEMANDA_MANUS-004 — Regra: Cursor só executa com Card

**Versão:** 1.0  
**Data de Criação:** 11 de Janeiro de 2026  
**Solicitado por:** CEO  
**Executor:** Manus (Agent)  
**Status:** BACKLOG

---

## 🎯 END (IMUTÁVEL)

> "Cursor só executa trabalho se existir card no Kanban. Sem card → sem execução → commit inválido por design."

---

## 📋 CONTEXTO

**Situação detectada:**

Execuções do Cursor sem rastreabilidade total por card, o que:
- Viola KANBAN_CANONICO.md
- Viola CONTRATO_ESTADOS.md
- Reintroduz metacognição humana ("alguém precisa lembrar")

**Problema estrutural:**

Cursor pode executar trabalho sem card associado, criando:
- Execução invisível
- Status narrativo
- Dependência de disciplina humana

**Solução:**

Selar estruturalmente a regra:

> **No card, no work.**

---

## 🔒 ESCOPO DESTA DEMANDA

⚠️ **Esta demanda está em BACKLOG.** Não executar ainda.

**Quando for executada, deverá:**

1. Atualizar documentação para deixar explícito que:
   - Cursor só trabalha se houver card
   - Commit sem `Refs #X` é inválido
   - Bloquear interpretação humana

2. Tornar a regra impossível de "não saber"

---

## 📦 ENTREGÁVEIS ESPERADOS (FUTURO)

⚠️ **Manus não executa agora, apenas registra.**

**Quando executada, atualizar:**

1. **EXECUTOR_ONBOARDING_PROCESS.md**
   - Adicionar regra explícita: "Cursor só executa com card"
   - Fluxo obrigatório: Card existe → Cursor move para DOING → Cursor executa

2. **CURSOR_INSTRUCTIONS.md**
   - Reforçar regra: "Sem card, sem execução"
   - Adicionar exemplos de bloqueio estrutural

3. **KANBAN_CANONICO.md**
   - Regra explícita: "Execução sem card é inválida"
   - Automação: Sistema detecta commits sem `Refs #X`

4. **CONTRATO_ESTADOS.md**
   - Regra: "Cursor não move card que não existe"
   - Bloqueio: Commit sem card = erro estrutural

5. **PROMPT_CURSOR.md** (stub)
   - Atualizar para apontar para regra

6. **README.md**
   - Frase cultural: "No card, no work"

7. **(Opcional) Template de Issue**
   - Template obrigatório com campo "Card associado: #X"

---

## ✅ CRITÉRIOS DE ACEITAÇÃO (FUTURO)

**Quando executada, validar:**

- [ ] Cursor não consegue executar sem card (bloqueio estrutural)
- [ ] Commit sem card é estruturalmente inválido
- [ ] Nenhuma regra depende de "lembrar" ou "atenção"
- [ ] Documentação explícita em todos os arquivos relevantes
- [ ] Frase cultural no README
- [ ] Template de issue (se aplicável) com campo obrigatório

---

## 🚫 RESTRIÇÕES

**Proibido:**
- ❌ Manus NÃO executa agora
- ❌ Manus NÃO cria commits agora
- ❌ Manus NÃO atualiza documentos agora

**Permitido:**
- ✅ Manus SOMENTE:
  - Cria o arquivo da DEMANDA
  - Cria o card no Kanban
  - Deixa em BACKLOG

---

## 📊 STATUS ESPERADO APÓS ESTA AÇÃO

**DEMANDA_MANUS-004:**
- 📍 Existe no Git
- 📍 Existe no Kanban
- 📍 Estado: BACKLOG
- 📍 Execução: NÃO iniciada

---

## 🧠 PRINCÍPIO ONTOLÓGICO APLICADO

**OD-009:** Processo > Disciplina  
**OD-011 (estendida):** Metacognição fora do caminho crítico

**Frase canônica:**
> "Se o Cursor precisar lembrar de pedir card, o design falhou."

---

## 📝 OBSERVAÇÃO FINAL

**Registrar demanda ≠ executar demanda**

Backlog é compromisso futuro, não ação presente.

---

## 📜 HISTÓRICO DE MUDANÇAS

| Data | Versão | Mudança | Autor |
|------|--------|---------|-------|
| 2026-01-11 | 1.0 | DEMANDA_MANUS-004 criada e colocada em BACKLOG | CEO |

---

**Governado por:** `/METODO/PILAR_ENDFIRST.md`  
**Path Canônico:** `/DEMANDAS_MANUS/DEMANDA_MANUS-004_CURSOR_SO_EXECUTA_COM_CARD.md`
