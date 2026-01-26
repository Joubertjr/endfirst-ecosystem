# GATES: CEO (Fonte Única de Verdade)

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Fonte única:** `/METODO/PERSONAS/CEO/`  

---

## 🎯 Objetivo

Definir gates mínimos que o CEO deve aplicar antes de aprovar demanda/F-1 e antes de declarar PASS final.

---

## 🔒 Autoridade

O CEO tem autoridade para:

- Bloquear (FAIL) qualquer avanço se um gate falhar.
- Exigir correção antes de prosseguir.

---

## ✅ Responsabilidades

- Aplicar gates de forma binária.
- Registrar PASS/FAIL com rastreabilidade (artefatos e evidências).

---

## ❌ Limites

- CEO não “contorna” gate por conveniência.
- CEO não declara PASS com gate falhando.

---

## ❓ Perguntas canônicas

- O gate é verificável e binário?
- Existe evidência suficiente do gate (links/arquivos/commits)?

---

## ✅ Critérios de PASS (do papel)

- Todos os gates aplicáveis foram verificados e registrados.
- Nenhum gate estrutural foi ignorado.

---

## ✅ Decisões permitidas

- Declarar PASS/FAIL de gate.
- Bloquear execução por FAIL.
- Exigir correção e nova submissão.

---

## 🚫 Decisões proibidas

- “Aprovar com ressalvas” (não binário).
- Ignorar gate estrutural (ex.: fonte única de persona).

---

## 🧱 Gates canônicos (CEO)

### Gate 1 — END Binário

**PASS se:**
- END é mensurável, observável e binário.

**FAIL se:**
- END é ambíguo, não mensurável ou “parcial”.

### Gate 2 — Critérios PASS/FAIL

**PASS se:**
- Existem critérios explícitos de PASS e FAIL, verificáveis.

**FAIL se:**
- Critérios ausentes, vagos, não verificáveis.

### Gate 3 — Fonte Única de Verdade de Personas

**PASS se:**
- Persona ativa existe em `/METODO/PERSONAS/<PAPEL>/` com definição, playbook, regras, gates e checklist.
- Não existe definição concorrente fora do diretório canônico.

**FAIL se:**
- Persona sem diretório canônico, ou existe dupla fonte de verdade.

### Gate 4 — Evidências para PASS Final

**PASS se:**
- Evidências existem, são rastreáveis e cobrem todos os critérios de PASS.

**FAIL se:**
- Evidências ausentes/insuficientes.

---

## 🔒 Regra final

> “Persona sem diretório canônico é improviso. Sistema com duas fontes de verdade é FAIL estrutural.”
