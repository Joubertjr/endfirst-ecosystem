---
document_id: BANCO_CONTEXTO_INTERNO
type: canonical
owner: CEO (Joubert Jr)
status: approved
approved_by: CEO
approved_at: 2026-01-24
governed_by: /METODO/PILAR_ENDFIRST.md
version: 1.0
created_at: 2026-01-24
demanda_origem: DEMANDA-SOFT-006
---

# BANCO DE CONTEXTO INTERNO — END-FIRST v2.5

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Status:** Canônico (Aprovado)  
**Demanda de Origem:** DEMANDA-SOFT-006  
**Path Canônico:** `/METODO/BANCO_CONTEXTO_INTERNO.md`

---

## 🎯 O QUE É BANCO DE CONTEXTO INTERNO

O **Banco de Contexto Interno** é a estrutura que organiza, indexa e consulta todo o conhecimento gerado dentro do repositório `endfirst-ecosystem`.

**Frase canônica:**
> "Todo documento do repositório é parte do contexto interno."

---

## 📋 DEFINIÇÃO CANÔNICA

### O que é Contexto Interno

**Contexto interno** é:
- Todo documento do repositório
- Todas as demandas
- Todas as evidências
- Todos os produtos
- Toda a governança

**Exemplos de contexto interno:**
- Documentos em `/METODO/`
- Demandas em `/DEMANDAS_MANUS/`
- Evidências em `/EVIDENCIAS/`
- Produtos em `/PRODUTOS/`
- Governança em `/GOV/`, `/PROD/`, `/SOFT/`

### Diferença entre Contexto Interno e Externo

**Contexto interno:**
- Conhecimento gerado dentro do repositório
- Rastreabilidade completa no Git
- Versionamento automático
- Governança direta pelo método

**Contexto externo:**
- Conhecimento gerado fora do repositório
- Requer processo de importação
- Governança via aprovação de fonte externa
- Definido em `/METODO/FONTES_EXTERNAS_CONHECIMENTO.md`

### Escopo do Contexto Interno

**Contexto interno inclui:**
- ✅ Documentos de método
- ✅ Demandas e F-1s
- ✅ Evidências de execução
- ✅ Produtos e seus artefatos
- ✅ Governança e regras

**Contexto interno não inclui:**
- ❌ Conhecimento gerado externamente (antes de importação)
- ❌ Arquivos temporários
- ❌ Artefatos não versionados

---

## 🔍 ESTRATÉGIA DE INDEXAÇÃO

### RAG (Retrieval-Augmented Generation)

**O que é:**
- Busca semântica de documentos
- Geração aumentada por recuperação
- Combinação de busca e geração

**Casos de uso:**
- Buscar documentos relevantes para uma demanda
- Encontrar evidências relacionadas
- Recuperar contexto histórico

**Frase canônica:**
> "RAG/Vetor/Grafo são estratégias complementares, não excludentes."

### Vetor (Embeddings)

**O que é:**
- Embedding de documentos em espaço vetorial
- Similaridade vetorial entre documentos
- Busca por similaridade semântica

**Casos de uso:**
- Encontrar documentos similares
- Agrupar documentos relacionados
- Buscar por significado, não por palavras-chave

### Grafo (Relações)

**O que é:**
- Relações entre documentos
- Rastreabilidade de dependências
- Estrutura de conhecimento como grafo

**Casos de uso:**
- Rastrear dependências entre demandas
- Mapear relações entre produtos e método
- Visualizar estrutura do conhecimento

### Estratégias Complementares

**RAG, Vetor e Grafo são complementares:**
- ✅ RAG para busca e geração
- ✅ Vetor para similaridade semântica
- ✅ Grafo para relações e dependências

**Não são excludentes:**
- Sistema pode usar todas as estratégias
- Cada estratégia serve a propósito diferente
- Combinação aumenta capacidade de consulta

---

## 📦 VERSIONAMENTO DE CONTEXTO

### Regra de Versionamento

**Contexto é versionado junto com o método.**

**Critérios de versionamento:**
- ✅ Versão segue padrão do método (semantic versioning)
- ✅ Mudanças no contexto geram nova versão
- ✅ Histórico de versões mantido no Git
- ✅ Rastreabilidade de versões preservada

### Processo de Atualização

**Quando contexto muda:**

1. **Mudança no repositório:**
   - Novo documento adicionado
   - Documento modificado
   - Documento removido

2. **Versionamento automático:**
   - Git versiona mudanças automaticamente
   - Commit registra mudança
   - Histórico mantido

3. **Indexação:**
   - Contexto é reindexado
   - Estratégias (RAG/Vetor/Grafo) atualizadas
   - Consultas refletem mudanças

**Frase canônica:**
> "Contexto é versionado junto com o método."

---

## 🔗 VÍNCULO COM PRODUTO/MÉTODO

### Metadata de Vínculo

Todo documento do contexto interno DEVE conter metadata de vínculo:

```yaml
---
document_id: DOCUMENT_ID
type: canonical
owner: CEO (Joubert Jr)
status: approved
governed_by: /METODO/PILAR_ENDFIRST.md
version: 1.0
created_at: 2026-01-24
demanda_origem: DEMANDA-XXX
produto_origem: PRODUTO-XXX
---
```

### Campos de Vínculo

- **demanda_origem:** ID da demanda que gerou o documento
- **produto_origem:** ID do produto relacionado (se aplicável)
- **governed_by:** Documento do método que governa
- **owner:** Responsável pelo documento

### Rastreabilidade de Origem

**Cada documento mantém:**
- Origem (demanda, produto, método)
- Dependências (governed_by)
- Histórico de mudanças (Git)

**Frase canônica:**
> "Contexto está vinculado a produto/método via metadata."

---

## 🛡️ GOVERNANÇA DE CONTEXTO

### Regra de Governança

**Contexto governado é consultável. Contexto não governado não é consultável.**

**Critérios de governança:**
- ✅ Documento segue template canônico
- ✅ Documento tem metadata completa
- ✅ Documento está versionado no Git
- ✅ Documento está aprovado (se aplicável)

### Critérios de Governança

**Documento está governado se:**
- ✅ Segue estrutura canônica
- ✅ Tem metadata obrigatória
- ✅ Está versionado
- ✅ Está referenciado no método

### Processo de Governança

**Para governar novo documento:**

1. **Criação:**
   - Criar documento seguindo template
   - Adicionar metadata obrigatória
   - Versionar no Git

2. **Aprovação:**
   - CEO aprova documento (se necessário)
   - Documento é marcado como aprovado

3. **Integração:**
   - Documento é indexado
   - Referências cruzadas criadas
   - Documento fica consultável

**Frase canônica:**
> "Contexto não governado não é consultável."

---

## 🔗 REFERÊNCIAS CRUZADAS

- `/METODO/GOVERNANCA_PRODUTOS.md` — Versionamento de produtos
- `/METODO/PILAR_ENDFIRST.md` — Princípios fundacionais
- `/METODO/FONTES_EXTERNAS_CONHECIMENTO.md` — Fontes externas

---

## 📜 DECLARAÇÃO FINAL

**Este documento define como contexto interno é estruturado, indexado e consultado.**

**Contexto não governado não é consultável.**

---

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Criado por:** Manus (Agent)  
**Aprovado por:** CEO (Joubert Jr)  
**Status:** Canônico (Aprovado)
