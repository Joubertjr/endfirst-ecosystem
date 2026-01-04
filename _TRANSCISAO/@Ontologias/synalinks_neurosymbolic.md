# SynaLinks: Arquitetura Neuro-Simbólica com Knowledge Graphs

**Fonte**: Memgraph Blog - Dr. Yoan Sallami (CEO SynaLinks)
**URL**: https://memgraph.com/blog/deep-learning-knowledge-graph

## Conceito Principal

SynaLinks é um framework neuro-simbólico de IA baseado em Keras, projetado para trazer estrutura, contexto e flexibilidade a sistemas baseados em LLMs através de knowledge graphs.

## Três Pilares da Arquitetura

### 1. Workflows (Pipelines)
- Estruturados como DAGs (Directed Acyclic Graphs)
- Cada módulo processa dados e passa para o próximo
- Inputs/outputs definidos usando Pydantic models
- Constraint-based decoding para garantir outputs bem-formados em JSON

### 2. Knowledge Graphs como Data Models
- Regra única: toda entidade e relação deve ter um label
- Schema flexível adaptável a diferentes necessidades de negócio
- Relações expressas como `subject–label–object`
- Metadata pode incluir nomes, descrições
- Tudo implementado em Pydantic para serialização consistente

### 3. Otimização para Negócios
- Robustez e usabilidade em contextos empresariais
- Integração direta com Memgraph
- Deduplicação via vector index (HNSW)

## Estratégias de Extração

### One-Stage Extraction
- **Como funciona**: Um único LLM identifica entidades e relações simultaneamente
- **Vantagens**: Simplicidade e velocidade
- **Desvantagens**: Menos controle, maior chance de erros em tarefas complexas

### Two-Stage Extraction
- **Como funciona**: 
  1. Primeiro extrai entidades
  2. Depois identifica relações usando entidades como contexto
- **Vantagens**: Mais preciso, mais fácil de debugar
- **Desvantagens**: Ligeiramente mais complexo de configurar

### Multi-Stage Extraction
- **Como funciona**: Diferentes generators especializados em subconjuntos de dados
  - Ex: um para cidades, outro para eventos, outro para organizações
  - Outputs são então mesclados
- **Vantagens**: 
  - Máximo controle
  - Evita sobrecarregar o LLM
  - Permite grafos parciais quando alguns generators falham
- **Desvantagens**: Mais complexo de orquestrar

### Relation-Only Extraction
- **Como funciona**: Foca apenas em relações
- **Vantagens**: Garante que todas entidades estão conectadas, evita nós órfãos
- **Uso**: Mantém o grafo limpo e coeso

## Integração com Memgraph

### Deduplicação Inteligente
- Usa vector index do Memgraph (HNSW - Hierarchical Navigable Small World)
- Similarity search decide se atualiza nó existente ou cria novo
- Mais rápido que algoritmos tradicionais (ex: Hungarian algorithm)
- Computação pesada feita pelo banco de dados

### Multi-Document Ingestion
- Entidades de diferentes páginas/arquivos mescladas em grafo único
- Grafo cresce em tempo real conforme documentos são adicionados
- Demonstrado ao vivo no Memgraph Lab

## Casos de Uso Reais

### Segurança
- Modelar incidentes, pessoas, hosts

### Biologia
- Mapear moléculas, efeitos, composições de produtos

### Finanças e Saúde
- Requerem limpeza estrita de dados
- Knowledge graphs estruturados são essenciais

## Best Practices Recomendadas

1. **Se já tem dados estruturados**: Escreva script para extrair primeiro
2. **Use LLMs apenas para conteúdo não estruturado**: PDFs, logs, relatórios de texto livre
3. **Sempre projete schemas com especialistas de domínio**: Schema mal projetado = grafo ruim
4. **Modelagem é o desafio real**: LLMs podem ajudar a escrever schema, mas não capturam decisões de modelagem
5. **Foque no problema**: Que queries você precisa? Qual o propósito do KG? Como vai usá-lo?

## Insights Técnicos

### Por que Knowledge Graphs > Embeddings?
- Estrutura explícita de relações
- Raciocínio simbólico sobre conexões
- Explicabilidade das inferências
- Manutenção e evolução mais claras

### Arquitetura Modular
- Inspirada em Keras para facilitar uso
- Estilo declarativo
- Cada componente é independente e testável
- Fácil de adaptar para diferentes contextos de negócio

## Limitações e Desafios

1. **Design de Schema**: Requer expertise de domínio, não pode ser totalmente automatizado
2. **Complexidade Inicial**: Curva de aprendizado para configurar pipelines multi-estágio
3. **Trade-offs**: Precisão vs velocidade vs complexidade

## Tecnologias Envolvidas

- **Framework Base**: Keras (fork customizado)
- **Data Validation**: Pydantic
- **Graph Database**: Memgraph
- **Vector Search**: HNSW indexing
- **Query Language**: Cypher
- **LLM Integration**: Constraint-based decoding

## Conclusão Chave

A abordagem neuro-simbólica combina:
- **Neural (LLMs)**: Processamento de linguagem natural, extração de informação
- **Symbolic (KG)**: Estrutura, raciocínio lógico, explicabilidade

Resultado: Sistemas mais robustos, interpretáveis e adaptáveis que LLMs puros ou sistemas simbólicos puros isoladamente.
