# MODELO DE EVIDÊNCIA: Aprovação de F-1 (Produto)

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST  
**Fonte única:** `/METODO/PERSONAS/PRODUTO/`  

---

## 🎯 Objetivo

Registrar evidência rastreável da submissão de um F-1 criado por Produto para aprovação do CEO.

---

## 🔒 Autoridade

Produto pode criar F-1 (quando aplicável) e submetê-lo; **não** aprova.

---

## ✅ Responsabilidades

- Garantir END(F-1) alinhado ao END(demanda).
- Garantir fases com END por fase + artefatos + critérios.
- Garantir referência às personas na fonte única.

---

## ❌ Limites

- Não aprovar F-1.
- Não criar fases genéricas.

---

## ❓ Perguntas canônicas

- END(F-1) bate com END(demanda)?
- Cada fase tem END + artefatos + PASS/FAIL?
- Personas referenciadas na fonte única?

---

## ✅ Critérios de PASS

- F-1 está completo e pronto para aprovação do CEO.

---

## ✅ Decisões permitidas

- Submeter / não submeter.

---

## 🚫 Decisões proibidas

- Aprovar/rejeitar F-1.

---

## 🔗 Rastreabilidade

- F-1: `DEMANDAS/ATIVAS/<DEMANDA-ID>/...F1...md`
- Evidência: `DEMANDAS/ATIVAS/<DEMANDA-ID>/EVIDENCIAS/...`

---

## 🧬 Versionamento

- Mudanças neste modelo exigem demanda de método.

---

## 📌 Registro (preencher)

**Demanda:** `DEMANDA-...`  
**F-1:** `...`  
**Data:** `YYYY-MM-DD`  
**Status de submissão:** ✅ PRONTO / ❌ NÃO PRONTO  

### Checklist binário

- Alinhamento END(F-1) ↔ END(demanda): ✅/❌
- Fases completas (END + artefatos + critérios): ✅/❌
- Sem fases genéricas: ✅/❌
- Referência a personas em `/METODO/PERSONAS/<PAPEL>/`: ✅/❌
