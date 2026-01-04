# 🛠️ Setup do Projeto - Banco de Referências

**Data:** 2025-12-16

---

## ✅ Checklist de Setup

### 1. Configuração Inicial

- [x] Estrutura de diretórios criada
- [x] Arquivos base configurados
- [x] Docker Compose configurado
- [ ] Variáveis de ambiente configuradas

### 2. Variáveis de Ambiente

Criar arquivo `.env` na raiz do projeto (copiar de `.env.example`):

```env
# Google Gemini API (OBRIGATÓRIO)
GEMINI_API_KEY=sua_chave_aqui

# Google Gemini Model (opcional)
GEMINI_MODEL=gemini-2.5-flash

# Google File Search Store ID (opcional - será criado automaticamente)
FILE_STORE_ID=

# PostgreSQL (configurado no docker-compose.yml)
# Não precisa configurar - será criado automaticamente
POSTGRES_USER=banco_ref
POSTGRES_PASSWORD=banco_ref_password
POSTGRES_DB=banco_referencias

# Environment
ENVIRONMENT=development
DEBUG=true
```

---

## 🐳 Setup com Docker (Recomendado)

### Passo 1: Configurar .env

```bash
cp .env.example .env
# Editar .env e adicionar GEMINI_API_KEY
```

### Passo 2: Iniciar com Docker Compose

```bash
# Na raiz do projeto
docker-compose up --build
```

Isso vai:
1. ✅ Criar container PostgreSQL
2. ✅ Criar container Backend (FastAPI)
3. ✅ Conectar backend ao PostgreSQL
4. ✅ Criar tabelas automaticamente

### Passo 3: Acessar Aplicação

- **API**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/api/docs
- **Health Check**: http://localhost:8000/health
- **PostgreSQL**: localhost:5432

---

## 🛠️ Setup Local (Desenvolvimento)

### Pré-requisitos

- Python 3.12+
- PostgreSQL 16+ (ou usar Docker para PostgreSQL)

### Passo 1: Criar Ambiente Virtual

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
```

### Passo 2: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 3: Configurar .env

```env
# Database (local)
DATABASE_URL=postgresql+asyncpg://banco_ref:banco_ref_password@localhost:5432/banco_referencias

# Google Gemini
GEMINI_API_KEY=sua_chave_aqui
GEMINI_MODEL=gemini-2.5-flash
```

### Passo 4: Rodar PostgreSQL (Docker)

```bash
# Se não quiser instalar PostgreSQL localmente, use Docker
docker run -d \
  --name banco_ref_postgres \
  -e POSTGRES_USER=banco_ref \
  -e POSTGRES_PASSWORD=banco_ref_password \
  -e POSTGRES_DB=banco_referencias \
  -p 5432:5432 \
  postgres:16-alpine
```

### Passo 5: Rodar Aplicação

```bash
# Com ambiente virtual ativado
python -m app.main
# ou
uvicorn app.main:app --reload
```

---

## 🔍 Verificação

### Verificar se está funcionando

1. **Health Check:**
   ```bash
   curl http://localhost:8000/health
   # Deve retornar: {"status":"healthy"}
   ```

2. **Documentação Swagger:**
   - Acessar: http://localhost:8000/api/docs
   - Deve abrir interface Swagger

3. **PostgreSQL:**
   ```bash
   # Se usando Docker
   docker exec -it banco_referencias_postgres psql -U banco_ref -d banco_referencias
   # Listar tabelas
   \dt
   ```

---

## 📋 Comandos Úteis

### Docker

```bash
# Iniciar todos os serviços
docker-compose up --build

# Parar serviços
docker-compose down

# Ver logs
docker-compose logs -f backend

# Acessar PostgreSQL
docker exec -it banco_referencias_postgres psql -U banco_ref -d banco_referencias
```

### Desenvolvimento

```bash
# Rodar testes (quando implementados)
pytest

# Formatar código
black app/
isort app/

# Verificar tipos
mypy app/
```

---

## ⚠️ Troubleshooting

### Erro: "Connection refused" no PostgreSQL

**Solução:** Verificar se PostgreSQL está rodando:
```bash
docker-compose ps postgres
# Deve mostrar "Up" e "healthy"
```

### Erro: "GEMINI_API_KEY não definido"

**Solução:** Verificar se `.env` existe e tem `GEMINI_API_KEY` configurado.

### Erro: "DATABASE_URL inválido"

**Solução:** Verificar formato do `DATABASE_URL`:
- Formato correto: `postgresql+asyncpg://user:password@host:port/dbname`
- No Docker: será criado automaticamente
- Local: configurar manualmente no `.env`

---

**Status:** ✅ Docker Compose configurado com PostgreSQL  
**Próximo passo:** Configurar `.env` e rodar `docker-compose up --build`
