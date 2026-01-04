# 🛠️ Stack Tecnológico Decidido - Banco de Referências

**Data:** 2025-12-16  
**Baseado em:** Análise técnica e melhores práticas 2025/2026

---

## ✅ Premissas Fixas (Obrigatórias)

1. **Google File Search Store** - RAG nativo (obrigatório)
2. **Docker** - Containerização (obrigatório)

---

## 🎯 Stack Decidido (Melhor Escolha Técnica)

### Backend

**Framework: FastAPI** ⭐
- **Performance**: 18.000 req/s (vs Flask 2.500 req/s) - **7x mais rápido**
- **Async nativo**: asyncio/await out-of-the-box
- **Type safety**: Validação automática com Pydantic
- **Documentação**: OpenAPI automático (Swagger)
- **Moderno**: Python 3.12+, recursos modernos

**Database: PostgreSQL (Neon Serverless)**
- **Serverless**: Auto-scaling, sem gerenciamento
- **Custo**: Free tier 0.5 GB (suficiente para MVP)
- **Escalável**: Multi-user desde o início
- **DX**: Branches como Git, CLI intuitivo
- **Padrão**: Banco relacional robusto

**Por que não SQLite?**
- ❌ Não escala bem para múltiplos usuários simultâneos
- ❌ Limitado para produção
- ❌ PostgreSQL é gratuito no Neon e muito melhor

### Frontend

**Framework: Next.js 15** (Fase 3)
- **RSC**: React Server Components (menor bundle)
- **Server Actions**: Mutations sem criar endpoints
- **SEO**: Importante para Banco de Referências público
- **Performance**: Otimizações automáticas

**Alternativa (mais simples): React 18 + Vite**
- Se quiser começar mais simples
- Pode migrar para Next.js depois

### Cache (Opcional - Fase 2)

**Redis simples** (MVP)
- Suficiente para começar
- Pode migrar para Dragonfly depois se necessário

---

## 📊 Comparação: Decisão vs @google_Store

| Componente | @google_Store | Banco de Referências | Razão |
|------------|---------------|----------------------|-------|
| **Backend** | Flask | **FastAPI** | 7x performance, async nativo |
| **Database** | SQLite | **PostgreSQL (Neon)** | Escalável, multi-user |
| **Vector DB** | Google File Search | **Google File Search** | Obrigatório ✅ |
| **Cache** | Nenhum | **Redis** (Fase 2) | Performance |
| **Frontend** | React + Vite | **Next.js 15** (Fase 3) | SEO, RSC |
| **Containerização** | Docker | **Docker** | Obrigatório ✅ |

---

## 🚀 Por Que Essas Escolhas?

### FastAPI sobre Flask

**Vantagens:**
- ✅ 7x mais rápido (18k vs 2.5k req/s)
- ✅ Async nativo (melhor para I/O)
- ✅ Type safety automático
- ✅ Documentação automática
- ✅ Moderno e mantido ativamente

**Desvantagens:**
- ⚠️ Curva de aprendizado (mas vale a pena)
- ⚠️ Ecossistema menor (mas suficiente)

**Decisão:** FastAPI - Performance e modernidade valem o investimento

### PostgreSQL sobre SQLite

**Vantagens:**
- ✅ Escalável desde o início
- ✅ Multi-user nativo
- ✅ Free tier no Neon (0.5 GB)
- ✅ Serverless (auto-scaling)
- ✅ Padrão da indústria

**Desvantagens:**
- ⚠️ Requer conta externa (Neon)
- ⚠️ Ligeiramente mais complexo

**Decisão:** PostgreSQL (Neon) - Escalabilidade e robustez valem a pena

### Next.js sobre React simples

**Vantagens:**
- ✅ SEO melhor (importante para referências)
- ✅ RSC (menor bundle)
- ✅ Server Actions (código mais simples)
- ✅ Performance otimizada

**Desvantagens:**
- ⚠️ Mais complexo
- ⚠️ Curva de aprendizado

**Decisão:** Next.js 15 - Para Fase 3, vale o investimento

---

## 📋 Stack Completo

### Fase 1 (MVP)

| Camada | Tecnologia | Versão | Justificativa |
|--------|-----------|--------|---------------|
| **Backend** | FastAPI | 0.115+ | Performance, async, type-safe |
| **Database** | PostgreSQL (Neon) | 16+ | Serverless, free tier, escalável |
| **Vector DB** | Google File Search | - | Obrigatório, RAG nativo |
| **Language** | Python | 3.12+ | Async nativo, type hints |
| **Containerização** | Docker | 26+ | Obrigatório |

### Fase 2 (Core)

| Componente | Tecnologia | Quando |
|------------|-----------|--------|
| **Cache** | Redis | Fase 2 (opcional) |
| **Workers** | Threading Python | Fase 2 (suficiente para MVP) |

### Fase 3 (Frontend)

| Componente | Tecnologia | Versão |
|------------|-----------|--------|
| **Framework** | Next.js | 15+ |
| **Language** | TypeScript | 5.5+ |
| **Styling** | Tailwind CSS | 4.0+ |
| **Components** | shadcn/ui | latest |

---

## 💰 Custos Estimados

### MVP (10 usuários)

| Serviço | Custo/mês |
|---------|-----------|
| Neon PostgreSQL (free tier) | **$0** |
| Google File Search | ~$5 |
| Gemini API | ~$0.15 |
| Docker (self-hosted) | $0 |
| **Total** | **~$5-10/mês** |

---

## ✅ Checklist de Implementação

### Backend
- [x] Decidir FastAPI (não Flask)
- [x] Decidir PostgreSQL/Neon (não SQLite)
- [ ] Configurar FastAPI
- [ ] Configurar Neon PostgreSQL
- [ ] Integrar Google File Search

### Frontend (Fase 3)
- [ ] Setup Next.js 15
- [ ] Configurar TypeScript
- [ ] Setup Tailwind CSS
- [ ] Integrar shadcn/ui

---

## 📝 Próximos Passos

1. **Atualizar `requirements.txt`** para FastAPI
2. **Configurar Neon PostgreSQL** (criar conta, obter connection string)
3. **Atualizar `main.py`** para FastAPI
4. **Configurar SQLAlchemy** (async) para PostgreSQL
5. **Testar integração** completa

---

**Decisão tomada em:** 2025-12-16  
**Justificativa:** Baseada em análise técnica e melhores práticas 2025/2026


