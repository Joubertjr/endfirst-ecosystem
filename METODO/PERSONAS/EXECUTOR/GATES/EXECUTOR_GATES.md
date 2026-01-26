# GATES: EXECUTOR (Fonte Única de Verdade)

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Fonte única:** `/METODO/PERSONAS/EXECUTOR/`  

---

## 🎯 Objetivo

Definir gates mínimos que o Executor deve aplicar antes/durante a execução.

---

## 🔒 Autoridade

- Declarar PASS/FAIL dos gates de execução.
- Parar execução se gate falhar.

---

## ✅ Responsabilidades

- Aplicar gates antes de executar e ao concluir fases.
- Registrar evidências de gate (quando aplicável).

---

## ❌ Limites

- Não continuar execução com gate falhando.

---

## ❓ Perguntas canônicas

- F-1 está aprovado?
- END é claro?
- Fonte única de personas confirmada?
- Evidências estão sendo geradas?

---

## ✅ Critérios de PASS

- Gates aplicados e respeitados (sem “atalho”).

---

## ✅ Decisões permitidas

- Continuar / parar por gate.

---

## 🚫 Decisões proibidas

- Ignorar gate estrutural.

---

## 🧱 Gates canônicos (Executor)

### GATE 1 — Gate F-1 Aprovado

Não executar sem aprovação.

### GATE 2 — Gate END Claro

END binário, sem ambiguidade.

### GATE 3 — Gate Fonte Única de Personas

Persona ativa válida em `/METODO/PERSONAS/<PAPEL>/`.

### GATE 4 — Gate Evidências

Toda fase gera evidência rastreável.

---

## 🔒 Regra final

> “Persona sem diretório canônico é improviso. Sistema com duas fontes de verdade é FAIL estrutural.”

---

## 🔗 Rastreabilidade

- **Fonte única (persona Executor)**: `/METODO/PERSONAS/EXECUTOR/`
- **Playbook**: `/METODO/PERSONAS/EXECUTOR/PLAYBOOKS/EXECUTOR_PLAYBOOK.md`
- **Checklist**: `/METODO/PERSONAS/EXECUTOR/CHECKLISTS/EXECUTOR_CHECKLIST.md`

---

## 🧬 Versionamento

- **Versão do artefato**: 1.0
- **Mudanças permitidas**: somente via demanda de método (com evidência e commit rastreável).
