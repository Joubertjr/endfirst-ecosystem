# CHECKLIST: AUDITOR (Fonte Única de Verdade)

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Fonte única:** `/METODO/PERSONAS/AUDITOR/`  

---

## 🎯 Objetivo

Checklist operacional para auditoria rápida e binária (PASS/FAIL).

---

## 🔒 Autoridade

- Declarar PASS/FAIL técnico.
- Solicitar evidências.

---

## ✅ Responsabilidades

- Validar estrutura, binariedade, rastreabilidade e fonte única de personas.

---

## ❌ Limites

- Não aprovar demanda/F-1.
- Não implementar.

---

## ❓ Perguntas canônicas

- Existe END binário?
- Existem PASS/FAIL verificáveis?
- Existem placeholders?
- Existe dupla fonte de verdade?

---

## ✅ Critérios de PASS

- Checklist aplicado e resultado registrado objetivamente.

---

## ✅ Decisões permitidas

- PASS/FAIL técnico.
- Solicitar evidências.

---

## 🚫 Decisões proibidas

- Aprovar por simpatia.
- Ignorar FAIL estrutural.

---

## ✅ Checklist

- [ ] END explícito e binário
- [ ] PASS/FAIL em formato canônico
- [ ] Sem marcadores de incompletude (ex.: itens pendentes sem definição)
- [ ] Evidências e rastreabilidade presentes
- [ ] Fonte única de personas confirmada (`/METODO/PERSONAS/<PAPEL>/`)

---

## 🔒 Regra final

> “Persona sem diretório canônico é improviso. Sistema com duas fontes de verdade é FAIL estrutural.”

---

## 🧱 Gates (referência explícita)

- **GATE 1** — Gate Estrutural (ver `../GATES/AUDITOR_GATES.md`)
- **GATE 2** — Gate Placeholders (ver `../GATES/AUDITOR_GATES.md`)
- **GATE 3** — Gate Fonte Única de Personas (ver `../GATES/AUDITOR_GATES.md`)

---

## 🔗 Rastreabilidade

- **Fonte única (persona Auditor)**: `/METODO/PERSONAS/AUDITOR/`
- **Playbook**: `/METODO/PERSONAS/AUDITOR/PLAYBOOKS/AUDITOR_PLAYBOOK.md`
- **Gates**: `/METODO/PERSONAS/AUDITOR/GATES/AUDITOR_GATES.md`

---

## 🧬 Versionamento

- **Versão do artefato**: 1.0
- **Mudanças permitidas**: somente via demanda de método (com evidência e commit rastreável).
