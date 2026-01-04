# 🗂️ Banco de Referências - Sistema RAG

**Versão:** 1.0.0 (MVP)  
**Data:** 2025-12-16  
**Status:** ✅ MVP BASE COMPLETO E FUNCIONAL

---

## 🎯 O Que É?

Sistema de gestão de conhecimento com RAG (Retrieval-Augmented Generation) usando Google Gemini File Search API. Permite indexar, buscar e analisar documentos de forma semântica.

---

## 🛠️ Stack Tecnológico

### Backend
- **FastAPI** 0.115+ (Python 3.12+)
- **PostgreSQL** 16 (Docker)
- **SQLAlchemy** async (ORM)
- **Google Gemini File Search** (RAG nativo) ⭐ **OBRIGATÓRIO**

### Infraestrutura
- **Docker** + **Docker Compose** ⭐ **OBRIGATÓRIO**

### Frontend (Fase 3)
- **Next.js** 15
- **TypeScript** 5.5+
- **Tailwind CSS** 4.0+

---

## 🚀 Início Rápido

### Pré-requisitos

- Docker e Docker Compose instalados
- Google Gemini API Key

### 1. Configurar Variáveis de Ambiente

```bash
cp .env.example .env
# Editar .env e adicionar GEMINI_API_KEY
```

### 2. Iniciar com Docker

```bash
docker-compose up --build
```

### 3. Acessar Aplicação

- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/api/docs
- **Health Check**: http://localhost:8000/health

---

## 📁 Estrutura do Projeto

```
BANCO_REFERENCIAS/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app
│   │   ├── api/v1/              # Endpoints
│   │   ├── services/            # Business logic
│   │   ├── repositories/        # Data access
│   │   ├── models/              # SQLAlchemy models
│   │   ├── schemas/             # Pydantic schemas
│   │   └── core/                # Config, database
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 🔗 Endpoints Disponíveis

### Documentos
- `POST /api/v1/documents` - Upload de documento
- `GET /api/v1/documents` - Listar documentos
- `GET /api/v1/documents/{id}` - Obter documento
- `DELETE /api/v1/documents/{id}` - Deletar documento

### Busca
- `POST /api/v1/search` - Busca semântica RAG

---

## 📚 Documentação

- [`00_START_HERE.md`](00_START_HERE.md) - Como começar
- [`SETUP.md`](SETUP.md) - Guia de setup detalhado
- [`ARQUITETURA_COMPLETA.md`](ARQUITETURA_COMPLETA.md) - Arquitetura do sistema
- [`PLANO_IMPLEMENTACAO.md`](PLANO_IMPLEMENTACAO.md) - Roadmap completo
- [`STATUS_PROJETO.md`](STATUS_PROJETO.md) - Status atual

---

## 🔧 Desenvolvimento

### Setup Local

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Configurar .env com DATABASE_URL local se necessário
python -m app.main
```

### Testes

```bash
# Quando implementados
pytest
```

---

## 📊 Status

**Fase 1 (MVP):** ✅ 100% COMPLETO E FUNCIONAL

- [x] ✅ Estrutura completa (26 arquivos Python)
- [x] ✅ Models (Document, Reference, Project, Analysis)
- [x] ✅ Repositories (VectorRepository, DocumentRepository)
- [x] ✅ Services (DocumentService, SearchService)
- [x] ✅ Endpoints REST (documents CRUD + busca semântica)
- [x] ✅ PostgreSQL no Docker configurado
- [x] ✅ FastAPI funcionando
- [x] ✅ Google File Search integrado
- [x] ✅ .cursorrules criado
- [ ] Testes (próxima fase)
- [ ] Deploy (próxima fase)

---

**Última atualização:** 2025-12-16
