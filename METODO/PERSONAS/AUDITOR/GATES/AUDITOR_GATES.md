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

## ✅ Critérios de PASS (do papel)

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

1. **Gate Estrutural**: demanda/F-1 seguem estrutura canônica.
2. **Gate Placeholders**: ausência de TODO/TBD em END e critérios.
3. **Gate Rastreabilidade**: artefatos + evidências + commits.
4. **Gate Fonte Única de Personas**: persona válida apenas em `/METODO/PERSONAS/<PAPEL>/`.

---

## 🔒 Regra final

> “Persona sem diretório canônico é improviso. Sistema com duas fontes de verdade é FAIL estrutural.”
