# 🔧 DIMENSÃO 2: ANÁLISE TECNOLÓGICA

**Data da Análise:** 22 de Dezembro de 2025  
**Arquivo:** `DIMENSAO_2_ANALISE_TECNOLOGICA.md`

---

## 2.1 Stack do Banco de Referências

### Backend
- **Framework:** FastAPI 0.115+ (Python 3.12+)
  - **Performance:** 18.000 req/s (7x mais rápido que Flask)
  - **Async nativo:** asyncio/await out-of-the-box
  - **Type safety:** Validação automática com Pydantic
  - **Documentação:** OpenAPI automático (Swagger)

### Database
- **PostgreSQL 16** (Docker)
  - **ORM:** SQLAlchemy async
  - **Driver:** asyncpg 0.30.0
  - **Migrations:** Alembic 1.13.0
  - **Status:** Funcional em Docker Compose

### Vector DB / RAG
- **Google File Search** ⭐ **OBRIGATÓRIO**
  - **RAG nativo:** Embeddings gerenciados
  - **Busca semântica:** Linguagem natural
  - **Integração:** google-genai >= 1.0.0
  - **Status:** Integrado e funcionando

### Frontend
- **React 18.2.0 + Vite 5.0** (MVP atual)
  - **Estado:** Funcional e operacional
  - **Planejado:** Migração para Next.js 15 (Fase 3)
  - **Dependências:** axios 1.6.0, React DOM 18.2.0

### Infraestrutura
- **Docker + Docker Compose** ⭐ **OBRIGATÓRIO**
  - **3 serviços:** postgres, backend, frontend
  - **Networking:** Rede isolada (banco_ref_network)
  - **Volumes:** postgres_data persistente
  - **Status:** 100% funcional

---

## 2.2 Arquitetura do Sistema

### Padrões Arquiteturais
1. **Repository Pattern:** Separação de acesso a dados
   - `DocumentRepository` - PostgreSQL
   - `VectorRepository` - Google File Search

2. **Service Layer:** Lógica de negócio isolada
   - `DocumentService` - Operações de documentos
   - `SearchService` - Busca semântica RAG

3. **DTO Pattern:** Pydantic schemas
   - `DocumentBase`, `DocumentCreate`, `DocumentResponse`
   - `SearchRequest`, `SearchResponse`

4. **Dependency Injection:** FastAPI `Depends`
   - `get_db_session` - Sessão do banco
   - Injeção automática nos endpoints

### Estrutura de Diretórios
```
backend/app/
├── main.py              # FastAPI app
├── core/                # Config, database, exceptions
├── api/v1/              # Endpoints REST
│   ├── endpoints/       # documents.py, search.py
│   └── router.py        # Agrega routers
├── services/            # Business logic
├── repositories/        # Data access
├── models/              # SQLAlchemy models
└── schemas/             # Pydantic schemas
```

**Arquivos Relevantes:**
- `BANCO_REFERENCIAS/ARQUITETURA_COMPLETA.md`
- `BANCO_REFERENCIAS/STACK_DECIDIDO.md`
- `BANCO_REFERENCIAS/backend/app/`

---

## 2.3 Integrações

### Google Gemini API
- **File Search Store:** Criado automaticamente se não existir
- **Upload:** Documentos indexados automaticamente
- **Search:** Busca semântica com RAG
- **Model:** gemini-2.5-flash (configurável)

### PostgreSQL
- **Connection:** Async connection pool
- **Migrations:** Alembic preparado
- **Models:** Document, Reference, Project, Analysis

**Arquivos Relevantes:**
- `BANCO_REFERENCIAS/backend/app/repositories/vector_repository.py`
- `BANCO_REFERENCIAS/backend/app/core/database.py`

---

## 2.4 Tecnologias Futuras (Roadmap)

### Fase 2 (Planejado)
- **Cache:** Redis/Dragonfly
- **Workers:** Threading Python → Temporal (futuro)

### Fase 3 (Planejado)
- **Frontend:** Next.js 15 + TypeScript 5.5+
- **Styling:** Tailwind CSS 4.0+
- **Components:** shadcn/ui

### Fase 4 (Planejado)
- **Deploy:** Google Cloud Run
- **Auth:** Clerk (10k MAU grátis)
- **Observability:** Prometheus + Grafana + Tempo

**Arquivos Relevantes:**
- `BANCO_REFERENCIAS/PLANO_IMPLEMENTACAO.md`

---

## 🔗 REFERÊNCIAS CRUZADAS

- **Dimensão 3:** Análise de Código - Implementação detalhada
- **Dimensão 10:** Análise de Dependências - Versões e compatibilidade
- **Dimensão 6:** Análise de Planejamento - Roadmap tecnológico

---

**Próxima Dimensão:** [DIMENSÃO 3: ANÁLISE DE CÓDIGO](DIMENSAO_3_ANALISE_CODIGO.md)  
**Índice:** [INDICE_ANALISE.md](INDICE_ANALISE.md)
