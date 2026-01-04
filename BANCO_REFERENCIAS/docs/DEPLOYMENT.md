# 🚀 Guia de Deployment

**Versão:** 1.0.0  
**Última atualização:** 22 de Dezembro de 2025

---

## 📋 Índice

1. [Requisitos](#requisitos)
2. [Deployment com Docker](#deployment-com-docker)
3. [Deployment em Produção](#deployment-em-produção)
4. [Configuração de Ambiente](#configuração-de-ambiente)
5. [Monitoramento](#monitoramento)
6. [Backup](#backup)
7. [Segurança](#segurança)

---

## ✅ Requisitos

### Infraestrutura

- **Servidor** com Docker e Docker Compose
- **PostgreSQL** 16+ (pode usar Docker ou serviço gerenciado)
- **Redis** 7+ (pode usar Docker ou serviço gerenciado)
- **Domínio** (opcional, para HTTPS)

### Recursos Mínimos

- **CPU:** 2 cores
- **RAM:** 4GB
- **Disco:** 20GB (para dados)
- **Rede:** Conexão estável

---

## 🐳 Deployment com Docker

### 1. Preparar Servidor

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Instalar Docker Compose
sudo apt install docker-compose-plugin

# Verificar instalação
docker --version
docker compose version
```

### 2. Clonar Repositório

```bash
# Clonar repositório
git clone <repository-url>
cd BANCO_REFERENCIAS

# Criar .env de produção
cp .env.example .env.production
```

### 3. Configurar Variáveis de Ambiente

Edite `.env.production`:

```bash
# Application
ENVIRONMENT=production
DEBUG=false

# Database
DATABASE_URL=postgresql+asyncpg://user:password@postgres:5432/banco_referencias

# Google Gemini
GEMINI_API_KEY=your_production_api_key
GEMINI_MODEL=gemini-2.5-flash
FILE_STORE_ID=your_file_store_id

# Clerk
CLERK_SECRET_KEY=sk_live_...
CLERK_PUBLISHABLE_KEY=pk_live_...

# Redis
REDIS_URL=redis://redis:6379/0

# Security
ALLOWED_ORIGINS=https://yourdomain.com
```

### 4. Iniciar Aplicação

```bash
# Build e start
docker-compose -f docker-compose.yml --env-file .env.production up -d --build

# Verificar status
docker-compose ps

# Ver logs
docker-compose logs -f
```

---

## 🌐 Deployment em Produção

### Opção 1: Servidor Dedicado (VPS)

**Passos:**

1. **Configurar Firewall**
```bash
# UFW
sudo ufw allow 22/tcp  # SSH
sudo ufw allow 80/tcp  # HTTP
sudo ufw allow 443/tcp # HTTPS
sudo ufw enable
```

2. **Configurar Nginx (Reverse Proxy)**
```nginx
# /etc/nginx/sites-available/banco_referencias
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

3. **HTTPS com Let's Encrypt**
```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx

# Obter certificado
sudo certbot --nginx -d yourdomain.com
```

### Opção 2: Cloud Providers

#### AWS

1. **EC2 Instance**
   - Tipo: t3.medium ou maior
   - AMI: Ubuntu 22.04
   - Security Group: Portas 80, 443, 22

2. **RDS PostgreSQL**
   - Engine: PostgreSQL 16
   - Instance: db.t3.micro (dev) ou db.t3.small (prod)

3. **ElastiCache Redis**
   - Engine: Redis 7
   - Node: cache.t3.micro

#### Google Cloud Platform

1. **Compute Engine**
   - Machine Type: e2-medium
   - OS: Ubuntu 22.04

2. **Cloud SQL**
   - Database: PostgreSQL 16
   - Tier: db-f1-micro (dev)

3. **Memorystore**
   - Redis 7

---

## ⚙️ Configuração de Ambiente

### Variáveis de Ambiente de Produção

```bash
# Application
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO

# Database (exemplo com RDS)
DATABASE_URL=postgresql+asyncpg://user:password@db.example.com:5432/banco_referencias

# Google Gemini
GEMINI_API_KEY=your_production_key
GEMINI_MODEL=gemini-2.5-flash
FILE_STORE_ID=fileSearchStores/xxx

# Clerk
CLERK_SECRET_KEY=sk_live_...
CLERK_PUBLISHABLE_KEY=pk_live_...
CLERK_FRONTEND_API=https://your-clerk-frontend-api

# Redis (exemplo com ElastiCache)
REDIS_URL=redis://redis.example.com:6379/0

# CORS
ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# File Limits
MAX_FILE_SIZE_MB=50
MIN_QUERY_LENGTH=3
MAX_QUERY_LENGTH=500
```

### Docker Compose para Produção

Crie `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    restart: always
    env_file:
      - .env.production
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - REDIS_URL=${REDIS_URL}
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # PostgreSQL (ou usar serviço gerenciado)
  postgres:
    image: postgres:16-alpine
    restart: always
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}

  # Redis (ou usar serviço gerenciado)
  redis:
    image: redis:7-alpine
    restart: always
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes

volumes:
  postgres_data:
  redis_data:
```

---

## 📊 Monitoramento

### Health Checks

```bash
# Health endpoint
curl http://localhost:8000/health

# Resposta esperada:
{"status": "healthy"}
```

### Logs

```bash
# Ver logs
docker-compose logs -f backend

# Logs apenas erros
docker-compose logs backend | grep ERROR

# Últimas 100 linhas
docker-compose logs --tail=100 backend
```

### Métricas (Futuro)

Com Prometheus e Grafana (ver Observabilidade).

---

## 💾 Backup

### Backup do PostgreSQL

```bash
# Backup manual
docker exec banco_referencias_postgres pg_dump -U banco_ref banco_referencias > backup.sql

# Restaurar
docker exec -i banco_referencias_postgres psql -U banco_ref banco_referencias < backup.sql

# Backup automático (cron)
# Adicionar ao crontab:
0 2 * * * docker exec banco_referencias_postgres pg_dump -U banco_ref banco_referencias > /backups/backup-$(date +\%Y\%m\%d).sql
```

### Backup do Redis

```bash
# Redis persiste automaticamente com AOF
# Backup manual:
docker exec banco_referencias_redis redis-cli BGSAVE
docker cp banco_referencias_redis:/data/dump.rdb ./backup.rdb
```

---

## 🔒 Segurança

### Checklist de Segurança

- [ ] **Variáveis de ambiente** não commitadas no Git
- [ ] **HTTPS** configurado (Let's Encrypt)
- [ ] **Firewall** configurado (apenas portas necessárias)
- [ ] **Senhas** fortes para banco de dados
- [ ] **API Keys** em produção (não usar keys de teste)
- [ ] **CORS** configurado corretamente
- [ ] **Rate limiting** (implementar se necessário)
- [ ] **Logs** não expor informações sensíveis
- [ ] **Updates** regulares do sistema e dependências

### Hardening do Docker

```bash
# Executar containers como usuário não-root
# No Dockerfile:
USER 1000:1000

# Limitar recursos
deploy:
  resources:
    limits:
      cpus: '2'
      memory: 2G
```

---

## 🔄 Atualização

### Processo de Atualização

```bash
# 1. Backup
docker exec banco_referencias_postgres pg_dump -U banco_ref banco_referencias > backup-$(date +%Y%m%d).sql

# 2. Pull código atualizado
git pull origin main

# 3. Rebuild
docker-compose build --no-cache

# 4. Restart
docker-compose up -d

# 5. Verificar logs
docker-compose logs -f backend
```

### Rollback

```bash
# 1. Parar containers
docker-compose down

# 2. Voltar código
git checkout <previous-commit>

# 3. Rebuild
docker-compose build

# 4. Iniciar
docker-compose up -d

# 5. Restaurar backup se necessário
docker exec -i banco_referencias_postgres psql -U banco_ref banco_referencias < backup.sql
```

---

## 📞 Troubleshooting de Produção

### Container não inicia

```bash
# Ver logs
docker-compose logs backend

# Verificar recursos
docker stats

# Verificar espaço em disco
df -h
```

### Performance

```bash
# Ver uso de recursos
docker stats

# Verificar conexões
docker exec banco_referencias_postgres psql -U banco_ref -c "SELECT count(*) FROM pg_stat_activity;"

# Limpar cache do Redis se necessário
docker exec banco_referencias_redis redis-cli FLUSHALL
```

---

**Última atualização:** 22 de Dezembro de 2025

