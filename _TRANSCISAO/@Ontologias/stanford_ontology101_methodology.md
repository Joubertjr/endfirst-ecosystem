# Stanford Ontology Development 101: Metodologia

**Fonte**: Natalya F. Noy and Deborah L. McGuinness, Stanford University
**URL**: https://protege.stanford.edu/publications/ontology_development/ontology101.pdf

## Por que desenvolver uma ontologia?

### Razões principais identificadas no guia:

1. **Compartilhar entendimento comum** da estrutura de informação entre pessoas ou agentes de software
2. **Habilitar reuso de conhecimento de domínio**
3. **Tornar suposições de domínio explícitas**
4. **Separar conhecimento de domínio do conhecimento operacional**
5. **Analisar conhecimento de domínio**

### Exemplos de uso prático:

#### Compartilhamento de estrutura comum
- Sites médicos diferentes podem usar vocabulário comum
- Agentes de software podem extrair e agregar informações
- Responder queries de usuários usando informação agregada

#### Reuso de conhecimento de domínio
- Integrar várias ontologias existentes (ex: UNSPSC ontology)
- Estender ontologias para novos domínios

#### Tornar suposições explícitas
- Hard-coding de suposições em código dificulta mudanças
- Ontologias tornam suposições explícitas e fáceis de modificar
- Útil para novos usuários que precisam aprender o domínio

#### Separar conhecimento de domínio do operacional
- Configurar produtos a partir de especificações
- Desenvolver algoritmos independentes de domínio
- "Feed" ontologia de componentes ao algoritmo

#### Analisar conhecimento de domínio
- Análise formal de termos
- Reusar ontologias existentes
- Estender ontologias (McGuinness et al. 2000)

## Sobre o guia

### Ferramentas mencionadas:
- **Protégé-2000** (Protege 2000)
- **Ontolingua** (Ontolingua 1997)
- **Chimaera** (Chimaera 2000)

### Exemplo usado no guia:
- **Domínio**: Vinhos e alimentos
- **Base**: Sistema CLASSIC (knowledge-representation system)
- Desenvolvido em paper de Brachman et al. 1991
- Tutorial de McGuinness et al. 1994

### Origem das ideias:
- Literatura sobre design orientado a objetos (Rumbaugh et al. 1991, Booch et al. 1997)
- Adaptado para desenvolvimento de ontologias
- Foco em propriedades **estruturais** de classes (não métodos)

## Conceitos-chave extraídos

### 1. Ontologia como vocabulário comum
Uma ontologia define um vocabulário comum para pesquisadores que precisam compartilhar informação em um domínio. Inclui definições interpretáveis por máquina de conceitos básicos e relações entre eles.

### 2. Usos práticos de ontologias
- Problem-solving methods
- Aplicações independentes de domínio
- Agentes de software usando ontologias como bases de conhecimento

### 3. Exemplo: Ontologia de vinhos e alimentos
- Criar sugestões de vinhos para menus
- Analisar inventário de adegas
- Sugerir quais vinhos comprar para menus futuros ou livros de receitas

### 4. Abordagem baseada em descrição-lógica
O exemplo usa sistema CLASSIC, baseado em description-logics approach, que descreve ontologias declarativamente, indicando explicitamente:
- Hierarquia de classes
- Classes às quais indivíduos pertencem

## Insights para começar com casos de uso específicos

### Princípio fundamental
**Comece com um caso de uso concreto e específico**, não tente criar uma ontologia universal.

### Exemplo prático do guia
Em vez de criar "ontologia de vinhos genérica", o guia usa:
- Caso de uso: Sistema de recomendação de vinhos para restaurante
- Escopo limitado: Vinhos e alimentos específicos
- Aplicação clara: Sugestões de menu e gestão de inventário

### Vantagens da abordagem orientada a casos de uso

1. **Escopo definido**: Evita over-engineering
2. **Validação imediata**: Pode testar se ontologia resolve o problema
3. **Iteração prática**: Fácil expandir conforme necessário
4. **Engajamento de stakeholders**: Caso de uso concreto facilita feedback

### Processo sugerido (baseado no guia)

1. **Identificar caso de uso específico**
   - Qual problema precisa resolver?
   - Quem vai usar?
   - Que queries precisam ser respondidas?

2. **Definir escopo limitado**
   - Não tentar cobrir todo o domínio
   - Focar no necessário para o caso de uso

3. **Desenvolver iterativamente**
   - Começar simples
   - Expandir conforme necessário
   - Validar continuamente contra caso de uso

4. **Reusar quando possível**
   - Verificar ontologias existentes
   - Adaptar e estender ao invés de criar do zero

## Aplicação prática moderna

### Como aplicar hoje (2025)

1. **Defina o problema de negócio específico**
   - Ex: "Melhorar busca de produtos em e-commerce"
   - Ex: "Automatizar triagem de tickets de suporte"

2. **Identifique as entidades principais**
   - Apenas as necessárias para o caso de uso
   - Ex: Produto, Categoria, Atributo, Cliente

3. **Modele as relações críticas**
   - Apenas as que impactam o caso de uso
   - Ex: Produto "pertence a" Categoria

4. **Valide com dados reais**
   - Use subset de dados reais
   - Teste queries específicas do caso de uso

5. **Itere e expanda**
   - Adicione complexidade conforme necessário
   - Mantenha foco no valor de negócio

## Conexão com ferramentas modernas

### Protégé (mencionado no guia)
- Ainda amplamente usado hoje
- Interface gráfica para construção de ontologias
- Suporta OWL, RDF/RDFS

### Abordagem moderna com LLMs
- OntoGPT pode automatizar extração de conceitos
- LLMs podem sugerir relações
- Mas **especialista de domínio ainda essencial** para validar

### Integração com Knowledge Graphs
- Ontologia define schema
- Knowledge Graph armazena instâncias
- Neo4j, Memgraph para armazenamento
- SPARQL, Cypher para queries

## Lições-chave para casos de uso específicos

1. **Não busque perfeição**: Ontologia "suficientemente boa" é melhor que ontologia "perfeita" que nunca termina
2. **Valide continuamente**: Teste contra casos de uso reais
3. **Envolva especialistas**: Conhecimento de domínio é crítico
4. **Documente decisões**: Por que modelou de certa forma?
5. **Planeje para evolução**: Ontologias mudam, prepare-se para isso
