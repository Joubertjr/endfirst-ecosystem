---
document_id: EXECUTION_MODEL
type: operational
owner: CEO (Joubert Jr)
status: approved
approved_by: CEO
approved_at: 2026-01-08
governed_by: /METODO/PILAR_ENDFIRST.md
---

# EXECUTION MODEL — Modelo de Execução

**Versão:** 1.0  
**Data:** 8 de Janeiro de 2026  
**Tipo:** Operacional (Tipo B)  
**Status:** Aprovado pelo CEO

---

## 🎯 OBJETIVO

Definir explicitamente **quem executa o quê** no sistema ENDFIRST, eliminando ambiguidade sobre papéis de execução.

**Princípio:**
> "Demandas são executadas por agentes de tecnologia, nunca por pessoas."

---

## 👥 PAPÉIS E RESPONSABILIDADES

### CEO (Autorizador)
**O que faz:**
- ✅ Autoriza execução de demandas
- ✅ Valida resultados
- ✅ Decide prioridades
- ✅ Cobra resultado

**O que NÃO faz:**
- ❌ Não executa demandas
- ❌ Não escreve código
- ❌ Não implementa specs

---

### Manus (Especificador)
**O que faz:**
- ✅ Escreve demandas
- ✅ Escreve specs (ENDFIRST_SPEC)
- ✅ Documenta decisões
- ✅ Faz governança

**O que NÃO faz:**
- ❌ Não executa demandas
- ❌ Não escreve código de produção
- ❌ Não autoriza execução

---

### Cursor (Executor)
**O que faz:**
- ✅ Lê demandas do Git
- ✅ Implementa especificações
- ✅ Escreve código
- ✅ Executa testes
- ✅ Faz commits de resultado

**O que NÃO faz:**
- ❌ Não decide o que executar
- ❌ Não autoriza execução
- ❌ Não escreve specs
- ❌ Não pergunta "quem executa?"

---

## 🔄 FLUXO CANÔNICO DE EXECUÇÃO

### Passo 1: CEO autoriza
**Ação:** CEO decide que uma demanda deve ser executada  
**Saída:** Autorização explícita (ex: "Pode seguir. Próximo movimento legítimo: execução da DEMANDA-001")

---

### Passo 2: Manus escreve/spec
**Ação:** Manus cria ou atualiza a demanda no Git  
**Saída:** Demanda completa com:
- YAML frontmatter (incluindo `executor: cursor`)
- Spec validada
- Produto declarado
- Status: LIBERADA PARA EXECUÇÃO

---

### Passo 3: Git é a fonte única
**Ação:** Demanda é commitada e pushed para o repositório  
**Saída:** Demanda disponível no Git (fonte única de verdade)

---

### Passo 4: Cursor lê do Git
**Ação:** Cursor acessa o repositório e lê a demanda  
**Entrada:** Caminho da demanda (ex: `/DEMANDAS/DEMANDA-001_LLM_ORCHESTRATOR.md`)

---

### Passo 5: Cursor executa
**Ação:** Cursor implementa a spec conforme demanda  
**Saída:** Código, testes, documentação

---

### Passo 6: Resultado volta para o Git
**Ação:** Cursor faz commit e push do resultado  
**Saída:** Resultado disponível no Git para validação

---

## ✅ REGRAS OBRIGATÓRIAS

### Regra 1: Toda demanda DEVE ter executor
**Campo obrigatório no YAML:**
```yaml
executor: cursor
```

**Validação:**
- ❌ Demanda sem `executor` → inválida
- ❌ Executor diferente de `cursor` → erro ontológico (por enquanto)

---

### Regra 2: Git é a fonte única
**Princípio:** Cursor lê do Git, não de mensagens

**Implicações:**
- Demanda deve estar commitada e pushed
- Cursor não acessa mensagens de chat
- Cursor não acessa arquivos locais fora do Git

---

### Regra 3: Executor não decide
**Princípio:** Cursor executa o que foi autorizado, não decide o que executar

**Implicações:**
- Cursor não escolhe prioridades
- Cursor não decide se executa ou não
- Cursor não pergunta "devo executar?"

---

### Regra 4: Pessoas não executam demandas
**Princípio:** Demandas são executadas por tecnologia, não por pessoas

**Implicações:**
- CEO não executa
- Manus não executa
- Contribuidores não executam
- Execução manual = erro de processo

---

## ❌ ANTI-PADRÕES (PROIBIDOS)

### 1. CEO tenta executar
**Problema:** CEO não tem papel de executor  
**Solução:** CEO autoriza, Cursor executa

---

### 2. Manus tenta executar
**Problema:** Manus não tem papel de executor  
**Solução:** Manus especifica, Cursor executa

---

### 3. Cursor pergunta "quem executa?"
**Problema:** Contrato de execução deve estar explícito  
**Solução:** Campo `executor` no YAML elimina ambiguidade

---

### 4. Demanda sem executor
**Problema:** Ambiguidade sobre quem deve executar  
**Solução:** Campo `executor` obrigatório no YAML

---

### 5. Execução fora do Git
**Problema:** Git não é fonte única de verdade  
**Solução:** Toda demanda deve estar no Git antes de execução

---

## 📋 CHECKLIST DE EXECUÇÃO

**Antes de executar, verificar:**
- [ ] Demanda está no Git (commitada e pushed)
- [ ] Campo `executor: cursor` presente no YAML
- [ ] Status: LIBERADA PARA EXECUÇÃO
- [ ] Produto declarado
- [ ] Spec validada
- [ ] CEO autorizou explicitamente

**Durante execução:**
- [ ] Cursor lê demanda do Git (não de mensagens)
- [ ] Cursor implementa conforme spec
- [ ] Cursor não decide, apenas executa

**Após execução:**
- [ ] Resultado commitado no Git
- [ ] CEO valida resultado
- [ ] Demanda marcada como concluída (se aplicável)

---

## 🎯 FRASE CANÔNICA

> **"Demandas são executadas por agentes de tecnologia, nunca por pessoas."**

**Uso:**
- Onboarding de novos contribuidores
- Revisão de processos
- Cultura organizacional
- Ontologia prática

---

## 📜 DECLARAÇÃO DO CEO

> "O sistema está certo. A dúvida mostrou onde ele ainda estava silencioso. Vamos torná-lo explícito — e seguir."

**Data:** 2026-01-08  
**Responsável:** CEO (Joubert Jr)

---

## 📊 EXEMPLO PRÁTICO

### DEMANDA-001 (LLM Orchestrator)

**Fluxo completo:**

1. **CEO autoriza:**
   > "Pode seguir. Próximo movimento legítimo: execução da DEMANDA-001."

2. **Manus atualiza demanda:**
   - Adiciona `executor: cursor` no YAML
   - Status: LIBERADA PARA EXECUÇÃO
   - Commit e push para Git

3. **Git é fonte única:**
   - Demanda disponível em: `/DEMANDAS/DEMANDA-001_LLM_ORCHESTRATOR.md`

4. **Cursor lê do Git:**
   - Acessa repositório
   - Lê demanda completa
   - Lê spec EF-2026-001

5. **Cursor executa:**
   - Implementa LLM Orchestrator
   - Escreve código
   - Escreve testes

6. **Resultado volta para Git:**
   - Cursor faz commit
   - CEO valida resultado

---

## 🔗 DOCUMENTOS RELACIONADOS

- `/METODO/ONTOLOGY_DECISIONS.md` (OD-006: Execução é responsabilidade da Tecnologia)
- `/METODO/ROLES_AND_RESPONSIBILITIES.md` (Papéis: CEO/Manus/Cursor)
- `/METODO/TEMPLATE_DEMANDA.md` (Template com campo `executor`)
- `/METODO/PILAR_ENDFIRST.md` (Meta-pilar)

---

## 📋 HISTÓRICO DE VERSÕES

| Versão | Data | Mudança | Responsável |
|--------|------|---------|-------------|
| 1.0 | 2026-01-08 | Criação do modelo de execução | Manus (Agent) |

---

**Versão:** 1.0  
**Criado:** 8 de Janeiro de 2026  
**Criado por:** Manus (Agent)  
**Aprovado por:** CEO (Joubert Jr)  
**Status:** Operacional (Tipo B)
