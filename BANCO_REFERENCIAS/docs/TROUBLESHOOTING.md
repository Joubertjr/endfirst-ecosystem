# 🔧 Troubleshooting Guide

**Versão:** 1.0.0  
**Última atualização:** 22 de Dezembro de 2025

---

## 📋 Índice

1. [Problemas Comuns](#problemas-comuns)
2. [Problemas de Banco de Dados](#problemas-de-banco-de-dados)
3. [Problemas de Cache](#problemas-de-cache)
4. [Problemas de Autenticação](#problemas-de-autenticação)
5. [Problemas de API](#problemas-de-api)
6. [Problemas de Docker](#problemas-de-docker)
7. [Problemas de Testes](#problemas-de-testes)

---

## 🐛 Problemas Comuns

### Erro: "Module not found"

**Sintoma:**
```
ModuleNotFoundError: No module named 'app'
```

**Solução:**
```bash
# Verificar PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/backend"

# Ou rodar do diretório backend
cd backend
python -m app.main
```

---

### Erro: "Connection refused"

**Sintoma:**
```
ConnectionRefusedError: [Errno 61] Connection refused
```

**Solução:**
```bash
# Verificar se serviços estão rodando
docker-compose ps

# Verificar logs
docker-compose logs backend
docker-compose logs postgres
docker-compose logs redis

# Reiniciar serviços
docker-compose restart
```

---

## 💾 Problemas de Banco de Dados

### PostgreSQL não conecta

**Sintoma:**
```
asyncpg.exceptions.InvalidPasswordError: password authentication failed
```

**Solução:**
```bash
# Verificar variáveis de ambiente
cat .env | grep DATABASE_URL

# Verificar se PostgreSQL está rodando
docker ps | grep postgres

# Verificar logs
docker-compose logs postgres

# Recriar banco
docker-compose down -v
docker-compose up -d postgres
```

---

### Tabelas não criadas

**Sintoma:**
```
relation "documents" does not exist
```

**Solução:**
```bash
# Verificar se models estão sendo importados
# Em app/main.py deve ter:
from app.models import Document, Reference, Project, Analysis

# Reiniciar backend
docker-compose restart backend

# Verificar logs de inicialização
docker-compose logs backend | grep "Banco de dados inicializado"
```

---

### Erro de migração

**Sintoma:**
```
alembic.util.exc.CommandError: Target database is not up to date
```

**Solução:**
```bash
# Criar migração
cd backend
alembic revision --autogenerate -m "description"

# Aplicar migração
alembic upgrade head

# Ou recriar banco (desenvolvimento)
docker-compose down -v
docker-compose up -d
```

---

## 🔄 Problemas de Cache

### Redis não conecta

**Sintoma:**
```
Error 111 connecting to localhost:6379. Connection refused.
```

**Solução:**
```bash
# Verificar Redis
docker ps | grep redis

# Testar conexão
docker exec -it banco_referencias_redis redis-cli ping
# Deve retornar: PONG

# Verificar URL no .env
REDIS_URL=redis://redis:6379/0

# Reiniciar Redis
docker-compose restart redis
```

---

### Cache não funciona

**Sintoma:**
Cache sempre retorna None

**Solução:**
```bash
# Verificar se cache está habilitado
# Em .env deve ter:
REDIS_URL=redis://redis:6379/0

# Verificar logs
docker-compose logs backend | grep "Cache Redis"

# Testar manualmente
docker exec -it banco_referencias_redis redis-cli
> SET test "value"
> GET test
```

---

## 🔐 Problemas de Autenticação

### Erro: "Token inválido"

**Sintoma:**
```
401 Unauthorized: Token inválido ou expirado
```

**Solução:**
```bash
# Verificar chaves do Clerk
cat .env | grep CLERK

# Verificar se chaves estão corretas
# CLERK_SECRET_KEY=sk_test_...
# CLERK_PUBLISHABLE_KEY=pk_test_...

# Em desenvolvimento, auth está desabilitada se não configurada
# Verificar logs:
docker-compose logs backend | grep "Clerk"
```

---

### Erro: "Authentication required"

**Sintoma:**
```
401 Unauthorized: Token de autenticação requerido
```

**Solução:**
```bash
# Verificar header Authorization
# Deve ter formato:
Authorization: Bearer <token>

# Em desenvolvimento, pode usar mock user se auth desabilitada
# Verificar app/core/auth.py para modo desenvolvimento
```

---

## 🌐 Problemas de API

### Erro 422: Validation Error

**Sintoma:**
```json
{
  "detail": [
    {
      "loc": ["body", "query"],
      "msg": "ensure this value has at least 3 characters"
    }
  ]
}
```

**Solução:**
- Verificar dados enviados
- Consultar schema em `/api/docs`
- Query deve ter mínimo 3 caracteres
- File size máximo: 50MB

---

### Erro 404: Not Found

**Sintoma:**
```
404 Not Found: Documento 'uuid' não encontrado
```

**Solução:**
```bash
# Verificar se ID existe
curl -X GET "http://localhost:8000/api/v1/documents/uuid" \
  -H "Authorization: Bearer TOKEN"

# Verificar ownership (user_id)
# Documentos são filtrados por usuário
```

---

### Erro 500: Internal Server Error

**Sintoma:**
```
500 Internal Server Error
```

**Solução:**
```bash
# Verificar logs
docker-compose logs backend

# Verificar Google File Search
# Verificar GEMINI_API_KEY
cat .env | grep GEMINI

# Verificar se File Store existe
# Pode ser criado automaticamente
```

---

## 🐳 Problemas de Docker

### Container não inicia

**Sintoma:**
```
Error starting userland proxy: listen tcp4 0.0.0.0:8000: bind: address already in use
```

**Solução:**
```bash
# Verificar se porta está em uso
lsof -i :8000

# Matar processo
kill -9 <PID>

# Ou mudar porta no docker-compose.yml
ports:
  - '8001:8000'
```

---

### Volume não monta

**Sintoma:**
```
Changes not reflected in container
```

**Solução:**
```bash
# Rebuild container
docker-compose build --no-cache backend

# Recriar containers
docker-compose up -d --force-recreate
```

---

### Erro de memória

**Sintoma:**
```
Error response from daemon: cannot start container: OCI runtime create failed
```

**Solução:**
```bash
# Verificar uso de memória
docker stats

# Limpar recursos não usados
docker system prune -a

# Aumentar memória do Docker (Docker Desktop)
```

---

## 🧪 Problemas de Testes

### Testes falham

**Sintoma:**
```
pytest failures
```

**Solução:**
```bash
# Limpar cache
pytest --cache-clear

# Rodar com verbose
pytest -v

# Rodar teste específico
pytest tests/unit/test_document_service.py::test_create_document -v

# Verificar variáveis de ambiente
pytest --env-file=.env.test
```

---

### Erro de importação em testes

**Sintoma:**
```
ImportError: cannot import name 'DocumentService' from 'app.services'
```

**Solução:**
```bash
# Verificar PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/backend"

# Verificar pytest.ini
# Deve ter:
# pythonpath = app

# Rodar do diretório backend
cd backend
pytest
```

---

### Testes de integração falham

**Sintoma:**
```
Database connection errors in tests
```

**Solução:**
```bash
# Verificar se usa SQLite in-memory
# Em tests/conftest.py deve usar:
# sqlite+aiosqlite:///:memory:

# Verificar fixtures
pytest tests/integration/ -v

# Limpar estado
pytest --cache-clear
```

---

## 📞 Buscar Ajuda

### Logs Úteis

```bash
# Todos os logs
docker-compose logs

# Logs específicos
docker-compose logs backend
docker-compose logs postgres
docker-compose logs redis

# Seguir logs
docker-compose logs -f backend
```

### Verificar Status

```bash
# Status dos containers
docker-compose ps

# Uso de recursos
docker stats

# Health checks
docker-compose ps | grep "healthy"
```

### Limpar Tudo

```bash
# Parar e remover containers
docker-compose down

# Remover volumes também
docker-compose down -v

# Limpar sistema
docker system prune -a
```

---

## 🔍 Checklist de Diagnóstico

Antes de reportar problema, verifique:

- [ ] Todos os containers estão rodando (`docker-compose ps`)
- [ ] Variáveis de ambiente estão configuradas (`.env`)
- [ ] Logs não mostram erros críticos
- [ ] Portas não estão em conflito
- [ ] Chaves de API estão válidas (GEMINI_API_KEY, CLERK)
- [ ] Banco de dados está acessível
- [ ] Redis está acessível (se usando cache)
- [ ] Dependências estão instaladas (`pip install -r requirements.txt`)

---

**Última atualização:** 22 de Dezembro de 2025

