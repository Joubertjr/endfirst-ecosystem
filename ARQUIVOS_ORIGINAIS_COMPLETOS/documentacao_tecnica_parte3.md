## 3. Requisitos do Sistema

### 3.1 Requisitos Funcionais

| ID | Requisito | Descrição | Prioridade |
|---|---|---|---|
| **RF-01** | Gerenciamento de Projetos | Usuário deve poder criar, listar, editar e deletar projetos. Cada projeto é um container isolado para um Banco de Referências. | Essencial |
| **RF-02** | Gerenciamento de Documentos | Usuário deve poder fazer upload, listar e deletar documentos dentro de um projeto. | Essencial |
| **RF-03** | Consulta Semântica (RAG) | Usuário deve poder fazer uma consulta em linguagem natural e receber uma resposta contextualizada, baseada nos documentos do projeto. | Essencial |
| **RF-04** | Citação de Fontes | A resposta da IA deve incluir citações que indiquem quais documentos e trechos foram usados para gerar a resposta. | Essencial |
| **RF-05** | Gerenciamento de Templates | Administrador deve poder criar e gerenciar templates de análise, que são prompts pré-definidos para consultas comuns. | Alta |
| **RF-06** | Gerenciamento de Usuários | Sistema deve suportar autenticação e autorização de usuários. | Essencial |
| **RF-07** | Versionamento de Análises | Sistema deve salvar o histórico de análises (consulta + resposta) para rastreabilidade e comparação. | Alta |
| **RF-08** | Filtro por Metadados | Usuário deve poder filtrar a busca por metadados customizáveis dos documentos (ex: autor, ano, categoria). | Média |
| **RF-09** | Exportação de Resultados | Usuário deve poder exportar os resultados de uma análise em formato Markdown ou PDF. | Média |
| **RF-10** | Dashboard de Projeto | Cada projeto deve ter um dashboard com estatísticas de uso (nº de documentos, consultas, etc.). | Baixa |

### 3.2 Requisitos Não-Funcionais

| ID | Requisito | Descrição | Métrica de Sucesso |
|---|---|---|---|
| **RNF-01** | Performance | A latência de ponta a ponta para uma consulta RAG deve ser baixa. | P95 < 5 segundos |
| **RNF-02** | Escalabilidade | O sistema deve suportar um aumento no número de usuários, projetos e documentos sem degradação de performance. | Suporte a 10.000 usuários concorrentes e 1 TB de dados por projeto. |
| **RNF-03** | Disponibilidade | O sistema deve estar disponível e operacional a maior parte do tempo. | 99.9% de uptime (menos de 8.76 horas de downtime por ano). |
| **RNF-04** | Segurança | Todos os dados devem ser criptografados em trânsito e em repouso. O acesso deve ser controlado por autenticação e autorização. | Passar em testes de penetração (pentests) e seguir as melhores práticas da OWASP. |
| **RNF-05** | Manutenibilidade | O código deve ser limpo, bem documentado e testado para facilitar a manutenção e evolução do sistema. | Cobertura de testes > 80%, pontuação de Code Quality > A (SonarQube). |
| **RNF-06** | Usabilidade | A interface do usuário deve ser intuitiva e fácil de usar. | Taxa de sucesso de tarefas do usuário > 95% em testes de usabilidade. |

### 3.3 Regras de Negócio

- **RN-01:** Cada projeto tem seu próprio `FileSearchStore` no Google Gemini API, garantindo isolamento total dos dados.
- **RN-02:** O tamanho máximo de um documento para upload é de 100 MB.
- **RN-03:** O armazenamento total por projeto é limitado pelo tier do Google File Search (começando com 1 GB no tier gratuito).
- **RN-04:** Apenas o administrador do projeto pode deletar o projeto ou gerenciar templates.
- **RN-05:** Todas as chamadas para a API do backend devem ser autenticadas com um token JWT.
