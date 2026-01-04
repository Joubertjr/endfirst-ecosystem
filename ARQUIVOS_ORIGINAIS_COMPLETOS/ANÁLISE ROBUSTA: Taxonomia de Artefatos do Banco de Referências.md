# ANÁLISE ROBUSTA: Taxonomia de Artefatos do Banco de Referências

**Objetivo:** Criar uma taxonomia completa e exaustiva de todos os tipos de artefatos que um Banco de Referências pode conter.

**Método:** Pensamento reverso a partir de todos os casos de uso possíveis.

---

## DIMENSÕES DE ANÁLISE

Para criar uma taxonomia completa, vou analisar os artefatos em 3 dimensões:

### **Dimensão 1: Origem**
- Interno (criado pelo projeto)
- Externo (criado fora do projeto)

### **Dimensão 2: Temporalidade**
- Estático (não muda)
- Dinâmico (evolui com o tempo)

### **Dimensão 3: Função**
- Operacional (para executar o projeto)
- Estratégico (para planejar o projeto)
- Histórico (para documentar o projeto)
- Fundamentação (para justificar o projeto)

---

## TAXONOMIA PROPOSTA (10 CATEGORIAS)

### **CATEGORIA 1: Artefatos de Estado**
**Origem:** Interno | **Temporalidade:** Dinâmico | **Função:** Operacional

**Descrição:** Documentos que descrevem o estado atual do projeto.

**Exemplos:**
- PROJECT_STATE.md (onde estamos)
- PROJECT_CONTEXT.md (visão geral)
- NEXT_STEPS.md (próximas ações)
- FILE_MAP.md (índice de arquivos)
- Status reports
- Dashboards de progresso

**Quando consultar:** Sempre que um agente precisa entender "onde estamos agora".

---

### **CATEGORIA 2: Artefatos de Decisão**
**Origem:** Interno | **Temporalidade:** Estático | **Função:** Histórico

**Descrição:** Documentos que registram decisões importantes e suas justificativas.

**Exemplos:**
- Architecture Decision Records (ADR)
- Changelogs (v10.3 → v10.4)
- Decision logs
- Meeting minutes (decisões tomadas)
- Trade-off analysis

**Quando consultar:** Quando alguém pergunta "por que decidimos X ao invés de Y?".

---

### **CATEGORIA 3: Artefatos de Aprendizado**
**Origem:** Interno | **Temporalidade:** Estático | **Função:** Histórico

**Descrição:** Documentos que registram falhas, erros e aprendizados.

**Exemplos:**
- Post-mortems
- Lessons learned
- Error logs (com análise de causa raiz)
- Retrospectives
- "What went wrong" documents

**Quando consultar:** Para evitar repetir erros passados.

---

### **CATEGORIA 4: Artefatos de Método**
**Origem:** Interno | **Temporalidade:** Dinâmico | **Função:** Operacional

**Descrição:** Documentos que definem como o trabalho deve ser feito.

**Exemplos:**
- ENDFIRST Method v10.4
- Pilares (0, 0.5, 1-7)
- Critérios transversais
- Checklists
- Workflows
- Standard Operating Procedures (SOP)

**Quando consultar:** Quando um agente precisa saber "como fazer X".

---

### **CATEGORIA 5: Artefatos de Conhecimento Externo**
**Origem:** Externo | **Temporalidade:** Estático | **Função:** Fundamentação

**Descrição:** Documentos externos que fundamentam o método ou o projeto.

**Exemplos:**
- Papers científicos (Kahneman, Baumeister, Gollwitzer)
- Livros de referência (Thinking Fast and Slow, Atomic Habits)
- Artigos de blog relevantes
- Whitepapers
- Industry reports

**Quando consultar:** Para entender a base científica ou conceitual de uma decisão.

---

### **CATEGORIA 6: Artefatos de Dados e Evidências**
**Origem:** Interno + Externo | **Temporalidade:** Estático | **Função:** Fundamentação

**Descrição:** Dados, benchmarks e evidências que validam o método ou decisões.

**Exemplos:**
- Análises externas (validação tripla)
- A/B tests
- Benchmarks
- Surveys
- Analytics data
- Métricas de sucesso

**Quando consultar:** Para validar se uma decisão ou método está funcionando.

---

### **CATEGORIA 7: Artefatos de Estratégia**
**Origem:** Interno | **Temporalidade:** Estático/Dinâmico | **Função:** Estratégico

**Descrição:** Documentos que definem a visão de longo prazo e o roadmap.

**Exemplos:**
- Plano de ação (2030 → hoje)
- Roadmap de série de artigos
- OKRs (Objectives and Key Results)
- Vision statements
- Strategic plans

**Quando consultar:** Para alinhar ações de curto prazo com objetivos de longo prazo.

---

### **CATEGORIA 8: Artefatos de Deliverables**
**Origem:** Interno | **Temporalidade:** Estático | **Função:** Operacional

**Descrição:** Produtos finais do projeto (versões finais, não rascunhos).

**Exemplos:**
- Artigo 1 (publicado)
- Artigo 2 (final)
- Código-fonte (release versions)
- Documentação técnica
- Apresentações finais

**Quando consultar:** Para acessar versões finais de produtos do projeto.

---

### **CATEGORIA 9: Artefatos de Contexto e Onboarding**
**Origem:** Interno | **Temporalidade:** Dinâmico | **Função:** Operacional

**Descrição:** Documentos criados especificamente para facilitar onboarding de novos agentes.

**Exemplos:**
- README principal
- Getting Started guides
- FAQs
- Glossários
- Tutoriais

**Quando consultar:** Quando um novo agente (humano ou IA) entra no projeto.

---

### **CATEGORIA 10: Artefatos de Integração e Ferramentas**
**Origem:** Interno + Externo | **Temporalidade:** Dinâmico | **Função:** Operacional

**Descrição:** Documentos sobre ferramentas, APIs e integrações usadas no projeto.

**Exemplos:**
- API documentation
- Tool configurations
- Integration guides
- Scripts e automações
- Credentials e access management (se aplicável)

**Quando consultar:** Para entender como usar ferramentas ou APIs do projeto.

---

## MATRIZ DE VALIDAÇÃO

| Categoria | Origem | Temporalidade | Função | Exemplo ENDFIRST |
|-----------|--------|---------------|--------|------------------|
| 1. Estado | Interno | Dinâmico | Operacional | PROJECT_STATE.md |
| 2. Decisão | Interno | Estático | Histórico | changelog_v10.4.md |
| 3. Aprendizado | Interno | Estático | Histórico | Post-mortem Pilar 0.5 |
| 4. Método | Interno | Dinâmico | Operacional | endfirst-method-v10.4/ |
| 5. Conhecimento Externo | Externo | Estático | Fundamentação | Papers de Kahneman |
| 6. Dados/Evidências | Ambos | Estático | Fundamentação | Análise Externa |
| 7. Estratégia | Interno | Ambos | Estratégico | Plano 2030 |
| 8. Deliverables | Interno | Estático | Operacional | Artigo 1 publicado |
| 9. Onboarding | Interno | Dinâmico | Operacional | README_CURSOR.md |
| 10. Ferramentas | Ambos | Dinâmico | Operacional | Cursor setup guide |

---

## CONCLUSÃO

**Esta taxonomia cobre 100% dos casos de uso?**

Para validar, vou fazer o teste reverso: "Existe algum tipo de informação que um projeto precisaria reter que NÃO se encaixa em nenhuma dessas 10 categorias?"

**Aguardando sua análise...** ⏸️
