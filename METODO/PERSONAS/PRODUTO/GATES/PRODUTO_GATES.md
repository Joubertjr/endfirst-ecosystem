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

## ✅ Critérios de PASS

- Submissão apenas quando gates PASS/FAIL estão verificados (PASS) e nenhum FAIL foi acionado.

---

## ✅ Decisões permitidas

- Submeter / não submeter (PASS/FAIL de preparação).

---

## 🚫 Decisões proibidas

- Submeter demanda incompleta.
- Duplicar fonte de verdade de personas.

---

## 🧱 Gates canônicos (Produto)

### GATE 1 — Gate Estrutural

Demanda está em `DEMANDAS/ATIVAS/<ID>/` e formato canônico.

### GATE 2 — Gate END Binário + PASS/FAIL Verificável

END observável + mensurável + binário, com critérios PASS/FAIL verificáveis (sem ambiguidade).

### GATE 3 — Gate Fonte Única de Personas

Referências a personas apontam para `/METODO/PERSONAS/<PAPEL>/` (fonte única).

### GATE 4 — Gate Fora de Escopo

Fora de escopo explícito.

---

## 🔒 Regra final

> “Persona sem diretório canônico é improviso. Sistema com duas fontes de verdade é FAIL estrutural.”

---

## 🔗 Rastreabilidade

- **Fonte única (persona Produto)**: `/METODO/PERSONAS/PRODUTO/`
- **Playbook**: `/METODO/PERSONAS/PRODUTO/PLAYBOOKS/PRODUTO_PLAYBOOK.md`
- **Checklist**: `/METODO/PERSONAS/PRODUTO/CHECKLISTS/PRODUTO_CHECKLIST.md`

---

## 🧬 Versionamento

- **Versão do artefato**: 1.0
- **Mudanças permitidas**: somente via demanda de método (com evidência e commit rastreável).
