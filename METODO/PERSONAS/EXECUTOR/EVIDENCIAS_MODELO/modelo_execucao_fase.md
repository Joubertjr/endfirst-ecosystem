# MODELO DE EVIDÊNCIA: Execução de Fase (Executor)

**Versão:** 1.0  
**Data:** 2026-01-26  
**Método:** END-FIRST  
**Fonte única:** `/METODO/PERSONAS/EXECUTOR/`  

---

## 🎯 Objetivo

Registrar evidência rastreável de execução de uma fase do F-1 (artefatos criados + validação PASS/FAIL).

---

## 🔒 Autoridade

Executor pode executar fases e gerar evidências; não aprova demanda/F-1.

---

## ✅ Responsabilidades

- Criar artefatos da fase.
- Validar critérios de PASS.
- Registrar evidência e caminhos.

---

## ❌ Limites

- Não pular fase.
- Não mudar END.

---

## ❓ Perguntas canônicas

- Qual é o END da fase?
- Quais artefatos foram criados?
- PASS atendido? FAIL ativado?

---

## ✅ Critérios de PASS

- Evidência contém artefatos, validações e rastreabilidade.

---

## ✅ Decisões permitidas

- Declarar fase concluída (PASS) / bloqueada (FAIL) conforme critérios.

---

## 🚫 Decisões proibidas

- Declarar PASS sem evidência.

---

## 🔗 Rastreabilidade

- Demanda: `DEMANDAS/ATIVAS/<DEMANDA-ID>/...`
- F-1: `...F1...md`
- Evidência: `DEMANDAS/ATIVAS/<DEMANDA-ID>/EVIDENCIAS/...`
- Commit(s): `git log` (hashes)

---

## 🧬 Versionamento

- Cada fase executada deve ter evidência versionada via commit.

---

## 📌 Registro (preencher)

**Demanda:** `DEMANDA-...`  
**Fase:** `F...`  
**Data:** `YYYY-MM-DD`  

### Artefatos gerados (paths)

- `<path 1>`
- `<path 2>`

### Validação binária

- Critérios de PASS atendidos: ✅/❌
- Critérios de FAIL ativados: ✅/❌

### Observações / bloqueios

- (Se FAIL, descrever bloqueio estrutural/técnico)
