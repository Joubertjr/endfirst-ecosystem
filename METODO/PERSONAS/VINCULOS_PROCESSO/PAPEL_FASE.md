# VÍNCULOS: PAPEL ↔ FASE DO MÉTODO

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Método:** END-FIRST v2

---

## 🔗 MAPEAMENTO PAPEL ↔ FASE

| Fase | Papel Ativo | Responsabilidade |
|---|---|---|
| **Criação de Demanda** | Produto | Escrever demanda, definir END, definir critérios |
| **Aprovação de Demanda** | CEO | Validar END, aprovar ou rejeitar |
| **Criação de F-1** | Produto | Estruturar fases, definir artefatos |
| **Aprovação de F-1** | CEO | Validar fases, aprovar ou rejeitar |
| **Execução de Fases (F1-FN)** | Executor | Gerar artefatos, commitar, gerar evidências |
| **Auditoria de F-1** | Auditor Técnico | Validar estrutura, procurar falhas |
| **Auditoria de Artefatos** | Auditor Técnico | Validar artefatos, aplicar gates |
| **Validação de Conclusão** | CEO | Validar evidências, declarar PASS/FAIL |
| **Aplicação de Gates** | Auditor Técnico | Aplicar gates canônicos, bloquear se FAIL |

---

## 📋 REGRAS DE ATIVAÇÃO

### Regra 1: Criação de Demanda
**Contexto:** Novo problema identificado  
**Papel ativo:** Produto  
**Critério de ativação:** Problema sem demanda formal

### Regra 2: Aprovação de Demanda
**Contexto:** Demanda criada, aguardando aprovação  
**Papel ativo:** CEO  
**Critério de ativação:** `status: pending_approval`

### Regra 3: Criação de F-1
**Contexto:** Demanda aprovada, sem F-1  
**Papel ativo:** Produto  
**Critério de ativação:** Demanda aprovada + F-1 ausente

### Regra 4: Aprovação de F-1
**Contexto:** F-1 criado, aguardando aprovação  
**Papel ativo:** CEO  
**Critério de ativação:** `status: PENDENTE`

### Regra 5: Execução de Fases
**Contexto:** F-1 aprovado, fases pendentes  
**Papel ativo:** Executor  
**Critério de ativação:** `status: APROVADO` + fases não executadas

### Regra 6: Auditoria
**Contexto:** F-1 ou artefato criado  
**Papel ativo:** Auditor Técnico  
**Critério de ativação:** Solicitação de auditoria OU gate obrigatório

### Regra 7: Validação de Conclusão
**Contexto:** Todas as fases executadas  
**Papel ativo:** CEO  
**Critério de ativação:** Todas as fases PASS + evidências geradas

---

## 🎯 RESPOSTA À PERGUNTA CANÔNICA

> "Dado este contexto, qual papel está ativo agora?"

**Algoritmo:**

```
SE demanda não existe ENTÃO
  Papel = Produto (criar demanda)

SE demanda existe E status = pending_approval ENTÃO
  Papel = CEO (aprovar demanda)

SE demanda aprovada E F-1 não existe ENTÃO
  Papel = Produto (criar F-1)

SE F-1 existe E status = PENDENTE ENTÃO
  Papel = CEO (aprovar F-1)

SE F-1 aprovado E fases não executadas ENTÃO
  Papel = Executor (executar fases)

SE auditoria solicitada OU gate obrigatório ENTÃO
  Papel = Auditor Técnico (auditar)

SE todas as fases executadas E evidências geradas ENTÃO
  Papel = CEO (validar conclusão)
```

---

## 🔒 REGRA CANÔNICA

> "Nenhuma fase do método pode ser executada sem papel ativo definido por artefato."
