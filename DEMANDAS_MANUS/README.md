---
document_id: DEMANDAS_MANUS_README
type: operational
owner: CEO (Joubert Jr)
status: approved
approved_by: CEO
approved_at: 2026-01-08
governed_by: /METODO/PILAR_ENDFIRST.md
version: 1.0
created_at: 2026-01-08
---

# DEMANDAS_MANUS — Demandas para Manus (Agent)

**Versão:** 1.0  
**Data:** 8 de Janeiro de 2026  
**Executor:** Manus (Agent)  
**Tipo:** Operacional

---

## 🎯 OBJETIVO

Este diretório contém **demandas formais para Manus (Agent)**, seguindo o mesmo regime de ENDFIRST que demandas para Cursor.

**Princípio:**
> "Se Cursor recebe demandas no Git, Manus TAMBÉM deve receber."

**Função:**
- Eliminar ordens fora do Git
- Garantir rastreabilidade de solicitações ao Manus
- Garantir versionamento de decisões
- Garantir END formal para trabalho de Manus

---

## 📋 TIPOS DE DEMANDAS PARA MANUS

### 1️⃣ Ontologia
- Criar decisões ontológicas (OD-XXX)
- Revisar ontologia existente
- Resolver ambiguidades conceituais

### 2️⃣ Método
- Criar processos do método
- Revisar processos existentes
- Documentar práticas

### 3️⃣ Governança
- Criar documentos de governança
- Revisar aprovações
- Atualizar logs

### 4️⃣ Produto
- Especificar produtos
- Criar specs ENDFIRST
- Definir critérios de aceitação

---

## 🔒 REGRAS ABSOLUTAS

### Manus NÃO executa ordens fora do repositório

- ❌ Manus não executa ordens em mensagens
- ❌ Manus não executa ordens verbais
- ❌ Manus não executa ordens sem END
- ✅ Manus executa demandas no Git

**Princípio:**
> "Toda solicitação ao Manus DEVE existir como DEMANDA no Git, com END explícito, escopo definido e critério de encerramento."

---

### Demandas para Manus seguem ENDFIRST

- ✅ END explícito (resultado esperado)
- ✅ Escopo definido
- ✅ Critério de encerramento
- ✅ Versionado no Git
- ✅ Aprovado pelo CEO

**Princípio:**
> "Demandas ao Manus seguem o mesmo regime de ENDFIRST que demandas ao Cursor."

---

## 📄 TEMPLATE

Use o template oficial:
- `/DEMANDAS_MANUS/TEMPLATE_DEMANDA_MANUS.md`

**Campos obrigatórios:**
- `id` — ID único da demanda
- `title` — Título descritivo
- `end` — Resultado final esperado (obrigatório)
- `type` — Tipo (ontologia | método | governança | produto)
- `executor` — Sempre "manus"
- `requested_by` — Sempre "CEO"
- `status` — Status atual

**Sem END → inválida.**

---

## 🔄 FLUXO DE DEMANDA PARA MANUS

```
1. CEO identifica necessidade
   ↓
2. CEO cria DEMANDA_MANUS-XXX.md (usando template)
   ↓
3. CEO define END explícito
   ↓
4. CEO commita no Git
   ↓
5. Manus lê demanda do Git
   ↓
6. Manus executa conforme END
   ↓
7. Manus commita resultado
   ↓
8. CEO valida resultado
   ↓
9. CEO decide (✅ APROVADO / ⚠️ AJUSTAR / ❌ REJEITADO)
```

---

## 📊 DIFERENÇA: DEMANDAS vs DEMANDAS_MANUS

| Aspecto | /DEMANDAS/ | /DEMANDAS_MANUS/ |
|---------|------------|------------------|
| **Executor** | Cursor (tecnologia) | Manus (agent) |
| **Tipo de trabalho** | Código, implementação | Ontologia, método, governança, produto |
| **Resultado** | Sistema funcional | Documento, decisão, processo |
| **Template** | TEMPLATE_DEMANDA.md | TEMPLATE_DEMANDA_MANUS.md |
| **Critérios** | DEMANDA-XXX_ACCEPTANCE.md | END explícito na demanda |

**Princípio comum:**
> Ambos seguem ENDFIRST. Ambos estão no Git. Ambos têm END explícito.

---

## 🚫 ANTI-PADRÕES (PROIBIDOS)

### 1. CEO manda ordem em mensagem
**Problema:** Ordem fora do Git  
**Solução:** Criar DEMANDA_MANUS-XXX.md

---

### 2. Manus executa sem END
**Problema:** Sem resultado esperado definido  
**Solução:** Exigir END explícito na demanda

---

### 3. Demanda sem versionamento
**Problema:** Não está no Git  
**Solução:** Commitar demanda antes de executar

---

### 4. Demanda sem critério de encerramento
**Problema:** Não sabe quando parar  
**Solução:** Definir END claro e objetivo

---

## 📜 FRASE CANÔNICA

> **"END primeiro. HOW depois. Sempre."**

**Aplicação:**
- CEO define END antes de pedir execução
- Manus executa conforme END
- Sem END, sem execução

---

## 🔗 DOCUMENTOS RELACIONADOS

- `/METODO/PILAR_ENDFIRST.md` (Meta-pilar)
- `/METODO/ONTOLOGY_DECISIONS.md` (OD-007: END é pré-condição absoluta)
- `/METODO/EXECUTION_MODEL.md` (Modelo de execução)
- `/DEMANDAS/` (Demandas para Cursor)

---

## 📜 DECLARAÇÃO DO CEO

> "Se Cursor recebe demandas no Git, Manus TAMBÉM deve receber. Caso contrário, Manus vira 'cabeça pensante informal', decisões viram conversa, END vira interpretação, e o sistema apodrece com o tempo."

**Data:** 2026-01-08  
**Responsável:** CEO (Joubert Jr)

---

## 📊 HISTÓRICO DE VERSÕES

| Versão | Data | Mudança | Responsável |
|--------|------|---------|-------------|
| 1.0 | 2026-01-08 | Criação da estrutura DEMANDAS_MANUS | CEO (Joubert Jr) |

---

**Versão:** 1.0  
**Criado:** 8 de Janeiro de 2026  
**Criado por:** Manus (Agent)  
**Aprovado por:** CEO (Joubert Jr)  
**Status:** Operacional
