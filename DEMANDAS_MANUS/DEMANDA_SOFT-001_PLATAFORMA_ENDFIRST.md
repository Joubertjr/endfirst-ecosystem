---
demanda_id: DEMANDA-SOFT-001
title: Plataforma END-FIRST (Interface Visual)
type: software / plataforma
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-SOFT-001 — Plataforma END-FIRST (Interface Visual)

**Tipo:** Software / Plataforma  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existe um software em Docker que permite executar o método END-FIRST via interface visual estilo chat
- ✅ O software tem histórico persistente, múltiplas personas e rastreabilidade completa
- ✅ O software consome `/METODO/` do repositório `endfirst-ecosystem`
- ✅ O software sobe via `docker compose up` e executa uma demanda real

**Resultado esperado do sistema:**

> "Existe um software (em Docker) que permite executar o método END-FIRST via interface visual estilo chat, com histórico persistente, múltiplas personas e rastreabilidade completa."

---

## 🚫 Regras Canônicas

**Plataforma END-FIRST:**

> "Plataforma não redefine método. Plataforma consome método. Plataforma que redefine regras é FAIL estrutural."

**Docker Obrigatório:**

> "Software DEVE rodar em Docker. Software sem Docker não é portável."

**Sincronização de Método:**

> "Software DEVE sincronizar `/METODO/` do repositório. Software que não sincroniza método não implementa END-FIRST."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Software sobe via `docker compose up`
- ✅ Interface visual estilo chat funciona
- ✅ Personas configuráveis (CEO, Chefe de Produto, Executor)
- ✅ Banco de dados persiste histórico de interações
- ✅ Login Google funciona
- ✅ Método embarcado (consome `/METODO/`)
- ✅ Sincroniza `/METODO/` do repositório
- ✅ Executa uma demanda real (de ponta a ponta)

### FAIL

- ❌ Software não sobe via Docker
- ❌ Interface não funciona
- ❌ Personas não são configuráveis
- ❌ Histórico não é persistido
- ❌ Login não funciona
- ❌ Método não é embarcado
- ❌ Sincronização não funciona
- ❌ Não executa demanda real

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um software que permita executar o método END-FIRST via interface visual. Isso gera:

1. **Barreira de entrada:** Usuários não técnicos não conseguem usar o método
2. **Falta de histórico:** Não há persistência de interações
3. **Perda de rastreabilidade:** Não há registro de execuções
4. **Impossibilidade de auditoria:** Não é possível auditar execuções

### Impacto

Sem plataforma visual:
- Método é inacessível para não técnicos
- Histórico é perdido
- Rastreabilidade é impossível
- Auditoria é impossível

---

## 🚫 DO / DON'T

### ✅ DO

- **Criar interface estilo chat**
- **Implementar personas configuráveis**
- **Persistir histórico em banco de dados**
- **Implementar login Google**
- **Embarcar método (consumir `/METODO/`)**
- **Sincronizar `/METODO/` do repositório**
- **Executar demanda real de ponta a ponta**

### ❌ DON'T

- **Criar software sem Docker**
- **Criar interface sem histórico**
- **Criar software sem personas**
- **Criar software sem login**
- **Criar software que redefine método**
- **Criar software que não sincroniza método**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- **Depende de:** DEMANDA-METODO-013 (Governança de Software)
- **Depende de:** DEMANDA-METODO-014 (Personas Operacionais)

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. **Docker Compose**
   - `docker-compose.yml`
   - `Dockerfile` (frontend)
   - `Dockerfile` (backend)

2. **Frontend**
   - Interface estilo chat
   - Seleção de persona
   - Histórico de interações

3. **Backend**
   - API REST
   - Autenticação Google
   - Sincronização de `/METODO/`
   - Execução de demandas

4. **Banco de Dados**
   - Modelo de dados
   - Migrations
   - Seeds

### Validações

1. Software sobe via `docker compose up`
2. Interface funciona
3. Personas são configuráveis
4. Histórico é persistido
5. Login funciona
6. Método é embarcado
7. Sincronização funciona
8. Demanda real é executada

---

## ❌ Fora de Escopo

- Criação de produtos específicos (isso será feito em demandas de produto)
- Implementação de features avançadas (isso será feito em demandas futuras)
- Migração de dados existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Plataforma sem Docker não é portável. Plataforma sem método embarcado não implementa END-FIRST. Plataforma sem histórico não é auditável. Plataforma END-FIRST é condição de passagem para qualquer software no método END-FIRST."
