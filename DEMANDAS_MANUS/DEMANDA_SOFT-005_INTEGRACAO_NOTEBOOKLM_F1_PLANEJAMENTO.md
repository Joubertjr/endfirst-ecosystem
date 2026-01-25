# F-1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-SOFT-005 — Integração NotebookLM como Fonte Externa de Geração de Conhecimento  
**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Método:** END-FIRST v2.5  
**Executor:** Manus  
**Chefe de Produto:** CEO (Joubert Jr)

---

## 🔒 END — ESTADO FINAL ESPERADO (EXATO)

> "O método define como conhecimento gerado externamente (NotebookLM) é importado, rastreado e versionado no repositório."

### Critérios de Aceitação (Binários)

**PASS:**
- ✅ Documento canônico `/METODO/FONTES_EXTERNAS_CONHECIMENTO.md` existe
- ✅ Pipeline de ingestão NotebookLM → Markdown → Repositório está documentado
- ✅ Rastreabilidade de origem está definida (metadata obrigatória)
- ✅ Versionamento de conhecimento importado está definido
- ✅ Governança de fontes externas está definida

**FAIL:**
- ❌ Nenhum documento canônico criado
- ❌ Pipeline não documentado
- ❌ Rastreabilidade ausente
- ❌ Versionamento ausente
- ❌ Governança ausente

---

## 📋 FASES DE EXECUÇÃO

### F1 — Definir Conceito de Fonte Externa de Conhecimento

**END desta fase:**
> "O conceito de 'fonte externa de conhecimento' está definido canonicamente no método."

**Artefato:**
- Seção "Definição de Fonte Externa" no documento `/METODO/FONTES_EXTERNAS_CONHECIMENTO.md`

**Critérios de PASS:**
- ✅ Definição canônica de "fonte externa de conhecimento"
- ✅ Exemplos de fontes externas (NotebookLM, ChatGPT, Claude, etc.)
- ✅ Diferença entre fonte interna e externa definida
- ✅ Critérios de identificação de fonte externa
- ✅ Frase canônica: "Conhecimento gerado fora do repositório exige rastreabilidade de origem."

**Critérios de FAIL:**
- ❌ Definição não existe
- ❌ Exemplos não fornecidos
- ❌ Diferença não está clara
- ❌ Frase canônica ausente

---

### F2 — Documentar Pipeline de Ingestão

**END desta fase:**
> "O pipeline de ingestão NotebookLM → Markdown → Repositório está documentado."

**Artefato:**
- Seção "Pipeline de Ingestão" no documento

**Critérios de PASS:**
- ✅ Pipeline NotebookLM documentado:
  - Upload de documentos no NotebookLM
  - Geração de conhecimento (resumos, análises, FAQs)
  - Exportação em Markdown
- ✅ Pipeline Repositório documentado:
  - Importação de Markdown
  - Validação de formato
  - Versionamento
  - Integração ao repositório
- ✅ Fluxo completo documentado (passo a passo)
- ✅ Frase canônica: "Ingestão de conhecimento externo é processo governado, não ad-hoc."

**Critérios de FAIL:**
- ❌ Pipeline não documentado
- ❌ Fluxo incompleto
- ❌ Frase canônica ausente

---

### F3 — Definir Rastreabilidade de Origem

**END desta fase:**
> "A rastreabilidade de origem está definida com metadata obrigatória."

**Artefato:**
- Seção "Rastreabilidade" no documento

**Critérios de PASS:**
- ✅ Metadata obrigatória definida:
  - Origem (ferramenta: NotebookLM)
  - Data de geração
  - Autor (usuário que gerou)
  - Documentos fonte (upload original)
  - Versão da ferramenta
- ✅ Formato de metadata definido (YAML frontmatter)
- ✅ Referência à fonte original obrigatória
- ✅ Frase canônica: "Todo documento importado deve referenciar fonte original."

**Critérios de FAIL:**
- ❌ Metadata não definida
- ❌ Formato não especificado
- ❌ Referência não obrigatória
- ❌ Frase canônica ausente

---

### F4 — Definir Versionamento de Conhecimento Importado

**END desta fase:**
> "O versionamento de conhecimento importado está definido."

**Artefato:**
- Seção "Versionamento" no documento

**Critérios de PASS:**
- ✅ Regra de versionamento definida:
  - Conhecimento importado é versionado
  - Mudanças na fonte externa geram nova versão
  - Versão segue padrão do método (semantic versioning)
- ✅ Processo de atualização documentado
- ✅ Rastreabilidade de versões mantida
- ✅ Frase canônica: "Conhecimento externo é versionado como qualquer artefato do método."

**Critérios de FAIL:**
- ❌ Regra não definida
- ❌ Processo não documentado
- ❌ Rastreabilidade não mantida
- ❌ Frase canônica ausente

---

### F5 — Definir Governança de Fontes Externas

**END desta fase:**
> "A governança de fontes externas está definida."

**Artefato:**
- Seção "Governança" no documento

**Critérios de PASS:**
- ✅ Lista de fontes externas aprovadas definida
- ✅ Critérios de aprovação de fonte externa definidos
- ✅ Processo de revisão de fonte externa documentado
- ✅ Regra de bloqueio: "Fonte externa não aprovada não pode ser importada."
- ✅ Frase canônica: "Fonte externa não aprovada não pode ser importada."

**Critérios de FAIL:**
- ❌ Lista não definida
- ❌ Critérios não definidos
- ❌ Processo não documentado
- ❌ Regra de bloqueio ausente
- ❌ Frase canônica ausente

---

### F6 — Integrar ao Método END-FIRST v2.5

**END desta fase:**
> "A governança de fontes externas está integrada ao método END-FIRST v2.5."

**Artefato:**
- Documento `/METODO/FONTES_EXTERNAS_CONHECIMENTO.md` completo
- Referências atualizadas em documentos do método

**Critérios de PASS:**
- ✅ Documento criado em `/METODO/`
- ✅ Documento segue template canônico
- ✅ Referências cruzadas criadas:
  - `/METODO/GOVERNANCA_PRODUTOS.md` (versionamento)
  - `/METODO/PILAR_ENDFIRST.md` (princípios)
- ✅ Documento versionado e commitado
- ✅ Evidência de execução criada em `/EVIDENCIAS/`

**Critérios de FAIL:**
- ❌ Documento não criado
- ❌ Template não seguido
- ❌ Referências não criadas
- ❌ Evidência não gerada

---

## 🚫 BLOQUEIOS ESTRUTURAIS

- 🔒 **Nenhuma implementação de código**
- 🔒 **Nenhuma automação de pipeline**
- 🔒 **Nenhuma integração com API do NotebookLM**
- 🔒 **Apenas documentação de método**

---

## 📊 ORDEM DE EXECUÇÃO

1. F1: Definir conceito de fonte externa
2. F2: Documentar pipeline de ingestão
3. F3: Definir rastreabilidade
4. F4: Definir versionamento
5. F5: Definir governança
6. F6: Integrar ao método

**Regra:** Executar sequencialmente, sem pular fases.

---

## ❌ CRITÉRIOS DE FAIL

- ❌ Criar código ou automação
- ❌ Integrar com API externa
- ❌ Pular fases
- ❌ Não gerar evidência por fase
- ❌ Não seguir template canônico

---

## 📌 STATUS

**Status atual:** Aprovado  
**Próximo passo:** Executar F1

---

## 🧭 REGRA FINAL

> "Este F-1 governa a execução da DEMANDA-SOFT-005. Nenhuma fase é executada sem este planejamento aprovado. Nenhuma decisão é tomada durante execução que não esteja prevista aqui."

---

**Aprovado por:** CEO (Joubert Jr)  
**Data de aprovação:** 2026-01-24  
**Versão:** 1.0
