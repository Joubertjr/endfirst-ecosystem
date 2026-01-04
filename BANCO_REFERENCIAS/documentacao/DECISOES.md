# 🏛️ Architecture Decision Records (ADRs)

**Data de Criação:** 2025-12-16  
**Mantido por:** Equipe de Desenvolvimento

---

## ADR-001: FastAPI como Framework Backend

**Data:** 2025-12-16  
**Status:** ✅ Aceita

### Contexto

Precisávamos escolher um framework Python para o backend. Opções consideradas:
- Flask (simples, familiar)
- Django (completo, mas pesado)
- FastAPI (moderno, async, rápido)

### Decisão

Escolhemos **FastAPI** como framework principal do backend.

**Justificativa:**
- **Performance**: 18.000 req/s (vs Flask 2.500 req/s) - **7x mais rápido**
- **Async nativo**: Suporte a asyncio/await out-of-the-box
- **Type safety**: Validação automática com Pydantic
- **OpenAPI**: Documentação automática (Swagger)
- **Moderno**: Suporte a Python 3.12+, recursos modernos

**Referências:**
- [FastAPI Benchmarks](https://www.techempower.com/benchmarks/)
- Especificação Técnica v2.0, Seção 5.2.2

### Consequências

**Positivas:**
- ✅ Alta performance desde o início
- ✅ Código mais limpo com async/await
- ✅ Documentação automática da API
- ✅ Validação de tipos automática

**Negativas:**
- ⚠️ Curva de aprendizado (se time não conhece)
- ⚠️ Ecossistema menor que Django (mas suficiente)

---

## ADR-002: PostgreSQL (Neon) como Database Principal

**Data:** 2025-12-16  
**Status:** ✅ Aceita

### Contexto

Precisávamos escolher um banco de dados. Opções consideradas:
- SQLite (simples, mas não escala)
- PostgreSQL tradicional (self-hosted, complexo)
- Neon PostgreSQL (serverless, gerenciado)

### Decisão

Escolhemos **PostgreSQL via Neon** como database principal.

**Justificativa:**
- **Serverless**: Auto-scaling, sem gerenciamento de servidor
- **Custo**: Free tier 0.5 GB (suficiente para MVP)
- **Performance**: Separação compute/storage, instant branching
- **PostgreSQL**: Padrão da indústria, rico em features
- **DX**: CLI, branches como Git

### Consequências

**Positivas:**
- ✅ Custo zero no MVP
- ✅ Escalabilidade automática
- ✅ Sem necessidade de gerenciar servidor
- ✅ Branches para testes isolados
- ✅ Multi-user desde o início

**Negativas:**
- ⚠️ Vendor lock-in (mas PostgreSQL é padrão, fácil migrar)
- ⚠️ Limite do free tier pode ser atingido

### Alternativas Consideradas

- **SQLite**: Rejeitado - não suporta múltiplos usuários bem, não escala
- **Supabase**: Considerado, mas Neon tem melhor DX
- **Self-hosted PostgreSQL**: Rejeitado - complexidade desnecessária no MVP

**Referências:**
- [Neon Documentation](https://neon.tech/docs)

---

## ADR-003: Google File Search como Vector DB (RAG)

**Data:** 2025-12-16  
**Status:** ✅ Aceita (Obrigatório)

### Contexto

Precisávamos de busca semântica (RAG). Opções consideradas:
- Google File Search (nativo Gemini) ⭐ **OBRIGATÓRIO**
- pgvector (PostgreSQL extension)
- Qdrant/Pinecone (vector DBs dedicados)

### Decisão

Escolhemos **Google File Search** como solução de RAG.

**Justificativa:**
- **Obrigatório**: Premissa fixa do projeto
- **Nativo**: Integração direta com Gemini API
- **Zero setup**: Sem necessidade de configurar embeddings
- **Gerenciado**: Google cuida de tudo (indexação, busca)
- **Custo baixo**: $0.01 por documento (one-time)
- **Qualidade**: Embeddings do Gemini são state-of-the-art

### Consequências

**Positivas:**
- ✅ Zero configuração de vector DB
- ✅ Busca semântica de alta qualidade
- ✅ Integração simples com Gemini
- ✅ Sem necessidade de gerenciar embeddings

**Negativas:**
- ⚠️ Vendor lock-in (mitigado com pgvector como fallback futuro)
- ⚠️ Custo por documento (mas baixo)

### Plano de Mitigação

- **pgvector como fallback**: Implementar no futuro se necessário migrar
- **Exportar metadata**: Manter metadata no PostgreSQL para migração futura

---

## ADR-004: Threading Python para Processamento Assíncrono (MVP)

**Data:** 2025-12-16  
**Status:** ✅ Aceita (MVP)

### Contexto

Precisávamos de processamento assíncrono para análises. Opções:
- Threading Python (simples)
- Celery (robusto, mas complexo)
- Temporal (workflows, mas overkill para MVP)

### Decisão

Escolhemos **Threading Python simples** para o MVP.

**Justificativa:**
- **Simplicidade**: Já vem com Python, sem dependências
- **Suficiente**: Para MVP, análises não são críticas
- **Iteração rápida**: Podemos implementar rápido
- **Migração fácil**: Fácil migrar para Temporal depois

### Consequências

**Positivas:**
- ✅ Implementação rápida
- ✅ Sem dependências externas
- ✅ Fácil de testar

**Negativas:**
- ⚠️ Não é durável (se processo morrer, perde jobs)
- ⚠️ Não tem retry automático
- ⚠️ Não tem observabilidade

### Plano de Migração

**Fase 4:** Migrar para Temporal quando necessário:
- Análises críticas
- Workflows complexos
- Necessidade de observabilidade

---

## ADR-005: Next.js 15 para Frontend

**Data:** 2025-12-16  
**Status:** ✅ Aceita (Fase 3)

### Contexto

Precisávamos escolher framework frontend. Opções:
- React + Vite (simples, já usado no @google_Store)
- Next.js 15 (RSC, Server Actions, SEO)
- SvelteKit (mais leve, menos popular)

### Decisão

Escolhemos **Next.js 15** como framework frontend.

**Justificativa:**
- **RSC**: React Server Components reduzem bundle size
- **Server Actions**: Mutations sem criar endpoints
- **SEO**: Metadata API para indexação
- **Maturidade**: Ecossistema robusto
- **Performance**: Otimizações automáticas

### Consequências

**Positivas:**
- ✅ Melhor SEO (importante para Banco de Referências público)
- ✅ Código mais simples (Server Actions)
- ✅ Performance otimizada
- ✅ Bundle size menor (RSC)

**Negativas:**
- ⚠️ Mais complexo que React simples
- ⚠️ Curva de aprendizado para RSC

**Referências:**
- [Next.js 15 Documentation](https://nextjs.org/docs)

---

## ADR-006: Docker como Containerização

**Data:** 2025-12-16  
**Status:** ✅ Aceita (Obrigatório)

### Contexto

Premissa fixa do projeto. Docker é obrigatório.

### Decisão

**Docker** é usado para containerização.

**Justificativa:**
- **Obrigatório**: Premissa fixa do projeto
- **Padrão da indústria**: Ferramenta mais usada
- **Isolamento**: Ambiente consistente
- **Portabilidade**: Funciona em qualquer lugar

---

## 📝 Template para Novos ADRs

```markdown
## ADR-XXX: [Título da Decisão]

**Data:** YYYY-MM-DD  
**Status:** Proposta | Aceita | Rejeitada | Substituída

### Contexto

[Por que precisamos tomar essa decisão?]

### Decisão

[O que decidimos fazer?]

### Justificativa

[Por que escolhemos essa opção?]

### Consequências

**Positivas:**
- ✅ [Consequência positiva 1]
- ✅ [Consequência positiva 2]

**Negativas:**
- ⚠️ [Consequência negativa 1]
- ⚠️ [Consequência negativa 2]

### Alternativas Consideradas

- [Alternativa 1]: [Por que foi rejeitada]
- [Alternativa 2]: [Por que foi rejeitada]

### Referências

- [Link ou documento relacionado]
```

---

**Última atualização:** 2025-12-16
