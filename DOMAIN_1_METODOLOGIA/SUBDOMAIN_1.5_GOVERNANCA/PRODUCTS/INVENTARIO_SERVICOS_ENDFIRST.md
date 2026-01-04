# 📋 Inventário de Serviços e APIs - Ecossistema ENDFIRST

**Versão:** 1.0  
**Data:** 4 de Janeiro de 2026  
**Status:** ✅ Ativo

---

## 🎯 OBJETIVO

Este documento mantém o **inventário completo** de todos os serviços e APIs disponíveis em **TODO o ecossistema ENDFIRST**, garantindo que não perdemos o controle do que temos disponível em cada projeto.

**⚠️ IMPORTANTE:** Este é um documento VIVO. Deve ser atualizado sempre que:
- Novo serviço/API é criado em qualquer projeto
- Serviço/API é deprecado
- Script é transformado em API
- Novo projeto com software é adicionado ao ecossistema

---

## 📊 RESUMO EXECUTIVO

**Total de Projetos com Software:** 1  
**Total de Serviços:** 2  
**Total de APIs:** 16+ endpoints  
**Total de OLAs:** 2  
**Scripts Transformados em API:** 6

---

## 🏗️ ESTRUTURA DO ECOSSISTEMA

### Projetos com Software

| Projeto | Tipo | Status | Inventário Local |
|---------|------|--------|-----------------|
| **Banco de Referências** | Sistema RAG | ✅ Ativo | `BANCO_REFERENCIAS/INTEGRACOES/INVENTARIO_SERVICOS.md` |
| **ENDFIRST Flow** | Sistema de Tracking | 🔄 Planejado | - |
| **CLI ENDFIRST** | CLI Tool | 🔄 Planejado | - |

---

## 🔧 SERVIÇOS POR PROJETO

### 1. Banco de Referências (BANCO_REFERENCIAS)

**Status:** ✅ Ativo  
**Tecnologias:** FastAPI, PostgreSQL, Redis, Next.js, Google Gemini  
**Base URL:** `http://localhost:8000/api/v1`

#### Serviços Disponíveis

##### 1.1. Serviço de Upload de Documentos

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

**Service:** `BANCO_REFERENCIAS/backend/app/services/document_service.py`  
**Schemas:** `BANCO_REFERENCIAS/backend/app/schemas/document.py`  
**OLA:** `BANCO_REFERENCIAS/INTEGRACOES/OLA_UPLOAD_SERVICE_v1.md`

**Script Substituído:**
- ❌ `BANCO_REFERENCIAS/scripts/popular_banco_fase2.py` (removido em 4/01/2026)

**Características:**
- ✅ Funcionalidade dentro do software
- ✅ Endpoint de API reutilizável
- ✅ Documentado com OpenAPI/Swagger
- ✅ Suporta upload individual e em lote
- ✅ Agent-first (pode ser consumido por agentes)

---

##### 1.2. Serviço de Validação de Fases (Manus)

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

**Service:** `BANCO_REFERENCIAS/backend/app/services/validation_service.py`  
**Schemas:** `BANCO_REFERENCIAS/backend/app/schemas/validation.py`  
**OLA:** `BANCO_REFERENCIAS/INTEGRACOES/OLA_MANUS_VALIDATION_v1.md`

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

#### Outras APIs do Banco de Referências

**Base URL:** `http://localhost:8000/api/v1`

| Endpoint | Método | Descrição | Status |
|----------|--------|-----------|--------|
| `/search` | POST | Busca semântica | ✅ Ativo |
| `/references` | * | Gestão de referências | ✅ Ativo |
| `/projects` | * | Gestão de projetos | ✅ Ativo |
| `/playbooks` | * | Gestão de playbooks | ✅ Ativo |
| `/analysis` | * | Análises | ✅ Ativo |
| `/ontology` | * | Ontologias | ✅ Ativo |
| `/validation` | * | Validação humana | ✅ Ativo |
| `/api-keys` | * | Gestão de API Keys | ✅ Ativo |
| `/training` | * | Treinamento | ✅ Ativo |
| `/metrics` | * | Métricas | ✅ Ativo |
| `/fine-tuning` | * | Fine-tuning | ✅ Ativo |
| `/models/cards` | * | Model Cards | ✅ Ativo |
| `/feedback` | * | Feedback de usuários | ✅ Ativo |

**Total:** 16+ endpoints

**Documentação:** http://localhost:8000/api/docs

---

### 2. ENDFIRST Flow

**Status:** 🔄 Planejado  
**Tipo:** Sistema de Tracking de Projetos  
**Inventário:** A ser criado quando implementado

---

### 3. CLI ENDFIRST (endfirst-cli)

**Status:** 🔄 Planejado  
**Tipo:** CLI Tool para Governança  
**Inventário:** A ser criado quando implementado

---

## 📜 SCRIPTS LEGADOS (Avaliar)

### Scripts de Organização e Manutenção (Raiz)

Estes scripts são para **manutenção do projeto**, não para funcionalidades de negócio. Podem permanecer como scripts:

| Script | Propósito | Deve virar API? | Status |
|--------|-----------|-----------------|--------|
| `scripts/limpar_raiz_projeto.py` | Limpar raiz do projeto | ❌ Não (manutenção) | ✅ Manter |
| `scripts/organizar_projeto_completo.sh` | Organizar projeto | ❌ Não (manutenção) | ✅ Manter |
| `scripts/executar_todos_testes.sh` | Executar testes | ❌ Não (CI/CD) | ✅ Manter |
| `scripts/testar_limpeza_raiz.py` | Testar limpeza | ❌ Não (teste) | ✅ Manter |
| `scripts/testar_organizacao_completa.sh` | Testar organização | ❌ Não (teste) | ✅ Manter |
| `scripts/testar_deploy_completo.sh` | Testar deploy | ❌ Não (CI/CD) | ✅ Manter |
| `scripts/release.sh` | Release | ❌ Não (CI/CD) | ✅ Manter |

**Decisão:** Scripts de manutenção, testes e CI/CD podem permanecer como scripts. Apenas funcionalidades de negócio devem ser APIs.

---

## 🔄 HISTÓRICO DE TRANSFORMAÇÕES

### Scripts Transformados em API

| Data | Projeto | Script Removido | API Criada | Status |
|------|---------|-----------------|------------|--------|
| 4/01/2026 | Banco de Referências | `popular_banco_fase2.py` | `POST /api/v1/documents/bulk` | ✅ Completo |
| 4/01/2026 | Banco de Referências | `gerar_pacote_validacao.py` | `POST /api/v1/manus-validation/package` | ✅ Completo |
| 4/01/2026 | Banco de Referências | `enviar_para_manus.py` | `POST /api/v1/manus-validation/submit` | ✅ Completo |
| 4/01/2026 | Banco de Referências | `aguardar_validacao.py` | `GET /api/v1/manus-validation/{id}/status` | ✅ Completo |
| 4/01/2026 | Banco de Referências | `processar_resultado.py` | `GET /api/v1/manus-validation/{id}/resultado` | ✅ Completo |
| 4/01/2026 | Banco de Referências | `validar_fase.sh` | `POST /api/v1/manus-validation/complete` | ✅ Completo |

---

## 📋 OLAs (Operational Level Agreements)

### OLAs Ativos

| OLA | Projeto | Versão | Status | Data |
|-----|---------|--------|--------|------|
| `OLA_UPLOAD_SERVICE_v1.md` | Banco de Referências | 1.0 | ✅ Ativo | 4/01/2026 |
| `OLA_MANUS_VALIDATION_v1.md` | Banco de Referências | 1.0 | ✅ Ativo | 4/01/2026 |

**Localização:** `BANCO_REFERENCIAS/INTEGRACOES/`

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

### 3. Inventário Hierárquico
- ✅ Inventário geral na raiz (`GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`)
- ✅ Inventário específico em cada projeto (`<PROJETO>/INTEGRACOES/INVENTARIO_SERVICOS.md`)
- ✅ Ambos devem ser atualizados

### 4. Documentação Completa
- ✅ OpenAPI/Swagger para todas as APIs
- ✅ Exemplos de uso por agentes
- ✅ Schemas Pydantic bem definidos

---

## 📝 PROCESSO DE ADIÇÃO DE NOVO PROJETO COM SOFTWARE

### Passo 1: Criar Estrutura do Projeto

1. Criar diretório do projeto
2. Criar `INTEGRACOES/` dentro do projeto
3. Criar `INTEGRACOES/INVENTARIO_SERVICOS.md` (inventário local)

### Passo 2: Atualizar Inventário Geral

1. Adicionar projeto a este documento (seção "Projetos com Software")
2. Atualizar estatísticas
3. Linkar para inventário local

### Passo 3: Seguir Processo de Criação de Serviço

Ver: `GOVERNANCA/PROCESSO_GOVERNANCA_SERVICOS.md`

---

## 🔗 VINCULAÇÃO DE SERVIÇOS

### Regra Obrigatória

**⚠️ TODO serviço DEVE estar vinculado a:**
- **Projeto:** Projeto principal (ex: ENDFIRST Method v11.6)
- **Subprojeto:** (Opcional) Subprojeto dentro do projeto (ex: Banco de Referências)
- **Produto:** (Opcional) Produto específico dentro do subprojeto

### Formato de Vinculação

Cada serviço deve ter seção "Vinculação" com:
- **Projeto:** Nome do projeto principal
- **Subprojeto:** Nome do subprojeto (se aplicável)
- **Produto:** Nome do produto (se aplicável)

### Exemplos

**Serviço do Banco de Referências:**
- Projeto: ENDFIRST Method v11.6
- Subprojeto: Banco de Referências
- Produto: Sistema RAG

**Serviço do ENDFIRST Flow (futuro):**
- Projeto: ENDFIRST Method v11.6
- Subprojeto: ENDFIRST Flow
- Produto: Sistema de Tracking

---

## ✅ CHECKLIST DE GOVERNANÇA

Antes de considerar um serviço completo:

- [ ] API criada no backend (não script)
- [ ] Service layer implementado
- [ ] Schemas Pydantic criados
- [ ] Endpoints documentados (OpenAPI/Swagger)
- [ ] OLA criado (se serviço público)
- [ ] Inventário local atualizado (`<PROJETO>/INTEGRACOES/INVENTARIO_SERVICOS.md`)
- [ ] Inventário geral atualizado (este documento)
- [ ] README_SERVICOS.md atualizado (se aplicável)
- [ ] Exemplos de uso por agentes documentados
- [ ] Testes criados (opcional, mas recomendado)

---

## 📊 MÉTRICAS

**Última atualização:** 4 de Janeiro de 2026

- **Total de Projetos com Software:** 1
- **Total de Serviços:** 2
- **Total de APIs:** 16+ endpoints
- **Total de OLAs:** 2
- **Scripts Transformados:** 6
- **Scripts Legados (manutenção):** 7

---

## 🔗 REFERÊNCIAS

- **Processo de Governança:** `GOVERNANCA/PROCESSO_GOVERNANCA_SERVICOS.md`
- **Método ENDFIRST:** `METODO/processos/PROCESSO_XX_GOVERNANCA_SERVICOS.md`
- **Banco de Referências - Inventário:** `BANCO_REFERENCIAS/INTEGRACOES/INVENTARIO_SERVICOS.md`
- **Banco de Referências - OLAs:** `BANCO_REFERENCIAS/INTEGRACOES/OLA_*.md`
- **API Docs:** http://localhost:8000/api/docs

---

**Última atualização:** 4 de Janeiro de 2026

