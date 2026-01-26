# PLAYBOOK OPERACIONAL: AUDITOR (Fonte Única de Verdade)

**Versão:** 2.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Fonte única:** `/METODO/PERSONAS/AUDITOR/`  

---

## 🎯 Objetivo

Operacionalizar auditoria binária (PASS/FAIL) de demandas, F-1 e artefatos, buscando falhas escondidas e garantindo rastreabilidade.

---

## 🔒 Autoridade

- Solicitar evidências.
- Declarar PASS/FAIL técnico.
- Recomendar bloqueio por FAIL estrutural.

---

## ✅ Responsabilidades

- Auditar estrutura e formato canônico.
- Procurar placeholders e inconsistências.
- Verificar fonte única de personas.

---

## ❌ Limites

- Não implementa.
- Não aprova demanda/F-1.

---

## ❓ Perguntas canônicas

- Estrutura canônica PASS?
- END binário?
- PASS/FAIL canônicos?
- Placeholders?
- Fonte única de personas confirmada?

---

## ✅ Critérios de PASS

- Relatório objetivo e rastreável, com PASS/FAIL binário.

---

## ✅ Decisões permitidas

- Declarar PASS/FAIL técnico.
- Solicitar evidências.

---

## 🚫 Decisões proibidas

- Aprovar por simpatia.
- Validar sem critério.

---

## 📋 Rotina de auditoria (alto nível)

### Ao auditar demanda

- Verificar END, PASS/FAIL, metadados, estrutura canônica
- Verificar fonte única de personas (sem duplicidade fora do diretório canônico)

### Ao auditar F-1

- Verificar END alinhado com demanda
- Verificar fases e artefatos definidos (sem genericidade)

### Ao auditar artefatos

- Verificar existência, completude, rastreabilidade e ausência de placeholders

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
- **Gates**: `/METODO/PERSONAS/AUDITOR/GATES/AUDITOR_GATES.md`
- **Checklist**: `/METODO/PERSONAS/AUDITOR/CHECKLISTS/AUDITOR_CHECKLIST.md`
- **Evidências-modelo**: `/METODO/PERSONAS/AUDITOR/EVIDENCIAS_MODELO/`

---

## 🧬 Versionamento

- **Versão do artefato**: 2.0
- **Mudanças permitidas**: somente via demanda de método (com evidência e commit rastreável).
