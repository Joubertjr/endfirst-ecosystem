# 📚 Guia de Desenvolvimento - Banco de Referências

**Versão:** 1.0.0  
**Última atualização:** 22 de Dezembro de 2025

---

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Setup do Ambiente](#setup-do-ambiente)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Arquitetura](#arquitetura)
5. [Desenvolvimento](#desenvolvimento)
6. [Testes](#testes)
7. [Convenções de Código](#convenções-de-código)
8. [Troubleshooting](#troubleshooting)

---

## 🔧 Pré-requisitos

### Ferramentas Necessárias

- **Python 3.12+**
- **Node.js 18+** (para frontend)
- **Docker & Docker Compose**
- **Git**
- **Editor de código** (recomendado: VS Code ou Cursor)

### Contas Necessárias

- **Google Cloud Platform** - Para Gemini API Key
- **Clerk** (opcional) - Para autenticação
- **GitHub** - Para versionamento

---

## 🚀 Setup do Ambiente

### 1. Clone o Repositório

```bash
git clone <repository-url>
cd BANCO_REFERENCIAS
```

### 2. Configure Variáveis de Ambiente

```bash
cp .env.example .env
# Edite .env com suas configurações
```

**Variáveis obrigatórias:**
- `GEMINI_API_KEY` - Chave da API do Google Gemini
- `DATABASE_URL` - URL do PostgreSQL (ou use Docker)
- `CLERK_SECRET_KEY` - Secret key do Clerk (opcional)

### 3. Inicie os Serviços

```bash
docker-compose up --build
```

Isso iniciará:
- PostgreSQL (porta 5432)
- Redis (porta 6379)
- Backend FastAPI (porta 8000)
- Frontend React (porta 5173)

---

## 📁 Estrutura do Projeto

```
BANCO_REFERENCIAS/
├── backend/
│   ├── app/
│   │   ├── api/              # Endpoints da API
│   │   │   └── v1/
│   │   │       ├── endpoints/ # Endpoints específicos
│   │   │       └── router.py  # Router principal
│   │   ├── core/              # Configurações e utilitários
│   │   │   ├── config.py      # Configurações
│   │   │   ├── database.py    # Conexão com DB
│   │   │   ├── auth.py        # Autenticação
│   │   │   ├── cache.py       # Cache Redis
│   │   │   └── validators.py  # Validadores
│   │   ├── models/            # Models SQLAlchemy
│   │   ├── repositories/      # Data Access Layer
│   │   ├── schemas/           # DTOs (Pydantic)
│   │   ├── services/          # Business Logic Layer
│   │   └── main.py            # Aplicação FastAPI
│   ├── tests/                 # Testes
│   │   ├── unit/              # Testes unitários
│   │   └── integration/       # Testes de integração
│   └── requirements.txt       # Dependências Python
├── frontend/                  # Frontend React
├── docs/                      # Documentação
└── docker-compose.yml         # Configuração Docker
```

---

## 🏗️ Arquitetura

### Padrão Arquitetural

O projeto segue o **Repository Pattern** com **Service Layer**:

```
┌─────────────┐
│   Endpoint  │ ← FastAPI Router
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Service   │ ← Business Logic
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Repository  │ ← Data Access
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Model    │ ← SQLAlchemy
└─────────────┘
```

### Camadas

1. **API Layer** (`app/api/v1/endpoints/`)
   - Endpoints FastAPI
   - Validação de entrada
   - Respostas HTTP

2. **Service Layer** (`app/services/`)
   - Lógica de negócio
   - Orquestração
   - Validações de negócio

3. **Repository Layer** (`app/repositories/`)
   - Acesso a dados
   - Queries SQL
   - Abstração do banco

4. **Model Layer** (`app/models/`)
   - Models SQLAlchemy
   - Definição de tabelas

---

## 💻 Desenvolvimento

### Adicionando um Novo Endpoint

1. **Crie o Schema** (`app/schemas/`)
```python
# app/schemas/example.py
class ExampleCreate(BaseModel):
    name: str
    
class ExampleResponse(BaseModel):
    id: UUID
    name: str
```

2. **Crie o Repository** (se necessário)
```python
# app/repositories/example_repository.py
class ExampleRepository:
    async def create(self, name: str) -> Example:
        ...
```

3. **Crie o Service**
```python
# app/services/example_service.py
class ExampleService:
    async def create_example(self, data: ExampleCreate) -> ExampleResponse:
        ...
```

4. **Crie o Endpoint**
```python
# app/api/v1/endpoints/example.py
@router.post("", response_model=ExampleResponse)
async def create_example(data: ExampleCreate, db: AsyncSession = Depends(get_db_session)):
    service = ExampleService(db)
    return await service.create_example(data)
```

5. **Registre no Router**
```python
# app/api/v1/router.py
from app.api.v1.endpoints import example
api_router.include_router(example.router, prefix="/example", tags=["example"])
```

### Adicionando um Novo Model

1. **Crie o Model**
```python
# app/models/example.py
class Example(Base):
    __tablename__ = "examples"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(255))
```

2. **Importe no `__init__.py`**
```python
# app/models/__init__.py
from app.models.example import Example
```

---

## 🧪 Testes

### Rodar Testes

```bash
# Todos os testes
pytest

# Testes unitários
pytest tests/unit/

# Testes de integração
pytest tests/integration/

# Com cobertura
pytest --cov=app --cov-report=html
```

### Estrutura de Testes

**Testes Unitários:**
- Mock de dependências
- Teste de lógica isolada
- AAA Pattern (Arrange, Act, Assert)

**Testes de Integração:**
- Database real (SQLite in-memory)
- HTTP client real (httpx.AsyncClient)
- Fluxo completo end-to-end

### Exemplo de Teste

```python
@pytest.mark.asyncio
async def test_create_example(db_session: AsyncMock):
    # Arrange
    service = ExampleService(db_session)
    data = ExampleCreate(name="Test")
    
    # Act
    result = await service.create_example(data)
    
    # Assert
    assert result.name == "Test"
```

---

## 📝 Convenções de Código

### Nomenclatura

- **Classes:** `PascalCase` (ex: `DocumentService`)
- **Funções/Métodos:** `snake_case` (ex: `create_document`)
- **Constantes:** `UPPER_SNAKE_CASE` (ex: `MAX_FILE_SIZE`)
- **Variáveis:** `snake_case` (ex: `user_id`)

### Type Hints

Sempre use type hints:

```python
async def create_document(
    file_content: bytes,
    filename: str,
    user_id: str
) -> DocumentResponse:
    ...
```

### Docstrings

Use docstrings no formato Google:

```python
def create_document(self, filename: str) -> Document:
    """
    Cria um novo documento.
    
    Args:
        filename: Nome do arquivo
        
    Returns:
        Document criado
        
    Raises:
        ValidationError: Se nome inválido
    """
    ...
```

### Error Handling

Sempre trate erros:

```python
try:
    result = await service.create()
except SpecificError as e:
    raise HTTPException(status_code=400, detail=str(e))
```

---

## 🔍 Troubleshooting

### Problema: Banco não conecta

**Solução:**
```bash
# Verificar se PostgreSQL está rodando
docker ps | grep postgres

# Verificar logs
docker-compose logs postgres

# Reiniciar
docker-compose restart postgres
```

### Problema: Redis não conecta

**Solução:**
```bash
# Verificar Redis
docker ps | grep redis
docker-compose logs redis

# Testar conexão
docker exec -it banco_referencias_redis redis-cli ping
```

### Problema: Erro de importação

**Solução:**
```bash
# Reinstalar dependências
cd backend
pip install -r requirements.txt

# Verificar PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/backend"
```

### Problema: Testes falham

**Solução:**
```bash
# Limpar cache do pytest
pytest --cache-clear

# Rodar com verbose
pytest -v

# Verificar variáveis de ambiente de teste
pytest --cov=app --env-file=.env.test
```

---

## 📚 Recursos Adicionais

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pytest Documentation](https://docs.pytest.org/)

---

**Última atualização:** 22 de Dezembro de 2025

