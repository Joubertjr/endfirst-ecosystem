# 🗂️ Gestão de Ontologias no Banco de Referências

**Data:** 30 de Dezembro de 2025  
**Objetivo:** Plano completo de gestão de ontologias, integrado à arquitetura atual do projeto

---

## 📋 Sumário Executivo

Este documento define como as ontologias serão **estruturadas, versionadas, armazenadas e evoluídas** no Banco de Referências. A estratégia é baseada em **metodologia orientada a casos de uso** (Stanford), **modularização** e **automação** (OntoGPT), seguindo as melhores práticas identificadas na pesquisa de ontologias.

### Princípios Fundamentais

1. **Modularização:** Ontologias divididas em módulos por domínio
2. **Versionamento:** Controle de versão explícito com Git
3. **Automação:** Extração automática com OntoGPT
4. **Iteração:** Evolução baseada em casos de uso
5. **Integração:** Integração contínua com código e banco de dados

---

## 🏗️ 1. Estrutura de Diretórios

### 1.1 Organização Proposta

```
BANCO_REFERENCIAS/
├── backend/
│   ├── app/
│   │   ├── ontologies/              # NOVO - Ontologias do sistema
│   │   │   ├── __init__.py
│   │   │   ├── schemas/             # Schemas LinkML
│   │   │   │   ├── base/            # Ontologia base (conceitos fundamentais)
│   │   │   │   │   ├── document_schema.yaml
│   │   │   │   │   ├── reference_schema.yaml
│   │   │   │   │   └── project_schema.yaml
│   │   │   │   ├── v1/              # Versão 1 (atual)
│   │   │   │   │   └── banco_referencias_v1.yaml
│   │   │   │   └── v2/              # Versão 2 (futuro)
│   │   │   ├── owl/                 # Ontologias OWL (geradas/importadas)
│   │   │   │   ├── base.owl
│   │   │   │   └── banco_referencias.owl
│   │   │   ├── repository.py        # Repository para operações de ontologia
│   │   │   └── service.py           # Service para gestão de ontologias
│   │   │
│   │   ├── services/
│   │   │   └── ontology_service.py  # NOVO - Service de ontologias
│   │   │
│   │   └── repositories/
│   │       └── ontology_repository.py  # NOVO - Repository de ontologias
│   │
│   └── tests/
│       └── ontologies/              # Testes de ontologias
│           ├── test_schemas.py
│           └── test_ontology_service.py
│
├── documentacao/
│   └── ontologias/                  # NOVO - Documentação de ontologias
│       ├── README.md                # Visão geral
│       ├── DECISOES.md              # Decisões de modelagem (ADRs)
│       ├── EVOLUCAO.md              # Histórico de evolução
│       └── GLOSSARIO.md             # Glossário de termos
│
└── ontologies/                      # NOVO - Ontologias versionadas (Git)
    ├── .gitkeep
    ├── README.md
    ├── schemas/
    │   └── (schemas LinkML versionados)
    └── owl/
        └── (ontologias OWL versionadas)
```

### 1.2 Justificativa da Estrutura

**Por que duas localizações (`backend/app/ontologies/` e `ontologies/`)?**

1. **`backend/app/ontologies/`** - Ontologias em uso pela aplicação
   - Schemas LinkML ativos
   - Ontologias OWL compiladas
   - Código Python para gestão
   - Integração direta com o código

2. **`ontologies/`** - Repositório versionado de ontologias
   - Histórico completo de evolução
   - Branching para diferentes versões
   - Documentação de mudanças
   - Backup e controle de versão

**Fluxo:**
```
Ontologias em desenvolvimento → ontologies/ (Git)
                                ↓
Ontologias validadas e testadas → backend/app/ontologies/ (Código)
```

---

## 📦 2. Arquitetura de Ontologias

### 2.1 Estrutura Modular

**Baseado em:** Metodologia Stanford + Guia Técnico de Ontologias

#### Módulo 1: Ontologia Base (Conceitos Fundamentais)

**Arquivo:** `backend/app/ontologies/schemas/base/base_schema.yaml`

```yaml
id: http://banco-referencias.com/ontology/base
name: banco-referencias-base
version: 1.0.0

prefixes:
  linkml: https://w3id.org/linkml/
  br: http://banco-referencias.com/ontology/
  schema: https://schema.org/

default_prefix: br

classes:
  # Classe base para todos os recursos
  Resource:
    description: "Classe base para todos os recursos do sistema"
    attributes:
      id:
        identifier: true
        range: string
      title:
        range: string
        required: true
      description:
        range: string
      created_at:
        range: datetime
      updated_at:
        range: datetime
  
  # Classe para documentos
  Document:
    is_a: Resource
    description: "Documento indexado no sistema"
    attributes:
      filename:
        range: string
        required: true
      file_type:
        range: string
      file_size_bytes:
        range: integer
      google_file_id:
        range: string
        required: true
      status:
        range: DocumentStatus
        default: "active"
    slots:
      - concepts
      - entities
      - references_document
      - belongs_to_project
  
  # Classe para conceitos
  Concept:
    is_a: Resource
    description: "Conceito extraído ou definido no sistema"
    attributes:
      label:
        range: string
        required: true
      definition:
        range: string
      category:
        range: string
    slots:
      - broader
      - narrower
      - related_to
  
  # Classe para entidades
  Entity:
    is_a: Resource
    description: "Entidade nomeada extraída de documentos"
    attributes:
      label:
        range: string
        required: true
      entity_type:
        range: EntityType
        required: true
      confidence:
        range: float
        minimum_value: 0.0
        maximum_value: 1.0
  
  # Classe para referências
  Reference:
    is_a: Resource
    description: "Referência externa (artigos, papers, etc)"
    attributes:
      category:
        range: string
      subject:
        range: string
      sources:
        range: string
        multivalued: true
    slots:
      - concepts
      - references_reference
  
  # Classe para projetos
  Project:
    is_a: Resource
    description: "Projeto documentado no sistema"
    attributes:
      name:
        range: string
        required: true
      documentation_path:
        range: string
    slots:
      - uses_documents
      - references_project

enums:
  DocumentStatus:
    permissible_values:
      - active
      - archived
      - deleted
  
  EntityType:
    permissible_values:
      - person
      - organization
      - location
      - concept
      - event
      - other

slots:
  # Relações
  concepts:
    description: "Conceitos associados a um recurso"
    range: Concept
    multivalued: true
  
  entities:
    description: "Entidades extraídas de um documento"
    range: Entity
    multivalued: true
  
  broader:
    description: "Conceito mais genérico (hierarquia)"
    range: Concept
  
  narrower:
    description: "Conceitos mais específicos (hierarquia)"
    range: Concept
    multivalued: true
  
  related_to:
    description: "Conceito relacionado"
    range: Concept
    multivalued: true
  
  references_document:
    description: "Documento referenciado"
    range: Document
    multivalued: true
  
  references_reference:
    description: "Referência externa relacionada"
    range: Reference
    multivalued: true
  
  belongs_to_project:
    description: "Projeto ao qual pertence"
    range: Project
  
  uses_documents:
    description: "Documentos usados pelo projeto"
    range: Document
    multivalued: true
  
  references_project:
    description: "Projetos relacionados"
    range: Project
    multivalued: true
```

#### Módulo 2: Ontologia de Documentos

**Arquivo:** `backend/app/ontologies/schemas/document_schema.yaml`

```yaml
id: http://banco-referencias.com/ontology/document
name: banco-referencias-document
version: 1.0.0

imports:
  - base_schema.yaml

classes:
  Document:
    # Estende a classe Document da base
    slots:
      - extracted_entities
      - extracted_relations
      - main_topics
      - keywords
  
  ExtractedEntity:
    is_a: Entity
    attributes:
      source_text:
        range: string
      position:
        range: integer
  
  ExtractedRelation:
    description: "Relação extraída entre entidades"
    attributes:
      subject:
        range: Entity
        required: true
      predicate:
        range: string
        required: true
      object:
        range: Entity
        required: true
      confidence:
        range: float

slots:
  extracted_entities:
    range: ExtractedEntity
    multivalued: true
  
  extracted_relations:
    range: ExtractedRelation
    multivalued: true
  
  main_topics:
    range: Concept
    multivalued: true
  
  keywords:
    range: string
    multivalued: true
```

### 2.2 Estrutura Hierárquica de Módulos

```
Ontologia Base (br:base)
├── Conceitos Fundamentais (Resource, Concept, Entity)
├── Status e Enums
└── Relações Básicas

Ontologia de Documentos (br:document)
├── Extends: br:base
├── Document (especializado)
├── ExtractedEntity
└── ExtractedRelation

Ontologia de Referências (br:reference) [Futuro]
├── Extends: br:base
└── Reference (especializado)

Ontologia de Projetos (br:project) [Futuro]
├── Extends: br:base
└── Project (especializado)
```

---

## 🔄 3. Versionamento de Ontologias

### 3.1 Estratégia de Versionamento

**Baseado em:** Semantic Versioning (SemVer) + Git

**Formato:** `MAJOR.MINOR.PATCH`

- **MAJOR:** Mudanças incompatíveis (remoção de classes, mudanças fundamentais)
- **MINOR:** Novas funcionalidades compatíveis (novas classes, propriedades)
- **PATCH:** Correções e melhorias (bugs, refinamentos)

### 3.2 Estrutura de Versões

```
ontologies/
├── schemas/
│   ├── v1.0.0/
│   │   ├── base_schema.yaml
│   │   └── document_schema.yaml
│   ├── v1.1.0/
│   │   └── (novas features)
│   └── v2.0.0/
│       └── (mudanças incompatíveis)
│
└── owl/
    ├── v1.0.0/
    │   └── banco_referencias_v1.0.0.owl
    └── v2.0.0/
        └── banco_referencias_v2.0.0.owl
```

### 3.3 Processo de Versionamento

**1. Desenvolvimento:**
```bash
# Criar branch para nova versão
git checkout -b feature/ontology-v1.1.0

# Editar schemas em ontologies/schemas/
# Commit
git commit -m "feat(ontology): Adiciona suporte a keywords em documentos"
```

**2. Validação:**
```bash
# Validar schema LinkML
linkml-validate schemas/v1.1.0/document_schema.yaml

# Gerar OWL
linkml-gen-owl schemas/v1.1.0/document_schema.yaml -o owl/v1.1.0/banco_referencias.owl

# Testes
pytest tests/ontologies/
```

**3. Release:**
```bash
# Tag da versão
git tag -a v1.1.0 -m "Ontologia v1.1.0: Suporte a keywords"

# Copiar para backend/app/ontologies/ (versão ativa)
cp -r ontologies/schemas/v1.1.0/* backend/app/ontologies/schemas/v1/
cp -r ontologies/owl/v1.1.0/* backend/app/ontologies/owl/
```

**4. Documentação:**
- Atualizar `documentacao/ontologias/EVOLUCAO.md`
- Documentar mudanças em `documentacao/ontologias/DECISOES.md`

### 3.4 Migração entre Versões

**Estratégia:** Compatibilidade retroativa quando possível

```python
# backend/app/services/ontology_migration_service.py
class OntologyMigrationService:
    """Service para migração entre versões de ontologia."""
    
    async def migrate_data(
        self, 
        data: dict, 
        from_version: str, 
        to_version: str
    ) -> dict:
        """
        Migra dados de uma versão para outra.
        
        Args:
            data: Dados na versão antiga
            from_version: Versão de origem (ex: "1.0.0")
            to_version: Versão de destino (ex: "1.1.0")
            
        Returns:
            Dados na nova versão
        """
        # Lógica de migração baseada em regras
        if from_version == "1.0.0" and to_version == "1.1.0":
            # Adicionar campos novos com valores padrão
            if "keywords" not in data:
                data["keywords"] = []
            return data
        
        # ... outras migrações
```

---

## 🔧 4. Armazenamento e Persistência

### 4.1 Onde Armazenar Ontologias

**1. Schemas LinkML (Fonte):**
- **Localização:** `backend/app/ontologies/schemas/`
- **Formato:** YAML
- **Uso:** Fonte de verdade, usado por OntoGPT

**2. Ontologias OWL (Compiladas):**
- **Localização:** `backend/app/ontologies/owl/`
- **Formato:** OWL/RDF
- **Uso:** Queries SPARQL, reasoners, integração com sistemas externos

**3. Knowledge Graph (Instâncias):**
- **Localização:** Neo4j (Knowledge Graph Database)
- **Formato:** Grafo de nós e arestas
- **Uso:** Queries Cypher, buscas relacionais

**4. PostgreSQL (Metadata):**
- **Localização:** Tabelas `documents`, `references`, `projects`
- **Formato:** JSONB (campos `metadata`, `concepts`, `entities`)
- **Uso:** Queries SQL, backup, relatórios

### 4.2 Modelo de Dados Híbrido com Sincronização Resiliente

> **⚠️ Crítica Crítica Aplicada:** Implementa padrão Outbox/Saga para garantir consistência eventual e resiliência em ambiente distribuído.

**Arquitetura com Padrão Outbox:**

```
┌─────────────────────────────────────────┐
│         Schemas LinkML (YAML)           │
│  (Fonte de verdade, versionado em Git)  │
└───────────────┬─────────────────────────┘
                │
                │ Compilação
                ↓
┌─────────────────────────────────────────┐
│      Ontologias OWL (RDF/Turtle)        │
│     (Para integração e queries SPARQL)  │
└───────────────┬─────────────────────────┘
                │
                │ Instanciação
                ↓
┌─────────────────────────────────────────┐
│      PostgreSQL (Fonte de Verdade)      │
│  ┌──────────────────────────────────┐   │
│  │ Documents, References, Projects  │   │
│  └──────────────────────────────────┘   │
│  ┌──────────────────────────────────┐   │
│  │ ontology_outbox (NOVO) ⭐        │   │
│  │ - Eventos para sincronização     │   │
│  │ - Transação atômica com dados    │   │
│  └──────────────────────────────────┘   │
└───────────────┬─────────────────────────┘
                │
                │ Worker Assíncrono (Celery/RQ)
                │ (Sincronização Idempotente)
                ↓
┌─────────────────────────────────────────┐
│         Knowledge Graph (Neo4j)         │
│    (Instâncias: entidades e relações)   │
│    (Consistência Eventual)              │
└─────────────────────────────────────────┘
```

**Por Que Outbox Pattern?**

- ✅ **Atomicidade:** Eventos criados na mesma transação dos dados
- ✅ **Resiliência:** Se Neo4j estiver fora, sistema continua funcionando
- ✅ **Idempotência:** Worker pode reprocessar eventos sem duplicar dados
- ✅ **Rastreabilidade:** Histórico completo de sincronizações
- ✅ **Desacoplamento:** Lógica de negócio separada da sincronização

**Modelo de Outbox:**

```python
# backend/app/models/ontology_outbox.py
from sqlalchemy import Column, String, Text, DateTime, JSON, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
import json

class OntologyOutboxEvent(Base):
    """Eventos para sincronização com Knowledge Graph."""
    
    __tablename__ = "ontology_outbox"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_type = Column(String(100), nullable=False, index=True)
    # Tipos: DOCUMENT_ONTOLOGY_UPDATED, DOCUMENT_DELETED, ENTITY_RESOLVED, etc.
    
    aggregate_id = Column(UUID(as_uuid=True), nullable=False, index=True)  # document_id, etc
    aggregate_type = Column(String(50), nullable=False)  # "document", "reference", etc
    
    payload = Column(JSON, nullable=False)  # Dados do evento
    
    processed = Column(Boolean, default=False, nullable=False, index=True)
    processed_at = Column(DateTime(timezone=True), nullable=True)
    retry_count = Column(Integer, default=0, nullable=False)
    error_message = Column(Text, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    def __repr__(self) -> str:
        return f"<OntologyOutboxEvent(id={self.id}, event_type='{self.event_type}', processed={self.processed})>"
```

**Service Refatorado com Outbox:**

```python
# backend/app/services/ontology_service.py
class OntologyService:
    """Service para gestão de ontologias com sincronização resiliente."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.extraction_service = KnowledgeExtractionService()
        self.outbox_repository = OutboxRepository(db)
        self.document_repository = DocumentRepository(db)
    
    async def process_document_ontology(
        self, 
        document_id: UUID,
        document_content: str
    ) -> ProcessedOntology:
        """
        Processa ontologia de um documento usando padrão Outbox.
        
        A operação é atômica no PostgreSQL. Sincronização com Neo4j
        ocorre de forma assíncrona via worker.
        """
        async with self.db.begin() as session:
            # 1. Extrair conhecimento
            extracted = await self.extraction_service.extract_from_document(
                document_content
            )
            
            # 2. Validar (poderia ter EntityResolutionService aqui)
            validated = await self._validate_knowledge(extracted)
            
            # 3. Atualizar documento no PostgreSQL (FONTE DE VERDADE)
            await self.document_repository.update_ontology_fields(
                document_id=document_id,
                concepts=validated.concepts,
                entities=validated.entities,
                relations=validated.relations,
                ontology_version="1.0.0"
            )
            
            # 4. Criar evento na outbox (MESMA TRANSAÇÃO)
            await self.outbox_repository.create_event(
                event_type="DOCUMENT_ONTOLOGY_UPDATED",
                aggregate_id=document_id,
                aggregate_type="document",
                payload={
                    "document_id": str(document_id),
                    "entities": [e.dict() for e in validated.entities],
                    "concepts": [c.dict() for c in validated.concepts],
                    "relations": [r.dict() for r in validated.relations],
                }
            )
            # Commit da transação (atômico: dados + evento)
        
        # Retorna resultado (Neo4j será atualizado assincronamente)
        return ProcessedOntology(
            document_id=document_id,
            entities=validated.entities,
            concepts=validated.concepts,
            relations=validated.relations,
            sync_status="pending"  # Status da sincronização
        )
```

**Worker de Sincronização:**

```python
# backend/app/workers/neo4j_sync_worker.py
from celery import Celery
import logging

logger = logging.getLogger(__name__)

app = Celery('neo4j_sync')

@app.task(bind=True, max_retries=3)
def sync_neo4j_from_outbox(self):
    """
    Worker que sincroniza eventos da outbox com Neo4j.
    
    Executa de forma idempotente e resiliente a falhas.
    """
    from app.core.database import AsyncSessionLocal
    from app.repositories.ontology_outbox_repository import OutboxRepository
    from app.repositories.knowledge_graph_repository import KnowledgeGraphRepository
    
    db = AsyncSessionLocal()
    outbox_repo = OutboxRepository(db)
    kg_repo = KnowledgeGraphRepository()
    
    try:
        # Buscar eventos não processados
        events = await outbox_repo.get_unprocessed_events(limit=100)
        
        for event in events:
            try:
                # Aplicar mudança no Neo4j (idempotente)
                await kg_repo.apply_event(event)
                
                # Marcar como processado
                await outbox_repo.mark_as_processed(event.id)
                logger.info(f"Event {event.id} synced to Neo4j successfully")
                
            except Exception as e:
                # Incrementar retry count
                await outbox_repo.increment_retry(event.id, str(e))
                logger.error(f"Failed to sync event {event.id}: {e}", exc_info=True)
                
                # Se exceder máximo de retries, marcar para revisão manual
                if event.retry_count >= 3:
                    logger.critical(
                        f"Event {event.id} exceeded max retries. Requires manual review.",
                        extra={"event_id": str(event.id), "error": str(e)}
                    )
        
        await db.commit()
        
    except Exception as e:
        await db.rollback()
        logger.error(f"Error in sync worker: {e}", exc_info=True)
        raise self.retry(exc=e, countdown=60)  # Retry em 60 segundos
    
    finally:
        await db.close()

# Configurar para rodar a cada 5 segundos
app.conf.beat_schedule = {
    'sync-neo4j-outbox': {
        'task': 'neo4j_sync_worker.sync_neo4j_from_outbox',
        'schedule': 5.0,
    },
}
```

**Fonte da Verdade para Leitura:**

```python
# Estratégia de leitura híbrida
class HybridReadStrategy:
    """
    Define de onde ler dados baseado no tipo de query.
    
    PostgreSQL = Fonte de verdade para metadata e dados transacionais
    Neo4j = Fonte de verdade para relações e queries de grafo
    """
    
    async def get_document_with_ontology(self, document_id: UUID) -> DocumentWithOntology:
        """
        Busca documento com ontologia.
        
        - Metadata e campos básicos: PostgreSQL (fonte de verdade)
        - Relações e entidades relacionadas: Neo4j (se disponível)
        """
        # 1. Buscar metadata do PostgreSQL (sempre)
        document = await document_repository.get_by_id(document_id)
        
        # 2. Tentar buscar relações do Neo4j (opcional, degrada graciosamente)
        try:
            related_entities = await kg_repository.get_related_entities(document_id)
            document.related_entities = related_entities
        except Exception as e:
            logger.warning(f"Could not fetch relations from Neo4j: {e}")
            document.related_entities = []  # Degrada graciosamente
        
        return document
```

**Benefícios da Arquitetura Outbox:**

- ✅ **Resiliência:** Sistema continua funcionando se Neo4j estiver fora
- ✅ **Consistência Eventual:** Dados eventualmente ficam consistentes
- ✅ **Rastreabilidade:** Histórico completo de sincronizações
- ✅ **Idempotência:** Reprocessamento seguro de eventos
- ✅ **Desacoplamento:** Lógica de negócio independente da sincronização

### 4.3 Integração com Models Existentes

**Expandir models SQLAlchemy com campos de ontologia:**

```python
# backend/app/models/document.py
class Document(Base):
    """Model de documento com suporte a ontologias."""
    
    # ... campos existentes ...
    
    # Campos de ontologia (NOVO)
    concepts = Column(JSON, nullable=True)  # Lista de conceitos
    entities = Column(JSON, nullable=True)  # Entidades extraídas
    relations = Column(JSON, nullable=True)  # Relações extraídas
    ontology_version = Column(String(20), default="1.0.0")  # Versão da ontologia usada
    extracted_at = Column(DateTime(timezone=True), nullable=True)  # Quando foi extraído
```

---

## 🚀 5. Processo de Evolução

### 5.1 Ciclo de Vida da Ontologia

**Baseado em:** Metodologia Stanford + Best Practices

```
1. Definição de Caso de Uso
   ↓
2. Criação/Atualização de Schema LinkML
   ↓
3. Validação (linkml-validate)
   ↓
4. Extração com OntoGPT (teste)
   ↓
5. Revisão e Refinamento (humano)
   ↓
6. Compilação para OWL
   ↓
7. Testes (unitários + integração)
   ↓
8. Versionamento (Git tag)
   ↓
9. Deploy (copiar para app/ontologies/)
   ↓
10. Migração de Dados (se necessário)
    ↓
11. Monitoramento e Feedback
    ↓
12. Próxima iteração
```

### 5.2 Perguntas de Competência

> **Melhoria de Validação:** Conectar perguntas de competência a testes automatizados para validação contínua.

**Documentar perguntas que a ontologia deve responder:**

```markdown
# documentacao/ontologias/COMPETENCY_QUESTIONS.md

## Perguntas de Competência v1.0.0

### Documentos
1. Quais documentos contêm este conceito?
2. Quais são as entidades principais de um documento?
3. Quais documentos estão relacionados semanticamente?
4. Quais conceitos são mencionados neste documento?

### Referências
5. Quais referências citam este documento?
6. Quais referências são sobre este assunto?
7. Quais conceitos estão associados a esta referência?

### Projetos
8. Quais documentos pertencem a este projeto?
9. Quais projetos usam esta referência?
10. Quais são os conceitos principais deste projeto?
```

**Testes Automatizados para Perguntas de Competência:**

```python
# backend/tests/ontologies/test_competency.py
import pytest
from uuid import UUID

@pytest.mark.asyncio
async def test_cq_01_find_documents_by_concept(ontology_service, test_kg_data):
    """
    Testa a Pergunta de Competência 1: Quais documentos contêm este conceito?
    
    Arrange: Popula o KG com dados de teste
    Act: Executa a query
    Assert: Verifica o resultado
    """
    # Arrange: Popula o KG com dados de teste
    await populate_kg_with_test_data(test_kg_data)
    
    # Act: Executa a query
    concept = "Inteligência Artificial"
    documents = await ontology_service.find_documents_by_concept(concept)
    
    # Assert: Verifica o resultado
    assert len(documents) >= 2, "Deveria encontrar pelo menos 2 documentos"
    assert any("IA" in d.title or "Artificial Intelligence" in d.title for d in documents), \
        "Deveria encontrar documentos relacionados"

@pytest.mark.asyncio
async def test_cq_02_find_main_entities_in_document(ontology_service, test_kg_data):
    """Testa CQ 2: Quais são as entidades principais de um documento?"""
    document_id = UUID("123e4567-e89b-12d3-a456-426614174000")
    
    entities = await ontology_service.find_main_entities_in_document(document_id)
    
    assert len(entities) > 0, "Deveria encontrar pelo menos uma entidade"
    # Verificar que entidades têm confiança acima do threshold
    assert all(e.confidence >= 0.7 for e in entities), \
        "Entidades principais devem ter confiança >= 0.7"

@pytest.mark.asyncio
async def test_cq_03_find_semantically_related_documents(ontology_service, test_kg_data):
    """Testa CQ 3: Quais documentos estão relacionados semanticamente?"""
    document_id = UUID("123e4567-e89b-12d3-a456-426614174001")
    
    related_docs = await ontology_service.find_semantically_related_documents(
        document_id,
        min_similarity=0.8
    )
    
    assert len(related_docs) >= 1, "Deveria encontrar pelo menos um documento relacionado"
    assert all(doc.similarity_score >= 0.8 for doc in related_docs), \
        "Documentos relacionados devem ter similaridade >= 0.8"

# ... mais testes para outras perguntas de competência
```

**Benefícios:**
- ✅ **Regressão Automatizada:** Garante que novas versões da ontologia não quebrem funcionalidades existentes
- ✅ **Documentação Viva:** Os testes se tornam a prova executável de que a ontologia funciona como esperado
- ✅ **CI/CD Integration:** Testes rodam automaticamente em cada PR

### 5.3 Processo de Refinamento

**Baseado em:** Stanford Ontology 101

1. **Começar Simples:**
   - Schema mínimo necessário para casos de uso
   - Adicionar complexidade gradualmente

2. **Validar Continuamente:**
   - Testar contra perguntas de competência
   - Validar com dados reais
   - Obter feedback de usuários

3. **Iterar:**
   - Adicionar classes/propriedades conforme necessário
   - Refinar baseado em uso real
   - Documentar decisões

---

## 🤖 6. Automação e Ferramentas

### 6.1 Integração com OntoGPT (com Estratégia de Fallback)

**Service de Extração com Fallback:**

> **Melhoria de Robustez:** Implementa estratégia de fallback usando spaCy quando OntoGPT falha, garantindo alta disponibilidade do sistema.

```python
# backend/app/services/knowledge_extraction_service.py
import spacy
from ontogpt import extract
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class KnowledgeExtractionService:
    """Service para extração de conhecimento usando OntoGPT com fallback para spaCy."""
    
    def __init__(self):
        self.schema_path = Path(__file__).parent.parent / "ontologies" / "schemas" / "v1" / "document_schema.yaml"
        # Carregar modelo spaCy para fallback
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            logger.warning("spaCy model 'en_core_web_sm' not found. Install with: python -m spacy download en_core_web_sm")
            self.nlp = None
    
    async def extract_from_document(
        self, 
        document_content: str
    ) -> ExtractedKnowledge:
        """
        Extrai conhecimento estruturado usando OntoGPT com fallback para spaCy.
        
        Args:
            document_content: Conteúdo do documento (texto)
            
        Returns:
            ExtractedKnowledge com entidades, conceitos e relações
        """
        try:
            # Tenta a extração primária com OntoGPT
            result = extract(
                input_text=document_content,
                template="Document",
                schema=str(self.schema_path)
            )
            
            # Adicionar verificação de confiança, se disponível
            # if hasattr(result, 'confidence') and result.confidence < 0.7:
            #     raise ValueError("Low confidence extraction")
            
            return ExtractedKnowledge(
                entities=result.extracted_object.get("entities", []),
                concepts=result.extracted_object.get("concepts", []),
                relations=result.extracted_object.get("extracted_relations", []),
                extraction_method="ontogpt"
            )
        except Exception as e:
            logger.error(f"OntoGPT extraction failed: {e}. Using fallback.", exc_info=True)
            return await self._fallback_extraction(document_content)
    
    async def _fallback_extraction(self, document_content: str) -> ExtractedKnowledge:
        """
        Extração de fallback usando spaCy para entidades básicas.
        
        Retorna apenas entidades nomeadas (NER), sem conceitos ou relações complexas.
        """
        if not self.nlp:
            logger.error("Fallback extraction unavailable: spaCy model not loaded")
            return ExtractedKnowledge(entities=[], concepts=[], relations=[], extraction_method="none")
        
        doc = self.nlp(document_content)
        entities = []
        
        for ent in doc.ents:
            entities.append(Entity(
                label=ent.text,
                entity_type=ent.label_.lower(),  # Normalizar labels
                confidence=1.0  # spaCy não retorna confiança, usar 1.0 como padrão
            ))
        
        logger.info(f"Fallback extraction completed: {len(entities)} entities found")
        
        # Retorna apenas entidades, sem conceitos ou relações complexas
        return ExtractedKnowledge(
            entities=entities,
            concepts=[],
            relations=[],
            extraction_method="spacy_fallback"
        )
```

**Benefícios:**
- ✅ **Alta Disponibilidade:** O enriquecimento de documentos não para se a API externa falhar
- ✅ **Degradação Graciosa:** O sistema continua a extrair valor (entidades básicas) mesmo em modo de falha
- ✅ **Resiliência:** Sistema robusto para operação em produção

### 6.2 Compilação Automática

**Script de Build:**

```python
# backend/scripts/build_ontologies.py
"""Script para compilar ontologias LinkML para OWL."""

import subprocess
from pathlib import Path

def build_ontologies():
    """Compila schemas LinkML para OWL."""
    schemas_dir = Path("app/ontologies/schemas/v1")
    owl_dir = Path("app/ontologies/owl")
    
    for schema_file in schemas_dir.glob("*.yaml"):
        owl_file = owl_dir / f"{schema_file.stem}.owl"
        
        # Compilar usando linkml-gen-owl
        subprocess.run([
            "linkml-gen-owl",
            str(schema_file),
            "-o", str(owl_file)
        ])
        
        print(f"✅ Compilado: {schema_file} -> {owl_file}")

if __name__ == "__main__":
    build_ontologies()
```

### 6.3 Validação Automática

**Tests de Ontologia:**

```python
# backend/tests/ontologies/test_schemas.py
import pytest
from linkml.validators import JsonSchemaDataValidator
from pathlib import Path

class TestOntologySchemas:
    """Testes de validação de schemas de ontologia."""
    
    def test_base_schema_valid(self):
        """Testa se o schema base é válido."""
        schema_path = Path("app/ontologies/schemas/v1/base_schema.yaml")
        validator = JsonSchemaDataValidator(schema_path)
        # Schema deve ser válido
        assert validator is not None
    
    def test_document_schema_valid(self):
        """Testa se o schema de documentos é válido."""
        schema_path = Path("app/ontologies/schemas/v1/document_schema.yaml")
        validator = JsonSchemaDataValidator(schema_path)
        assert validator is not None
    
    def test_schema_consistency(self):
        """Testa consistência entre schemas."""
        # Validar que imports funcionam
        # Validar que classes referenciadas existem
        pass
```

### 6.4 Resolução e Deduplicação de Entidades

> **Melhoria de Qualidade:** Implementa deduplicação usando embeddings de similaridade para manter o Knowledge Graph limpo e conectado.

**Service de Resolução de Entidades:**

```python
# backend/app/services/entity_resolution_service.py
from sentence_transformers import SentenceTransformer
import logging

logger = logging.getLogger(__name__)

class EntityResolutionService:
    """Service para resolução e deduplicação de entidades usando embeddings."""
    
    def __init__(self, kg_repository: 'KnowledgeGraphRepository'):
        """
        Inicializa o service de resolução de entidades.
        
        Args:
            kg_repository: Repository para acessar o Knowledge Graph
        """
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Modelo leve e rápido
        self.kg_repository = kg_repository
        self.similarity_threshold = 0.95  # Threshold para considerar entidades similares
    
    async def resolve_entity(self, entity: Entity) -> Entity:
        """
        Encontra ou cria uma entidade canônica no KG.
        
        Usa busca por similaridade semântica para evitar duplicatas.
        
        Args:
            entity: Entidade a ser resolvida
            
        Returns:
            Entity canônica (existente ou criada)
        """
        # Gerar embedding da entidade
        entity_embedding = self.model.encode(entity.label, convert_to_numpy=True)
        
        # Busca por similaridade no Neo4j (usando Vector Index)
        similar_entities = await self.kg_repository.find_similar_entities(
            embedding=entity_embedding.tolist(),
            threshold=self.similarity_threshold,
            limit=1
        )
        
        if similar_entities:
            # Usa a primeira entidade similar como canônica
            canonical_entity = similar_entities[0]
            logger.info(
                f"Merging entity '{entity.label}' into existing entity '{canonical_entity.label}'",
                extra={
                    "original_label": entity.label,
                    "canonical_label": canonical_entity.label,
                    "similarity": similar_entities[0].similarity
                }
            )
            return canonical_entity
        else:
            # Cria uma nova entidade se nenhuma similar for encontrada
            new_entity = await self.kg_repository.create_entity(entity)
            # Adiciona o embedding ao nó para futuras buscas
            await self.kg_repository.add_embedding_to_entity(
                entity_id=new_entity.id,
                embedding=entity_embedding.tolist()
            )
            logger.info(f"Created new entity: '{entity.label}' (ID: {new_entity.id})")
            return new_entity
```

**Benefícios:**
- ✅ **Qualidade do Grafo:** Garante um KG limpo, conectado e com alta integridade
- ✅ **Melhora as Queries:** As buscas se tornam muito mais precisas e completas
- ✅ **Reduz Ruído:** Elimina duplicatas semânticas (ex: "IA", "Inteligência Artificial", "A.I.")

**Configuração do Neo4j:**

Para usar busca por similaridade no Neo4j, é necessário:

1. Instalar plugin de vector index (ex: `neo4j-vector`)
2. Criar índice vetorial para entidades
3. Armazenar embeddings nos nós

```cypher
// Criar índice vetorial (exemplo)
CREATE VECTOR INDEX entity_embeddings
FOR (e:Entity)
ON e.embedding
OPTIONS {indexConfig: {
  `vector.dimensions`: 384,  // all-MiniLM-L6-v2 tem 384 dimensões
  `vector.similarity_function`: 'cosine'
}}
```

---

## 🌐 11. Governança Federada em Escala

> **🔴 Crítica Nível 2 Aplicada:** Evolução para um modelo de ontologia federada (semantic data mesh) para evitar gargalo de governança centralizada e permitir escalabilidade organizacional.

**O Problema Original:** O plano, mesmo sendo modular, ainda opera sob o paradigma de uma única "fonte da verdade" para a ontologia, gerenciada por uma equipe central. Isso cria um **gargalo de governança** em potencial quando diferentes unidades de negócio (Marketing, P&D, Jurídico) precisam evoluir suas ontologias em ritmos diferentes.

**Por Que Importa em Escala:**
- À medida que o sistema se torna um sucesso, diferentes unidades de negócio terão suas próprias necessidades de modelagem
- Forçar todos a passarem por um comitê central cria atrito político, lentidão e desincentiva a adoção
- O processo de versionamento centralizado se torna o novo "deploy de monolito"

**A Solução: Modelo de Ontologia Federada (Semantic Data Mesh)**

### 11.1 Arquitetura Federada

**Princípios Fundamentais:**

1. **Múltiplos Repositórios de Ontologia:** Diferentes domínios de negócio podem ter seus próprios repositórios Git para suas "ontologias de aplicação"
2. **Herança Explícita:** Cada ontologia de aplicação deve `importar` a ontologia base (`base_schema.yaml`), que atua como "Upper Ontology" da organização
3. **Registro Centralizado:** Um serviço de registro (`OntologyRegistry`) descobre, carrega e compila as diferentes ontologias federadas
4. **Contextualização no Processamento:** O serviço de extração pode ser instruído a usar um "contexto ontológico" específico (ex: `base + marketing_v1.2`)

**Diagrama de Arquitetura:**

```
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ Repo Ontologia   │      │ Repo Ontologia   │      │ Repo Ontologia   │
│      Base        │      │     Marketing    │      │      P&D         │
│  (base_schema)   │      │  (marketing.yaml)│      │   (rnd.yaml)     │
└─────────┬────────┘      └─────────┬────────┘      └─────────┬────────┘
          │                         │                         │
          │ imports                 │ imports                 │ imports
          │                         │                         │
          └─────────────────────────┼─────────────────────────┘
                                    ↓
                          ┌──────────────────┐
                          │ Ontology Registry│
                          │  (Serviço Central)│
                          └─────────┬────────┘
                                    │
                                    ↓
      ┌───────────────────────────────────────────────────────────┐
      │ KnowledgeExtractionService                                 │
      │  (carrega contexto ontológico: base + domain_schema)       │
      └───────────────────────────────────────────────────────────┘
```

### 11.2 Estrutura de Repositórios Federados

**Ontologia Base (Upper Ontology):**

```
repo-ontologia-base/
├── base_schema.yaml          # Ontologia base da organização
├── core_concepts.yaml        # Conceitos core compartilhados
└── common_relations.yaml     # Relações comuns
```

**Ontologias de Domínio:**

```
repo-ontologia-marketing/
├── marketing_schema.yaml     # Importa base_schema.yaml
├── README.md
└── DECISOES.md

repo-ontologia-rnd/
├── rnd_schema.yaml           # Importa base_schema.yaml
├── biology_imports.yaml      # Importa ontologia de terceiros (ex: biologia)
└── README.md
```

**Exemplo de Schema Federado:**

```yaml
# repo-ontologia-marketing/marketing_schema.yaml
id: https://example.com/ontologies/marketing/v1
name: Marketing Ontology
imports:
  - https://example.com/ontologies/base/v1/base_schema

classes:
  CustomerJourney:
    is_a: Process  # Herda de conceito base
    description: "Jornada do cliente através dos pontos de contato"
    attributes:
      stages:
        range: JourneyStage
        multivalued: true
      touchpoints:
        range: Touchpoint
        multivalued: true

  Campaign:
    is_a: Project  # Herda de conceito base
    description: "Campanha de marketing"
    attributes:
      target_audience:
        range: AudienceSegment
      metrics:
        range: CampaignMetric
        multivalued: true
```

### 11.3 Serviço de Registro de Ontologias

**`OntologyRegistry`: Descoberta e Compilação**

```python
# backend/app/services/ontology_registry.py
from pathlib import Path
import yaml
from linkml_runtime import SchemaView
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class OntologyRegistry:
    """Registra e gerencia ontologias federadas."""
    
    def __init__(self, base_ontology_path: Path, domain_ontologies_dir: Path):
        self.base_ontology_path = base_ontology_path
        self.domain_ontologies_dir = domain_ontologies_dir
        self._registry: Dict[str, SchemaView] = {}
        self._load_base_ontology()
        self._discover_domain_ontologies()
    
    def _load_base_ontology(self):
        """Carrega a ontologia base (Upper Ontology)."""
        try:
            base_schema = SchemaView(str(self.base_ontology_path))
            self._registry["base"] = base_schema
            logger.info(f"Base ontology loaded from {self.base_ontology_path}")
        except Exception as e:
            logger.error(f"Failed to load base ontology: {e}")
            raise
    
    def _discover_domain_ontologies(self):
        """Descobre e carrega ontologias de domínio."""
        for domain_file in self.domain_ontologies_dir.glob("**/*_schema.yaml"):
            domain_name = domain_file.stem.replace("_schema", "")
            try:
                domain_schema = SchemaView(str(domain_file))
                # Resolve imports (incluindo base)
                domain_schema.merge_schemas([self._registry["base"].schema])
                self._registry[domain_name] = domain_schema
                logger.info(f"Domain ontology '{domain_name}' loaded from {domain_file}")
            except Exception as e:
                logger.warning(f"Failed to load domain ontology {domain_file}: {e}")
    
    def get_ontology_context(
        self, 
        domains: List[str] = None
    ) -> SchemaView:
        """
        Retorna um contexto ontológico combinado.
        
        Args:
            domains: Lista de domínios a incluir (ex: ["marketing", "rnd"])
                    Se None, retorna apenas base.
        
        Returns:
            SchemaView com ontologias combinadas
        """
        if domains is None:
            return self._registry["base"]
        
        # Começa com base
        combined_schema = self._registry["base"].schema
        
        # Merge cada domínio solicitado
        for domain in domains:
            if domain not in self._registry:
                logger.warning(f"Domain '{domain}' not found in registry. Skipping.")
                continue
            # Merge schema (resolver conflitos de nomes se necessário)
            combined_schema = self._merge_schemas(
                combined_schema, 
                self._registry[domain].schema
            )
        
        return SchemaView(combined_schema)
    
    def list_available_domains(self) -> List[str]:
        """Retorna lista de domínios registrados."""
        return [name for name in self._registry.keys() if name != "base"]
    
    def _merge_schemas(self, base_schema, domain_schema):
        """Merge dois schemas LinkML (simplificado - na prática usar linkml-runtime)."""
        # Implementação simplificada - na prática, usar biblioteca LinkML
        # para resolver imports e merge corretamente
        merged_classes = {**base_schema.classes, **domain_schema.classes}
        merged_slots = {**base_schema.slots, **domain_schema.slots}
        
        # Criar novo schema merged (pseudocódigo - usar SchemaDefinition do LinkML)
        merged_schema = base_schema.__class__()
        merged_schema.classes = merged_classes
        merged_schema.slots = merged_slots
        # ... copiar outros campos
        
        return merged_schema
```

### 11.4 Integração com KnowledgeExtractionService

**Contextualização no Processamento:**

```python
# backend/app/services/knowledge_extraction_service.py (atualizado)
class KnowledgeExtractionService:
    """Service para extração de conhecimento usando OntoGPT com contexto ontológico."""
    
    def __init__(self, ontology_registry: OntologyRegistry):
        self.ontology_registry = ontology_registry
        self.nlp = spacy.load("en_core_web_sm")
    
    async def extract_from_document(
        self,
        document_content: str,
        ontology_context: List[str] = None,  # Ex: ["marketing", "rnd"]
        schema_path: Optional[Path] = None
    ) -> ExtractedKnowledge:
        """
        Extrai conhecimento usando contexto ontológico específico.
        
        Args:
            document_content: Conteúdo do documento
            ontology_context: Lista de domínios a incluir (None = apenas base)
            schema_path: Override manual (opcional)
        """
        # Se não especificado, usar contexto ontológico
        if schema_path is None:
            schema_view = self.ontology_registry.get_ontology_context(ontology_context)
            # Compilar schema combinado para arquivo temporário
            temp_schema_path = self._compile_combined_schema(schema_view)
            schema_path = temp_schema_path
        
        try:
            result = extract(
                input_text=document_content,
                template="Document",
                schema=str(schema_path)
            )
            return ExtractedKnowledge(
                entities=result.extracted_object.get("entities", []),
                concepts=result.extracted_object.get("concepts", []),
                relations=result.extracted_object.get("extracted_relations", []),
                extraction_method="ontogpt",
                ontology_context=ontology_context or ["base"]
            )
        except Exception as e:
            logger.error(f"OntoGPT extraction failed: {e}. Using fallback.", exc_info=True)
            return await self._fallback_extraction(document_content)
    
    def _compile_combined_schema(self, schema_view: SchemaView) -> Path:
        """Compila schema combinado para arquivo temporário."""
        # Exportar schema para YAML
        temp_path = Path(f"/tmp/combined_schema_{uuid.uuid4()}.yaml")
        with open(temp_path, "w") as f:
            yaml.dump(schema_view.schema, f)
        return temp_path
```

### 11.5 Gestão de Conflitos e Resolução de Namespaces

**Estratégia de Resolução de Conflitos:**

```python
# backend/app/services/ontology_registry.py (adicionar)
class OntologyRegistry:
    # ... código anterior ...
    
    def resolve_namespace_conflicts(
        self,
        base_schema: SchemaDefinition,
        domain_schema: SchemaDefinition
    ) -> SchemaDefinition:
        """
        Resolve conflitos de nomes quando duas ontologias definem
        o mesmo conceito com significados diferentes.
        
        Estratégia:
        - Se conceito existe apenas em base: usar base
        - Se conceito existe apenas em domain: adicionar com namespace
        - Se existe em ambos com mesmo significado (hash): usar base (evitar duplicata)
        - Se existe em ambos com significado diferente: prefixar domain (ex: "Marketing::Project")
        """
        merged_classes = {}
        
        # Mapear classes da base
        for class_name, class_def in base_schema.classes.items():
            merged_classes[class_name] = class_def
        
        # Adicionar classes do domain (resolver conflitos)
        for class_name, class_def in domain_schema.classes.items():
            if class_name in merged_classes:
                # Conflito detectado - verificar se é mesmo conceito
                if self._same_concept(merged_classes[class_name], class_def):
                    # Mesmo conceito - manter base (evitar duplicata)
                    logger.info(f"Concept '{class_name}' already in base. Using base definition.")
                    continue
                else:
                    # Conceito diferente - prefixar com namespace
                    prefixed_name = f"{domain_schema.name}::{class_name}"
                    merged_classes[prefixed_name] = class_def
                    logger.warning(
                        f"Namespace conflict: '{class_name}' has different meanings. "
                        f"Domain version prefixed as '{prefixed_name}'"
                    )
            else:
                # Sem conflito - adicionar normalmente
                merged_classes[class_name] = class_def
        
        # Criar schema merged
        merged_schema = SchemaDefinition(
            name=f"{base_schema.name}_merged",
            classes=merged_classes,
            # ... outros campos
        )
        
        return merged_schema
    
    def _same_concept(self, class1, class2) -> bool:
        """Verifica se duas definições de classe representam o mesmo conceito."""
        # Comparação simplificada (na prática, usar hash semântico ou comparação mais sofisticada)
        return (
            class1.description == class2.description and
            class1.is_a == class2.is_a
        )
```

### 11.6 Configuração e Descoberta Automática

**Configuração via Arquivo:**

```yaml
# backend/config/ontology_registry.yaml
ontology_registry:
  base_ontology:
    path: "ontologies/schemas/v1/base_schema.yaml"
    repository: "https://github.com/org/repo-ontologia-base"
  
  domain_ontologies:
    - name: "marketing"
      path: "ontologies/schemas/marketing/marketing_schema.yaml"
      repository: "https://github.com/org/repo-ontologia-marketing"
      auto_update: true
    
    - name: "rnd"
      path: "ontologies/schemas/rnd/rnd_schema.yaml"
      repository: "https://github.com/org/repo-ontologia-rnd"
      auto_update: true
    
    - name: "legal"
      path: "ontologies/schemas/legal/legal_schema.yaml"
      repository: "https://github.com/org/repo-ontologia-legal"
      auto_update: false  # Requer aprovação manual
```

**Worker de Atualização Automática:**

```python
# backend/app/workers/ontology_registry_worker.py
@app.task
async def update_ontology_registry():
    """
    Worker periódico para atualizar ontologias federadas dos repositórios Git.
    
    Roda diariamente e verifica se há novas versões das ontologias de domínio.
    """
    config = load_ontology_registry_config()
    registry = OntologyRegistry(...)
    
    for domain in config.domain_ontologies:
        if not domain.auto_update:
            continue
        
        # Clonar/pull do repositório Git
        repo_path = clone_or_pull_repository(domain.repository)
        
        # Validar schema
        schema_path = repo_path / domain.path
        if validate_schema(schema_path):
            # Atualizar registry
            registry.reload_domain(domain.name, schema_path)
            logger.info(f"Domain ontology '{domain.name}' updated successfully")
        else:
            logger.error(f"Invalid schema for '{domain.name}'. Update skipped.")
```

### 11.7 Benefícios da Governança Federada

**Autonomia de Domínio:**
- Cada time pode evoluir sua ontologia no seu próprio ritmo
- Reduz dependência de releases centralizados

**Governança Descentralizada:**
- Reduz gargalo central e atrito político
- Permite especialização por domínio

**Escalabilidade Organizacional:**
- O modelo cresce com a organização
- Facilita adoção por diferentes unidades de negócio

**Flexibilidade e Reuso:**
- Ontologia base garante vocabulário comum
- Domínios podem importar e estender conforme necessário

**Riscos Mitigados:**
- ✅ **Gargalo de Governança:** Removido através de autonomia de domínio
- ✅ **Atrito Político:** Reduzido através de governança descentralizada
- ✅ **Escalabilidade Limitada:** Resolvido através de arquitetura federada

---

## 📚 12. Documentação e Governança

### 12.1 Estrutura de Documentação

```
documentacao/ontologias/
├── README.md              # Visão geral e introdução
├── DECISOES.md            # ADRs (Architecture Decision Records)
├── EVOLUCAO.md            # Histórico de versões e mudanças
├── GLOSSARIO.md           # Glossário de termos
├── COMPETENCY_QUESTIONS.md # Perguntas de competência
└── GUIA_DESENVOLVIMENTO.md # Guia para desenvolvedores
```

### 12.2 Decisões de Modelagem (ADRs)

**Template:**

```markdown
# ADR-001: Estrutura Modular de Ontologias

## Status
Aceito

## Contexto
Necessidade de organizar ontologias de forma modular e escalável.

## Decisão
Usar estrutura modular com ontologia base e módulos especializados.

## Consequências
- ✅ Facilita manutenção
- ✅ Permite reuso
- ⚠️ Requer gerenciamento de imports
```

### 12.3 Glossário de Termos

**Manter glossário atualizado:**

```markdown
# documentacao/ontologias/GLOSSARIO.md

## Termos da Ontologia

### Concept
Conceito extraído ou definido no sistema. Representa uma ideia ou noção.

### Entity
Entidade nomeada extraída de documentos (pessoas, organizações, locais).

### Relation
Relação entre entidades ou conceitos (ex: "documento A menciona entidade B").

...
```

---

## 🎨 7. Experiência do Usuário e Ciclo de Feedback

> **🔴 Crítica Crítica Aplicada:** Conecta a arquitetura técnica ao valor tangível para o usuário final, garantindo que a complexidade se traduza em benefícios claros.

### 7.1 Paradoxo da Complexidade vs. Valor

**O Problema:** Uma arquitetura tecnicamente impressionante (LinkML → OWL → Neo4j → PostgreSQL) só terá sucesso se traduzir complexidade técnica em valor claro e tangível para o usuário final.

**A Solução:** Definir explicitamente como a interface do usuário expõe o poder do Knowledge Graph e como os usuários interagem com o sistema enriquecido.

### 7.2 Interface de Usuário e Funcionalidades

**Mockup Conceitual da Busca Melhorada:**

```
┌─────────────────────────────────────────────────────────┐
│  Busca Semântica                                        │
├─────────────────────────────────────────────────────────┤
│  [Buscar documentos sobre "ontologias em IA"...]  [🔍] │
├─────────────────────────────────────────────────────────┤
│  Resultados (3 documentos encontrados)                  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │ 📄 Artigo: "Ontologias em Agentes de IA"        │   │
│  │    ✅ 15 entidades identificadas                 │   │
│  │    🔗 8 documentos relacionados                  │   │
│  │    📊 5 conceitos principais                     │   │
│  │    [Ver relacionamentos →]  [Validar entidades] │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │ 📄 Paper: "Knowledge Graphs e LLMs"             │   │
│  │    ✅ 12 entidades identificadas                 │   │
│  │    🔗 6 documentos relacionados                  │   │
│  │    📊 4 conceitos principais                     │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

**Funcionalidades Chave da UI:**

1. **Visualização de Relacionamentos (Graph View):**
   - Botão "Ver relacionamentos" abre visualização de grafo
   - Usuário vê documentos, conceitos e entidades conectados
   - Navegação interativa pelo Knowledge Graph

2. **Links para Entidades Relacionadas:**
   - Cada entidade extraída é clicável
   - Mostra todos os documentos que mencionam a mesma entidade
   - Facilita descoberta de conhecimento relacionado

3. **Filtros Facetados Baseados em Ontologia:**
   - Filtrar por conceitos
   - Filtrar por tipos de entidades (pessoas, organizações, etc)
   - Filtrar por relações (ex: "documentos que referenciam X")

4. **Busca Multi-hop (Killer Feature):**
   - Query exemplo: "Documentos sobre IA que também mencionam ontologias e foram publicados após 2020"
   - Combina busca vetorial (RAG) com raciocínio de grafo

### 7.3 Fluxo de Feedback do Usuário

**Ciclo de Feedback Completo:**

```
┌─────────────────────────────────────────────────────────┐
│  1. Usuário Encontra Problema                           │
│     Ex: Entidade "IA" foi extraída incorretamente      │
│         como "Inteligência Artificial Corp"            │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ↓
┌─────────────────────────────────────────────────────────┐
│  2. Reporte na UI                                       │
│     - Botão "Reportar erro" na entidade                │
│     - Formulário: Tipo de erro, descrição              │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ↓
┌─────────────────────────────────────────────────────────┐
│  3. Criação de Ticket de Validação                      │
│     - Salvo em PostgreSQL (extraction_validations)     │
│     - Status: "pending_review"                         │
│     - Atribuído a especialista de domínio              │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ↓
┌─────────────────────────────────────────────────────────┐
│  4. Validação no Dashboard                              │
│     - Especialista revisa no dashboard                 │
│     - Corrige entidade/conceito/relação                │
│     - Aprova ou rejeita                                │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ↓
┌─────────────────────────────────────────────────────────┐
│  5. Atualização do Knowledge Graph                      │
│     - Correção aplicada no Neo4j                       │
│     - Feedback salvo para fine-tuning                  │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ↓
┌─────────────────────────────────────────────────────────┐
│  6. Feedback para Schema (Opcional, Periódico)         │
│     - Múltiplos feedbacks similares                    │
│     - Gera PR para atualizar schema LinkML             │
│     - Versão nova da ontologia                         │
└─────────────────────────────────────────────────────────┘
```

**Diagrama de Sequência - Reporte de Erro:**

```
Usuário    Frontend    Backend API    PostgreSQL    Neo4j    Dashboard
  │            │            │              │          │          │
  │──Report──>│            │              │          │          │
  │            │──POST──>  │              │          │          │
  │            │  /validations           │          │          │
  │            │            │──INSERT──>  │          │          │
  │            │            │  (validation)          │          │
  │            │<──201────  │              │          │          │
  │<──Success──│            │              │          │          │
  │            │            │              │          │          │
  │            │            │              │          │          │
  │            │            │              │          │──Notify──>│
  │            │            │              │          │          │
  │            │            │              │          │<──Review──│
  │            │            │              │          │          │
  │            │            │<──Update──── │          │          │
  │            │            │  (approved)  │          │          │
  │            │            │──Apply──────>│          │          │
  │            │            │  (to Neo4j)  │          │          │
```

### 7.4 Métricas de Valor de Negócio

**Além das métricas técnicas, definir métricas de valor de negócio:**

```python
# Métricas de Valor de Negócio
class BusinessMetrics:
    """Métricas que medem o valor entregue aos usuários."""
    
    # Métricas de Eficiência
    time_to_find_related_documents: float  # Redução de 30% no tempo
    documents_discovered_via_relations: int  # Aumento de 25% em descoberta
    
    # Métricas de Qualidade
    search_result_relevance_score: float  # NPS de relevância
    user_satisfaction_with_relations: float  # Feedback direto dos usuários
    
    # Métricas de Uso
    graph_navigation_usage_rate: float  # % de usuários que usam visualização de grafo
    entity_click_through_rate: float  # % de entidades clicadas
    
    # Métricas de Impacto
    cross_reference_usage_in_projects: int  # Referências cruzadas em novos projetos
    knowledge_reuse_rate: float  # Reuso de conceitos entre projetos
```

**Exemplos de Objetivos:**

- ✅ **Redução de 30%** no tempo gasto para encontrar documentos relacionados
- ✅ **Aumento de 25%** no uso de referências cruzadas em novos projetos
- ✅ **Melhoria de 40%** na relevância dos resultados de busca (métrica NPS)
- ✅ **Taxa de adoção de 60%** para visualização de relacionamentos

### 7.5 Killer Features Habilitadas pela Arquitetura

**O que esta arquitetura habilita que RAG puro não conseguiria:**

1. **Busca Multi-hop:**
   - Query: "Documentos que mencionam 'ontologias' E também citam 'Stanford' E foram criados por projetos relacionados a 'IA'"
   - **Por quê importa:** Permite descobrir conexões não óbvias entre documentos

2. **Navegação Explícita:**
   - Clicar em uma entidade mostra todos os documentos relacionados
   - Não precisa fazer nova busca, a relação já está no grafo
   - **Por quê importa:** Facilita exploração e descoberta de conhecimento

3. **Agregação Semântica:**
   - "Quais são os conceitos mais comuns nos documentos deste projeto?"
   - "Qual é a rede de relacionamentos entre as referências?"
   - **Por quê importa:** Insights agregados que não são possíveis apenas com busca vetorial

---

## 🔗 8. Integração com Sistema Existente

### 8.1 Fluxo de Integração Completo

```
Upload de Documento
    ↓
1. Google File Search (RAG) - MANTÉM
    ↓
2. OntoGPT Extraction (NOVO)
   - Usa schema LinkML
   - Extrai entidades, conceitos, relações
    ↓
3. Validação (NOVO)
   - Valida contra schema
   - Remove duplicatas
    ↓
4. Knowledge Graph (NOVO)
   - Cria nós no Neo4j
   - Cria relações
    ↓
5. PostgreSQL (ATUALIZA)
   - Salva metadata
   - Salva entidades/conceitos em JSONB
   - Atualiza campos de ontologia
    ↓
6. Busca Híbrida (NOVO)
   - Busca vetorial (Google File Search)
   - Busca simbólica (Knowledge Graph)
   - Fusão de resultados
```

### 8.2 Service de Ontologia

```python
# backend/app/services/ontology_service.py
class OntologyService:
    """Service para gestão de ontologias."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.extraction_service = KnowledgeExtractionService()
        self.kg_repository = KnowledgeGraphRepository()
        self.document_repository = DocumentRepository(db)
    
    async def process_document_ontology(
        self, 
        document_id: UUID,
        document_content: str
    ) -> ProcessedOntology:
        """
        Processa ontologia de um documento.
        
        Args:
            document_id: ID do documento
            document_content: Conteúdo do documento
            
        Returns:
            ProcessedOntology com entidades, conceitos e relações
        """
        # 1. Extrair conhecimento
        extracted = await self.extraction_service.extract_from_document(
            document_content
        )
        
        # 2. Validar
        validated = await self._validate_knowledge(extracted)
        
        # 3. Popular Knowledge Graph
        kg_result = await self.kg_repository.create_from_extraction(
            document_id=document_id,
            knowledge=validated
        )
        
        # 4. Atualizar documento no PostgreSQL
        await self.document_repository.update_ontology_fields(
            document_id=document_id,
            concepts=validated.concepts,
            entities=validated.entities,
            relations=validated.relations,
            ontology_version="1.0.0"
        )
        
        return ProcessedOntology(
            document_id=document_id,
            entities=validated.entities,
            concepts=validated.concepts,
            relations=validated.relations,
            kg_nodes=kg_result.nodes_created,
            kg_relations=kg_result.relations_created
        )
```

---

## ✅ 9. Checklist de Implementação

### Fase 1: Estrutura Base (Semana 1)

- [ ] Criar estrutura de diretórios
- [ ] Criar schema LinkML base (`base_schema.yaml`)
- [ ] Criar schema de documentos (`document_schema.yaml`)
- [ ] Configurar OntoGPT
- [ ] **Criar `KnowledgeExtractionService` com estratégia de fallback (spaCy)** ⭐
- [ ] **Instalar e configurar spaCy** (`python -m spacy download en_core_web_sm`)
- [ ] **Criar `EntityResolutionService` com deduplicação básica** ⭐
- [ ] **Instalar SentenceTransformers** (`pip install sentence-transformers`)
- [ ] Testes básicos de extração
- [ ] Testes unitários para os novos services

### Fase 2: Integração (Semana 2)

- [ ] Integrar extração no `DocumentService`
- [ ] Popular Knowledge Graph (Neo4j)
- [ ] **Configurar Vector Index no Neo4j para busca de similaridade** ⭐
- [ ] Integrar `EntityResolutionService` no fluxo de processamento
- [ ] Atualizar models SQLAlchemy
- [ ] Atualizar `DocumentRepository`
- [ ] **Criar testes de integração baseados nas Perguntas de Competência** ⭐
- [ ] Testes de integração gerais

### Fase 3: Versionamento e Governança (Semana 3)

- [ ] Setup de versionamento (Git tags)
- [ ] Scripts de build (LinkML → OWL)
- [ ] Processo de validação
- [ ] **Implementar padrão Outbox para sincronização** ⭐⭐
- [ ] **Criar tabela ontology_outbox** ⭐⭐
- [ ] **Criar worker de sincronização Neo4j (Celery/RQ)** ⭐⭐
- [ ] **Iniciar desenvolvimento do Framework de Curadoria Ativa** ⭐
- [ ] **Implementar Active Learning Service** ⭐
- [ ] **Adicionar logging de custo de API (OpenAI)** ⭐
- [ ] Documentação inicial

### Fase 4: Evolução e Otimização (Contínuo)

- [ ] Processo de refinamento
- [ ] Perguntas de competência
- [ ] ADRs (Decisões)
- [ ] Glossário
- [ ] **Configurar pipeline de testes de performance (CI/CD)** ⭐
- [ ] **Dashboard de monitoramento de custos** ⭐
- [ ] **Implementar gamificação e leaderboard** ⭐
- [ ] **Criar service de fine-tuning periódico** ⭐
- [ ] **Implementar métricas de valor de negócio** ⭐⭐
- [ ] **Criar UI para visualização de relacionamentos** ⭐⭐
- [ ] **Implementar busca multi-hop na interface** ⭐⭐
- [ ] Monitoramento e feedback

---

## 📊 10. Métricas e Monitoramento

### 10.1 Métricas de Qualidade (Técnicas)

- **Cobertura:** % de documentos com ontologia processada
- **Precisão:** Validação manual de extrações
- **Completude:** % de campos preenchidos
- **Consistência:** Conflitos entre versões
- **Taxa de Deduplicação:** % de entidades que foram mescladas (resolução)
- **Taxa de Sincronização:** % de eventos outbox processados com sucesso
- **Latência de Sincronização:** Tempo médio entre criação de evento e sincronização no Neo4j

### 10.1.1 Métricas de Valor de Negócio

> **🔴 Crítica Crítica Aplicada:** Métricas que medem valor real para usuários, não apenas métricas técnicas.

**Métricas de Eficiência:**
- **Tempo médio para encontrar documentos relacionados:** Objetivo: Redução de 30%
- **Taxa de descoberta via relações:** % de documentos descobertos através de navegação de grafo
- **Uso de busca multi-hop:** % de queries que utilizam raciocínio de grafo

**Métricas de Qualidade Percebida:**
- **NPS de relevância de busca:** Net Promoter Score dos resultados
- **Taxa de cliques em entidades relacionadas:** Engajamento com funcionalidades de grafo
- **Taxa de uso de visualização de relacionamentos:** Adoção da feature de grafo

**Métricas de Impacto:**
- **Taxa de reuso de conhecimento:** Conceitos reutilizados entre projetos
- **Referências cruzadas em novos projetos:** Aumento de 25% no uso de referências relacionadas
- **Taxa de validação humana:** % de extrações validadas (meta: 60%+)
- **Pontuação média de curadores:** Engajamento no framework de curadoria

**Dashboard de Métricas de Negócio:**

```python
# backend/app/api/v1/endpoints/metrics.py
@router.get("/metrics/business")
async def get_business_metrics(
    period: str = "month"
) -> BusinessMetricsResponse:
    """
    Retorna métricas de valor de negócio.
    """
    metrics_service = BusinessMetricsService()
    
    return BusinessMetricsResponse(
        period=period,
        efficiency=await metrics_service.get_efficiency_metrics(period),
        quality=await metrics_service.get_quality_metrics(period),
        impact=await metrics_service.get_impact_metrics(period),
        trends=await metrics_service.get_trends(period)
    )
```

### 10.2 Logging Estruturado

```python
# Log de operações de ontologia
logger.info(
    "Ontology extraction completed",
    extra={
        "document_id": document_id,
        "entities_count": len(entities),
        "concepts_count": len(concepts),
        "relations_count": len(relations),
        "ontology_version": "1.0.0",
        "processing_time_ms": processing_time,
        "extraction_method": extraction_method,  # "ontogpt" ou "spacy_fallback"
        "fallback_used": extraction_method == "spacy_fallback"
    }
)
```

### 10.3 Análise de Custo e Monitoramento de API

> **Melhoria de Governança:** Monitoramento de custos de APIs externas (OpenAI) para controle financeiro e visibilidade operacional.

**Logging de Custo:**

```python
# backend/app/services/knowledge_extraction_service.py
def _calculate_openai_cost(self, tokens: int, model: str = "gpt-4-turbo") -> float:
    """
    Calcula o custo de uma chamada à API OpenAI.
    
    Args:
        tokens: Número total de tokens (input + output)
        model: Modelo usado (gpt-4-turbo, gpt-3.5-turbo, etc)
        
    Returns:
        Custo em USD
    """
    # Preços por 1K tokens (exemplo para GPT-4 Turbo)
    prices = {
        "gpt-4-turbo": {"input": 0.01, "output": 0.03},
        "gpt-3.5-turbo": {"input": 0.001, "output": 0.002},
    }
    
    model_prices = prices.get(model, prices["gpt-4-turbo"])
    # Estimativa: 70% input, 30% output (ajustar conforme necessário)
    input_tokens = int(tokens * 0.7)
    output_tokens = int(tokens * 0.3)
    
    cost = (input_tokens / 1000 * model_prices["input"]) + \
           (output_tokens / 1000 * model_prices["output"])
    
    return cost

async def extract_from_document(self, document_content: str) -> ExtractedKnowledge:
    try:
        result = extract(...)
        
        # Logging de custo (se disponível na resposta)
        if hasattr(result, 'response_metadata'):
            total_tokens = result.response_metadata.get('total_tokens', 0)
            cost = self._calculate_openai_cost(total_tokens)
            
            logger.info(
                "OntoGPT API call completed",
                extra={
                    "tokens": total_tokens,
                    "cost_usd": cost,
                    "model": "gpt-4-turbo"
                }
            )
        
        return ExtractedKnowledge(...)
    except Exception as e:
        # ... fallback ...
```

**Dashboard de Monitoramento:**

Métricas a serem monitoradas (usando Grafana, Datadog ou similar):

1. **Custo Total:**
   - Custo diário/mensal de APIs
   - Custo médio por documento
   - Documentos mais caros para processar

2. **Performance:**
   - Latência de extração (p50, p95, p99)
   - Taxa de fallback (spaCy usado)
   - Throughput (documentos/minuto)

3. **Qualidade:**
   - Taxa de deduplicação
   - Número de entidades/conceitos extraídos
   - Taxa de validação humana (aprovado/rejeitado)

**Alertas Configurados:**

```python
# Exemplo de alerta de custo
if daily_cost > BUDGET_LIMIT:
    send_alert(
        level="warning",
        message=f"Daily API cost ({daily_cost:.2f} USD) exceeded budget ({BUDGET_LIMIT} USD)"
    )
```

### 10.4 Testes de Performance

> **Melhoria de Otimização:** Pipeline de testes de performance para detectar regressões antes da produção.

**Testes de Performance:**

```python
# backend/tests/ontologies/test_performance.py
import pytest
from time import time
import asyncio

@pytest.mark.performance
@pytest.mark.asyncio
async def test_extraction_latency_for_standard_document(ontology_service):
    """Verifica se a extração de um documento padrão leva menos de 10s."""
    standard_content = "A" * 50000  # ~50KB de texto
    
    start_time = time()
    result = await ontology_service.extract_from_document(standard_content)
    duration = time() - start_time
    
    assert duration < 10.0, f"Extração muito lenta: {duration:.2f}s (limite: 10s)"
    assert result.entities_count > 0, "Nenhuma entidade extraída"

@pytest.mark.performance
@pytest.mark.asyncio
async def test_extraction_latency_for_large_document(ontology_service):
    """Verifica se a extração de um documento grande (10MB) leva menos de 30s."""
    large_content = "A" * 10_000_000  # ~10MB
    
    start_time = time()
    result = await ontology_service.extract_from_document(large_content)
    duration = time() - start_time
    
    assert duration < 30.0, f"Extração muito lenta para documento grande: {duration:.2f}s (limite: 30s)"

@pytest.mark.performance
@pytest.mark.asyncio
async def test_query_latency_competency_questions(ontology_service, test_kg):
    """Verifica latência das principais queries de competência."""
    queries = [
        ("find_documents_by_concept", "Inteligência Artificial"),
        ("find_related_documents", "doc-123"),
        ("find_concepts_in_document", "doc-456"),
    ]
    
    for query_name, param in queries:
        start_time = time()
        result = await ontology_service.execute_competency_query(query_name, param)
        duration = time() - start_time
        
        assert duration < 2.0, \
            f"Query '{query_name}' muito lenta: {duration:.2f}s (limite: 2s)"
```

**Integração com CI/CD:**

```yaml
# .github/workflows/performance-tests.yml
name: Performance Tests

on:
  pull_request:
    paths:
      - 'backend/app/services/ontology_service.py'
      - 'backend/app/services/knowledge_extraction_service.py'

jobs:
  performance-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run performance tests
        run: |
          pytest backend/tests/ontologies/test_performance.py \
            -m performance \
            --durations=10
```

### 10.5 Framework de Curadoria Ativa

> **🟠 Crítica Crítica Aplicada:** Transforma o "Dashboard de Validação" em um framework operacional que resolve o problema do "humano no loop" através de gamificação, aprendizado ativo e integração ao fluxo de trabalho.

**O Problema Original:** O dashboard se tornaria um "cemitério de validações pendentes" sem fluxo de trabalho bem definido e incentivos claros.

**A Solução:** Framework de Curadoria Ativa com 3 pilares:

#### 10.5.1 Dashboard de Validação (Base)

**Requisitos da Interface:**

1. **Visualização:**
   - Texto original com entidades/conceitos destacados
   - Relações visualizadas graficamente
   - Confiança de extração exibida
   - **Priorização automática** (Active Learning)

2. **Ações:**
   - Aprovar/Rejeitar extração completa
   - Editar entidades (adicionar/remover/modificar)
   - Editar relações
   - Adicionar conceitos manualmente

3. **Feedback Loop:**
   - Correções salvas como dataset de treino
   - Métricas de taxa de aprovação
   - Histórico de correções

**Estrutura de Dados para Feedback:**

```python
# Model para armazenar validações
class ExtractionValidation(Base):
    """Validação humana de extração."""
    __tablename__ = "extraction_validations"
    
    id = Column(UUID, primary_key=True)
    document_id = Column(UUID, ForeignKey("documents.id"))
    extraction_id = Column(UUID)  # ID da extração original
    validator_id = Column(String)  # ID do usuário (Clerk)
    status = Column(String)  # "approved", "rejected", "modified"
    corrections = Column(JSON)  # Entidades/conceitos corrigidos
    feedback = Column(Text)  # Comentários do validador
    priority_score = Column(Float)  # Score de prioridade (Active Learning)
    validated_at = Column(DateTime, server_default=func.now())
    
    # Campos para gamificação
    validator_contribution_score = Column(Integer, default=0)
```

#### 10.5.2 Aprendizado Ativo (Active Learning)

**Priorização Inteligente de Validações:**

O sistema não mostra todas as extrações para validação. Em vez disso, usa **Aprendizado Ativo** para priorizar o que trará maior ganho de informação.

```python
# backend/app/services/active_learning_service.py
class ActiveLearningService:
    """Service para priorizar validações usando Active Learning."""
    
    def calculate_priority_score(
        self, 
        extraction: ExtractedKnowledge,
        document_importance: float = 1.0
    ) -> float:
        """
        Calcula score de prioridade para validação.
        
        Prioriza extrações onde o modelo está mais "incerto"
        e que trarão maior ganho de informação.
        """
        # Fator 1: Incerteza do modelo (baixa confiança = alta prioridade)
        uncertainty_score = 1.0 - extraction.average_confidence
        
        # Fator 2: Raridade de entidades (entidades novas = alta prioridade)
        entity_rarity = self._calculate_entity_rarity(extraction.entities)
        
        # Fator 3: Importância do documento (documentos importantes = alta prioridade)
        importance_factor = document_importance
        
        # Fator 4: Diversidade (extrações com tipos diferentes de entidades)
        diversity_score = self._calculate_diversity(extraction)
        
        # Score combinado
        priority_score = (
            uncertainty_score * 0.4 +
            entity_rarity * 0.3 +
            importance_factor * 0.2 +
            diversity_score * 0.1
        )
        
        return priority_score
    
    async def get_next_validation_batch(
        self, 
        limit: int = 10
    ) -> list[ExtractionValidation]:
        """
        Retorna próximas extrações a serem validadas, priorizadas.
        """
        # Buscar extrações não validadas
        unvalidated = await validation_repository.get_unvalidated_extractions()
        
        # Calcular scores de prioridade
        scored = [
            (extraction, self.calculate_priority_score(extraction))
            for extraction in unvalidated
        ]
        
        # Ordenar por prioridade (maior primeiro)
        scored.sort(key=lambda x: x[1], reverse=True)
        
        # Retornar top N
        return [extraction for extraction, score in scored[:limit]]
```

**Interface do Dashboard com Priorização:**

```python
# Exemplo de endpoint da API
@router.get("/validation/queue")
async def get_validation_queue(
    user_id: str = Depends(get_current_user),
    limit: int = 10
) -> ValidationQueueResponse:
    """
    Retorna fila de validações priorizadas para o usuário.
    
    Usa Active Learning para mostrar apenas as mais importantes.
    """
    active_learning_service = ActiveLearningService()
    queue = await active_learning_service.get_next_validation_batch(limit)
    
    return ValidationQueueResponse(
        items=queue,
        total_pending=await validation_repository.count_unvalidated(),
        estimated_time_minutes=len(queue) * 2  # Estimativa: 2min por validação
    )
```

#### 10.5.3 Gamificação e Incentivos

**Sistema de Pontuação e Reconhecimento:**

```python
# backend/app/services/curation_gamification_service.py
class CurationGamificationService:
    """Service para gamificação da curadoria."""
    
    async def record_validation(
        self, 
        validator_id: str,
        validation: ExtractionValidation
    ) -> CurationScore:
        """
        Registra validação e atualiza pontuação do curador.
        """
        # Calcular pontos baseados na qualidade da validação
        base_points = 10
        
        # Bonus por correções (quanto mais correções úteis, mais pontos)
        correction_bonus = len(validation.corrections) * 5
        
        # Bonus por validações de alta prioridade (mais impacto)
        priority_bonus = validation.priority_score * 20
        
        total_points = base_points + correction_bonus + priority_bonus
        
        # Atualizar pontuação do usuário
        await user_repository.add_curation_points(validator_id, total_points)
        
        # Verificar badges/conquistas
        badges = await self._check_badges(validator_id)
        
        return CurationScore(
            user_id=validator_id,
            points_earned=total_points,
            total_points=await user_repository.get_total_points(validator_id),
            badges_earned=badges,
            rank=await self._get_rank(validator_id)
        )
```

**Badges e Conquistas:**

- 🏆 **Curador Iniciante:** Validou 10 extrações
- 🥇 **Curador Experiente:** Validou 100 extrações
- 🎯 **Precisão Perfeita:** 95%+ de validações aprovadas
- 🔍 **Caçador de Erros:** Encontrou e corrigiu 50 entidades incorretas
- ⚡ **Validador Rápido:** Validou 20 extrações em um dia

**Leaderboard:**

```python
@router.get("/curation/leaderboard")
async def get_curation_leaderboard(
    period: str = "month"  # "week", "month", "all_time"
) -> LeaderboardResponse:
    """
    Retorna leaderboard de curadores.
    """
    leaders = await user_repository.get_top_curators(period, limit=10)
    
    return LeaderboardResponse(
        period=period,
        leaders=[
            LeaderEntry(
                user_id=user.id,
                username=user.username,
                points=user.curation_points,
                validations_count=user.validations_count,
                rank=rank + 1
            )
            for rank, user in enumerate(leaders)
        ]
    )
```

#### 10.5.4 Integração ao Fluxo de Trabalho

**Validação Contextual (Não Isolada):**

Em vez de pedir ao usuário para ir a um dashboard separado, integrar validação no fluxo de trabalho existente:

1. **Antes de Usar um Documento:**
   - Ao abrir um documento na UI, mostrar banner: "Este documento tem 3 entidades não validadas. Deseja validar agora? (2 min)"
   - Se o usuário validar, ganha pontos e o documento fica marcado como "validado por você"

2. **Durante Criação de Projeto:**
   - Ao criar projeto, sugerir validar entidades dos documentos relacionados
   - "Você está adicionando 5 documentos. Deseja validar as entidades principais agora?"

3. **Notificações Contextuais:**
   - "Você é especialista em 'IA'. Há 3 extrações sobre este tema aguardando validação."

#### 10.5.5 Fine-Tuning Baseado em Feedback

**Dataset de Treino para Fine-Tuning:**

```python
# backend/app/services/fine_tuning_service.py
class FineTuningService:
    """Service para preparar dados de fine-tuning baseado em validações."""
    
    async def export_training_dataset(
        self,
        min_validations: int = 100
    ) -> TrainingDataset:
        """
        Exporta dataset de treino baseado em validações humanas.
        
        O dataset será usado para fine-tune de um modelo menor (ex: Llama 3)
        que pode substituir ou complementar o GPT-4.
        """
        # Buscar validações aprovadas com correções
        validations = await validation_repository.get_approved_with_corrections(
            min_count=min_validations
        )
        
        training_examples = []
        
        for validation in validations:
            # Buscar extração original
            original_extraction = await extraction_repository.get_by_id(
                validation.extraction_id
            )
            
            # Criar exemplo de treino (entrada: texto, saída: extração corrigida)
            example = TrainingExample(
                input_text=original_extraction.document_content,
                expected_output={
                    "entities": validation.corrections.get("entities", []),
                    "concepts": validation.corrections.get("concepts", []),
                    "relations": validation.corrections.get("relations", [])
                },
                metadata={
                    "validator_id": validation.validator_id,
                    "document_id": str(validation.document_id),
                    "confidence_improvement": validation.confidence_delta
                }
            )
            training_examples.append(example)
        
        # Salvar em formato JSONL (um exemplo por linha)
        dataset_path = f"training_datasets/fine_tuning_{datetime.now().isoformat()}.jsonl"
        await self._save_jsonl(training_examples, dataset_path)
        
        # Upload para S3 (para processamento futuro)
        await s3_client.upload_file(dataset_path, "training-datasets/")
        
        return TrainingDataset(
            path=dataset_path,
            examples_count=len(training_examples),
            total_validations=len(validations)
        )
```

**Processo de Fine-Tuning Periódico:**

```python
# backend/app/workers/fine_tuning_worker.py
@app.task
def periodic_fine_tuning():
    """
    Tarefa periódica (mensal) para fine-tuning do modelo de extração.
    
    Usa validações humanas acumuladas para melhorar o modelo.
    """
    fine_tuning_service = FineTuningService()
    
    # 1. Exportar dataset
    dataset = await fine_tuning_service.export_training_dataset(min_validations=500)
    
    # 2. Treinar modelo (Llama 3 fine-tuned)
    model_path = await train_model(dataset)
    
    # 3. Validar modelo (teste em conjunto de validação)
    evaluation_metrics = await evaluate_model(model_path)
    
    # 4. Se métricas melhorarem, fazer deploy do novo modelo
    if evaluation_metrics.f1_score > current_model_f1_score * 1.05:  # 5% de melhoria
        await deploy_model(model_path, version="v2")
        logger.info(f"Deployed improved extraction model: {evaluation_metrics}")
    
    return {
        "dataset_size": dataset.examples_count,
        "model_metrics": evaluation_metrics,
        "deployed": evaluation_metrics.f1_score > current_model_f1_score * 1.05
    }
```

### 10.5.6 MLOps e Governança de Modelos

> **🟠 Crítica Nível 2 Aplicada:** Framework de MLOps para governança, auditabilidade e explicabilidade de modelos fine-tuned, transformando o pipeline de fine-tuning de uma "caixa-preta" para um sistema auditável e explicável.

**O Problema Original:** O pipeline de fine-tuning periódico cria uma nova caixa-preta. Se o modelo fine-tuned começar a fazer extrações estranhas ou enviesadas, como depurar o problema? O processo de deploy é baseado em métricas de F1-score, mas isso não captura nuances de qualidade ou viés.

**Por Que Importa:**
- Em produção, a incapacidade de explicar ou auditar o comportamento de um modelo é um risco significativo
- Vieses sutis podem ser introduzidos silenciosamente
- Rastreabilidade é essencial para conformidade e confiança

**A Solução: Framework de MLOps para Governança de Modelos**

#### 10.5.6.1 Cartões de Modelo (Model Cards)

**Estrutura de Model Card:**

```python
# backend/app/services/model_card_service.py
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional
import json

@dataclass
class ModelCard:
    """Cartão de modelo para documentação e governança."""
    
    model_id: str
    model_name: str
    version: str
    base_model: str  # Ex: "llama-3-8b"
    training_date: datetime
    training_dataset_path: str  # S3 path
    training_dataset_size: int
    
    # Métricas de Performance
    performance_metrics: Dict[str, float]  # F1, precision, recall
    performance_by_slice: Dict[str, Dict[str, float]]  # Por tipo de documento, domínio, etc.
    
    # Análise de Viés
    bias_analysis: Optional[Dict[str, float]]  # Métricas de Fairlearn, etc.
    
    # Limitações Conhecidas
    known_limitations: List[str]
    intended_use_cases: List[str]
    
    # Linhagem
    parent_model_id: Optional[str]  # Modelo anterior (se houver)
    fine_tuning_hyperparameters: Dict[str, any]
    
    def to_markdown(self) -> str:
        """Exporta Model Card para Markdown."""
        return f"""# Model Card: {self.model_name} v{self.version}

## Informações Básicas

- **Model ID:** {self.model_id}
- **Base Model:** {self.base_model}
- **Training Date:** {self.training_date.isoformat()}
- **Training Dataset:** {self.training_dataset_path} ({self.training_dataset_size} examples)

## Métricas de Performance

### Métricas Globais

- **F1-Score:** {self.performance_metrics.get('f1', 'N/A'):.3f}
- **Precision:** {self.performance_metrics.get('precision', 'N/A'):.3f}
- **Recall:** {self.performance_metrics.get('recall', 'N/A'):.3f}

### Performance por Slice

{self._format_performance_by_slice()}

## Análise de Viés

{self._format_bias_analysis()}

## Limitações Conhecidas

{chr(10).join(f'- {limitation}' for limitation in self.known_limitations)}

## Casos de Uso Pretendidos

{chr(10).join(f'- {use_case}' for use_case in self.intended_use_cases)}

## Linhagem

- **Parent Model:** {self.parent_model_id or 'None (base model)'}
- **Hyperparameters:** {json.dumps(self.fine_tuning_hyperparameters, indent=2)}
"""

class ModelCardService:
    """Service para criar e gerenciar Model Cards."""
    
    async def create_model_card(
        self,
        model_id: str,
        model_path: str,
        training_dataset_path: str,
        evaluation_results: Dict
    ) -> ModelCard:
        """
        Cria Model Card após treinamento de modelo.
        """
        # Buscar informações do modelo
        model_info = await self._load_model_info(model_path)
        
        # Avaliar em slices de dados críticos
        performance_by_slice = await self._evaluate_by_slice(model_path)
        
        # Análise de viés
        bias_analysis = await self._analyze_bias(model_path)
        
        model_card = ModelCard(
            model_id=model_id,
            model_name=model_info["name"],
            version=model_info["version"],
            base_model=model_info["base_model"],
            training_date=datetime.utcnow(),
            training_dataset_path=training_dataset_path,
            training_dataset_size=evaluation_results["dataset_size"],
            performance_metrics=evaluation_results["metrics"],
            performance_by_slice=performance_by_slice,
            bias_analysis=bias_analysis,
            known_limitations=await self._identify_limitations(model_path),
            intended_use_cases=["Knowledge extraction from documents"],
            parent_model_id=evaluation_results.get("parent_model_id"),
            fine_tuning_hyperparameters=model_info["hyperparameters"]
        )
        
        # Salvar Model Card
        await self._save_model_card(model_card)
        
        return model_card
    
    async def _evaluate_by_slice(
        self,
        model_path: str
    ) -> Dict[str, Dict[str, float]]:
        """
        Avalia modelo em slices de dados críticos.
        
        Slices:
        - Por tipo de documento (técnico, legal, financeiro, etc.)
        - Por domínio (marketing, P&D, jurídico)
        - Por tamanho de documento
        """
        slices = {
            "document_type": await self._evaluate_by_document_type(model_path),
            "domain": await self._evaluate_by_domain(model_path),
            "document_size": await self._evaluate_by_document_size(model_path)
        }
        
        return slices
```

#### 10.5.6.2 Linhagem de Extração

**Modelo de Dados para Rastreabilidade:**

```python
# backend/app/models/ontology.py (adicionar)
class ExtractionLineage(Base):
    """Linhagem de uma extração (qual modelo produziu qual dado)."""
    __tablename__ = "extraction_lineage"
    
    id = Column(UUID, primary_key=True, default=uuid4)
    extraction_id = Column(UUID, ForeignKey("extractions.id"))
    model_id = Column(String)  # ID do modelo usado
    model_version = Column(String)
    model_card_path = Column(String)  # Path para Model Card
    extraction_timestamp = Column(DateTime, server_default=func.now())
    
    # Metadata do modelo no momento da extração
    model_metadata = Column(JSONB)  # Hyperparameters, dataset usado, etc.

# Atualizar ExtractionValidation para incluir linhagem
class ExtractionValidation(Base):
    # ... campos existentes ...
    
    extraction_model_id = Column(String)  # ID do modelo que produziu a extração
    extraction_model_version = Column(String)
```

**Integração no Serviço de Extração:**

```python
# backend/app/services/knowledge_extraction_service.py (atualizado)
class KnowledgeExtractionService:
    # ... código anterior ...
    
    async def extract_from_document(
        self,
        document_content: str,
        model_id: str = None  # Modelo específico (ou None para usar padrão)
    ) -> ExtractedKnowledge:
        """
        Extrai conhecimento e registra linhagem.
        """
        # Determinar modelo a usar
        if model_id is None:
            model_id = await self._get_current_production_model_id()
        
        model_info = await self._get_model_info(model_id)
        
        # Executar extração
        extracted = await self._execute_extraction(document_content, model_info)
        
        # Registrar linhagem
        lineage = ExtractionLineage(
            extraction_id=extracted.id,
            model_id=model_id,
            model_version=model_info["version"],
            model_card_path=model_info["model_card_path"],
            model_metadata={
                "base_model": model_info["base_model"],
                "training_date": model_info["training_date"],
                "dataset_path": model_info["training_dataset_path"]
            }
        )
        self.db.add(lineage)
        await self.db.commit()
        
        # Adicionar metadata de modelo ao resultado
        extracted.extraction_model_id = model_id
        extracted.extraction_model_version = model_info["version"]
        
        return extracted
```

#### 10.5.6.3 Suíte de Testes Comportamentais

**Framework de Testes Qualitativos:**

```python
# backend/tests/ontologies/test_model_behavior.py
import pytest
from checklist.test_types import MFT, INV, DIR  # Behavioral testing library
from typing import List, Dict

class ModelBehaviorTestSuite:
    """Suíte de testes comportamentais para modelos de extração."""
    
    def __init__(self, model: ExtractorModel):
        self.model = model
    
    def test_robustness_to_typos(self):
        """
        Testa robustez a typos comuns.
        
        O modelo deve extrair o mesmo conceito mesmo com typos.
        """
        test_cases = [
            ("Inteligência Artificial", "Inteligencia Artificial"),  # Sem acento
            ("Machine Learning", "Machine Learing"),  # Typo
            ("Deep Learning", "Deep Learing"),  # Typo
        ]
        
        for correct, typo in test_cases:
            original_extraction = self.model.extract(f"Documento sobre {correct}")
            typo_extraction = self.model.extract(f"Documento sobre {typo}")
            
            # Verificar que conceitos extraídos são similares
            assert self._concepts_similar(
                original_extraction.concepts,
                typo_extraction.concepts
            ), f"Model should be robust to typo: '{typo}'"
    
    def test_invariance_to_gender(self):
        """
        Testa invariância a mudanças de gênero em nomes.
        
        O modelo não deve associar gênero a conceitos específicos.
        """
        test_cases = [
            ("João Silva trabalha com IA", "Maria Silva trabalha com IA"),
            ("Engenheiro desenvolveu sistema", "Engenheira desenvolveu sistema"),
        ]
        
        for male_text, female_text in test_cases:
            male_extraction = self.model.extract(male_text)
            female_extraction = self.model.extract(female_text)
            
            # Extrações devem ser semanticamente equivalentes
            assert self._extractions_equivalent(
                male_extraction,
                female_extraction
            ), "Model should be invariant to gender"
    
    def test_negation_handling(self):
        """
        Testa capacidade de lidar com negação.
        
        "Não é sobre IA" não deve extrair "IA" como conceito principal.
        """
        positive_text = "Este documento é sobre Inteligência Artificial"
        negative_text = "Este documento não é sobre Inteligência Artificial"
        
        positive_extraction = self.model.extract(positive_text)
        negative_extraction = self.model.extract(negative_text)
        
        # Texto negativo não deve ter "IA" como conceito principal
        ia_concept_positive = any(
            "inteligência artificial" in c.label.lower()
            for c in positive_extraction.concepts
        )
        ia_concept_negative = any(
            "inteligência artificial" in c.label.lower()
            for c in negative_extraction.concepts
        )
        
        assert ia_concept_positive, "Positive text should extract IA"
        # Negação pode ainda extrair IA, mas com menor confiança ou como conceito secundário
        # (depende da estratégia - aqui é um exemplo simplificado)
    
    def test_known_failure_cases(self):
        """
        Testa casos de falha conhecidos de versões anteriores.
        
        Garante que regressões não são introduzidas.
        """
        known_failures = [
            {
                "input": "Documento sobre projeto de pesquisa em IA",
                "expected_concepts": ["Inteligência Artificial", "Pesquisa"],
                "previous_failure": "Não extraía 'Pesquisa' como conceito"
            },
            # Adicionar mais casos conhecidos
        ]
        
        for case in known_failures:
            extraction = self.model.extract(case["input"])
            extracted_concepts = [c.label for c in extraction.concepts]
            
            for expected in case["expected_concepts"]:
                assert any(
                    expected.lower() in c.lower() for c in extracted_concepts
                ), f"Known failure case not fixed: {case['previous_failure']}"

# Testes pytest
@pytest.mark.behavior
def test_model_behavior_suite(current_extraction_model):
    """Executa suíte completa de testes comportamentais."""
    suite = ModelBehaviorTestSuite(current_extraction_model)
    
    suite.test_robustness_to_typos()
    suite.test_invariance_to_gender()
    suite.test_negation_handling()
    suite.test_known_failure_cases()
```

#### 10.5.6.4 Explainability no Dashboard

**Integração de SHAP/LIME no Dashboard:**

```python
# backend/app/services/explainability_service.py
import shap
import lime
from lime.lime_text import LimeTextExplainer
from typing import List, Dict

class ExplainabilityService:
    """Service para explicabilidade de extrações."""
    
    def __init__(self, model: ExtractorModel):
        self.model = model
        self.explainer = LimeTextExplainer(class_names=["entities", "concepts", "relations"])
    
    async def explain_extraction(
        self,
        document_text: str,
        extracted_entity: Entity
    ) -> ExtractionExplanation:
        """
        Explica por que uma entidade foi extraída.
        
        Retorna quais palavras no texto mais influenciaram a extração.
        """
        # Usar LIME para explicação
        explanation = self.explainer.explain_instance(
            document_text,
            lambda x: self._predict_entity_probability(x, extracted_entity),
            num_features=10  # Top 10 palavras mais influentes
        )
        
        # Extrair features mais importantes
        important_words = explanation.as_list()
        
        return ExtractionExplanation(
            entity_id=extracted_entity.id,
            entity_label=extracted_entity.label,
            important_words=important_words,  # Lista de (palavra, importância)
            explanation_html=explanation.as_html(),
            confidence=extracted_entity.confidence
        )
    
    def _predict_entity_probability(
        self,
        text_variations: List[str],
        target_entity: Entity
    ) -> List[float]:
        """
        Prediz probabilidade de extrair entidade para variações de texto.
        
        Usado pelo LIME.
        """
        probabilities = []
        for text in text_variations:
            extraction = self.model.extract(text)
            # Verificar se target_entity está presente
            entity_present = any(
                target_entity.label.lower() in e.label.lower()
                for e in extraction.entities
            )
            probabilities.append(1.0 if entity_present else 0.0)
        
        return probabilities

# Endpoint para explicabilidade
@router.get("/extractions/{extraction_id}/explain/{entity_id}")
async def explain_entity_extraction(
    extraction_id: UUID,
    entity_id: UUID
) -> ExtractionExplanationResponse:
    """
    Explica por que uma entidade específica foi extraída.
    
    Retorna palavras-chave que influenciaram a extração.
    """
    extraction = await extraction_repository.get_by_id(extraction_id)
    entity = next(e for e in extraction.entities if e.id == entity_id)
    
    explainability_service = ExplainabilityService(current_model)
    explanation = await explainability_service.explain_extraction(
        extraction.document_content,
        entity
    )
    
    return ExtractionExplanationResponse(
        entity_label=explanation.entity_label,
        important_words=explanation.important_words,
        explanation_html=explanation.explanation_html,
        confidence=explanation.confidence
    )
```

#### 10.5.6.5 Processo de Deploy com Governança

**Pipeline de Deploy com Validações:**

```python
# backend/app/workers/fine_tuning_worker.py (atualizado)
@app.task
async def periodic_fine_tuning_with_governance():
    """
    Fine-tuning periódico com validações de governança.
    """
    fine_tuning_service = FineTuningService()
    model_card_service = ModelCardService()
    behavior_test_suite = ModelBehaviorTestSuite()
    
    # 1. Exportar dataset
    dataset = await fine_tuning_service.export_training_dataset(min_validations=500)
    
    # 2. Treinar modelo
    model_path = await train_model(dataset)
    
    # 3. Avaliar métricas globais
    evaluation_metrics = await evaluate_model(model_path)
    
    # 4. Criar Model Card
    model_card = await model_card_service.create_model_card(
        model_id=f"extraction-model-{datetime.now().strftime('%Y%m%d')}",
        model_path=model_path,
        training_dataset_path=dataset.path,
        evaluation_results={
            "dataset_size": dataset.examples_count,
            "metrics": evaluation_metrics
        }
    )
    
    # 5. Executar testes comportamentais
    behavior_results = await behavior_test_suite.run_all_tests(model_path)
    
    # 6. Validações de deploy
    deploy_approved = await _validate_deploy(
        evaluation_metrics,
        behavior_results,
        model_card
    )
    
    if deploy_approved:
        # 7. Deploy do modelo
        await deploy_model(model_path, version="v2", model_card=model_card)
        logger.info(f"Deployed model with governance: {model_card.model_id}")
    else:
        logger.warning("Model deployment rejected by governance checks")
    
    return {
        "model_id": model_card.model_id,
        "metrics": evaluation_metrics,
        "behavior_tests": behavior_results,
        "deployed": deploy_approved
    }

async def _validate_deploy(
    evaluation_metrics: Dict,
    behavior_results: Dict,
    model_card: ModelCard
) -> bool:
    """
    Valida se modelo deve ser deployado.
    
    Checks:
    - Métricas melhoraram (>5% F1)
    - Testes comportamentais passaram
    - Sem vieses críticos detectados
    - Model Card completo
    """
    # Check 1: Melhoria de métricas
    current_f1 = await get_current_production_f1()
    new_f1 = evaluation_metrics["f1"]
    if new_f1 <= current_f1 * 1.05:
        logger.warning("F1 improvement < 5%. Deployment rejected.")
        return False
    
    # Check 2: Testes comportamentais
    if not behavior_results["all_passed"]:
        logger.warning("Behavioral tests failed. Deployment rejected.")
        return False
    
    # Check 3: Viés crítico
    if model_card.bias_analysis:
        critical_bias = any(
            score > 0.2  # Limiar de viés crítico
            for score in model_card.bias_analysis.values()
        )
        if critical_bias:
            logger.warning("Critical bias detected. Deployment rejected.")
            return False
    
    # Check 4: Model Card completo
    if not model_card.known_limitations:
        logger.warning("Model Card incomplete. Deployment rejected.")
        return False
    
    return True
```

### 10.5.6.6 Benefícios do Framework de MLOps

**Auditabilidade:**
- Rastreabilidade completa de qual modelo produziu qual dado
- Model Cards documentam decisões e limitações

**Segurança e Justiça:**
- Detecção de vieses através de análise e testes comportamentais
- Prevenção de regressões através de testes conhecidos

**Confiança:**
- Explicabilidade permite depuração e compreensão
- Transparência aumenta confiança dos stakeholders

**Riscos Mitigados:**
- ✅ **Caixa-Preta:** Transformado em sistema explicável e auditável
- ✅ **Vieses Sutis:** Detectados através de análise e testes comportamentais
- ✅ **Rastreabilidade:** Linhagem completa de extrações
- ✅ **Deploy Não-Governado:** Pipeline de validação antes do deploy

---

**Benefícios do Framework de Curadoria Ativa:**

- ✅ **Eficiência Humana:** Maximiza impacto do tempo limitado do especialista
- ✅ **Sistema que Aprende:** Cria ciclo virtuoso onde sistema fica mais inteligente
- ✅ **Engajamento:** Transforma tarefa tediosa em parte integrada e recompensada
- ✅ **Redução de Custos:** Fine-tuning reduz dependência de GPT-4 ao longo do tempo
- ✅ **Qualidade Crescente:** Sistema melhora continuamente com feedback humano

### 10.6 Monitoramento de Concept Drift Semântico

> **🟡 Crítica Nível 2 Aplicada:** Implementação de detecção proativa de concept drift para garantir que o Knowledge Graph continue sendo um reflexo fiel da realidade ao longo do tempo, mesmo quando a estrutura da ontologia não muda.

**O Problema Original:** O plano é excepcional em gerenciar o *versionamento* da ontologia, mas não possui um mecanismo para *detectar* quando a própria *realidade* que a ontologia descreve mudou. O significado de "IA Responsável" em 2025 pode ser diferente de 2028. Este fenômeno é conhecido como **concept drift**.

**Por Que Importa:**
- Com o tempo, o Knowledge Graph se torna uma representação defasada da realidade
- As extrações podem continuar sendo sintaticamente corretas, mas semanticamente erradas
- Leva a insights incorretos de forma silenciosa

**A Solução: Serviço de Detecção de Concept Drift Semântico**

### 10.6.1 Armazenamento de Embeddings de Contexto

**Modelo de Dados:**

```python
# backend/app/models/ontology.py (adicionar)
class ConceptContext(Base):
    """Contexto de onde um conceito foi extraído (para cálculo de drift)."""
    __tablename__ = "concept_contexts"
    
    id = Column(UUID, primary_key=True, default=uuid4)
    concept_id = Column(UUID, ForeignKey("knowledge_graph_concepts.id"))
    document_id = Column(UUID, ForeignKey("documents.id"))
    context_text = Column(Text)  # Parágrafo/sentença de origem
    context_embedding = Column(Vector(384))  # Embedding do contexto (all-MiniLM-L6-v2)
    extracted_at = Column(DateTime, server_default=func.now())
    
    # Índice para busca por embedding
    __table_args__ = (
        Index('idx_concept_context_embedding', 'context_embedding', postgresql_using='ivfflat'),
    )

class ConceptCentroid(Base):
    """Centróide semântico de um conceito (média dos embeddings de contexto)."""
    __tablename__ = "concept_centroids"
    
    concept_id = Column(UUID, ForeignKey("knowledge_graph_concepts.id"), primary_key=True)
    centroid_embedding = Column(Vector(384))  # Embedding médio histórico
    contexts_count = Column(Integer, default=0)  # Número de contextos usados
    last_updated = Column(DateTime, server_default=func.now())
    drift_threshold = Column(Float, default=0.15)  # Limiar para alerta de drift
```

### 10.6.2 Cálculo de Centróide Semântico

**Serviço de Cálculo de Centróide:**

```python
# backend/app/services/concept_drift_service.py
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Tuple
import logging

logger = logging.getLogger(__name__)

class ConceptDriftService:
    """Service para detecção de concept drift semântico."""
    
    def __init__(self, db: AsyncSession, kg_repository: KnowledgeGraphRepository):
        self.db = db
        self.kg_repository = kg_repository
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.drift_threshold = 0.15  # Limiar padrão (ajustável por conceito)
    
    async def store_concept_context(
        self,
        concept_id: UUID,
        document_id: UUID,
        context_text: str
    ):
        """
        Armazena contexto de onde um conceito foi extraído.
        
        Usado para cálculo futuro de drift semântico.
        """
        # Gerar embedding do contexto
        context_embedding = self.model.encode(context_text).tolist()
        
        # Salvar contexto
        context = ConceptContext(
            concept_id=concept_id,
            document_id=document_id,
            context_text=context_text,
            context_embedding=context_embedding
        )
        self.db.add(context)
        await self.db.commit()
        
        logger.debug(f"Stored context for concept {concept_id}")
    
    async def update_centroid(
        self,
        concept_id: UUID,
        include_recent: bool = True
    ) -> Tuple[np.ndarray, int]:
        """
        Atualiza o centróide semântico de um conceito.
        
        Calcula a média dos embeddings de todos os contextos históricos
        (ou apenas contextos recentes se include_recent=False).
        """
        # Buscar todos os contextos do conceito
        contexts = await self.db.execute(
            select(ConceptContext)
            .where(ConceptContext.concept_id == concept_id)
        )
        contexts = contexts.scalars().all()
        
        if not contexts:
            logger.warning(f"No contexts found for concept {concept_id}")
            return None, 0
        
        # Converter embeddings para numpy array
        embeddings = np.array([ctx.context_embedding for ctx in contexts])
        
        # Calcular centróide (média)
        centroid = np.mean(embeddings, axis=0)
        contexts_count = len(contexts)
        
        # Atualizar ou criar registro de centróide
        centroid_record = await self.db.get(ConceptCentroid, concept_id)
        if centroid_record:
            centroid_record.centroid_embedding = centroid.tolist()
            centroid_record.contexts_count = contexts_count
            centroid_record.last_updated = func.now()
        else:
            centroid_record = ConceptCentroid(
                concept_id=concept_id,
                centroid_embedding=centroid.tolist(),
                contexts_count=contexts_count
            )
            self.db.add(centroid_record)
        
        await self.db.commit()
        
        logger.info(
            f"Updated centroid for concept {concept_id} "
            f"(based on {contexts_count} contexts)"
        )
        
        return centroid, contexts_count
    
    def cosine_distance(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """
        Calcula distância de cosseno entre dois embeddings.
        
        Returns:
            Distância (0 = idênticos, 1 = ortogonais, 2 = opostos)
        """
        # Normalizar embeddings
        norm1 = np.linalg.norm(embedding1)
        norm2 = np.linalg.norm(embedding2)
        
        if norm1 == 0 or norm2 == 0:
            return 1.0  # Máxima distância
        
        # Produto escalar normalizado (cosseno de similaridade)
        cosine_sim = np.dot(embedding1, embedding2) / (norm1 * norm2)
        
        # Converter para distância (1 - similaridade)
        distance = 1 - cosine_sim
        
        return distance
```

### 10.6.3 Serviço de Monitoramento de Drift

**Worker Periódico para Detecção de Drift:**

```python
# backend/app/workers/concept_drift_worker.py
from datetime import datetime, timedelta
import numpy as np
from typing import List
import logging

logger = logging.getLogger(__name__)

class ConceptDriftWorker:
    """Worker para detectar concept drift semântico."""
    
    def __init__(
        self,
        concept_drift_service: ConceptDriftService,
        validation_repository
    ):
        self.concept_drift_service = concept_drift_service
        self.validation_repository = validation_repository
        self.drift_threshold = 0.15  # Limiar padrão
    
    async def check_concept_drift(
        self,
        lookback_period_days: int = 90
    ) -> List[DriftAlert]:
        """
        Verifica drift semântico para todos os conceitos.
        
        Args:
            lookback_period_days: Período para considerar contextos "recentes" (padrão: 90 dias)
        
        Returns:
            Lista de alertas de drift detectados
        """
        cutoff_date = datetime.utcnow() - timedelta(days=lookback_period_days)
        
        # Buscar todos os conceitos com centróides
        concepts_with_centroids = await self._get_concepts_with_centroids()
        
        drift_alerts = []
        
        for concept in concepts_with_centroids:
            # Buscar contextos recentes
            recent_contexts = await self._get_recent_contexts(
                concept.id,
                cutoff_date
            )
            
            if len(recent_contexts) < 10:  # Mínimo de contextos para análise
                logger.debug(
                    f"Concept {concept.label} has only {len(recent_contexts)} "
                    f"recent contexts. Skipping drift check."
                )
                continue
            
            # Calcular novo centróide dos contextos recentes
            recent_embeddings = np.array([ctx.context_embedding for ctx in recent_contexts])
            new_centroid = np.mean(recent_embeddings, axis=0)
            
            # Comparar com centróide histórico
            historic_centroid = np.array(concept.centroid_embedding)
            drift_distance = self.concept_drift_service.cosine_distance(
                historic_centroid,
                new_centroid
            )
            
            # Verificar se excede limiar
            threshold = concept.drift_threshold or self.drift_threshold
            if drift_distance > threshold:
                # Criar alerta de drift
                alert = await self._create_drift_alert(
                    concept_id=concept.id,
                    concept_label=concept.label,
                    drift_score=drift_distance,
                    threshold=threshold,
                    recent_contexts_count=len(recent_contexts),
                    message=(
                        f"O significado de '{concept.label}' pode ter mudado. "
                        f"Drift detectado: {drift_distance:.3f} (threshold: {threshold:.3f})"
                    )
                )
                drift_alerts.append(alert)
                
                logger.warning(
                    f"Concept drift detected for '{concept.label}': "
                    f"{drift_distance:.3f} > {threshold:.3f}"
                )
        
        return drift_alerts
    
    async def _create_drift_alert(
        self,
        concept_id: UUID,
        concept_label: str,
        drift_score: float,
        threshold: float,
        recent_contexts_count: int,
        message: str
    ) -> DriftAlert:
        """Cria alerta de drift no sistema de validação."""
        alert = DriftAlert(
            concept_id=concept_id,
            concept_label=concept_label,
            drift_score=drift_score,
            threshold=threshold,
            contexts_count=recent_contexts_count,
            message=message,
            detected_at=datetime.utcnow(),
            status="pending_review"  # Requer revisão humana
        )
        
        # Salvar alerta
        self.db.add(alert)
        await self.db.commit()
        
        # Notificar no dashboard de validação (alta prioridade)
        await self.validation_repository.create_validation_task(
            task_type="concept_drift_review",
            concept_id=concept_id,
            priority_score=0.9,  # Alta prioridade
            metadata={
                "drift_score": drift_score,
                "threshold": threshold,
                "contexts_count": recent_contexts_count
            }
        )
        
        return alert

# Worker periódico (Celery/RQ)
@app.task
async def periodic_concept_drift_check():
    """
    Tarefa periódica (mensal/trimestral) para verificar concept drift.
    
    Roda no primeiro dia de cada mês.
    """
    logger.info("Starting periodic concept drift check...")
    
    worker = ConceptDriftWorker(
        concept_drift_service=ConceptDriftService(...),
        validation_repository=ValidationRepository(...)
    )
    
    alerts = await worker.check_concept_drift(lookback_period_days=90)
    
    logger.info(f"Concept drift check completed. {len(alerts)} alerts created.")
    
    return {
        "alerts_count": len(alerts),
        "alerts": [alert.id for alert in alerts]
    }
```

### 10.6.4 Integração com Pipeline de Extração

**Armazenar Contexto Durante Extração:**

```python
# backend/app/services/ontology_service.py (atualizado)
class OntologyService:
    # ... código anterior ...
    
    async def process_document_ontology(
        self,
        document_id: UUID,
        document_content: str
    ) -> ProcessedOntology:
        # ... extração e processamento existente ...
        
        # NOVO: Armazenar contextos para cada conceito extraído
        concept_drift_service = ConceptDriftService(self.db, self.kg_repository)
        
        for concept in validated.concepts:
            # Extrair contexto (parágrafo onde conceito aparece)
            context_text = self._extract_concept_context(
                document_content,
                concept.label
            )
            
            # Armazenar contexto com embedding
            await concept_drift_service.store_concept_context(
                concept_id=concept.id,
                document_id=document_id,
                context_text=context_text
            )
        
        # ... resto do processamento ...
    
    def _extract_concept_context(
        self,
        document_content: str,
        concept_label: str,
        context_window: int = 200
    ) -> str:
        """
        Extrai contexto (parágrafo/sentença) onde um conceito aparece.
        
        Args:
            document_content: Conteúdo completo do documento
            concept_label: Label do conceito a localizar
            context_window: Número de caracteres ao redor do conceito
        
        Returns:
            Texto do contexto
        """
        # Localizar primeira ocorrência do conceito
        index = document_content.lower().find(concept_label.lower())
        
        if index == -1:
            # Conceito não encontrado no texto (pode ter sido inferido)
            return document_content[:context_window]  # Retornar início
        
        # Extrair contexto ao redor
        start = max(0, index - context_window // 2)
        end = min(len(document_content), index + len(concept_label) + context_window // 2)
        
        context = document_content[start:end]
        
        # Garantir que começa e termina em palavras completas
        context = context.strip()
        if not context.startswith(concept_label):
            # Tentar encontrar início de palavra/sentença
            first_space = context.find(' ')
            if first_space > 0:
                context = context[first_space+1:]
        
        return context
```

### 10.6.5 Dashboard de Alertas de Drift

**Interface para Visualização de Drift:**

```python
# backend/app/api/v1/endpoints/concept_drift.py
@router.get("/concept-drift/alerts")
async def get_drift_alerts(
    status: str = "pending_review",
    min_score: float = 0.15
) -> List[DriftAlertResponse]:
    """
    Retorna alertas de concept drift pendentes de revisão.
    """
    alerts = await drift_repository.get_alerts(
        status=status,
        min_score=min_score
    )
    
    return [
        DriftAlertResponse(
            id=alert.id,
            concept_id=alert.concept_id,
            concept_label=alert.concept_label,
            drift_score=alert.drift_score,
            threshold=alert.threshold,
            contexts_count=alert.contexts_count,
            message=alert.message,
            detected_at=alert.detected_at,
            status=alert.status
        )
        for alert in alerts
    ]

@router.post("/concept-drift/alerts/{alert_id}/resolve")
async def resolve_drift_alert(
    alert_id: UUID,
    action: DriftResolutionAction,
    notes: str = None
):
    """
    Resolve um alerta de drift.
    
    Actions:
    - "update_ontology": Conceito mudou - atualizar ontologia
    - "update_centroid": Significado mudou - atualizar centróide
    - "false_positive": Falso positivo - manter como está
    """
    alert = await drift_repository.get_alert(alert_id)
    
    if action == "update_centroid":
        # Atualizar centróide histórico com novos contextos
        await concept_drift_service.update_centroid(alert.concept_id)
        alert.status = "resolved"
        alert.resolution_action = "centroid_updated"
    
    elif action == "update_ontology":
        # Criar task para atualizar ontologia (requer revisão)
        await ontology_repository.create_update_task(
            concept_id=alert.concept_id,
            reason="concept_drift",
            notes=notes
        )
        alert.status = "resolved"
        alert.resolution_action = "ontology_update_requested"
    
    elif action == "false_positive":
        alert.status = "resolved"
        alert.resolution_action = "false_positive"
    
    alert.resolved_at = datetime.utcnow()
    alert.resolution_notes = notes
    
    await drift_repository.save(alert)
    
    return {"status": "resolved", "alert_id": str(alert_id)}
```

### 10.6.6 Benefícios do Monitoramento de Concept Drift

**Manutenção Proativa:**
- Sistema avisa quando ontologia está ficando obsoleta
- Detecta mudanças semânticas antes que causem problemas

**Governança Orientada a Dados:**
- Revisões da ontologia acionadas por evidências quantitativas
- Não depende apenas de intuição humana

**Sustentabilidade de Longo Prazo:**
- Garante que KG continue sendo reflexo fiel da realidade
- Mantém qualidade semântica ao longo do tempo

**Riscos Mitigados:**
- ✅ **Degradação Silenciosa:** Detectada proativamente através de drift scoring
- ✅ **Insights Incorretos:** Prevenidos através de alertas e revisão
- ✅ **Ontologia Obsoleta:** Atualizada baseada em evidências de mudança semântica

---

## 🎯 Conclusão

Este plano de gestão de ontologias fornece uma **estrutura completa e prática** para:

1. ✅ **Organizar** ontologias de forma modular
2. ✅ **Versionar** com controle explícito
3. ✅ **Automatizar** extração e compilação
4. ✅ **Integrar** com sistema existente
5. ✅ **Evoluir** baseado em casos de uso
6. ✅ **Documentar** decisões e mudanças

A estratégia é **incremental**, permitindo começar simples e evoluir gradualmente, sempre validando contra casos de uso reais.

---

**Próximos Passos:**
1. Implementar estrutura de diretórios
2. Criar schemas LinkML base
3. Integrar OntoGPT **com fallback (spaCy)**
4. Implementar deduplicação de entidades
5. Criar testes de competência
6. Testar com documentos reais
7. Iterar baseado em feedback

---

## 🔄 Melhorias Implementadas

### v1.1.0 - Melhorias de Engenharia

Este documento foi atualizado com **6 melhorias críticas** baseadas em análise de engenharia:

1. ✅ **Estratégia de Fallback para Extrator** (Seção 6.1)
   - spaCy como fallback quando OntoGPT falha
   - Alta disponibilidade e degradação graciosa

2. ✅ **Resolução e Deduplicação de Entidades** (Seção 6.4)
   - Embeddings de similaridade para evitar duplicatas
   - Knowledge Graph limpo e conectado

3. ✅ **Testes de Competência Automatizados** (Seção 5.2)
   - Testes conectados às perguntas de competência
   - Validação contínua e regressão automatizada

4. ✅ **Dashboard de Validação Humana** (Seção 10.5)
   - Interface para validação humana de extrações
   - Feedback loop para melhoria contínua

5. ✅ **Testes de Performance** (Seção 10.4)
   - Pipeline de testes de performance
   - Detecção de regressões antes da produção

6. ✅ **Análise de Custo e Monitoramento** (Seção 10.3)
   - Logging de custos de API
   - Dashboard de monitoramento
   - Alertas de orçamento

### v1.2.0 - Melhorias Críticas de Red Team

Este documento foi atualizado com **3 melhorias críticas** baseadas em análise de Red Team (riscos estratégicos e operacionais):

7. ✅ **Sincronização Resiliente com Padrão Outbox** (Seção 4.2) ⭐⭐
   - Padrão Outbox/Saga para consistência eventual
   - Resiliência a falhas do Neo4j
   - Worker assíncrono para sincronização idempotente
   - **Resolve:** Calcanhar de Aquiles da Sincronização

8. ✅ **Experiência do Usuário e Ciclo de Feedback** (Nova Seção 7) ⭐⭐
   - Mockups de UI e funcionalidades visíveis
   - Fluxo completo de feedback do usuário
   - Métricas de valor de negócio (não apenas técnicas)
   - Killer features habilitadas pela arquitetura
   - **Resolve:** Paradoxo da Complexidade vs. Valor

9. ✅ **Framework de Curadoria Ativa** (Seção 10.5 expandida) ⭐⭐
   - Aprendizado Ativo para priorização inteligente
   - Gamificação e sistema de incentivos
   - Integração ao fluxo de trabalho
   - Fine-tuning periódico baseado em feedback
   - **Resolve:** Ilusão do "Humano no Loop"

**Impacto das Melhorias v1.2.0:**

- 🔴 **Risco Estratégico Mitigado:** Valor de negócio explícito e mensurável
- 🔴 **Risco Arquitetural Mitigado:** Sincronização resiliente e consistente
- 🔴 **Risco Operacional Mitigado:** Framework operacional para curadoria humana

### v1.3.0 - Melhorias Críticas de Red Team Nível 2

Este documento foi atualizado com **3 melhorias críticas de segunda ordem** baseadas em análise de Red Team Nível 2 (riscos de longo prazo, escala organizacional e sustentabilidade):

10. ✅ **Governança Federada em Escala** (Nova Seção 11) ⭐⭐⭐
    - Arquitetura de ontologia federada (semantic data mesh)
    - Múltiplos repositórios de ontologia por domínio
    - Serviço de registro de ontologias (OntologyRegistry)
    - Herança explícita e resolução de conflitos de namespace
    - **Resolve:** Falácia do "Cérebro Único" - gargalo de governança centralizada

11. ✅ **Monitoramento de Concept Drift Semântico** (Nova Seção 10.6) ⭐⭐⭐
    - Detecção proativa de mudanças semânticas ao longo do tempo
    - Armazenamento de embeddings de contexto
    - Cálculo de centróides semânticos
    - Worker periódico para detecção de drift
    - Dashboard de alertas e resolução
    - **Resolve:** Pressuposição do "Mundo Estático" - degradação silenciosa do KG

12. ✅ **MLOps e Governança de Modelos** (Seção 10.5.6 expandida) ⭐⭐⭐
    - Model Cards para documentação e governança
    - Linhagem de extração (rastreabilidade completa)
    - Suíte de testes comportamentais (robustez, invariância, negação)
    - Explainability no dashboard (SHAP/LIME)
    - Pipeline de deploy com validações de governança
    - **Resolve:** Caixa-Preta do Fine-Tuning - auditabilidade e explicabilidade

**Impacto das Melhorias v1.3.0:**

- 🔴 **Risco de Escala Organizacional Mitigado:** Governança federada permite crescimento sem gargalos
- 🔴 **Risco de Degradação Silenciosa Mitigado:** Concept drift detectado proativamente
- 🔴 **Risco de Caixa-Preta Mitigado:** Modelos explicáveis, auditáveis e governados
- ✅ **Sustentabilidade de Longo Prazo:** Sistema projetado para evolução contínua e manutenção proativa
- ✅ **Capacidade Organizacional:** Transforma sistema técnico em capacidade estratégica de gestão de conhecimento

---

**Documento criado em:** 30 de Dezembro de 2025  
**Versão:** 1.3.0 (atualizada com melhorias críticas de Red Team Nível 2)  
**Próxima revisão:** Após implementação da Fase 1

---

## 📝 Notas Finais sobre as Críticas Aplicadas

Este plano evoluiu de um **documento de implementação técnica** para um **plano de sistema sociotécnico de IA de classe mundial**, abordando proativamente:

1. ✅ **Valor de Negócio Explícito:** Conexão clara entre arquitetura e experiência do usuário
2. ✅ **Resiliência Arquitetural:** Padrão Outbox garante consistência em ambiente distribuído
3. ✅ **Operacionalização do Feedback:** Framework de Curadoria Ativa resolve o problema humano
4. ✅ **Escalabilidade Organizacional:** Governança federada permite crescimento sem gargalos
5. ✅ **Sustentabilidade de Longo Prazo:** Detecção proativa de concept drift mantém qualidade semântica
6. ✅ **Governança de IA:** MLOps e explicabilidade transformam caixa-preta em sistema auditável

Os maiores desafios em IA não são puramente técnicos, mas residem na **intersecção da tecnologia com processos humanos, valor de negócio e sustentabilidade organizacional**. Este plano agora os aborda de forma integrada, projetando não apenas para o lançamento, mas para o sucesso, escala e sustentabilidade em um horizonte de 3 a 5 anos.

**Evolução do Documento:**
- **v1.0.0:** Plano técnico inicial de gestão de ontologias
- **v1.1.0:** Melhorias de engenharia (fallback, deduplicação, testes, performance)
- **v1.2.0:** Melhorias críticas de Red Team (sincronização, UX, curadoria)
- **v1.3.0:** Melhorias críticas de Red Team Nível 2 (governança federada, concept drift, MLOps)

O plano agora representa uma **capacidade organizacional de gestão de conhecimento**, não apenas um sistema de software.

