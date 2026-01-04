### 6.2 Roadmap de Implementação (v2.1)

**Fase 1: MVP (8 semanas)**
- **Objetivo:** Lançar uma versão funcional com os recursos essenciais.
- **Requisitos:**
  - RF-01: Gerenciamento de Projetos
  - RF-02: Gerenciamento de Documentos
  - RF-03: Consulta Semântica (RAG)
  - RF-04: Citação de Fontes
  - RF-06: Gerenciamento de Usuários
  - RF-11: Versionamento de Documentos
  - RNF-07: Backup e Recuperação
  - RNF-08: Monitoramento de Custos
- **Stack Simplificado:**
  - Redis para cache (ao invés de Dragonfly)
  - BullMQ para jobs (ao invés de Temporal)
  - Apenas Google File Search (sem pgvector)

**Fase 2: Beta (12 semanas)**
- **Objetivo:** Adicionar funcionalidades avançadas e coletar feedback.
- **Requisitos:**
  - RF-05: Gerenciamento de Playbooks
  - RF-07: Versionamento de Análises
  - RF-08: Filtros Avançados
  - RF-12: Feedback e Métricas de Qualidade
- **Stack Completo:**
  - Migrar para Dragonfly (se necessário)
  - Migrar para Temporal (se necessário)
  - Adicionar OpenTelemetry completo

**Fase 3: Produção (16+ semanas)**
- **Objetivo:** Lançar para o público geral e escalar.
- **Requisitos:**
  - RF-09: Exportação de Resultados
  - RF-10: Dashboard de Projeto
- **Opcional (Avaliar):**
  - Fallback para pgvector
  - Suporte a colaboração e multilíngue
