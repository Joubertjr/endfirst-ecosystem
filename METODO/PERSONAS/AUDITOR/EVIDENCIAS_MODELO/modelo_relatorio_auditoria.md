# MODELO DE EVIDÊNCIA: Relatório de Auditoria (Auditor)

**Versão:** 1.0  
**Data:** 2026-01-26  
**Método:** END-FIRST  
**Fonte única:** `/METODO/PERSONAS/AUDITOR/`  

---

## 🎯 Objetivo

Padronizar relatório de auditoria com veredito binário (PASS/FAIL) e rastreabilidade.

---

## 🔒 Autoridade

Auditor pode declarar PASS/FAIL técnico e solicitar evidências; não aprova demanda/F-1.

---

## ✅ Responsabilidades

- Verificar estrutura, binariedade, rastreabilidade e consistência cruzada.
- Registrar falhas objetivamente (com caminhos/trechos).

---

## ❌ Limites

- Não aprovar por simpatia.
- Não validar sem critério binário.

---

## ❓ Perguntas canônicas

- END e PASS/FAIL são binários?
- Existem placeholders?
- Existe dupla fonte de verdade (personas)?

---

## ✅ Critérios de PASS

- Relatório contém veredito binário e evidências rastreáveis.

---

## ✅ Decisões permitidas

- Declarar PASS/FAIL técnico.

---

## 🚫 Decisões proibidas

- Declarar PASS sem evidência.

---

## 🔗 Rastreabilidade

- Escopo auditado: `<paths>`
- Evidências consultadas: `<paths>`
- Commits consultados: `<hashes>`

---

## 🧬 Versionamento

- Relatório deve ser versionado por commit e referenciar o commit auditado.

---

## 📌 Relatório (preencher)

**Demanda/F-1/Artefato:** `<id/path>`  
**Data:** `YYYY-MM-DD`  
**Veredito técnico:** ✅ PASS / ❌ FAIL  

### Falhas identificadas (se FAIL)

- `<falha 1>` (prova: `<path>:Lx-Ly`)
- `<falha 2>` (prova: `<path>:Lx-Ly`)

### Observações

- (opcional)
