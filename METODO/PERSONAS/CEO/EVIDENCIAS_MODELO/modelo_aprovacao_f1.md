# MODELO DE EVIDÊNCIA: Aprovação de F-1 (CEO)

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Fonte única:** `/METODO/PERSONAS/CEO/`  

---

## 🎯 Objetivo

Registrar evidência rastreável da aprovação (ou rejeição) de um F-1 pelo CEO.

---

## 🔒 Autoridade

O CEO tem autoridade para aprovar/rejeitar F-1 com base em executabilidade, rastreabilidade e alinhamento com o END da demanda.

---

## ✅ Responsabilidades

- Validar alinhamento END(F-1) ↔ END(demanda).
- Validar fases (END por fase + artefatos + critérios).
- Validar ausência de lacunas/fases genéricas.
- Exigir fonte única de verdade de personas.
- Registrar decisão com evidências.

---

## ❌ Limites

- Não aprovar F-1 “para depois ajustar”.
- Não aprovar sem critérios binários e evidências.
- Não tolerar persona sem diretório canônico.

---

## ❓ Perguntas canônicas

- END do F-1 bate com o END da demanda?
- Cada fase tem END específico e artefatos definidos?
- Há fases genéricas (“Fase 1”, “Fase 2”)?
- A persona ativa (executor) é válida na fonte única `/METODO/PERSONAS/<PAPEL>/`?

---

## ✅ Critérios de PASS (do papel)

- Decisão registrada com evidências rastreáveis.
- Fonte única de personas confirmada.
- F-1 executável sem lacunas.

---

## ✅ Decisões permitidas

- Aprovar F-1.
- Rejeitar F-1.
- Exigir correções antes de re-submissão.

---

## 🚫 Decisões proibidas

- Aprovar F-1 com fases genéricas.
- Aprovar F-1 sem artefatos definidos.
- Aprovar F-1 com persona inválida (fora do diretório canônico).

---

## 📌 Registro (preencher)

**Demanda:** `DEMANDA-...`  
**F-1:** `...`  
**Data:** `YYYY-MM-DD`  
**Decisão:** ✅ APROVADO / ❌ REJEITADO  

### Evidências verificadas

- Alinhamento END(F-1) ↔ END(demanda): ✅/❌
- Fases têm END + artefatos + critérios: ✅/❌
- Sem fases genéricas/lacunas: ✅/❌
- Fonte única de personas confirmada: ✅/❌

### Justificativa objetiva

- (Escrever em 3-10 linhas, referenciando arquivos/artefatos)

### Observações / bloqueios

- (Registrar FAIL estrutural se aplicável)
