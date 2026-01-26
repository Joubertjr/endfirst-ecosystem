# F-1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-SOFT-006 — Banco de Contexto Interno (RAG/Vetor/Grafo) do Método  
**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Método:** END-FIRST v2.5  
**Executor:** Manus  
**Chefe de Produto:** CEO (Joubert Jr)

---

## 🔒 END — ESTADO FINAL ESPERADO (EXATO)

> "O método define como contexto interno (documentos, demandas, evidências) é estruturado, indexado e consultado."

### Critérios de Aceitação (Binários)

**PASS:**
- ✅ Documento canônico `/METODO/BANCO_CONTEXTO_INTERNO.md` existe
- ✅ Estratégia RAG/Vetor/Grafo está documentada
- ✅ Versionamento de contexto está definido
- ✅ Vínculo com produto/método está definido
- ✅ Governança de contexto está definida

**FAIL:**
- ❌ Nenhum documento canônico criado
- ❌ Estratégia não documentada
- ❌ Versionamento ausente
- ❌ Vínculo ausente
- ❌ Governança ausente

---

## 📋 FASES DE EXECUÇÃO

### F1 — Definir Conceito de Banco de Contexto Interno

**END desta fase:**
> "O conceito de 'banco de contexto interno' está definido canonicamente no método."

**Artefato:**
- Seção "Definição de Banco de Contexto Interno" no documento `/METODO/BANCO_CONTEXTO_INTERNO.md`

**Critérios de PASS:**
- ✅ Definição canônica de "banco de contexto interno"
- ✅ Exemplos de contexto interno (documentos, demandas, evidências, produtos)
- ✅ Diferença entre contexto interno e externo definida
- ✅ Escopo do contexto interno definido
- ✅ Frase canônica: "Todo documento do repositório é parte do contexto interno."

**Critérios de FAIL:**
- ❌ Definição não existe
- ❌ Exemplos não fornecidos
- ❌ Diferença não está clara
- ❌ Escopo não definido
- ❌ Frase canônica ausente

---

### F2 — Documentar Estratégia RAG/Vetor/Grafo

**END desta fase:**
> "A estratégia RAG/Vetor/Grafo está documentada."

**Artefato:**
- Seção "Estratégia de Indexação" no documento

**Critérios de PASS:**
- ✅ RAG (Retrieval-Augmented Generation) documentado:
  - Busca semântica
  - Geração aumentada por recuperação
  - Casos de uso
- ✅ Vetor (Embeddings) documentado:
  - Embedding de documentos
  - Similaridade vetorial
  - Casos de uso
- ✅ Grafo (Relações) documentado:
  - Relações entre documentos
  - Rastreabilidade de dependências
  - Casos de uso
- ✅ Estratégias complementares (não excludentes) definidas
- ✅ Frase canônica: "RAG/Vetor/Grafo são estratégias complementares, não excludentes."

**Critérios de FAIL:**
- ❌ Estratégias não documentadas
- ❌ Casos de uso não fornecidos
- ❌ Complementaridade não definida
- ❌ Frase canônica ausente

---

### F3 — Definir Versionamento de Contexto

**END desta fase:**
> "O versionamento de contexto está definido."

**Artefato:**
- Seção "Versionamento" no documento

**Critérios de PASS:**
- ✅ Regra de versionamento definida:
  - Contexto é versionado junto com o método
  - Mudanças no contexto geram nova versão
  - Versão segue padrão do método
- ✅ Processo de atualização documentado
- ✅ Rastreabilidade de versões mantida
- ✅ Frase canônica: "Contexto é versionado junto com o método."

**Critérios de FAIL:**
- ❌ Regra não definida
- ❌ Processo não documentado
- ❌ Rastreabilidade não mantida
- ❌ Frase canônica ausente

---

### F4 — Definir Vínculo com Produto/Método

**END desta fase:**
> "O vínculo entre contexto e produto/método está definido."

**Artefato:**
- Seção "Vínculo com Produto/Método" no documento

**Critérios de PASS:**
- ✅ Metadata de vínculo definida:
  - Produto associado
  - Método associado
  - Demanda associada
  - Evidência associada
- ✅ Formato de metadata definido (YAML frontmatter)
- ✅ Rastreabilidade de origem mantida
- ✅ Frase canônica: "Contexto está vinculado a produto/método via metadata."

**Critérios de FAIL:**
- ❌ Metadata não definida
- ❌ Formato não especificado
- ❌ Rastreabilidade não mantida
- ❌ Frase canônica ausente

---

### F5 — Definir Governança de Contexto

**END desta fase:**
> "A governança de contexto está definida."

**Artefato:**
- Seção "Governança" no documento

**Critérios de PASS:**
- ✅ Regra de governança definida:
  - Contexto governado é consultável
  - Contexto não governado não é consultável
- ✅ Critérios de governança definidos
- ✅ Processo de governança documentado
- ✅ Frase canônica: "Contexto não governado não é consultável."

**Critérios de FAIL:**
- ❌ Regra não definida
- ❌ Critérios não definidos
- ❌ Processo não documentado
- ❌ Frase canônica ausente

---

### F6 — Integrar ao Método END-FIRST v2.5

**END desta fase:**
> "A governança de banco de contexto interno está integrada ao método END-FIRST v2.5."

**Artefato:**
- Documento `/METODO/BANCO_CONTEXTO_INTERNO.md` completo
- Referências atualizadas em documentos do método

**Critérios de PASS:**
- ✅ Documento criado em `/METODO/`
- ✅ Documento segue template canônico
- ✅ Referências cruzadas criadas:
  - `/METODO/GOVERNANCA_PRODUTOS.md` (versionamento)
  - `/METODO/PILAR_ENDFIRST.md` (princípios)
  - `DEMANDA-SOFT-005` (fontes externas)
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
- 🔒 **Nenhum banco de dados real**
- 🔒 **Nenhuma integração com ferramentas de RAG/Vetor/Grafo**
- 🔒 **Apenas documentação de método**

---

## 📊 ORDEM DE EXECUÇÃO

1. F1: Definir conceito de banco de contexto interno
2. F2: Documentar estratégia RAG/Vetor/Grafo
3. F3: Definir versionamento
4. F4: Definir vínculo com produto/método
5. F5: Definir governança
6. F6: Integrar ao método

**Regra:** Executar sequencialmente, sem pular fases.

---

## ❌ CRITÉRIOS DE FAIL

- ❌ Criar código ou banco de dados
- ❌ Integrar com ferramentas externas
- ❌ Pular fases
- ❌ Não gerar evidência por fase
- ❌ Não seguir template canônico

---

## 📌 STATUS

**Status atual:** Aprovado  
**Próximo passo:** Executar F1

---

## 🧭 REGRA FINAL

> "Este F-1 governa a execução da DEMANDA-SOFT-006. Nenhuma fase é executada sem este planejamento aprovado. Nenhuma decisão é tomada durante execução que não esteja prevista aqui."

---

**Aprovado por:** CEO (Joubert Jr)  
**Data de aprovação:** 2026-01-24  
**Versão:** 1.0
