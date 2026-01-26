# CHECKLIST: PRODUTO (Fonte Única de Verdade)

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Fonte única:** `/METODO/PERSONAS/PRODUTO/`  

---

## 🎯 Objetivo

Checklist rápido para criação/submissão de demanda com END binário e governança por artefatos.

---

## 🔒 Autoridade

- Preparar/submeter demandas ao CEO.

---

## ✅ Responsabilidades

- Garantir END binário.
- Garantir PASS/FAIL verificáveis.
- Garantir fonte única de personas.

---

## ❌ Limites

- Não aprovar.
- Não implementar.

---

## ❓ Perguntas canônicas

- END é binário?
- PASS/FAIL são verificáveis?
- Fora de escopo está explícito?
- Personas referenciadas na fonte única?

---

## ✅ Critérios de PASS

- Checklist aplicado com tudo PASS.

---

## ✅ Decisões permitidas

- Submeter / corrigir.

---

## 🚫 Decisões proibidas

- Submeter demanda incompleta.
- Criar persona fora do diretório canônico.

---

## ✅ Checklist

- [ ] Pasta canônica `DEMANDAS/ATIVAS/<DEMANDA-ID>/` criada
- [ ] END (exato) definido e binário
- [ ] PASS definido (verificável)
- [ ] FAIL definido (verificável)
- [ ] Fora de escopo explícito
- [ ] Referência a `/METODO/PERSONAS/<PAPEL>/` (fonte única)

---

## 🔒 Regra final

> “Persona sem diretório canônico é improviso. Sistema com duas fontes de verdade é FAIL estrutural.”

---

## 🧱 Gates (referência explícita)

- **GATE 1** — Gate Estrutural (ver `../GATES/PRODUTO_GATES.md`)
- **GATE 2** — Gate END Binário + PASS/FAIL Verificável (ver `../GATES/PRODUTO_GATES.md`)
- **GATE 3** — Gate Fonte Única de Personas (ver `../GATES/PRODUTO_GATES.md`)

---

## 🔗 Rastreabilidade

- **Fonte única (persona Produto)**: `/METODO/PERSONAS/PRODUTO/`
- **Playbook**: `/METODO/PERSONAS/PRODUTO/PLAYBOOKS/PRODUTO_PLAYBOOK.md`
- **Gates**: `/METODO/PERSONAS/PRODUTO/GATES/PRODUTO_GATES.md`

---

## 🧬 Versionamento

- **Versão do artefato**: 1.0
- **Mudanças permitidas**: somente via demanda de método (com evidência e commit rastreável).
