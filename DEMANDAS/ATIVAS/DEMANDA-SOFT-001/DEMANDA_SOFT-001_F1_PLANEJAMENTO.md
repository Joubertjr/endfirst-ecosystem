# F-1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-SOFT-001 — Plataforma END-FIRST (Interface Visual)  
**Versão:** 1.0  
**Data:** 23 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Executor:** Manus  
**Chefe de Produto:** CEO (Joubert Jr)

---

## 🔒 END — ESTADO FINAL ESPERADO (EXATO)

> "Existe um software (em Docker) que permite executar o método END-FIRST via interface visual estilo chat, com histórico persistente, múltiplas personas e rastreabilidade completa."

### Critérios de Aceitação (Binários)

**PASS:**
- ✅ Software sobe via `docker compose up`
- ✅ Interface visual estilo chat funciona
- ✅ Personas configuráveis (CEO, Chefe de Produto, Executor)
- ✅ Banco de dados persiste histórico de interações
- ✅ Login Google funciona
- ✅ Método embarcado (consome `/METODO/`)
- ✅ Sincroniza `/METODO/` do repositório
- ✅ Executa uma demanda real (de ponta a ponta)

**FAIL:**
- ❌ Software não sobe via Docker
- ❌ Interface não funciona
- ❌ Personas não são configuráveis
- ❌ Histórico não é persistido
- ❌ Login não funciona
- ❌ Método não é embarcado
- ❌ Sincronização não funciona
- ❌ Não executa demanda real

---

## 📋 FASES DE EXECUÇÃO

### F1 — Criar Infraestrutura Docker

**END desta fase:**
> "A infraestrutura Docker está criada e o software sobe via `docker compose up`."

**Artefato:**
- `docker-compose.yml`
- `Dockerfile` (frontend)
- `Dockerfile` (backend)

**Critérios de PASS:**
- ✅ `docker-compose.yml` define 3 serviços: frontend, backend, database
- ✅ Frontend roda em Node.js (React/Next.js)
- ✅ Backend roda em Python (FastAPI)
- ✅ Database roda em PostgreSQL
- ✅ `docker compose up` sobe todos os serviços
- ✅ Frontend acessível em `http://localhost:3000`
- ✅ Backend acessível em `http://localhost:8000`
- ✅ Database acessível internamente

---

### F2 — Implementar Interface Estilo Chat

**END desta fase:**
> "A interface estilo chat está implementada e funcional."

**Artefato:**
- Frontend com interface chat
- Componentes React

**Critérios de PASS:**
- ✅ Interface estilo chat implementada
- ✅ Usuário pode enviar mensagens
- ✅ Usuário pode receber respostas
- ✅ Histórico de mensagens é exibido
- ✅ Interface é responsiva
- ✅ Interface tem seleção de persona

---

### F3 — Implementar Personas Configuráveis

**END desta fase:**
> "As personas são configuráveis e o usuário pode alternar entre CEO, Chefe de Produto e Executor."

**Artefato:**
- Sistema de personas no frontend
- API de personas no backend

**Critérios de PASS:**
- ✅ Usuário pode selecionar persona (CEO, Chefe de Produto, Executor)
- ✅ Persona selecionada determina comportamento do sistema
- ✅ Persona é persistida no banco de dados
- ✅ Persona é exibida na interface
- ✅ Persona pode ser alterada a qualquer momento

---

### F4 — Implementar Banco de Dados e Histórico

**END desta fase:**
> "O banco de dados persiste histórico de interações e o histórico é exibido na interface."

**Artefato:**
- Modelo de dados
- Migrations
- API de histórico

**Critérios de PASS:**
- ✅ Modelo de dados criado (users, sessions, messages, personas)
- ✅ Migrations executadas
- ✅ Histórico de interações é persistido
- ✅ Histórico é exibido na interface
- ✅ Histórico é filtrado por sessão

---

### F5 — Implementar Login Google

**END desta fase:**
> "O login Google está implementado e funcional."

**Artefato:**
- Autenticação Google OAuth
- API de autenticação

**Critérios de PASS:**
- ✅ Login Google implementado
- ✅ Usuário pode fazer login com Google
- ✅ Sessão é criada após login
- ✅ Usuário é redirecionado para interface após login
- ✅ Logout funciona

---

### F6 — Embarcar Método e Sincronizar

**END desta fase:**
> "O método está embarcado e o software sincroniza `/METODO/` do repositório."

**Artefato:**
- Sistema de sincronização de método
- API de método

**Critérios de PASS:**
- ✅ Software clona repositório `endfirst-ecosystem`
- ✅ Software lê `/METODO/` do repositório
- ✅ Software sincroniza `/METODO/` periodicamente
- ✅ Método é acessível via API
- ✅ Método é usado para executar demandas

---

### F7 — Executar Demanda Real

**END desta fase:**
> "O software executa uma demanda real de ponta a ponta."

**Artefato:**
- Sistema de execução de demandas
- Evidência de execução

**Critérios de PASS:**
- ✅ Usuário pode criar demanda via interface
- ✅ Usuário pode criar F-1 via interface
- ✅ Usuário pode executar F-1 via interface
- ✅ Software gera artefatos conforme F-1
- ✅ Software registra evidência de execução
- ✅ Demanda é marcada como concluída

---

## 🚫 REGRAS CANÔNICAS

**Plataforma END-FIRST:**
> "Plataforma não redefine método. Plataforma consome método. Plataforma que redefine regras é FAIL estrutural."

**Docker Obrigatório:**
> "Software DEVE rodar em Docker. Software sem Docker não é portável."

**Sincronização de Método:**
> "Software DEVE sincronizar `/METODO/` do repositório. Software que não sincroniza método não implementa END-FIRST."

---

## 🧱 BLOQUEIOS ESTRUTURAIS

### Bloqueios Técnicos
- Nenhum

### Bloqueios de Método
- **Depende de:** DEMANDA-METODO-013 (Governança de Software)
- **Depende de:** DEMANDA-METODO-014 (Personas Operacionais)

### Bloqueios de Governança
- Nenhum

---

## ❌ FORA DE ESCOPO

- Criação de produtos específicos (isso será feito em demandas de produto)
- Implementação de features avançadas (isso será feito em demandas futuras)
- Migração de dados existentes

---

## 📌 STATUS

**Status atual:** Aprovado  
**Próximo passo:** Executar F1

---

## 🧭 REGRA FINAL

> "Plataforma sem Docker não é portável. Plataforma sem método embarcado não implementa END-FIRST. Plataforma sem histórico não é auditável. Plataforma END-FIRST é condição de passagem para qualquer software no método END-FIRST."
