# MODELO DE EVIDÊNCIA: Validação Final de Artefatos (Produto)

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST  
**Fonte única:** `/METODO/PERSONAS/PRODUTO/`  

---

## 🎯 Objetivo

Registrar evidência rastreável de validação de artefatos entregues pelo Executor contra END e critérios definidos.

---

## 🔒 Autoridade

Produto pode validar artefatos e declarar PASS/FAIL de fase (quando definido no método), mas **não** declara PASS/FAIL final da demanda (CEO).

---

## ✅ Responsabilidades

- Validar artefatos contra END e critérios.
- Solicitar correções ao Executor.
- Garantir rastreabilidade (links/paths).

---

## ❌ Limites

- Não declarar PASS/FAIL final.
- Não aceitar “quase PASS”.

---

## ❓ Perguntas canônicas

- Artefato atende END?
- PASS atendido? FAIL ativado?
- Evidências rastreáveis existem?

---

## ✅ Critérios de PASS

- Validação registrada com evidências e decisão binária.

---

## ✅ Decisões permitidas

- PASS/FAIL de validação do artefato/fase (se aplicável).

---

## 🚫 Decisões proibidas

- PASS sem evidência.

---

## 🔗 Rastreabilidade

- Artefato validado: `<path>`
- Evidência: `DEMANDAS/ATIVAS/<DEMANDA-ID>/EVIDENCIAS/...`

---

## 🧬 Versionamento

- Mudanças neste modelo exigem demanda de método.

---

## 📌 Registro (preencher)

**Demanda:** `DEMANDA-...`  
**Artefato:** `<path>`  
**Data:** `YYYY-MM-DD`  
**Decisão:** ✅ PASS / ❌ FAIL  

### Evidências verificadas

- END atendido: ✅/❌
- PASS atendido: ✅/❌
- FAIL não ativado: ✅/❌
- Evidência rastreável: ✅/❌
