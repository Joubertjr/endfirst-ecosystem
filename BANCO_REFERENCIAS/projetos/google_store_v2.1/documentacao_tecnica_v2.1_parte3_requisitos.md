_This is a large model so I will generate the content in multiple steps. First, I will generate the content for the file `documentacao_tecnica_v2.1_parte3_requisitos.md`. Then, I will generate the content for the file `documentacao_tecnica_v2.1_parte4_roadmap.md`. Then, I will generate the content for the file `documentacao_tecnica_v2.1_parte5_custos.md`. Then, I will generate the content for the file `documentacao_tecnica_v2.1_parte6_testes.md`. Finally, I will generate the content for the file `DOCUMENTACAO_TECNICA_COMPLETA_V2.1.md` by concatenating all the parts. This is the content for the file `documentacao_tecnica_v2.1_parte3_requisitos.md`: "## 3. REQUISITOS DO SISTEMA (v2.1)

### 3.1 Requisitos Funcionais (RF)

| ID | Requisito | Descrição | Prioridade | Fase |
|---|---|---|---|---|
| **RF-01** | Gerenciamento de Projetos | Usuário pode criar, listar, editar e deletar projetos. Cada projeto é um Banco de Referências isolado. | 🔴 CRÍTICA | MVP |
| **RF-02** | Gerenciamento de Documentos | Usuário pode fazer upload, listar, deletar e visualizar documentos dentro de um projeto. | 🔴 CRÍTICA | MVP |
| **RF-03** | Consulta Semântica (RAG) | Usuário pode fazer perguntas em linguagem natural e receber respostas contextualizadas baseadas nos documentos do projeto. | 🔴 CRÍTICA | MVP |
| **RF-04** | Citação de Fontes | O sistema DEVE citar os documentos e trechos específicos que foram usados para gerar a resposta. | 🔴 CRÍTICA | MVP |
| **RF-05** | Gerenciamento de Playbooks | Usuário pode criar, editar e usar templates de análise (playbooks) para consultas recorrentes. | 🟡 IMPORTANTE | Fase 2 |
| **RF-06** | Gerenciamento de Usuários | Autenticação e autorização de usuários (via Clerk). | 🔴 CRÍTICA | MVP |
| **RF-07** | Versionamento de Análises | O sistema DEVE manter um histórico de todas as análises realizadas, permitindo que o usuário as revise. | 🟡 IMPORTANTE | Fase 2 |
| **RF-08** | Filtros Avançados | Usuário pode filtrar documentos por metadados (autor, data), categoria, tags e status (rascunho/final/obsoleto). | 🟡 IMPORTANTE | Fase 2 |
| **RF-09** | Exportação de Resultados | Usuário pode exportar os resultados de uma análise para Markdown ou PDF. | 🟢 NICE-TO-HAVE | Fase 3 |
| **RF-10** | Dashboard de Projeto | Usuário pode visualizar um dashboard com estatísticas de uso do projeto (nº de docs, análises, etc.). | 🟢 NICE-TO-HAVE | Fase 3 |
| **RF-11** | **Versionamento de Documentos** | O sistema DEVE manter um histórico de versões de cada documento. Análises DEVEM referenciar a versão específica do documento. | 🔴 CRÍTICA | MVP |
| **RF-12** | **Feedback e Métricas de Qualidade** | Usuário PODE avaliar a qualidade das análises (1-5 estrelas). O sistema DEVE rastrear a taxa de sucesso por playbook. | 🟡 IMPORTANTE | Fase 2 |

### 3.2 Requisitos Não-Funcionais (RNF)

| ID | Requisito | Descrição | Métrica de Sucesso |
|---|---|---|---|
| **RNF-01** | Performance | O sistema deve ser rápido e responsivo. | P95 de latência de consulta RAG < 5 segundos. |
| **RNF-02** | Escalabilidade | O sistema deve suportar um grande número de usuários e documentos. | Suporte a 10.000 usuários ativos e 1TB de documentos por projeto. |
| **RNF-03** | Disponibilidade | O sistema deve estar disponível e acessível. | 99.9% de uptime mensal. |
| **RNF-04** | Segurança | O sistema deve ser seguro e proteger os dados dos usuários. | Conformidade com OWASP Top 10; zero vulnerabilidades críticas em testes de penetração. |
| **RNF-05** | Manutenibilidade | O código deve ser limpo, bem documentado e fácil de manter. | Cobertura de testes > 80%; Code Climate score > 3.5. |
| **RNF-06** | Usabilidade | A interface deve ser intuitiva e fácil de usar. | Taxa de sucesso de tarefas > 95% em testes de usabilidade; NPS > 50. |
| **RNF-07** | **Backup e Recuperação** | O sistema DEVE manter cópia de backup de todos os documentos em storage separado do File Search. | RPO < 1 hora; RTO < 24 horas. |
| **RNF-08** | **Monitoramento de Custos** | O sistema DEVE rastrear custos por serviço e enviar alertas quando limites forem atingidos. | Alertas configuráveis; dashboard de custos em tempo real. |

### 3.3 Regras de Negócio (RN)

| ID | Regra | Descrição |
|---|---|---|
| **RN-01** | Isolamento de Dados | Os dados de um projeto (documentos, análises) são completamente isolados e não podem ser acessados por outros projetos. |
| **RN-02** | Limites de Upload | Cada documento pode ter no máximo 100MB. Cada projeto pode ter no máximo 1TB de documentos. |
| **RN-03** | Tipos de Arquivo | O sistema suporta os seguintes tipos de arquivo: PDF, TXT, MD, DOCX, PPTX. |
| **RN-04** | Análises Assíncronas | Todas as análises são executadas em background jobs para não bloquear a interface do usuário. |
| **RN-05** | Curadoria de Conteúdo | Apenas documentos marcados como 
