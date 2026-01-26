# MODELO: Evidência — Aprovação de Demanda (Produto)

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST  
**Fonte única:** `/METODO/PERSONAS/PRODUTO/`  

---

## 🎯 Objetivo

Registrar evidência rastreável da **submissão** e dos critérios de prontidão de uma demanda criada por Produto para aprovação do CEO.

---

## 🔒 Autoridade

Produto pode criar a demanda e declarar “pronta para aprovação”, mas **não** aprova.

---

## ✅ Responsabilidades

- Garantir END binário e mensurável.
- Garantir PASS/FAIL verificáveis.
- Garantir fora de escopo explícito.
- Garantir referência às personas na fonte única `/METODO/PERSONAS/<PAPEL>/`.

---

## ❌ Limites

- Não aprovar demanda.
- Não tratar persona como prompt.

---

## ❓ Perguntas canônicas

- END é binário?
- PASS/FAIL são verificáveis?
- Fora de escopo está explícito?
- Personas referenciadas na fonte única?

---

## ✅ Critérios de PASS

- Demanda está completa e rastreável para aprovação do CEO.

---

## ✅ Decisões permitidas

- Declarar “pronta para aprovação do CEO” / “não pronta”.

---

## 🚫 Decisões proibidas

- Aprovar/rejeitar demanda.

---

## 🔗 Rastreabilidade

- Demanda: `DEMANDAS/ATIVAS/<DEMANDA-ID>/...`
- Evidência: `DEMANDAS/ATIVAS/<DEMANDA-ID>/EVIDENCIAS/...`

---

## 🧬 Versionamento

- Mudanças neste artefato exigem demanda de método e evidência de atualização.

---

## 📌 Registro (preencher)

**Demanda:** `DEMANDA-...`  
**Data:** `YYYY-MM-DD`  
**Status de submissão:** ✅ PRONTA / ❌ NÃO PRONTA  

### Checklist binário

- END binário e mensurável: ✅/❌
- PASS verificável: ✅/❌
- FAIL verificável: ✅/❌
- Fora de escopo explícito: ✅/❌
- Referência a `/METODO/PERSONAS/<PAPEL>/` (fonte única): ✅/❌
