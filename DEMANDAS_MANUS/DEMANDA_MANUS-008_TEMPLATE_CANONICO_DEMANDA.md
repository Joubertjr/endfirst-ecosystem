---
demanda_id: DEMANDA_MANUS-008
title: Template Canônico de Demanda (END-FIRST v2)
type: Método / Governança
method: END-FIRST v2
status: doing
scope: Ecossistema END-FIRST (todas as demandas futuras)
impact: Global / Estrutural
created_at: 2026-01-19
created_by: CEO (Joubert Jr)
executor: Manus (Agent)
---

# DEMANDA_MANUS-008 — TEMPLATE CANÔNICO DE DEMANDA (END-FIRST v2)

**Tipo:** Método / Governança  
**Método:** END-FIRST v2  
**Status:** DOING  
**Escopo:** Ecossistema END-FIRST (todas as demandas futuras)  
**Impacto:** Global / Estrutural

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existe **UM template canônico oficial de demanda**
- ✅ Toda demanda futura deve **obrigatoriamente** usar esse template
- ✅ Demandas fora do template são **FAIL estrutural**
- ✅ Não é mais necessário revisar manualmente demandas
- ✅ Não existe ambiguidade entre:
  - bug
  - UX
  - produto
  - método
- ✅ Todas as demandas:
  - possuem END explícito
  - possuem critérios binários
  - possuem bloqueios estruturais claros
  - possuem frases canônicas explícitas
- ✅ O executor (Cursor) nunca interpreta
- ✅ O arquiteto/CEO não revisa texto, apenas aprova F-1

**Resultado esperado do sistema:**

> Criar uma demanda passa a ser um ato determinístico, verificável e bloqueante — não um texto interpretável.

---

## 🧠 Problema Observado (Causa Raiz)

Durante a execução real do projeto CoverageSummarizer:

- Demandas precisaram ser revisadas múltiplas vezes
- Critérios foram endurecidos tardiamente
- Regras importantes (ex.: UX sem scroll, vazamento técnico, progresso perceptível) surgiram durante a execução
- Bugs de UX se confundiram com refinamentos
- O CEO precisou "reexplicar" padrões várias vezes

**Causa raiz identificada:**

> O método END-FIRST v2 não define um template canônico obrigatório de demanda.

**Sem template:**
- Cada demanda vira um texto diferente
- Regras ficam implícitas
- Frases canônicas se perdem
- Overhead cognitivo cresce
- Revisão vira trabalho humano recorrente

---

## 🧱 Proposta (Obrigatória)

Criar um **TEMPLATE CANÔNICO DE DEMANDA** como artefato de primeira classe do método END-FIRST v2.

---

## 🔒 TEMPLATE CANÔNICO — REGRAS ABSOLUTAS

### 1️⃣ Estrutura Obrigatória (NÃO NEGOCIÁVEL)

Toda demanda DEVE conter, nesta ordem:

1. **Cabeçalho canônico**
2. **🔒 END (Resultado Observável)**
3. **🚫 Regras Canônicas** (quando aplicável)
4. **✅ Critérios de Aceitação** (PASS / FAIL binários)
5. **🧠 Problemas Observados** (contexto, não tarefas)
6. **🚫 DO / DON'T**
7. **🧱 Bloqueios Estruturais**
8. **📋 TODO Canônico**
9. **❌ Fora de Escopo**
10. **📌 Status**
11. **🧭 Regra Final** (frase canônica de fechamento)

**Qualquer demanda sem uma dessas seções é FAIL estrutural.**

---

### 2️⃣ Frases Canônicas Obrigatórias

Todo template DEVE conter frases canônicas explícitas.

**Exemplos (obrigatórias conforme tipo da demanda):**

- **Planejamento:**  
  > "Planejamento é artefato de primeira classe. Executor apenas executa."

- **UX:**  
  > "UX deve comunicar atividade contínua perceptível durante etapas longas, mesmo quando o percentual não muda."

- **Legibilidade:**  
  > "Se o usuário não vê o conteúdo imediatamente, o produto falhou."

- **Governança:**  
  > "Ausência de critério binário é FAIL estrutural."

**Demandas sem frases canônicas explícitas são FAIL.**

---

### 3️⃣ Regra de UX Canônica (GLOBAL)

Adicionar ao método:

> **Scroll interno é PROIBIDO.**

- Nenhum componente pode esconder conteúdo
- Todo bloco deve expandir verticalmente
- Conteúdo invisível ou cortado é BUG estrutural
- Isso vale para:
  - UX refinements
  - bugs
  - produto
  - evidências

**Essa regra deve constar:**
- no template
- na ontologia (OD)
- nas instruções do Cursor

---

### 4️⃣ Classificação Estrutural (eliminar ambiguidade)

O template DEVE obrigar a demanda a declarar explicitamente:

- **Tipo:** Bug / UX / Produto / Método
- Se altera ou não funcionalidade
- Se exige F-1 obrigatória

**Regra canônica:**

> "Dúvida entre bug e UX é FAIL de planejamento."

---

## 📦 Entregáveis Esperados

1. **📄 Arquivo oficial do template:**
   - `METODO/TEMPLATE_DEMANDA_CANONICA.md`

2. **🔁 Atualização de documentação:**
   - `PILAR_ENDFIRST.md`
   - `END_FIRST_V2.md`
   - `CURSOR_INSTRUCTIONS.md`
   - `ONTOLOGY_DECISIONS.md` (nova OD)

3. **🧠 Nova Ontology Decision:**
   - OD-013: Template de Demanda é Obrigatório

4. **📜 Registro no APPROVAL_LOG.md**

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Template único existe
- ✅ Template documentado como obrigatório
- ✅ Frases canônicas explícitas
- ✅ Regras de UX e legibilidade formalizadas
- ✅ Cursor instruído a rejeitar demandas fora do template
- ✅ Método END-FIRST v2 atualizado

### FAIL

- ❌ Template opcional
- ❌ Frases canônicas implícitas
- ❌ Espaço para interpretação
- ❌ "Cada demanda é diferente"
- ❌ Revisão humana recorrente

---

## 🧱 Bloqueios Estruturais

- 🔒 Manus não aceita demandas fora do template
- 🔒 Cursor não executa demandas fora do template
- 🔒 CEO não revisa demandas que não sigam o template
- 🔒 Template é fonte única da verdade

---

## 📌 Status

**DOING**

Execução autorizada pelo CEO.

---

## 🧭 Regra Final (Canônica)

> **Se uma demanda precisa ser explicada, ela está errada.**  
> **Se precisa ser revisada várias vezes, o método falhou.**

---

**Governado por:** `/METODO/END_FIRST_V2.md`  
**Path Canônico:** `/DEMANDAS_MANUS/DEMANDA_MANUS-008_TEMPLATE_CANONICO_DEMANDA.md`  
**Refs:** #13 (pendente criação)
