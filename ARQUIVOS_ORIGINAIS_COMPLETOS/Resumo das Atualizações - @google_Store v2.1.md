# Resumo das Atualizações - @google_Store v2.1

**Data:** 19 de Dezembro de 2025  
**Versão:** 2.1 (atualização da v2.0)

---

## 🎯 O Que Mudou

Esta atualização incorpora **5 melhorias críticas** identificadas através de análise técnica e best practices de sistemas de conhecimento, além de adicionar **roadmap de implementação**, **estimativa de custos** e **estratégia de testes detalhada**.

---

## ✅ Novos Requisitos Adicionados

### **RF-11: Versionamento de Documentos** 🔴 CRÍTICO (MVP)

**O que é:**
- O sistema mantém um histórico de versões de cada documento
- Análises referenciam a versão específica do documento
- Usuário pode marcar versões como rascunho/final/obsoleto

**Por quê:**
- Sem versionamento, você perde histórico ("qual era a versão do contrato em março?")
- Análises antigas podem ficar sem contexto se o documento for atualizado
- Curadoria de conteúdo (draft/final/obsolete) garante qualidade dos dados

**Implementação:**
```sql
ALTER TABLE documents ADD COLUMN version INT DEFAULT 1;
ALTER TABLE documents ADD COLUMN status VARCHAR(50) DEFAULT 'draft';
```

---

### **RNF-07: Backup e Recuperância** 🔴 CRÍTICO (MVP)

**O que é:**
- Sistema mantém cópia de backup de todos os documentos
- Backup em storage separado do File Search (Cloud Storage)
- RPO < 1 hora; RTO < 24 horas

**Por quê:**
- File Search é gerenciado, mas **não é backup**
- Se o Google mudar política ou pricing, você fica refém
- Reindexação custa dinheiro (cobrado por token)

**Implementação:**
```python
# Ao fazer upload
1. Upload para Google File Search (indexação)
2. Upload para Cloud Storage (backup)
3. Salvar ambos os IDs no PostgreSQL
```

---

### **RNF-08: Monitoramento de Custos** 🔴 CRÍTICO (MVP)

**O que é:**
- Sistema rastreia custos por serviço (File Search, Gemini, Storage)
- Alertas configuráveis quando limites forem atingidos
- Dashboard de custos em tempo real

**Por quê:**
- File Search cobra por token de indexação
- Sem monitoramento, você pode ter surpresas de $1.000+
- Alertas são essenciais para controle financeiro

**Implementação:**
```sql
CREATE TABLE cost_tracking (
    id UUID PRIMARY KEY,
    date DATE,
    service VARCHAR(50),
    tokens_used BIGINT,
    estimated_cost_usd DECIMAL(10,2)
);
```

---

### **RF-08: Filtros Avançados (Expandido)** 🟡 IMPORTANTE (Fase 2)

**O que mudou:**
- Antes: Filtro genérico por metadados
- Agora: Filtros específicos por categoria, tags, status

**Implementação:**
```sql
ALTER TABLE documents ADD COLUMN tags TEXT[];
ALTER TABLE documents ADD COLUMN category VARCHAR(100);
ALTER TABLE documents ADD COLUMN custom_metadata JSONB;
```

---

### **RF-12: Feedback e Métricas de Qualidade** 🟡 IMPORTANTE (Fase 2)

**O que é:**
- Usuário pode avaliar análises (1-5 estrelas)
- Sistema rastreia taxa de sucesso por playbook
- Dashboard mostra métricas qualitativas

**Por quê:**
- Dashboards básicos não bastam
- Métricas qualitativas (precisão, satisfação) são essenciais
- Ajudam a calibrar playbooks e melhorar o sistema

**Implementação:**
```sql
CREATE TABLE analysis_feedback (
    id UUID PRIMARY KEY,
    analysis_id UUID REFERENCES analyses(id),
    rating INT CHECK (rating BETWEEN 1 AND 5),
    feedback_text TEXT
);
```

---

## 🗺️ Roadmap de Implementação

### **Fase 1: MVP (8 semanas)**
- Requisitos essenciais: RF-01, RF-02, RF-03, RF-04, RF-06, RF-11
- Requisitos não-funcionais: RNF-07, RNF-08
- Stack simplificado: Redis (não Dragonfly), BullMQ (não Temporal)

### **Fase 2: Beta (12 semanas)**
- Requisitos avançados: RF-05, RF-07, RF-08, RF-12
- Stack completo: Migrar para Dragonfly e Temporal (se necessário)
- OpenTelemetry completo

### **Fase 3: Produção (16+ semanas)**
- Requisitos nice-to-have: RF-09, RF-10
- Avaliar fallback pgvector
- Avaliar colaboração e multilíngue

---

## 💰 Estimativa de Custos

| Fase | Usuários | Custo Mensal |
|---|---|---|
| MVP | 100 | $50 - $100 |
| Beta | 1.000 | $300 - $500 |
| Produção | 10.000 | $2.000 - $5.000 |

---

## 🧪 Estratégia de Testes

| Tipo | Ferramenta | Cobertura | Fase |
|---|---|---|---|
| Unit Tests | pytest | 80% | MVP |
| Integration Tests | pytest + httpx | Endpoints críticos | MVP |
| E2E Tests | Playwright | Fluxos principais | Beta |
| Load Tests | k6 / Locust | 1.000 req/s | Produção |

---

## 📊 Comparação v2.0 vs v2.1

| Aspecto | v2.0 | v2.1 |
|---|---|---|
| **Requisitos Funcionais** | 10 | 12 (+2) |
| **Requisitos Não-Funcionais** | 6 | 8 (+2) |
| **Roadmap** | ❌ Não | ✅ Sim (3 fases) |
| **Estimativa de Custos** | ❌ Não | ✅ Sim (por fase) |
| **Estratégia de Testes** | ⚠️ Básica | ✅ Detalhada |
| **Versionamento de Docs** | ❌ Não | ✅ Sim (RF-11) |
| **Backup** | ⚠️ Implícito | ✅ Explícito (RNF-07) |
| **Monitoramento de Custos** | ❌ Não | ✅ Sim (RNF-08) |

---

## ✅ Próximos Passos

1. **Revisar** a especificação completa atualizada
2. **Validar** os requisitos com stakeholders
3. **Iniciar Fase 1 (MVP)** - 8 semanas
4. **Configurar** infraestrutura básica (Supabase, Vercel, Railway)

---

**Especificação técnica v2.1 está completa e pronta para implementação!** 🚀
