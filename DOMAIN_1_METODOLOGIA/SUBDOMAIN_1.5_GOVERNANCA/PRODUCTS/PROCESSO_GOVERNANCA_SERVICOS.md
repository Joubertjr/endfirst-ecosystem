# 🔄 Processo de Governança de Serviços - Ecossistema ENDFIRST

**Código:** PROCESSO_GOVERNANCA_SERVICOS  
**Versão:** 1.0  
**Data:** 4 de Janeiro de 2026  
**Objetivo:** Padronizar a criação, manutenção e governança de serviços e APIs em TODO o ecossistema ENDFIRST

---

## 🎯 OBJETIVO

Este processo define como criar, manter e governar serviços e APIs em **TODO o ecossistema ENDFIRST**, garantindo que:
- Não perdemos o controle do inventário
- Scripts são transformados em APIs quando apropriado
- Serviços seguem padrões estabelecidos
- Documentação está sempre atualizada
- Cada projeto mantém seu próprio inventário
- Inventário geral está sempre atualizado

---

## 📋 PRINCÍPIOS FUNDAMENTAIS

### 1. Agent-First
- ✅ Todos os serviços devem ser consumíveis por agentes de IA
- ✅ Endpoints "complete" para fluxos inteiros
- ✅ Respostas padronizadas e claras

### 2. APIs, NÃO Scripts
- ❌ NUNCA criar scripts Python/Bash para funcionalidades de negócio
- ✅ SEMPRE criar endpoints de API no backend
- ✅ Scripts apenas para manutenção/CI/CD

### 3. Contrato Formal (OLA)
- ✅ Cada serviço público deve ter um OLA
- ✅ OLA define interface, garantias e responsabilidades
- ✅ Versionamento documentado

### 4. Inventário Hierárquico
- ✅ Inventário geral na raiz (`GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`)
- ✅ Inventário específico em cada projeto (`<PROJETO>/INTEGRACOES/INVENTARIO_SERVICOS.md`)
- ✅ Ambos devem ser atualizados sempre

---

## 🏗️ ESTRUTURA DE GOVERNANÇA

### Nível 1: Ecossistema (Raiz)

**Arquivo:** `GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`

**Conteúdo:**
- Lista de todos os projetos com software
- Resumo de serviços por projeto
- Estatísticas gerais
- Links para inventários locais

### Nível 2: Projeto

**Arquivo:** `<PROJETO>/INTEGRACOES/INVENTARIO_SERVICOS.md`

**Conteúdo:**
- Lista detalhada de serviços do projeto
- Endpoints específicos
- OLAs do projeto
- Scripts transformados
- Histórico de transformações

### Nível 3: OLA (Operational Level Agreement)

**Arquivo:** `<PROJETO>/INTEGRACOES/OLA_<NOME>_SERVICE_v1.md`

**Conteúdo:**
- Interface do serviço
- Garantias do provedor
- Responsabilidades do cliente
- Exemplos de uso

---

## 🔄 PROCESSO DE CRIAÇÃO DE SERVIÇO

### Passo 1: Identificar Necessidade

**Perguntas:**
1. Esta funcionalidade será usada por múltiplos projetos?
2. Esta funcionalidade será usada por agentes?
3. Esta funcionalidade é de negócio (não manutenção)?

**Se SIM para qualquer uma:** Criar API, não script.

---

### Passo 2: Criar API

**Arquitetura:** Repository → Service → API Endpoint

#### 2.1. Criar Schema (Pydantic)

**Arquivo:** `<PROJETO>/backend/app/schemas/<nome>.py`

```python
from pydantic import BaseModel, Field

class <Nome>Request(BaseModel):
    """Schema para requisição."""
    campo: str = Field(..., description="Descrição")

class <Nome>Response(BaseModel):
    """Schema para resposta."""
    resultado: str
```

#### 2.2. Criar Service

**Arquivo:** `<PROJETO>/backend/app/services/<nome>_service.py`

```python
class <Nome>Service:
    async def <operacao>(self, ...) -> <Nome>Response:
        """Operação do serviço."""
        # Implementação
        pass
```

#### 2.3. Criar Endpoint

**Arquivo:** `<PROJETO>/backend/app/api/v1/endpoints/<nome>.py`

```python
@router.post("", response_model=<Nome>Response)
async def <operacao>(
    data: <Nome>Request,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep),
):
    """Endpoint de API."""
    service = <Nome>Service()
    return await service.<operacao>(...)
```

#### 2.4. Adicionar ao Router

**Arquivo:** `<PROJETO>/backend/app/api/v1/router.py`

```python
from app.api.v1.endpoints import <nome>

api_router.include_router(
    <nome>.router, prefix="/<nome>", tags=["<nome>"]
)
```

---

### Passo 3: Criar OLA

**Arquivo:** `<PROJETO>/INTEGRACOES/OLA_<NOME>_SERVICE_v1.md`

**Conteúdo mínimo:**
- Partes envolvidas (Provedor/Cliente)
- Interface do serviço
- Parâmetros de entrada
- Resposta de sucesso
- Códigos de erro
- Garantias do provedor
- Responsabilidades do cliente
- Exemplos de uso

---

### Passo 4: Identificar Vinculação

**⚠️ OBRIGATÓRIO:** Todo serviço deve estar vinculado a:
- **Projeto:** Projeto principal (ex: ENDFIRST Method v11.6)
- **Subprojeto:** (Opcional) Subprojeto dentro do projeto
- **Produto:** (Opcional) Produto específico dentro do subprojeto

**Perguntas:**
1. Qual projeto principal este serviço pertence?
2. Qual subprojeto (se houver)?
3. Qual produto (se houver)?

**Documentar vinculação:**
```markdown
**Vinculação:**
- **Projeto:** [Nome do Projeto]
- **Subprojeto:** [Nome do Subprojeto] (se aplicável)
- **Produto:** [Nome do Produto] (se aplicável)
```

---

### Passo 5: Atualizar Inventários

#### 5.1. Inventário Local (Projeto)

**Arquivo:** `<PROJETO>/INTEGRACOES/INVENTARIO_SERVICOS.md`

**Adicionar:**
- Serviço na lista de serviços disponíveis
- **Vinculação (Projeto/Subprojeto/Produto)**
- Endpoints na lista de APIs
- OLA na lista de OLAs
- Atualizar estatísticas

#### 5.2. Inventário Geral (Raiz)

**Arquivo:** `GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`

**Adicionar/Atualizar:**
- Serviço na lista do projeto
- **Vinculação (Projeto/Subprojeto/Produto)**
- Atualizar estatísticas gerais
- Manter link para inventário local

---

### Passo 6: Documentar

**Arquivos:**
- `<PROJETO>/README_SERVICOS.md` - Adicionar serviço (se existir)
- OpenAPI/Swagger (automático via FastAPI)

---

## 🔄 PROCESSO DE TRANSFORMAÇÃO DE SCRIPT EM API

### Quando Transformar

**Transformar quando:**
- Script é usado por múltiplos projetos
- Script será usado por agentes
- Script é funcionalidade de negócio (não manutenção)

**NÃO transformar quando:**
- Script é de manutenção (limpeza, organização)
- Script é de CI/CD (testes, deploy, release)
- Script é específico de um projeto único

---

### Passo 1: Identificar Script

1. Listar script em inventário local (seção "Scripts a Avaliar")
2. Decidir se deve ser transformado
3. Marcar como "A transformar"

---

### Passo 2: Criar API

Seguir "Processo de Criação de Serviço" acima.

---

### Passo 3: Remover Script

1. Deletar script
2. Atualizar inventário local:
   - Mover para "Scripts Transformados"
   - Documentar data de transformação
3. Atualizar inventário geral:
   - Atualizar estatísticas
   - Documentar transformação

---

### Passo 4: Validar

1. Testar API
2. Verificar que funcionalidade antiga ainda funciona
3. Atualizar documentação

---

## 🏗️ PROCESSO DE ADIÇÃO DE NOVO PROJETO COM SOFTWARE

### Passo 1: Criar Estrutura

1. Criar diretório do projeto
2. Criar `INTEGRACOES/` dentro do projeto
3. Criar `INTEGRACOES/INVENTARIO_SERVICOS.md` (copiar template)

**Template de Inventário Local:**

```markdown
# 📋 Inventário de Serviços - <NOME_PROJETO>

**Versão:** 1.0  
**Data:** [DATA]  
**Status:** ✅ Ativo

## 🎯 OBJETIVO

Inventário de serviços e APIs do projeto <NOME_PROJETO>.

## 📊 RESUMO

**Total de Serviços:** 0  
**Total de APIs:** 0  
**Total de OLAs:** 0

## 🔧 SERVIÇOS DISPONÍVEIS

[Adicionar serviços conforme criados]

## 📋 OLAs

[Adicionar OLAs conforme criados]

## 🔄 HISTÓRICO DE TRANSFORMAÇÕES

[Adicionar transformações conforme ocorrem]
```

### Passo 2: Atualizar Inventário Geral

**Arquivo:** `GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`

1. Adicionar projeto na tabela "Projetos com Software"
2. Adicionar seção do projeto
3. Linkar para inventário local
4. Atualizar estatísticas

### Passo 3: Seguir Processo de Criação de Serviço

Quando criar serviços no novo projeto, seguir processo acima.

---

## 📋 CHECKLIST DE GOVERNANÇA

Antes de considerar um serviço completo:

### Criação
- [ ] API criada no backend (não script)
- [ ] Service layer implementado
- [ ] Schemas Pydantic criados
- [ ] Endpoints documentados (OpenAPI/Swagger)
- [ ] **Vinculação identificada (Projeto/Subprojeto/Produto)**
- [ ] OLA criado (se serviço público)
- [ ] Inventário local atualizado (`<PROJETO>/INTEGRACOES/INVENTARIO_SERVICOS.md`)
- [ ] **Vinculação documentada no inventário local**
- [ ] Inventário geral atualizado (`GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`)
- [ ] **Vinculação documentada no inventário geral**
- [ ] README_SERVICOS.md atualizado (se aplicável)
- [ ] Exemplos de uso por agentes documentados

### Transformação de Script
- [ ] Script identificado e avaliado
- [ ] API criada seguindo processo
- [ ] Script removido
- [ ] Inventário local atualizado (mover para "Transformados")
- [ ] Inventário geral atualizado
- [ ] Funcionalidade validada

### Novo Projeto
- [ ] Estrutura criada (`INTEGRACOES/` dentro do projeto)
- [ ] Inventário local criado
- [ ] Inventário geral atualizado
- [ ] Link para inventário local funcionando

### Manutenção
- [ ] Inventários atualizados regularmente
- [ ] OLAs revisados periodicamente
- [ ] Documentação atualizada
- [ ] Scripts legados avaliados

---

## 📊 MÉTRICAS E MONITORAMENTO

### Métricas a Acompanhar

- Total de projetos com software
- Total de serviços ativos (por projeto e geral)
- Total de APIs disponíveis (por projeto e geral)
- Total de OLAs (por projeto e geral)
- Scripts transformados em API (por projeto e geral)
- Scripts legados (manutenção)

### Frequência de Revisão

- **Semanal:** Verificar se há scripts novos a transformar
- **Mensal:** Revisar inventários completos (local e geral)
- **Trimestral:** Revisar OLAs

---

## 🔗 REFERÊNCIAS

- **Inventário Geral:** `GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`
- **Método ENDFIRST:** `METODO/processos/PROCESSO_XX_GOVERNANCA_SERVICOS.md`
- **Banco de Referências - Inventário:** `BANCO_REFERENCIAS/INTEGRACOES/INVENTARIO_SERVICOS.md`
- **Banco de Referências - Processo:** `BANCO_REFERENCIAS/INTEGRACOES/PROCESSO_GOVERNANCA_SERVICOS.md`

---

**Última atualização:** 4 de Janeiro de 2026

