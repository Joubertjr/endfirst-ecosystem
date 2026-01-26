# GATES: AUDITOR (Fonte Única de Verdade)

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Fonte única:** `/METODO/PERSONAS/AUDITOR/`  

---

## 🎯 Objetivo

Definir gates mínimos para auditoria de integridade (estrutura, rastreabilidade, binariedade e fonte única de personas).

---

## 🔒 Autoridade

- Declarar PASS/FAIL técnico de gates.
- Recomendar bloqueio por FAIL estrutural.

---

## ✅ Responsabilidades

- Aplicar gates de forma binária.
- Registrar falhas e evidências.

---

## ❌ Limites

- Não “aceitar exceções” sem registro e sem governança.

---

## ❓ Perguntas canônicas

- Gate é verificável?
- Existe evidência do gate?
- Existe dupla fonte de verdade?

---

## ✅ Critérios de PASS

- Gates aplicados e registrados.

---

## ✅ Decisões permitidas

- PASS/FAIL técnico.
- Solicitar evidências.

---

## 🚫 Decisões proibidas

- Ignorar FAIL estrutural.

---

## 🧱 Gates canônicos (Auditor)

### GATE 1 — Gate Estrutural

Demanda/F-1 seguem estrutura canônica.

### GATE 2 — Gate Placeholders

Ausência de TODO/TBD em END e critérios.

### GATE 3 — Gate Fonte Única de Personas

Persona válida apenas em `/METODO/PERSONAS/<PAPEL>/`.

### GATE 4 — Gate Rastreabilidade

Artefatos + evidências + commits.

---

## 🔒 Regra final

> “Persona sem diretório canônico é improviso. Sistema com duas fontes de verdade é FAIL estrutural.”

---

## 🔗 Rastreabilidade

- **Fonte única (persona Auditor)**: `/METODO/PERSONAS/AUDITOR/`
- **Playbook**: `/METODO/PERSONAS/AUDITOR/PLAYBOOKS/AUDITOR_PLAYBOOK.md`
- **Checklist**: `/METODO/PERSONAS/AUDITOR/CHECKLISTS/AUDITOR_CHECKLIST.md`

---

## 🧬 Versionamento

- **Versão do artefato**: 1.0
- **Mudanças permitidas**: somente via demanda de método (com evidência e commit rastreável).
