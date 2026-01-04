# 📝 Como Documentar Projetos para o Banco de Referências

**Objetivo:** Transformar seu projeto em conhecimento reutilizável.

---

## 🎯 Por Que Documentar?

**Benefícios:**
- ✅ Acelera projetos futuros (reutilize especificações)
- ✅ Evita erros repetidos (aprenda com o passado)
- ✅ Melhora a qualidade (decisões consistentes)
- ✅ Facilita onboarding (contexto claro)
- ✅ Cria um ativo de conhecimento (seu "segundo cérebro")

**Custo:** 2-4 horas de documentação  
**Retorno:** 10-20 horas economizadas no próximo projeto similar

---

## 📁 Estrutura Recomendada

```
BANCO_REFERENCIAS/projetos/meu_projeto/
├── README.md                      (Visão geral do projeto)
├── especificacao_tecnica.md       (Requisitos funcionais e não-funcionais)
├── analise_arquitetura.md         (Comparação de abordagens + decisão)
├── roadmap.md                     (Fases de implementação)
├── custos.md                      (Estimativa de custos)
├── testes.md                      (Estratégia de testes)
└── aprendizados.md                (O que funcionou, o que não funcionou)
```

---

## 📄 Template: README.md

```markdown
# [Nome do Projeto]

**Status:** [✅ Completo | 🚧 Em andamento | ⏸️ Pausado]  
**Data de Início:** [Data]  
**Data de Conclusão:** [Data]  
**Versão:** [ex: v1.0]

---

## 🎯 Objetivo

[Descreva o objetivo do projeto em 2-3 parágrafos]

---

## 📊 Resultados Alcançados

- **Métrica 1:** [ex: 100 usuários ativos]
- **Métrica 2:** [ex: Tempo de resposta < 2s]
- **Métrica 3:** [ex: 90% de satisfação]

---

## 🛠️ Stack Tecnológico

- **Frontend:** [ex: Next.js 15 + React 19]
- **Backend:** [ex: FastAPI (Python 3.12+)]
- **Database:** [ex: PostgreSQL 16]
- **Cache:** [ex: Dragonfly]
- **RAG/LLM:** [ex: Google Gemini API]
- **Orchestration:** [ex: Temporal]
- **Deploy:** [ex: Vercel + Railway]

---

## 📁 Documentação

1. [especificacao_tecnica.md](especificacao_tecnica.md) - Requisitos funcionais e não-funcionais
2. [analise_arquitetura.md](analise_arquitetura.md) - Análise de abordagens e decisão
3. [roadmap.md](roadmap.md) - Roadmap de implementação (3 fases)
4. [custos.md](custos.md) - Estimativa de custos por fase
5. [testes.md](testes.md) - Estratégia de testes
6. [aprendizados.md](aprendizados.md) - Aprendizados e retrospectiva

---

## 🎓 Principais Aprendizados

1. ✅ [Aprendizado 1]
2. ✅ [Aprendizado 2]
3. ✅ [Aprendizado 3]

---

## 🏷️ Tags

`[tag1]` `[tag2]` `[tag3]` `[tag4]`

Exemplos: `RAG`, `PostgreSQL`, `FastAPI`, `Next.js`, `Temporal`

---

## 🔗 Links

- **Repositório:** [URL do GitHub]
- **Deploy:** [URL do projeto em produção]
- **Documentação Técnica:** [URL da doc]
```

---

## 📄 Template: especificacao_tecnica.md

```markdown
# Especificação Técnica - [Nome do Projeto]

**Versão:** [ex: v2.1]  
**Data:** [Data]

---

## 🎯 Visão Geral

[Descrição do sistema em 2-3 parágrafos]

---

## 📋 Requisitos Funcionais (RF)

### RF-01: [Título]
**Descrição:** [Descrição detalhada]  
**Prioridade:** [Alta | Média | Baixa]  
**Fase:** [MVP | Beta | Produção]

**Critérios de Aceitação:**
- [ ] Critério 1
- [ ] Critério 2

---

### RF-02: [Título]
[...]

---

## 🔧 Requisitos Não-Funcionais (RNF)

### RNF-01: Performance
**Descrição:** [ex: Tempo de resposta < 2s para 95% das requisições]  
**Métrica:** [Como medir]  
**Fase:** [MVP | Beta | Produção]

---

### RNF-02: Escalabilidade
[...]

---

## 📊 Resumo

| Tipo | Quantidade | MVP | Beta | Produção |
|---|---|---|---|---|
| RF | [ex: 12] | 5 | 8 | 12 |
| RNF | [ex: 8] | 4 | 6 | 8 |
```

---

## 📄 Template: analise_arquitetura.md

```markdown
# Análise de Arquitetura - [Nome do Projeto]

**Data:** [Data]  
**Responsável:** [Nome]

---

## 🎯 Contexto

[Descreva o problema que a arquitetura precisa resolver]

---

## 🏗️ Abordagens Consideradas

### Abordagem A: [Nome]

**Descrição:**  
[Descrição detalhada]

**Prós:**
- [Pró 1]
- [Pró 2]

**Contras:**
- [Contra 1]
- [Contra 2]

**Custo Estimado:** [ex: $100/mês]

---

### Abordagem B: [Nome]
[...]

### Abordagem C: [Nome]
[...]

---

## 📊 Matriz de Decisão

| Critério | Peso | Abordagem A | Abordagem B | Abordagem C |
|---|---|---|---|---|
| Complexidade | 30% | 3 (0.9) | 5 (1.5) | 2 (0.6) |
| Custo | 25% | 4 (1.0) | 5 (1.25) | 3 (0.75) |
| Escalabilidade | 20% | 5 (1.0) | 3 (0.6) | 4 (0.8) |
| Time-to-Market | 25% | 3 (0.75) | 5 (1.25) | 4 (1.0) |
| **TOTAL** | **100%** | **3.65** | **4.60** ⭐ | **3.15** |

---

## ✅ Decisão Final

**Abordagem escolhida:** Abordagem B

**Justificativa:**
[Explique por que esta abordagem foi escolhida]

**Riscos identificados:**
1. [Risco 1] → Mitigação: [...]
2. [Risco 2] → Mitigação: [...]
```

---

## 📄 Template: roadmap.md

```markdown
# Roadmap de Implementação - [Nome do Projeto]

---

## Fase 1: MVP ([Duração])

**Objetivo:** [ex: Validar o core business com 5 usuários]

**Escopo:**
- RF-01: [...]
- RF-02: [...]
- RNF-01 a RNF-04

**Stack:**
- [Stack simplificado]

**Custo Estimado:** [ex: $50-$100/mês]

**Critérios de Sucesso:**
- [ ] [Critério 1]
- [ ] [Critério 2]

---

## Fase 2: Beta ([Duração])
[...]

## Fase 3: Produção ([Duração])
[...]
```

---

## 📄 Template: custos.md

```markdown
# Estimativa de Custos - [Nome do Projeto]

---

## Fase 1: MVP

| Serviço | Custo Mensal | Custo Anual |
|---|---|---|
| [ex: Vercel Pro] | $20 | $240 |
| [ex: Neon PostgreSQL] | $10 | $120 |
| [ex: Google Gemini API] | $20 | $240 |
| **TOTAL** | **$50** | **$600** |

---

## Fase 2: Beta
[...]

## Fase 3: Produção
[...]

---

## Resumo

| Fase | Usuários | Custo Mensal | Custo/Usuário |
|---|---|---|---|
| MVP | 5 | $50 | $10 |
| Beta | 50 | $300 | $6 |
| Produção | 1.000 | $2.000 | $2 |
```

---

## 📄 Template: testes.md

```markdown
# Estratégia de Testes - [Nome do Projeto]

---

## Tipos de Testes

### 1. Testes Unitários

**Ferramenta:** [ex: pytest]  
**Cobertura:** [ex: 80%]  
**Fase:** MVP

**Escopo:**
- [ex: Funções de validação]
- [ex: Lógica de negócio]

---

### 2. Testes de Integração

**Ferramenta:** [ex: pytest + httpx]  
**Cobertura:** [ex: Fluxos críticos]  
**Fase:** MVP

**Escopo:**
- [ex: Upload de documentos]
- [ex: Busca semântica]

---

### 3. Testes E2E

**Ferramenta:** [ex: Playwright]  
**Cobertura:** [ex: Principais fluxos de usuário]  
**Fase:** Beta

---

### 4. Testes de Carga

**Ferramenta:** [ex: k6 / Locust]  
**Objetivo:** [ex: 1.000 req/s]  
**Fase:** Produção

---

## Resumo

| Tipo | Ferramenta | Cobertura | Fase |
|---|---|---|---|
| Unit | pytest | 80% | MVP |
| Integration | pytest + httpx | Críticos | MVP |
| E2E | Playwright | Principais | Beta |
| Load | k6 / Locust | 1.000 req/s | Produção |
```

---

## 📄 Template: aprendizados.md

```markdown
# Aprendizados - [Nome do Projeto]

---

## ✅ O Que Funcionou Bem

### 1. [Aprendizado 1]
**Contexto:** [...]  
**Por quê funcionou:** [...]  
**Como reutilizar:** [...]

### 2. [Aprendizado 2]
[...]

---

## ❌ O Que Não Funcionou

### 1. [Erro/Problema 1]
**Contexto:** [...]  
**Por quê não funcionou:** [...]  
**Como evitar:** [...]

### 2. [Erro/Problema 2]
[...]

---

## 🔄 O Que Faria Diferente

### 1. [Melhoria 1]
**O que foi feito:** [...]  
**O que faria diferente:** [...]  
**Impacto esperado:** [...]

---

## 🎓 Aprendizados para o Método ENDFIRST

1. ✅ [ex: Validação incremental funciona]
2. ✅ [ex: Análise de riscos evita over-engineering]
3. ✅ [...]

---

## 📊 Métricas Finais

| Métrica | Planejado | Alcançado | Delta |
|---|---|---|---|
| [ex: Usuários] | 100 | 120 | +20% |
| [ex: Tempo de resposta] | < 2s | 1.5s | +25% |
| [ex: Satisfação] | 90% | 92% | +2% |
```

---

## ✅ Checklist de Documentação

Antes de adicionar ao Banco de Referências:

- [ ] README.md criado
- [ ] especificacao_tecnica.md criado (RF + RNF)
- [ ] analise_arquitetura.md criado (matriz de decisão)
- [ ] roadmap.md criado (3 fases)
- [ ] custos.md criado (estimativa por fase)
- [ ] testes.md criado (estratégia completa)
- [ ] aprendizados.md criado (retrospectiva)
- [ ] Tags adicionadas ao README
- [ ] INDICE.md atualizado com metadados

---

## 🚀 Próximo Passo

**Adicione ao Banco de Referências:**

```bash
mv PROJETOS/meu_projeto BANCO_REFERENCIAS/projetos/
```

**Atualize o índice:**

Edite `BANCO_REFERENCIAS/INDICE.md` e adicione:

```markdown
### [Número]. [Nome do Projeto]

**Diretório:** `projetos/meu_projeto/`

**Descrição:** [Descrição breve]

**Stack:** [Stack principal]

**Requisitos:** [X RF + Y RNF]

**Tags:** `[tag1]` `[tag2]` `[tag3]`

**Status:** ✅ Completo
```

---

**Pronto! Seu projeto agora faz parte do Banco de Referências!** 🎉  
**Ele será reutilizado em projetos futuros!** 🧠
