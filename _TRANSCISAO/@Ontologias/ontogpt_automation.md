# OntoGPT: Automação de Extração e Construção de Ontologias

**Fonte**: Monarch Initiative
**URL**: https://monarch-initiative.github.io/ontogpt/
**GitHub**: https://github.com/monarch-initiative/ontogpt

## Visão Geral

OntoGPT é um pacote Python para extrair informações estruturadas de texto usando LLMs, instruction prompts e grounding baseado em ontologias. Funciona com modelos OpenAI GPT e outros LLMs locais.

## Método Principal: SPIRES

**SPIRES**: Structured Prompt Interrogation and Recursive Extraction of Semantics

### Características
- Abordagem Zero-shot Learning (ZSL)
- Extrai estruturas semânticas aninhadas de texto
- Dois inputs necessários:
  1. Schema LinkML
  2. Texto livre
- Outputs: JSON, YAML, RDF ou OWL
- Conformante com o schema fornecido

## Casos de Uso

1. **Tarefas NLP gerais**
   - Named Entity Recognition (NER)
   - Relation Extraction

2. **Sumarização de texto**

3. **Construção de Knowledge Bases**

4. **Construção de Knowledge Graphs**

## Instalação e Uso

### Requisitos
- Python 3.9 ou superior

### Instalação
```bash
pip install ontogpt
```

### Configuração
```bash
# Definir API key da OpenAI
runoak set-apikey -e openai <sua_api_key>
```

### Comandos Básicos
```bash
# Ver todos os comandos
ontogpt --help

# Exemplo simples de extração
echo "One treatment for high blood pressure is carvedilol." > example.txt
ontogpt extract -i example.txt -t drug
```

### Web Application
```bash
# Instalar dependências web
pip install ontogpt[web]

# Iniciar aplicação web
web-ontogpt
```

**Nota**: Não recomendado hospedar publicamente sem autenticação

## Outputs

Resultados extraídos aparecem sob o heading `extracted_object` com:
- Entidades identificadas
- Relações extraídas
- Estrutura conformante com schema
- Formatos: JSON, YAML, RDF, OWL

## Vantagens para Automação

### 1. Zero-Shot Learning
- Não requer treinamento prévio
- Funciona com novos domínios imediatamente
- Apenas precisa de schema LinkML

### 2. Ontology-Based Grounding
- Resultados fundamentados em ontologias existentes
- Reduz alucinações
- Garante consistência semântica

### 3. Estruturas Aninhadas
- Captura relacionamentos complexos
- Não apenas entidades planas
- Hierarquias e dependências

### 4. Múltiplos Formatos de Output
- JSON para integração com aplicações
- YAML para legibilidade humana
- RDF/OWL para integração com sistemas semânticos

## Publicação Científica

**Citação**: Caufield JH, Hegde H, Emonet V, Harris NL, Joachimiak MP, Matentzoglu N, et al. "Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning." Bioinformatics. 2024;40. doi:10.1093/bioinformatics/btae104

## Suporte e Contribuições

- **Apoio**: Bosch Research
- **Contribuições**: Issues e PRs bem-vindos no GitHub
- **Comunidade**: Monarch Initiative

## Integração com Workflow

### Fluxo Típico
1. Definir schema LinkML do domínio
2. Preparar corpus de texto
3. Executar OntoGPT extract
4. Validar outputs
5. Integrar em knowledge base/graph

### Combinação com Outras Ferramentas
- **LangChain**: Para orquestração de agentes
- **Neo4j/Memgraph**: Para armazenamento de grafos
- **Protégé**: Para refinamento manual de ontologias
- **SPARQL**: Para consultas sobre outputs RDF

## Limitações

1. Requer API key OpenAI (ou LLM local)
2. Qualidade depende do schema LinkML fornecido
3. Custos de API para volumes grandes
4. Web app básica (não production-ready)

## Casos de Uso Práticos

### Biomedicina
- Extração de relações droga-doença
- Construção de knowledge graphs médicos
- Anotação de literatura científica

### Domínio Geral
- Extração de fatos de documentos
- Construção de bases de conhecimento corporativas
- Enriquecimento de ontologias existentes
