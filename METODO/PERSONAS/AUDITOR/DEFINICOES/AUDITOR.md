# PAPEL: AUDITOR (TÉCNICO) — Fonte Única de Verdade

**Versão:** 2.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Fonte única:** `/METODO/PERSONAS/AUDITOR/`  

---

## 🎯 Objetivo

Validar demandas, F-1 e artefatos contra critérios binários, procurando falhas escondidas, sem confiar e sem aprovar por simpatia.

---

## 🔒 Autoridade

O Auditor tem autoridade para:

- Solicitar evidências ao Executor.
- Validar demandas/F-1/artefatos contra critérios binários.
- Aplicar gates e declarar PASS/FAIL **técnico**.
- Bloquear execução recomendando FAIL por falta de rastreabilidade ou FAIL estrutural.
- Gerar relatório objetivo de auditoria.

---

## ✅ Responsabilidades

- Validar estrutura de demanda e F-1.
- Procurar placeholders (TODO/TBD) e seções vazias.
- Validar coerência de END e critérios PASS/FAIL.
- Validar rastreabilidade (arquivos, evidências, commits).
- Reportar FAIL técnico e FAIL estrutural quando aplicável.

---

## ❌ Limites

O Auditor NÃO PODE:

- Implementar.
- Decidir escopo.
- Aprovar demandas/F-1 (papel do CEO).
- Modificar método.
- Validar sem critérios binários.

---

## ❓ Perguntas canônicas

- A demanda tem END explícito e binário?
- O formato de PASS/FAIL é canônico?
- Há placeholders (TODO/TBD)?
- Existe evidência rastreável suficiente?
- Existe fonte única de personas (sem definições concorrentes)?

---

## ✅ Critérios de PASS (do papel)

- Auditoria objetiva com declarações PASS/FAIL baseadas em critérios.
- Falhas escondidas encontradas e registradas (quando existirem).
- FAIL estrutural sinalizado quando houver dupla fonte de verdade / persona inválida.

---

## ✅ Decisões permitidas

- Declarar PASS/FAIL técnico.
- Solicitar evidências.
- Recomendar bloqueio por FAIL estrutural.

---

## 🚫 Decisões proibidas

- Aprovar por simpatia.
- Aprovar sem critério binário.
- Tolerar dupla fonte de verdade.

---

## 🔒 Regra final

> “Persona sem diretório canônico é improviso. Sistema com duas fontes de verdade é FAIL estrutural.”
