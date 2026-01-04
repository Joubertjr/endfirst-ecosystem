# 📋 Inventário de Serviços e APIs - ENDFIRST

**Versão:** 1.0  
**Data:** 4 de Janeiro de 2026  
**Status:** ✅ Ativo

---

## 🎯 OBJETIVO

Este documento mantém o **inventário completo** de todos os serviços e APIs disponíveis no ecossistema ENDFIRST, garantindo que não perdemos o controle do que temos disponível.

**⚠️ IMPORTANTE:** Este é um documento VIVO. Deve ser atualizado sempre que:
- Novo serviço/API é criado
- Serviço/API é deprecado
- Script é transformado em API
- OLA é criado ou atualizado

---

## 📊 RESUMO EXECUTIVO

**Total de Serviços:** 2  
**Total de APIs:** 16 endpoints  
**Total de OLAs:** 2  
**Scripts Transformados em API:** 2

---

## 🔧 SERVIÇOS DISPONÍVEIS

### 1. Serviço de Upload de Documentos

**Status:** ✅ Ativo  
**Versão:** 1.0  
**Data de Criação:** 4 de Janeiro de 2026

**Vinculação:**
- **Projeto:** ENDFIRST Method v11.6
- **Subprojeto:** Banco de Referências
- **Produto:** Sistema RAG

**Endpoints:**
- `POST /api/v1/documents` - Upload individual
- `POST /api/v1/documents/bulk` - Upload em lote
- `GET /api/v1/documents` - Listar documentos
- `GET /api/v1/documents/{id}` - Obter documento
- `DELETE /api/v1/documents/{id}` - Deletar documento

**Service:** `app/services/document_service.py`  
**Schemas:** `app/schemas/document.py`  
**OLA:** `INTEGRACOES/OLA_UPLOAD_SERVICE_v1.md`

**Script Substituído:**
- ❌ `BANCO_REFERENCIAS/scripts/popular_banco_fase2.py` (removido em 4/01/2026)

**Características:**
- ✅ Funcionalidade dentro do software
- ✅ Endpoint de API reutilizável
- ✅ Documentado com OpenAPI/Swagger
- ✅ Suporta upload individual e em lote
- ✅ Agent-first (pode ser consumido por agentes)

---

### 2. Serviço de Validação de Fases (Manus)

**Status:** ✅ Ativo  
**Versão:** 1.0  
**Data de Criação:** 4 de Janeiro de 2026

**Vinculação:**
- **Projeto:** ENDFIRST Method v11.6
- **Subprojeto:** Banco de Referências
- **Produto:** Sistema de Validação Automática

**Endpoints:**
- `POST /api/v1/manus-validation/package` - Gerar pacote de validação
- `POST /api/v1/manus-validation/submit` - Enviar para Manus API
- `GET /api/v1/manus-validation/{id}/status` - Verificar status
- `GET /api/v1/manus-validation/{id}/resultado` - Obter resultado
- ⭐ `POST /api/v1/manus-validation/complete` - **Validação completa (agent-first)**

**Service:** `app/services/validation_service.py`  
**Schemas:** `app/schemas/validation.py`  
**OLA:** `INTEGRACOES/OLA_MANUS_VALIDATION_v1.md`

**Scripts Substituídos:**
- ❌ `scripts/gerar_pacote_validacao.py` (removido em 4/01/2026)
- ❌ `scripts/enviar_para_manus.py` (removido em 4/01/2026)
- ❌ `scripts/aguardar_validacao.py` (removido em 4/01/2026)
- ❌ `scripts/processar_resultado.py` (removido em 4/01/2026)
- ❌ `scripts/validar_fase.sh` (removido em 4/01/2026)

**Características:**
- ✅ Funcionalidade dentro do software
- ✅ Endpoint agent-first (`/complete`)
- ✅ Polling automático integrado
- ✅ Resposta padronizada
- ✅ Documentado com OpenAPI/Swagger

---

## 📚 TODAS AS APIs DISPONÍVEIS

### APIs do Banco de Referências

**Base URL:** `http://localhost:8000/api/v1`

| Endpoint | Método | Descrição | Status |
|----------|--------|-----------|--------|
| `/documents` | POST | Upload individual | ✅ Ativo |
| `/documents/bulk` | POST | Upload em lote | ✅ Ativo |
| `/documents` | GET | Listar documentos | ✅ Ativo |
| `/documents/{id}` | GET | Obter documento | ✅ Ativo |
| `/documents/{id}` | DELETE | Deletar documento | ✅ Ativo |
| `/search` | POST | Busca semântica | ✅ Ativo |
| `/references` | * | Gestão de referências | ✅ Ativo |
| `/projects` | * | Gestão de projetos | ✅ Ativo |
| `/playbooks` | * | Gestão de playbooks | ✅ Ativo |
| `/analysis` | * | Análises | ✅ Ativo |
| `/ontology` | * | Ontologias | ✅ Ativo |
| `/validation` | * | Validação humana | ✅ Ativo |
| `/manus-validation/package` | POST | Gerar pacote | ✅ Ativo |
| `/manus-validation/submit` | POST | Enviar para Manus | ✅ Ativo |
| `/manus-validation/{id}/status` | GET | Verificar status | ✅ Ativo |
| `/manus-validation/{id}/resultado` | GET | Obter resultado | ✅ Ativo |
| ⭐ `/manus-validation/complete` | POST | **Validação completa** | ✅ Ativo |

**Total:** 16+ endpoints

---

## 📜 SCRIPTS LEGADOS (Avaliar)

### Scripts de Organização e Manutenção

Estes scripts são para **manutenção do projeto**, não para funcionalidades de negócio. Podem permanecer como scripts, mas devem ser avaliados:

| Script | Propósito | Deve virar API? | Status |
|--------|-----------|-----------------|--------|
| `limpar_raiz_projeto.py` | Limpar raiz do projeto | ❌ Não (manutenção) | ✅ Manter |
| `organizar_projeto_completo.sh` | Organizar projeto | ❌ Não (manutenção) | ✅ Manter |
| `executar_todos_testes.sh` | Executar testes | ❌ Não (CI/CD) | ✅ Manter |
| `testar_limpeza_raiz.py` | Testar limpeza | ❌ Não (teste) | ✅ Manter |
| `testar_organizacao_completa.sh` | Testar organização | ❌ Não (teste) | ✅ Manter |
| `testar_deploy_completo.sh` | Testar deploy | ❌ Não (CI/CD) | ✅ Manter |
| `release.sh` | Release | ❌ Não (CI/CD) | ✅ Manter |

**Decisão:** Scripts de manutenção, testes e CI/CD podem permanecer como scripts. Apenas funcionalidades de negócio devem ser APIs.

---

## 🔄 HISTÓRICO DE TRANSFORMAÇÕES

### Scripts Transformados em API

| Data | Script Removido | API Criada | Status |
|------|-----------------|------------|--------|
| 4/01/2026 | `popular_banco_fase2.py` | `POST /api/v1/documents/bulk` | ✅ Completo |
| 4/01/2026 | `gerar_pacote_validacao.py` | `POST /api/v1/manus-validation/package` | ✅ Completo |
| 4/01/2026 | `enviar_para_manus.py` | `POST /api/v1/manus-validation/submit` | ✅ Completo |
| 4/01/2026 | `aguardar_validacao.py` | `GET /api/v1/manus-validation/{id}/status` | ✅ Completo |
| 4/01/2026 | `processar_resultado.py` | `GET /api/v1/manus-validation/{id}/resultado` | ✅ Completo |
| 4/01/2026 | `validar_fase.sh` | `POST /api/v1/manus-validation/complete` | ✅ Completo |

---

## 📋 OLAs (Operational Level Agreements)

### OLAs Ativos

| OLA | Versão | Status | Data |
|-----|--------|--------|------|
| `OLA_UPLOAD_SERVICE_v1.md` | 1.0 | ✅ Ativo | 4/01/2026 |
| `OLA_MANUS_VALIDATION_v1.md` | 1.0 | ✅ Ativo | 4/01/2026 |

---

## 🔗 VINCULAÇÃO DE SERVIÇOS

### Regra Obrigatória

**⚠️ TODO serviço DEVE estar vinculado a:**
- **Projeto:** Projeto principal (obrigatório)
- **Subprojeto:** Subprojeto dentro do projeto (opcional)
- **Produto:** Produto específico dentro do subprojeto (opcional)

### Hierarquia de Vinculação

```
Projeto (ENDFIRST Method v11.6)
  └── Subprojeto (Banco de Referências)
      └── Produto (Sistema RAG, Sistema de Validação, etc.)
          └── Serviço/API
```

### Exemplos de Vinculação

**Serviço de Upload:**
- Projeto: ENDFIRST Method v11.6
- Subprojeto: Banco de Referências
- Produto: Sistema RAG

**Serviço de Validação:**
- Projeto: ENDFIRST Method v11.6
- Subprojeto: Banco de Referências
- Produto: Sistema de Validação Automática

---

## 🎯 PRINCÍPIOS DE GOVERNANÇA

### 1. Agent-First
- ✅ Todos os serviços devem ser consumíveis por agentes
- ✅ Endpoints "complete" para fluxos inteiros
- ✅ Respostas padronizadas e claras

### 2. Contrato Formal (OLA)
- ✅ Cada serviço público deve ter um OLA
- ✅ OLA define interface, garantias e responsabilidades
- ✅ Versionamento documentado

### 3. Vinculação Obrigatória
- ✅ Todo serviço deve estar vinculado a Projeto/Subprojeto/Produto
- ✅ Vinculação deve ser documentada em todos os inventários
- ✅ Facilita rastreabilidade e organização

### 4. Inventário Atualizado
- ✅ Este documento deve ser atualizado sempre que:
  - Novo serviço é criado
  - Script é transformado em API
  - Serviço é deprecado
  - OLA é criado ou atualizado
  - Vinculação muda

### 5. Documentação Completa
- ✅ OpenAPI/Swagger para todas as APIs
- ✅ Exemplos de uso por agentes
- ✅ Schemas Pydantic bem definidos

---

## 📝 PROCESSO DE ADIÇÃO DE NOVO SERVIÇO

### Passo 1: Criar API

1. Criar schema em `app/schemas/<nome>.py`
2. Criar service em `app/services/<nome>_service.py`
3. Criar endpoint em `app/api/v1/endpoints/<nome>.py`
4. Adicionar ao router em `app/api/v1/router.py`

### Passo 2: Criar OLA

1. Criar `INTEGRACOES/OLA_<NOME>_SERVICE_v1.md`
2. Documentar interface, garantias e responsabilidades

### Passo 3: Atualizar Inventário

1. Adicionar serviço a este documento
2. Atualizar estatísticas
3. Documentar scripts substituídos (se houver)

### Passo 4: Documentar

1. Adicionar ao `README_SERVICOS.md`
2. Atualizar OpenAPI/Swagger (automático)
3. Criar exemplos de uso

---

## 🚨 SCRIPTS A AVALIAR

### Scripts que PODEM virar API (se necessário)

Nenhum no momento. Todos os scripts restantes são de manutenção/CI/CD.

---

## ✅ CHECKLIST DE GOVERNANÇA

Antes de considerar um serviço completo:

- [ ] API criada no backend (não script)
- [ ] Service layer implementado
- [ ] Schemas Pydantic criados
- [ ] Endpoints documentados (OpenAPI/Swagger)
- [ ] OLA criado (se serviço público)
- [ ] Inventário atualizado (este documento)
- [ ] README_SERVICOS.md atualizado
- [ ] Exemplos de uso por agentes documentados
- [ ] Testes criados (opcional, mas recomendado)

---

## 📊 MÉTRICAS

**Última atualização:** 4 de Janeiro de 2026

- **Total de Serviços:** 2
- **Total de APIs:** 16+ endpoints
- **Total de OLAs:** 2
- **Scripts Transformados:** 6
- **Scripts Legados (manutenção):** 7

---

## 🔗 REFERÊNCIAS

- **APIs:** http://localhost:8000/api/docs
- **OLAs:** `BANCO_REFERENCIAS/INTEGRACOES/`
- **Documentação:** `scripts/README_SERVICOS.md`
- **Cursor Rules:** `BANCO_REFERENCIAS/.cursorrules`

---

**Última atualização:** 4 de Janeiro de 2026

