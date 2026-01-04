# Pesquisa de Tecnologias 2025

## Backend Frameworks

### Top Performers (Performance):
1. **ASP.NET Core** (C#) - Melhor performance geral
2. **Fiber** (Go) - Extremamente rápido
3. **Actix** (Rust) - Alta performance
4. **FastAPI** (Python) - Rápido e moderno
5. **NestJS** (Node.js/TypeScript) - Estruturado e escalável

### Top Populares (Ecossistema):
1. **Node.js + Express/NestJS** - Maior ecossistema JavaScript
2. **Python + FastAPI/Django** - Excelente para IA/ML
3. **Spring Boot** (Java) - Enterprise-grade
4. **Laravel** (PHP) - Full-featured
5. **Ruby on Rails** - Produtividade

**Tendência 2025:** FastAPI e NestJS crescendo rapidamente

---

## Frontend Frameworks

### Top Frameworks 2025:
1. **React** - Dominante (mais usado)
2. **Next.js** - React com SSR/SSG (padrão de mercado)
3. **Svelte/SvelteKit** - Performance excepcional, DX incrível
4. **SolidJS** - Reatividade nativa, muito rápido
5. **Vue 3** - Progressivo e flexível

### Comparação:
- **React + Next.js**: Ecossistema gigante, mais vagas, maduro
- **Svelte**: Mais rápido, menos código, melhor DX
- **SolidJS**: Performance superior, reatividade nativa

**Tendência 2025:** Next.js continua dominante, Svelte crescendo

---

## Databases

### SQL:
1. **PostgreSQL** - Melhor banco relacional open-source
2. **MySQL** - Confiável para web apps
3. **SQLite** - Leve, embedded

### NoSQL:
1. **MongoDB** - Líder NoSQL, flexível
2. **Redis** - Cache e real-time
3. **Apache Cassandra** - Escalabilidade massiva

### BaaS (Backend-as-a-Service):
1. **Supabase** - PostgreSQL + real-time + auth (Firebase alternativa)
2. **Firebase** - Google, real-time, fácil integração

### Comparação Supabase vs MongoDB:
- **Supabase**: PostgreSQL (SQL), melhor para queries complexas, real-time, auth integrado
- **MongoDB**: NoSQL, melhor para dados não-estruturados, flexibilidade de schema

**Tendência 2025:** Supabase crescendo rapidamente, PostgreSQL continua forte

---

## Recomendação Stack 2025:

### Stack Moderna (Performance + DX):
- **Frontend:** Next.js 15 + React 19 + TypeScript
- **Backend:** FastAPI (Python) ou NestJS (Node.js)
- **Database:** PostgreSQL (via Supabase)
- **Cache:** Redis
- **Storage:** Google File Store (requisito)
- **Deploy:** Vercel (frontend) + Railway/Fly.io (backend)

### Stack Alternativa (Máxima Performance):
- **Frontend:** SvelteKit + TypeScript
- **Backend:** Actix (Rust) ou Fiber (Go)
- **Database:** PostgreSQL + Redis
- **Storage:** Google File Store
- **Deploy:** Cloudflare Workers/Pages

---

## Próximos Passos:
- Pesquisar Google File Store API
- Pesquisar ferramentas de AI/ML (Gemini, OpenAI)
- Pesquisar ferramentas de deployment
- Pesquisar ferramentas de monitoramento


---

## Google File Search (Gemini API) - Detalhes

### O que é:
- **RAG (Retrieval Augmented Generation)** totalmente gerenciado
- Sistema de busca semântica (não keyword-based)
- Indexação automática de documentos com embeddings
- Integrado ao Gemini API

### Capacidades:
- **Upload de arquivos:** Até 100 MB por documento
- **Storage total:**
  - Free: 1 GB
  - Tier 1: 10 GB
  - Tier 2: 100 GB
  - Tier 3: 1 TB
- **Tipos de arquivo:** PDFs, docs, texto, etc.
- **Chunking configurável:** max_tokens_per_chunk, max_overlap_tokens
- **Metadata customizável:** key-value pairs para filtros
- **Citations:** Rastreamento de fontes usadas na resposta

### Como funciona:
1. **Criar File Search Store** - Container persistente para embeddings
2. **Upload + Import** - Arquivo é chunked, embedded, indexed
3. **Query** - Busca semântica retorna chunks relevantes
4. **Generate** - Gemini usa chunks como contexto para resposta

### API:
```python
# Criar store
file_search_store = client.file_search_stores.create(
    config={'display_name': 'my-store'}
)

# Upload direto
operation = client.file_search_stores.upload_to_file_search_store(
    file='sample.txt',
    file_search_store_name=file_search_store.name,
    config={'display_name': 'display-file-name'}
)

# Query
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Your question",
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            file_search=types.FileSearch(
                file_search_store_names=[file_search_store.name]
            )
        )]
    )
)
```

### Pricing:
- **Indexação:** $0.15 per 1M tokens (embeddings)
- **Storage:** GRÁTIS
- **Query embeddings:** GRÁTIS
- **Retrieved tokens:** Cobrado como context tokens normais

### Limites:
- Max 100 MB por documento
- Recomendação: < 20 GB por store (latência ótima)
- File object deletado após 48h (mas embeddings persistem)

### Modelos Suportados:
- gemini-3-pro-preview
- gemini-2.5-pro
- gemini-2.5-flash (e previews)
- gemini-2.5-flash-lite (e previews)

---

## Decisão: Google File Search é PERFEITO para o Banco de Referências

**Por quê:**
- ✅ RAG gerenciado (não precisa implementar do zero)
- ✅ Busca semântica nativa
- ✅ Storage grátis
- ✅ Escalável (até 1 TB no Tier 3)
- ✅ Metadata e filtros
- ✅ Citations automáticas
- ✅ Integração direta com Gemini

**Atende aos requisitos:**
- RF-01 (Centralização): ✅ File Search Store único
- RF-02 (Curadoria): ✅ Upload controlado
- RF-03 (Anotação): ✅ Metadata customizável
- RF-04 (Acessibilidade): ✅ API REST
- RF-05 (Versionamento): ⚠️ Adicionar camada
- RF-06 (Indexação): ✅ Automático
- RF-07 (Escalabilidade): ✅ Busca semântica eficiente
- RF-08 (Preservação): ✅ Embeddings persistem indefinidamente
