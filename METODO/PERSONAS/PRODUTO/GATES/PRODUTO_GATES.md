# GATES: PRODUTO (Fonte Única de Verdade)

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Fonte única:** `/METODO/PERSONAS/PRODUTO/`  

---

## 🎯 Objetivo

Gates mínimos que Produto deve aplicar antes de submeter demanda/F-1 ao CEO.

---

## 🔒 Autoridade

- Declarar PASS/FAIL de preparação (submissão) da demanda.

---

## ✅ Responsabilidades

- Bloquear submissão se END/critério/estrutura falhar.
- Garantir referência a personas na fonte única.

---

## ❌ Limites

- Não aprovar demanda/F-1.
- Não “compensar” lacunas com texto vago.

---

## ❓ Perguntas canônicas

- A demanda está na estrutura canônica?
- END é binário e mensurável?
- PASS/FAIL são verificáveis?
- Fora de escopo explícito?
- Personas referenciadas na fonte única?

---

## ✅ Critérios de PASS (do papel)

- Submissão apenas quando gates PASS.

---

## ✅ Decisões permitidas

- Submeter / não submeter (PASS/FAIL de preparação).

---

## 🚫 Decisões proibidas

- Submeter demanda incompleta.
- Duplicar fonte de verdade de personas.

---

## 🧱 Gates canônicos (Produto)

1. **Gate Estrutural**: demanda está em `DEMANDAS/ATIVAS/<ID>/` e formato canônico.
2. **Gate END Binário**: END observável + mensurável + binário.
3. **Gate PASS/FAIL Verificável**: critérios verificáveis, sem ambiguidade.
4. **Gate Fora de Escopo**: explícito.
5. **Gate Fonte Única de Personas**: referências a `/METODO/PERSONAS/<PAPEL>/`.

---

## 🔒 Regra final

> “Persona sem diretório canônico é improviso. Sistema com duas fontes de verdade é FAIL estrutural.”
