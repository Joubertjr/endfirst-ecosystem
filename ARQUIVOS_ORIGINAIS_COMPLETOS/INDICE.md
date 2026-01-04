# Banco de Referências - ENDFIRST Method

**Última atualização:** 19 de Dezembro de 2025  
**Versão:** 1.1

---

## 📚 O que é o Banco de Referências?

O Banco de Referências é o **"cérebro" do método ENDFIRST**. Ele armazena:

- ✅ Especificações técnicas de projetos
- ✅ Análises de arquitetura e trade-offs
- ✅ Casos de uso documentados
- ✅ Aprendizados e retrospectivas
- ✅ Templates e frameworks reutilizáveis

**Objetivo:** Transformar aprendizados implícitos em conhecimento explícito e reutilizável.

---

## 📁 Estrutura de Diretórios

```
banco_referencias/
├── INDICE.md (este arquivo)
├── google_store_v2.1/
│   ├── RESUMO_ATUALIZACOES_V2.1.md
│   ├── documentacao_tecnica_v2.1_parte3_requisitos.md
│   ├── documentacao_tecnica_v2.1_parte4_modelo_dados.md
│   ├── documentacao_tecnica_v2.1_parte5_roadmap.md
│   ├── documentacao_tecnica_v2.1_parte6_custos.md
│   └── documentacao_tecnica_v2.1_parte7_testes.md
└── [futuros projetos]
```

---

## 🗂️ Projetos Documentados

### **1. @google_Store v2.1 - Sistema de Banco de Referências**

**Diretório:** `google_store_v2.1/`

**Descrição:**  
Sistema RAG-based para gestão de conhecimento usando Google File Search Store. Suporta upload, busca semântica, análise contextual e playbooks automatizados.

**Stack:**  
- Frontend: Next.js 15 + React 19
- Backend: FastAPI (Python 3.12+)
- Database: PostgreSQL 16 (Neon Serverless)
- Cache: Dragonfly (Redis-compatible)
- RAG/LLM: Google Gemini API + File Search
- Orchestration: Temporal
- Observability: Prometheus + Grafana + OpenTelemetry

**Requisitos:**  
- 12 Requisitos Funcionais (RF-01 a RF-12)
- 8 Requisitos Não-Funcionais (RNF-01 a RNF-08)

**Roadmap:**  
- Fase 1: MVP (8 semanas) - Core + Versionamento + Backup + Custos
- Fase 2: Beta (12 semanas) - Playbooks + Filtros + Feedback + Métricas
- Fase 3: Produção (16+ semanas) - Exportação + Dashboard + Avaliação de pgvector

**Custos Estimados:**  
- MVP: $50-$100/mês (100 usuários)
- Beta: $300-$500/mês (1.000 usuários)
- Produção: $2.000-$5.000/mês (10.000 usuários)

**Arquivos:**
1. `RESUMO_ATUALIZACOES_V2.1.md` - Resumo executivo das mudanças v2.0 → v2.1
2. `documentacao_tecnica_v2.1_parte3_requisitos.md` - 12 RF + 8 RNF detalhados
3. `documentacao_tecnica_v2.1_parte4_modelo_dados.md` - Schema PostgreSQL completo
4. `documentacao_tecnica_v2.1_parte5_roadmap.md` - Roadmap de 3 fases
5. `documentacao_tecnica_v2.1_parte6_custos.md` - Estimativa de custos por fase
6. `documentacao_tecnica_v2.1_parte7_testes.md` - Estratégia de testes (unit, integration, e2e, load)

**Aprendizados:**
- ✅ Análise de riscos evita over-engineering (score ponderado)
- ✅ Roadmap em fases reduz risco e acelera entrega de valor
- ✅ Versionamento de documentos é crítico para rastreabilidade
- ✅ Backup independente do File Search é essencial
- ✅ Monitoramento de custos deve ser MVP, não "nice to have"

**Tags:** `RAG`, `Google File Search`, `PostgreSQL`, `FastAPI`, `Next.js`, `Temporal`, `Dragonfly`

**Status:** ✅ Especificação completa (v2.1)

---

## 🔍 Como Usar Este Banco

### **1. Ao Iniciar um Novo Projeto:**
- Busque projetos similares neste índice
- Leia os aprendizados documentados
- Reutilize templates e frameworks

### **2. Ao Finalizar um Projeto:**
- Crie um novo diretório com o nome do projeto
- Documente especificações, decisões e aprendizados
- Atualize este índice com metadados

### **3. Ao Aplicar o Método ENDFIRST:**
- Consulte o Pilar 7 (Aprendizagem Contínua)
- Use este banco como referência no Pilar 3 (Calibração com a Realidade)
- Documente casos de uso para futura consulta

---

## 📊 Estatísticas

- **Total de Projetos:** 1
- **Total de Arquivos:** 6
- **Última Adição:** @google_Store v2.1 (19/12/2025)

---

**Este banco cresce com cada aplicação do método ENDFIRST!** 🚀
