# 🏗️ Arquitetura Completa - Banco de Referências

**Data:** 2025-12-16  
**Baseado em:** Especificação Técnica v2.0 (análise completa)  
**Status:** Definitivo

---

## ✅ Arquitetura Definitiva (Seguindo Especificação v2.0)

Esta é a arquitetura completa definida na análise técnica. **Seguiremos tudo exatamente como especificado.**

---

## 📊 Stack Completo (Conforme Especificação)

### Backend Layer
- **FastAPI** 0.115+ ⭐
  - Performance: 18.000 req/s
  - Async nativo
  - Type safety (Pydantic)
  - OpenAPI automático

### Database Layer
- **PostgreSQL (Neon Serverless)** ⭐
  - Free tier: 0.5 GB
  - Auto-scaling
  - Branches como Git
  - Multi-user nativo

### Vector DB (RAG)
- **Google File Search** ⭐ **OBRIGATÓRIO**
  - RAG nativo
  - Embeddings gerenciados
  - Busca semântica

### Cache Layer (Fase 2)
- **Dragonfly** ou **Redis** simples (MVP)
  - Cache de resultados
  - Sessions
  - Hot data

### Frontend Layer (Fase 3)
- **Next.js 15** ⭐
  - React Server Components (RSC)
  - Server Actions
  - Streaming UI
  - SEO otimizado
- **TypeScript** 5.5+
- **Tailwind CSS** 4.0+
- **shadcn/ui** (componentes)

### Workers (Fase 2)
- **Threading Python** (MVP)
  - Processamento assíncrono
  - Análises em background
- **Temporal** (Fase 4, se necessário)
  - Workflows duráveis
  - Retries automáticos

### Infraestrutura
- **Docker** ⭐ **OBRIGATÓRIO**
- **Docker Compose** (desenvolvimento)
- **Google Cloud Run** (produção - Fase 4)

### Observability (Fase 4)
- **Prometheus** (métricas)
- **Grafana** (dashboards)
- **Tempo** (traces - OpenTelemetry)

### Auth (Fase 2)
- **Clerk** (opcional)
  - 10k MAU grátis
  - OAuth integrado
  - RBAC

---

## 🏛️ Arquitetura de Alto Nível

```
┌─────────────────────────────────────────────────────┐
│                  FRONTEND LAYER                      │
│  Next.js 15 (React Server Components)               │
│  - Server Actions                                    │
│  - Streaming UI (Suspense)                          │
│  - Real-time updates (SSE)                          │
│  - TypeScript + Zod                                 │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ REST API
                   │
┌──────────────────▼──────────────────────────────────┐
│              APPLICATION LAYER                       │
│  FastAPI Backend (Python 3.12+)                     │
│  ┌──────────────────────────────────────────────┐   │
│  │  Controllers (Routers)                       │   │
│  │  - /documents                                │   │
│  │  - /search                                   │   │
│  │  - /references                               │   │
│  │  - /projects                                 │   │
│  │  - /analysis                                 │   │
│  └──────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────┐   │
│  │  Services (Business Logic)                   │   │
│  │  - DocumentService                           │   │
│  │  - SearchService (RAG)                       │   │
│  │  - ReferenceService                          │   │
│  │  - AnalysisService                           │   │
│  └──────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────┐   │
│  │  Repositories (Data Access)                  │   │
│  │  - DocumentRepository (PostgreSQL)           │   │
│  │  - VectorRepository (Google File Search)     │   │
│  │  - CacheRepository (Dragonfly/Redis)         │   │
│  └──────────────────────────────────────────────┘   │
└───────────┬────────────────────────┬────────────────┘
            │                        │
    ┌───────▼────────┐    ┌──────────▼──────────┐
    │  PostgreSQL    │    │  Google File Search │
    │  (Neon)        │    │  (RAG Vector DB)    │
    │                │    │                     │
    │  - Metadata    │    │  - Documents        │
    │  - References  │    │  - Embeddings       │
    │  - Projects    │    │  - Semantic Search  │
    │  - Analyses    │    │                     │
    └────────────────┘    └─────────────────────┘
            │
    ┌───────▼────────┐
    │  Dragonfly/    │
    │  Redis         │
    │  (Cache)       │
    └────────────────┘
```

---

## 📁 Estrutura de Diretórios (Conforme Especificação)

```
BANCO_REFERENCIAS/
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI app
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── documents.py    # Document endpoints
│   │   │       ├── search.py       # Search endpoints
│   │   │       ├── references.py   # Reference endpoints
│   │   │       ├── projects.py     # Project endpoints
│   │   │       └── analysis.py     # Analysis endpoints
│   │   ├── services/
│   │   │   ├── document_service.py
│   │   │   ├── search_service.py
│   │   │   ├── reference_service.py
│   │   │   └── analysis_service.py
│   │   ├── repositories/
│   │   │   ├── document_repository.py
│   │   │   ├── cache_repository.py
│   │   │   └── vector_repository.py
│   │   ├── models/
│   │   │   ├── document.py         # SQLAlchemy models
│   │   │   ├── reference.py
│   │   │   ├── project.py
│   │   │   └── analysis.py
│   │   ├── core/
│   │   │   ├── config.py           # Settings (Pydantic)
│   │   │   ├── database.py         # DB connection
│   │   │   └── security.py         # Auth (se necessário)
│   │   └── schemas/
│   │       ├── document.py         # Pydantic schemas (DTOs)
│   │       ├── reference.py
│   │       └── project.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── alembic/                    # Migrations
│
├── frontend/                       # Fase 3
│   ├── app/                        # Next.js App Router
│   │   ├── (dashboard)/
│   │   │   ├── documents/
│   │   │   ├── search/
│   │   │   ├── references/
│   │   │   ├── projects/
│   │   │   └── analytics/
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/
│   │   ├── ui/                     # shadcn/ui
│   │   ├── features/
│   │   └── shared/
│   ├── lib/
│   │   ├── actions/                # Server Actions
│   │   ├── api/                    # API client
│   │   └── utils/
│   ├── package.json
│   └── Dockerfile
│
├── documentacao/
│   ├── ARQUITETURA_COMPLETA.md     # Este arquivo
│   ├── DECISOES.md                 # ADRs
│   └── ESPECIFICACAO_TECNICA.md    # Detalhamento completo
│
└── docker-compose.yml
```

---

## 🔧 Padrões de Design (Conforme Especificação)

### Repository Pattern
- Abstração do acesso a dados
- Isolamento da lógica de negócio
- Fácil de testar e mockar

### Service Layer
- Lógica de negócio isolada
- Orquestração de operações
- Validações e regras

### Dependency Injection
- FastAPI `Depends` nativo
- Testabilidade
- Baixo acoplamento

### DTO Pattern
- Pydantic schemas para validação
- Separação request/response
- Type safety

---

## 📊 Modelo de Dados (PostgreSQL)

```sql
-- Usuários (se usar auth)
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Referências Externas (2.400+ fontes)
CREATE TABLE references (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(500) NOT NULL,
    category VARCHAR(100),
    subject TEXT,
    sources TEXT,  -- JSON array
    concepts TEXT, -- JSON array
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Projetos Documentados
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    documentation_path TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Documentos Indexados no Google File Search
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    google_file_id VARCHAR(255) UNIQUE NOT NULL,
    filename VARCHAR(500) NOT NULL,
    file_type VARCHAR(50),
    file_size_bytes BIGINT,
    upload_date TIMESTAMP DEFAULT NOW(),
    metadata JSONB,
    reference_id UUID REFERENCES references(id),
    project_id UUID REFERENCES projects(id),
    status VARCHAR(50) DEFAULT 'active'
);

-- Análises com Playbooks (genérico)
CREATE TABLE analyses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID REFERENCES documents(id),
    playbook_id VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending',
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    results JSONB,
    error_message TEXT,
    metrics JSONB
);

-- Índices para performance
CREATE INDEX idx_documents_google_file_id ON documents(google_file_id);
CREATE INDEX idx_documents_reference_id ON documents(reference_id);
CREATE INDEX idx_documents_project_id ON documents(project_id);
CREATE INDEX idx_analyses_document_id ON analyses(document_id);
CREATE INDEX idx_analyses_status ON analyses(status);
```

---

## 🔄 Fluxos Principais

### 1. Upload de Documento

```
Cliente → FastAPI → DocumentService → VectorRepository (Google File Search)
                                      ↓
                                    DocumentRepository (PostgreSQL)
```

### 2. Busca Semântica (RAG)

```
Cliente → FastAPI → SearchService → VectorRepository (Google File Search)
                                              ↓
                                         Gemini API (RAG)
                                              ↓
                                         CacheRepository (Dragonfly)
```

### 3. Análise com Playbook

```
Cliente → FastAPI → AnalysisService → PlaybookLoader
                                      ↓
                                    Gemini API
                                      ↓
                                    AnalysisRepository (PostgreSQL)
```

---

## 📈 Fases de Implementação

### Fase 1: Fundação (MVP)
- ✅ FastAPI backend
- ✅ PostgreSQL (Neon)
- ✅ Google File Search integration
- ✅ Upload e busca básica

### Fase 2: Core Features
- ⏭️ Cache (Dragonfly/Redis)
- ⏭️ Processamento assíncrono (threading)
- ⏭️ Auth (Clerk - opcional)
- ⏭️ Sistema de playbooks

### Fase 3: Frontend
- ⏭️ Next.js 15
- ⏭️ Interface completa
- ⏭️ Real-time updates

### Fase 4: Produção
- ⏭️ Observabilidade (Prometheus + Grafana)
- ⏭️ Analytics
- ⏭️ Temporal (workflows)
- ⏭️ Deploy produção

---

## ✅ Checklist de Conformidade

### Arquitetura
- [x] FastAPI como backend
- [x] PostgreSQL (Neon) como database
- [x] Google File Search como vector DB
- [x] Next.js 15 como frontend (Fase 3)
- [x] Repository Pattern
- [x] Service Layer
- [x] DTO Pattern (Pydantic)

### Infraestrutura
- [x] Docker obrigatório
- [x] Docker Compose (dev)
- [ ] Google Cloud Run (prod - Fase 4)

### Observabilidade (Fase 4)
- [ ] Prometheus
- [ ] Grafana
- [ ] Tempo (traces)

---

**Status:** 🟢 Arquitetura definitiva conforme especificação v2.0  
**Última atualização:** 2025-12-16


