## 5. Segurança, Deploy e Infraestrutura

### 5.1 Segurança

A segurança é um pilar fundamental do sistema, com múltiplas camadas de proteção.

| Camada | Medida de Segurança |
|---|---|
| **Autenticação** | Autenticação baseada em token JWT (JSON Web Token). Supabase Auth será utilizado para gerenciamento de usuários e emissão de tokens. |
| **Autorização** | Acesso a projetos e documentos é controlado por políticas de Row-Level Security (RLS) no PostgreSQL, garantindo que um usuário só possa acessar seus próprios dados. |
| **Criptografia** | Todos os dados são criptografados em trânsito (TLS 1.3) e em repouso (padrão de criptografia do Google Cloud e Supabase). |
| **Segredos** | Chaves de API e outros segredos são gerenciados através de um serviço de gerenciamento de segredos (como Google Secret Manager ou Doppler) e nunca são expostos no código-fonte. |
| **Prevenção de Ataques** | A API do backend deve incluir proteções contra ataques comuns da OWASP Top 10, como SQL Injection (prevenido por ORM), XSS (prevenido por frameworks de frontend modernos) e CSRF. |
| **Auditoria** | Todas as ações críticas (login, upload, delete) são registradas em logs de auditoria para rastreabilidade. |

### 5.2 Estratégia de Deploy

O deploy será automatizado através de um pipeline de CI/CD (Continuous Integration/Continuous Deployment).

**Frontend (Next.js):**
- **Plataforma:** Vercel
- **Workflow:**
  1. Desenvolvedor faz push para o repositório Git (GitHub).
  2. Vercel detecta o push e inicia um novo build.
  3. Testes de unidade e integração são executados.
  4. Se os testes passarem, o build é feito e o deploy é realizado automaticamente.
  5. Vercel fornece um preview do deploy para cada pull request.

**Backend (FastAPI):**
- **Plataforma:** Railway ou Fly.io
- **Workflow:**
  1. Desenvolvedor faz push para o repositório Git.
  2. GitHub Actions (ou similar) inicia o pipeline de CI/CD.
  3. Imagem Docker é construída.
  4. Testes são executados dentro do container.
  5. Imagem é enviada para um container registry (ex: Google Artifact Registry).
  6. Railway/Fly.io faz o deploy da nova imagem sem downtime (blue-green deployment).

### 5.3 Infraestrutura

A infraestrutura será baseada em serviços gerenciados para minimizar a carga operacional.

| Componente | Serviço Gerenciado |
|---|---|
| **Frontend** | Vercel |
| **Backend** | Railway / Fly.io |
| **Banco de Dados** | Supabase (PostgreSQL) |
| **Cache** | Upstash (Redis) |
| **RAG/LLM** | Google Gemini API |
| **Armazenamento de Arquivos** | Google File Search |
| **Repositório de Código** | GitHub |
| **CI/CD** | Vercel (frontend), GitHub Actions (backend) |

### 5.4 Monitoramento e Observabilidade

- **Monitoramento de Performance:** Ferramentas como Sentry (para frontend e backend) e o dashboard da Vercel/Railway serão usadas para monitorar a performance da aplicação e identificar gargalos.
- **Logging:** Logs de aplicação serão centralizados em um serviço como o Google Cloud Logging ou Logtail para facilitar a busca e análise.
- **Alertas:** Alertas serão configurados para notificar a equipe de desenvolvimento em caso de erros críticos, picos de latência ou indisponibilidade do sistema.
