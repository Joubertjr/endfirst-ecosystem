---
document_id: DEMANDA_METODO-006_F1
type: planning
parent_demand: DEMANDA-METODO-006
status: pending_approval
created_at: 2026-01-20
created_by: Manus (Agent)
approved_by: pending
governed_by: /METODO/END_FIRST_V2.md
version: 1.0
---

# F-1 (PLANEJAMENTO CANÔNICO) — DEMANDA-METODO-006

**Versão:** 1.0  
**Data de Criação:** 20 de Janeiro de 2026  
**Criado por:** Manus (Agent)  
**Status:** PENDENTE DE APROVAÇÃO DO CEO  
**Demanda:** DEMANDA-METODO-006 v1.1  
**Tipo:** Método / Governança  

---

## 📋 REFERÊNCIA

**Demanda:** `/DEMANDAS_MANUS/DEMANDA_METODO-006_GOVERNANCA_CONSUMO_METODO.md` (v1.1)  
**Issue:** Pendente de criação  
**Commit da demanda:** `9513421`  

---

## 🎯 OBJETIVO DESTE F-1

Este documento é o **planejamento canônico (F-1)** da DEMANDA-METODO-006 v1.1.

Conforme **OD-012 (Planning is a first-class artifact. Executor only executes.)**:
- Este F-1 define **o que será feito** e **como será feito**
- Nenhuma execução ocorre sem aprovação explícita do CEO
- O executor (Manus) apenas executa o que está planejado aqui

---

## 🔒 END DO F-1

Ao final da execução deste F-1, o método END-FIRST v2 terá:

1. ✅ **Artefatos conceituais definidos** para governança de consumo, atualização e onboarding
2. ✅ **Marcadores textuais mínimos** (grep-friendly) especificados
3. ✅ **Documentação canônica** de como projetos consomem e atualizam o método
4. ✅ **Contrato metodológico** para ferramentas (Cursor, agentes)
5. ✅ **Mecanismo de versionamento** do método documentado
6. ✅ **Integração ao método** END-FIRST v2 via referências canônicas

**Resultado observável:**
> "Um projeto consegue declarar consumo do método, saber quando ele mudou e onboardar novos executores sem memória humana."

---

## 🚫 BLOQUEIOS ESTRUTURAIS

- 🔒 **Nenhuma implementação de produto:** Esta demanda é de método, não de código
- 🔒 **Nenhuma automação obrigatória:** Não criar scripts de sincronização forçada
- 🔒 **Nenhuma imposição de README/Rules:** Permitir como implementação operacional opcional
- 🔒 **Nenhuma migração automática:** Não alterar projetos existentes
- 🔒 **Governar critérios, não implementar soluções:** Definir artefatos conceituais, não ferramentas específicas

---

## 📊 FASES DE EXECUÇÃO (F1-F6)

### FASE F1 — Definir Artefatos Conceituais de Consumo

**END desta fase:**
> Existe documentação canônica de METHOD_CONSUMPTION_DECLARATION com campos obrigatórios e exemplos.

**Tempo estimado:** 1-2 horas

**Artefato esperado:**
- `/METODO/METHOD_CONSUMPTION_DECLARATION.md`
- Campos obrigatórios: `method_name`, `method_version`, `adopted_at`, `source_of_truth_ref`, `exceptions`
- Exemplos de uso (README, YAML, comentário de código)
- Marcadores textuais mínimos (grep-friendly)

**Critérios de PASS:**
- ✅ Documento criado e versionado
- ✅ Campos obrigatórios especificados
- ✅ Exemplos operacionais fornecidos
- ✅ Marcadores grep-friendly definidos

---

### FASE F2 — Definir Artefatos Conceituais de Atualização

**END desta fase:**
> Existe documentação canônica de METHOD_CHANGELOG com estrutura de entradas e distinção retroativo/prospectivo.

**Tempo estimado:** 1-2 horas

**Artefato esperado:**
- `/METODO/METHOD_CHANGELOG.md`
- Estrutura de entrada: `change_id`, `version`, `date`, `scope`, `summary`, `impact`
- Regras de escopo: retroativo vs prospectivo
- Exemplos de entradas
- Como projetos verificam se precisam agir

**Critérios de PASS:**
- ✅ Documento criado e versionado
- ✅ Estrutura de entrada especificada
- ✅ Distinção retroativo/prospectivo clara
- ✅ Exemplos operacionais fornecidos

---

### FASE F3 — Definir Artefatos Conceituais de Onboarding

**END desta fase:**
> Existe documentação canônica de ONBOARDING_DEFINITION com checklist binário e critérios de "onboarding completo".

**Tempo estimado:** 2-3 horas

**Artefato esperado:**
- `/METODO/ONBOARDING_DEFINITION.md`
- Checklist de artefatos obrigatórios para leitura
- Critérios binários de "onboarding completo"
- Exemplos de verificação (ex: "consegue criar demanda", "consegue executar F1-F6")
- Marcadores de status (ex: `onboarding_status: complete`)

**Critérios de PASS:**
- ✅ Documento criado e versionado
- ✅ Checklist binário especificado
- ✅ Critérios de "onboarding completo" definidos
- ✅ Nenhuma dependência de explicação verbal

---

### FASE F4 — Definir Contrato Metodológico para Ferramentas

**END desta fase:**
> Existe documentação canônica de TOOL_CONTRACT especificando o que ferramentas (Cursor, agentes) DEVEM, NUNCA e SEMPRE fazem.

**Tempo estimado:** 2-3 horas

**Artefato esperado:**
- `/METODO/TOOL_CONTRACT.md`
- Lista de documentos que a ferramenta DEVE consultar
- Lista de ações que a ferramenta NUNCA executa sem referência explícita
- Lista de registros que a ferramenta SEMPRE cria
- Exemplos de uso (Cursor Rules, prompts de agentes)

**Critérios de PASS:**
- ✅ Documento criado e versionado
- ✅ Listas DEVE/NUNCA/SEMPRE especificadas
- ✅ Exemplos operacionais fornecidos
- ✅ Aplicável a Cursor, Manus e outros agentes

---

### FASE F5 — Definir Mecanismo de Versionamento do Método

**END desta fase:**
> Existe documentação canônica de VERSIONING_MECHANISM definindo como versões do método são identificadas e como projetos verificam se estão desatualizados.

**Tempo estimado:** 1-2 horas

**Artefato esperado:**
- `/METODO/VERSIONING_MECHANISM.md`
- Como versões do método são identificadas (ex: v2.5, v2.6)
- Como projetos sabem qual versão estão usando
- Como verificar se estão desatualizados
- Relação entre versão conceitual e commits/tags do repositório

**Critérios de PASS:**
- ✅ Documento criado e versionado
- ✅ Mecanismo de identificação de versão definido
- ✅ Mecanismo de verificação de desatualização definido
- ✅ Relação com repositório do método especificada

---

### FASE F6 — Integrar ao Método END-FIRST v2

**END desta fase:**
> Documentos do método END-FIRST v2 referenciam canonicamente os 5 artefatos criados.

**Tempo estimado:** 1 hora

**Artefato esperado:**
- `/METODO/END_FIRST_V2.md` atualizado com seção "Governança de Consumo, Atualização e Onboarding"
- Referências canônicas aos 5 documentos criados
- Histórico de versões atualizado (v1.5 → v1.6)

**Critérios de PASS:**
- ✅ END_FIRST_V2.md atualizado
- ✅ Seção de governança adicionada
- ✅ Referências canônicas aos 5 artefatos
- ✅ Versão incrementada

---

## 📊 RESUMO DAS FASES

| Fase | END | Artefato | Tempo |
|------|-----|----------|-------|
| F1 | METHOD_CONSUMPTION_DECLARATION definido | `/METODO/METHOD_CONSUMPTION_DECLARATION.md` | 1-2h |
| F2 | METHOD_CHANGELOG definido | `/METODO/METHOD_CHANGELOG.md` | 1-2h |
| F3 | ONBOARDING_DEFINITION definido | `/METODO/ONBOARDING_DEFINITION.md` | 2-3h |
| F4 | TOOL_CONTRACT definido | `/METODO/TOOL_CONTRACT.md` | 2-3h |
| F5 | VERSIONING_MECHANISM definido | `/METODO/VERSIONING_MECHANISM.md` | 1-2h |
| F6 | Integração ao método | `/METODO/END_FIRST_V2.md` (v1.6) | 1h |
| **TOTAL** | | **6 documentos** | **9-15h** |

---

## 🔗 DEPENDÊNCIAS

**Dependências satisfeitas:**
- ✅ DEMANDA-METODO-006 v1.1 aprovada como BACKLOG
- ✅ Critérios de aceitação binarizados
- ✅ Artefatos conceituais especificados
- ✅ Marcadores textuais mínimos definidos

**Nenhuma dependência bloqueante.**

---

## ⚠️ RISCOS E MITIGAÇÕES

### Risco 1: Artefatos muito abstratos
**Probabilidade:** Média  
**Impacto:** Alto (retrabalho)  
**Mitigação:** Incluir exemplos operacionais em cada artefato (README, YAML, comentários)

### Risco 2: Conflito com projetos existentes
**Probabilidade:** Baixa  
**Impacto:** Médio  
**Mitigação:** Artefatos são conceituais, não obrigatórios; projetos podem adotar gradualmente

### Risco 3: Marcadores não grep-friendly
**Probabilidade:** Baixa  
**Impacto:** Alto (falha no END)  
**Mitigação:** Testar marcadores com `grep` durante criação dos artefatos

---

## 📋 CRITÉRIOS DE APROVAÇÃO DO F-1

Para o CEO aprovar este F-1, os seguintes critérios devem ser satisfeitos:

1. ✅ **Fases bem definidas:** Cada fase tem END, artefato esperado, tempo estimado e critérios de PASS
2. ✅ **Bloqueios estruturais respeitados:** Nenhuma implementação de produto, nenhuma automação obrigatória, nenhuma imposição de README/Rules
3. ✅ **Artefatos conceituais claros:** 5 artefatos especificados (METHOD_CONSUMPTION_DECLARATION, METHOD_CHANGELOG, ONBOARDING_DEFINITION, TOOL_CONTRACT, VERSIONING_MECHANISM)
4. ✅ **Marcadores grep-friendly:** Cada artefato inclui marcadores textuais mínimos
5. ✅ **Integração ao método:** Fase F6 integra os artefatos ao END-FIRST v2
6. ✅ **Tempo realista:** 9-15 horas estimadas (razoável para escopo de método)

---

## 🧭 PRÓXIMOS PASSOS (APÓS APROVAÇÃO)

1. ✅ CEO aprova F-1
2. ✅ Status muda: F-1 PENDENTE → F-1 APROVADO
3. ✅ Execução começa (F1-F6)
4. ✅ Cada fase é executada sequencialmente
5. ✅ Artefatos são criados, versionados e integrados
6. ✅ DEMANDA-METODO-006 é declarada PASS

---

## 📜 DECLARAÇÃO CANÔNICA

> "Este F-1 governa a execução da DEMANDA-METODO-006. Nenhuma fase é executada sem este planejamento aprovado. Nenhuma decisão é tomada durante execução que não esteja prevista aqui."

---

**Status:** PENDENTE DE APROVAÇÃO DO CEO  
**Aguardando:** Validação e autorização explícita do CEO para executar

---

## 🔗 Referências

- `/DEMANDAS_MANUS/DEMANDA_METODO-006_GOVERNANCA_CONSUMO_METODO.md` (v1.1)
- `/METODO/END_FIRST_V2.md` — Método END-FIRST v2
- `/METODO/TEMPLATE_DEMANDA_CANONICA.md` — Template canônico
