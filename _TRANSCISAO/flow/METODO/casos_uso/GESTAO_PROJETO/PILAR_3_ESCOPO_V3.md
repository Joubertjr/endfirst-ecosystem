# Pilar 3: Calibragem de Escopo - Metodologia de Acompanhamento de Projeto ("ENDFIRST Flow")

**Data:** 30 de Dezembro de 2025  
**Versão:** v3.0 (Revisão Completa e Robusta)

---

## 🎯 Definição do Escopo

A calibragem de escopo é crucial para garantir uma entrega de valor rápida e focada. Este pilar define claramente **o que entra** e **o que fica de fora** da versão 1.0 do ENDFIRST Flow, seguindo o princípio de **Produto Mínimo Viável (MVP)**.

**Princípio Norteador:**

> **"Simplicidade acima de tudo. O ENDFIRST Flow v1.0 deve resolver 80% dos problemas com 20% da complexidade."**

Toda funcionalidade proposta deve passar pelo teste:
- **É absolutamente essencial para o problema central (perda de contexto)?**
- **Pode ser implementado sem adicionar burocracia significativa?**
- **Funciona sem dependências externas complexas?**

Se a resposta for "não" para qualquer uma dessas perguntas, a funcionalidade fica para versões futuras.

---

## ✅ DENTRO DO ESCOPO (v1.0)

### **1. Dashboard de Projeto em Markdown**

**Descrição:** Um arquivo único `STATUS_PROJETO.md` que centraliza todo o acompanhamento do projeto, servindo como fonte única de verdade para o estado atual do trabalho.

#### **Seções Obrigatórias do Dashboard**

##### **1.1. Visão Geral**

**Conteúdo:**
- Nome do projeto
- Objetivo principal (1-2 frases)
- Status geral (🟢 No Prazo | 🟡 Atenção | 🔴 Atrasado)
- Data de início
- Data de conclusão prevista
- Última atualização

**Exemplo:**
```markdown
# 📊 Dashboard do Projeto: Sistema de Autenticação

**Objetivo:** Implementar sistema completo de autenticação com JWT, recuperação de senha e 2FA.

**Status Geral:** 🟡 Atenção (bloqueio na integração com email)

**Início:** 15/12/2025  
**Previsão de Conclusão:** 05/01/2026  
**Última Atualização:** 30/12/2025 14:30
```

---

##### **1.2. Próximas Ações (AGORA)**

**Conteúdo:**
- 3-5 tarefas mais importantes
- **1 tarefa destacada como "AGORA"** (a próxima ação imediata)
- Cada tarefa com tipo, prioridade e estimativa

**Formato:**
```markdown
## 🎯 Próximas Ações

### **AGORA** 👉
- [🐛 Bug] [Alta] Corrigir erro de timeout na API de login (2h)

### Próximas na Fila:
1. [🎯 Feature] [Alta] Implementar recuperação de senha (4h)
2. [🧪 Teste] [Média] Criar testes de integração para JWT (3h)
3. [📚 Docs] [Baixa] Documentar fluxo de autenticação (1h)
```

**Critérios:**
- A tarefa "AGORA" deve ser sempre a primeira coisa a fazer ao abrir o projeto
- Máximo 5 tarefas na lista (foco!)
- Atualizar a cada fim de sessão

---

##### **1.3. Tarefas por Status**

**Conteúdo:**
- Tarefas organizadas pelos 8 estados do ciclo de vida
- Formato: `[Tipo] [Prioridade] Título (Estimativa)`
- Limite de 10 tarefas por status (arquivar o resto)

**Formato:**
```markdown
## 📦 Backlog (15 tarefas)
- [🎯 Feature] [Baixa] Adicionar login social com Google (6h)
- [🔧 Melhoria] [Baixa] Otimizar query de busca de usuários (2h)
- ...

## 📋 A Fazer (5 tarefas)
- [🎯 Feature] [Alta] Implementar recuperação de senha (4h)
- [🐛 Bug] [Média] Corrigir validação de email (1h)
- ...

## 🚧 Em Andamento (2 tarefas)
- [🐛 Bug] [Alta] Corrigir erro de timeout na API de login (2h) - Iniciado em 30/12 14:00
- ...

## 🔍 Em Revisão (1 tarefa)
- [🎯 Feature] [Alta] Endpoint de registro de usuário (3h) - Pronto para revisão desde 29/12

## 🧪 Em Teste (0 tarefas)

## 🎯 Em Homologação (0 tarefas)

## ✅ Concluído (Últimas 10)
- [🎯 Feature] [Alta] Configurar JWT no backend (2h) - Concluído em 28/12
- [📚 Docs] [Média] Criar README do projeto (1h) - Concluído em 27/12
- ...
- [Ver arquivo completo: LOG_DEZEMBRO_2025.md]

## 🚫 Bloqueado (1 tarefa)
- [🎯 Feature] [Alta] Integrar envio de email (3h)
  - **Bloqueio:** Aguardando credenciais SMTP do cliente
  - **Quem desbloqueia:** João (cliente)
  - **Follow-up:** Cobrar em 02/01/2026
  - **Bloqueado desde:** 29/12/2025
```

**Critérios:**
- Mostrar contagem total de tarefas por status
- Exibir no máximo 10 tarefas "Concluídas" (arquivar o resto)
- Tarefas bloqueadas devem ter informação completa do bloqueio

---

##### **1.4. Log de Progresso (Changelog)**

**Conteúdo:**
- Registro cronológico das últimas 20-30 entradas
- Entradas mais recentes no topo
- Formato padronizado

**Formato de entrada:**
```markdown
### [2025-12-30 14:30] Corrigido bug de timeout na API

**O que foi feito:** Aumentei o timeout de 5s para 15s e adicionei retry automático com backoff exponencial.

**Por que foi feito:** Usuários reportaram erro 504 em horários de pico. A causa raiz era timeout muito curto para queries complexas.

**Impacto:** Redução de 90% nos erros 504 em produção.

**Próximos passos:** Monitorar por 48h e considerar otimização de queries se o problema persistir.
```

**Regras:**
- Máximo 5 linhas por entrada
- Foco em "o que" e "por que", não em "como" (detalhes técnicos vão no Git)
- Incluir impacto quando relevante
- Arquivar logs antigos mensalmente (ex: `LOG_DEZEMBRO_2025.md`)

---

##### **1.5. Decisões Importantes**

**Conteúdo:**
- Registro de decisões arquiteturais e estratégicas
- Formato inspirado em ADRs (Architecture Decision Records)
- Permanente (não arquivar)

**Formato:**
```markdown
### [DEC-001] Usar JWT ao invés de Sessions

**Data:** 20/12/2025  
**Contexto:** Precisamos de autenticação stateless para escalar horizontalmente.  
**Decisão:** Usar JWT com refresh tokens armazenados no Redis.  
**Alternativas consideradas:** Sessions com Redis, OAuth2 puro.  
**Consequências:** Maior complexidade inicial, mas melhor escalabilidade.  
**Status:** ✅ Implementado
```

**Critérios:**
- Apenas decisões que impactam o projeto a longo prazo
- Máximo 10-15 decisões (se passar disso, o projeto precisa de revisão arquitetural)
- Cada decisão tem um ID único (DEC-001, DEC-002, etc.)

---

##### **1.6. Métricas e Sprints (OBRIGATÓRIO)**

**Conteúdo:**
- Tempo total investido (real, medido)
- Progresso percentual (calculado automaticamente)
- Sprint atual (semana de trabalho)
- Velocidade (tarefas concluídas/sprint)
- Taxa de bugs

**O que é um Sprint no ENDFIRST Flow?**

Um sprint é um **período de 1 semana** onde você define:
- Quais tarefas do "A Fazer" entram no sprint
- Objetivo do sprint (o que você quer alcançar)
- Data de início e fim

**Formato:**
```markdown
## 📈 Métricas e Sprint Atual

### Sprint Atual: Sprint #4 (30/12/2025 - 05/01/2026)

**Objetivo do Sprint:** Finalizar Pilares 3, 3.5 e 4 do ENDFIRST Flow

**Tarefas do Sprint:**
- [🎯 Feature] Revisar Pilar 3 completo (8h) - ✅ Concluído
- [📚 Docs] Criar Pilar 3.5 (4h) - 🚧 Em Andamento
- [📚 Docs] Criar Pilar 4 (4h) - 📋 A Fazer

**Progresso do Sprint:** 33% (1/3 tarefas concluídas)

---

### Métricas Gerais do Projeto

**Tempo Investido:** 12 horas (medido desde 30/12/2025 09:00)  
**Progresso Geral:** 25% (3/12 pilares concluídos)  
**Velocidade Média:** 2 pilares/sprint  
**Taxa de Bugs:** 0% (0 retrabalhos / 3 pilares concluídos)  
**Sprints Completados:** 3

**Histórico de Sprints:**
- Sprint #1 (16-22/12): 2 pilares concluídos
- Sprint #2 (23-29/12): 1 pilar concluído  
- Sprint #3 (30/12-05/01): Em andamento
```

**Como Definir um Sprint:**

1. **No início da semana (segunda-feira ou primeiro dia de trabalho):**
   - Escolha 3-5 tarefas do "A Fazer" que cabem em ~20-30 horas de trabalho
   - Defina um objetivo claro para o sprint
   - Mova essas tarefas para a seção "Sprint Atual"

2. **Durante o sprint:**
   - Trabalhe apenas nas tarefas do sprint
   - Se surgir algo urgente, adicione ao sprint OU remova outra tarefa
   - Atualize o progresso do sprint diariamente

3. **No fim do sprint (sexta-feira ou último dia):**
   - Revise o que foi concluído
   - Calcule a velocidade (tarefas concluídas / sprint)
   - Mova tarefas não concluídas de volta para "A Fazer"
   - Planeje o próximo sprint

**Critérios:**
- **Atualização diária:** Progresso do sprint é atualizado no Ritual de Fim de Sessão
- **Atualização semanal:** Métricas gerais são recalculadas no fim de cada sprint
- **Dados reais:** NUNCA invente dados. Use cronômetro, conte tarefas reais, calcule percentuais reais
- **Obrigatório:** Mesmo em projetos pequenos. Métricas são essenciais para saber se estamos no caminho certo

---

#### **Estrutura Completa do Dashboard (Template)**

```markdown
# 📊 Dashboard do Projeto: [NOME DO PROJETO]

**Objetivo:** [Objetivo principal em 1-2 frases]

**Status Geral:** [🟢/🟡/🔴] [Descrição breve]

**Início:** [Data]  
**Previsão de Conclusão:** [Data]  
**Última Atualização:** [Data e hora]

---

## 🎯 Próximas Ações

### **AGORA** 👉
- [Tipo] [Prioridade] Tarefa (Estimativa)

### Próximas na Fila:
1. [Tipo] [Prioridade] Tarefa (Estimativa)
2. ...

---

## 📦 Backlog (X tarefas)
- ...

## 📋 A Fazer (X tarefas)
- ...

## 🚧 Em Andamento (X tarefas)
- ...

## 🔍 Em Revisão (X tarefas)
- ...

## 🧪 Em Teste (X tarefas)
- ...

## 🎯 Em Homologação (X tarefas)
- ...

## ✅ Concluído (Últimas 10)
- ...

## 🚫 Bloqueado (X tarefas)
- ...

---

## 📝 Log de Progresso

### [YYYY-MM-DD HH:MM] Título da Atividade

**O que foi feito:** ...

**Por que foi feito:** ...

**Próximos passos:** ...

---

## 🎯 Decisões Importantes

### [DEC-001] Título da Decisão

**Data:** ...  
**Contexto:** ...  
**Decisão:** ...  
**Alternativas consideradas:** ...  
**Consequências:** ...  
**Status:** ...

---

## 📈 Métricas (Opcional)

**Tempo Investido:** X horas  
**Progresso:** X% (Y/Z tarefas concluídas)  
**Velocidade Média:** X tarefas/semana  
**Taxa de Bugs:** X%
```

---

#### **Manutenção e Arquivamento**

**Quando arquivar:**
- **Tarefas Concluídas:** Quando passar de 10 itens, mover as mais antigas para `ARQUIVO_TAREFAS_CONCLUIDAS.md`
- **Log de Progresso:** Mensalmente, mover para `LOG_[MES]_[ANO].md`
- **Backlog:** Quando passar de 20 itens, revisar e eliminar tarefas obsoletas

**Como arquivar:**
1. Criar arquivo de arquivo (ex: `LOG_DEZEMBRO_2025.md`)
2. Mover conteúdo antigo para lá
3. Adicionar link no dashboard: `[Ver logs antigos: LOG_DEZEMBRO_2025.md]`

---

#### **Critérios de Qualidade do Dashboard**

- [ ] **Legibilidade:** Qualquer pessoa consegue entender o estado do projeto em 30 segundos
- [ ] **Atualidade:** Última atualização foi há menos de 24 horas
- [ ] **Foco:** Seção "Próximas Ações" tem no máximo 5 itens
- [ ] **Completude:** Todas as seções obrigatórias estão preenchidas
- [ ] **Tamanho:** O arquivo tem menos de 500 linhas (se passar, arquivar conteúdo antigo)
- [ ] **Consistência:** Formato de tarefas e logs está padronizado

---

**Justificativa:** O dashboard é o coração do Flow. Ele resolve o problema central de perda de contexto ao centralizar todas as informações críticas em um único lugar, facilmente acessível e editável.

**Critério de Sucesso:** 
- O usuário consegue retomar o projeto em menos de 2 minutos lendo apenas o dashboard
- O dashboard é atualizado naturalmente como parte do fluxo de trabalho (não é um fardo)
- O usuário sente confiança de que nada importante está sendo esquecido

---

### **2. Ciclo de Vida da Tarefa**

**Descrição:** Um fluxo robusto e ágil para o status de cada tarefa, com critérios claros de transição e validação.

#### **Estados do Ciclo de Vida**

| # | Estado | Emoji | Descrição | O que significa? |
|:---|:-------|:------|:----------|:-----------------|
| **1** | **Backlog** | 📦 | Tarefa mapeada mas não detalhada | Ideia capturada, mas ainda não está pronta para ser trabalhada. Falta detalhamento, priorização ou dependências não resolvidas. |
| **2** | **A Fazer** | 📋 | Tarefa pronta para ser iniciada | Tarefa detalhada, priorizada e sem impedimentos. Passou pela Definition of Ready (DoR). |
| **3** | **Em Andamento** | 🚧 | Tarefa sendo desenvolvida | Alguém está trabalhando ativamente nesta tarefa. Deve haver apenas 1-2 tarefas neste estado por pessoa. |
| **4** | **Em Revisão** | 🔍 | Tarefa aguardando code review | Desenvolvimento concluído, aguardando revisão de código (por outra pessoa ou auto-revisão). |
| **5** | **Em Teste** | 🧪 | Tarefa sendo testada | Revisão aprovada, agora está sendo testada (unit tests, integration tests, testes manuais). |
| **6** | **Em Homologação** | 🎯 | Tarefa aguardando validação do cliente/usuário | Testes passaram, aguardando aprovação final do stakeholder ou usuário final. |
| **7** | **Concluído** | ✅ | Tarefa finalizada e aceita | Tarefa validada, aceita e pronta para produção. Passou pela Definition of Done (DoD). |
| **8** | **Bloqueado** | 🚫 | Tarefa impedida (pode ocorrer em qualquer fase) | Trabalho pausado devido a bloqueio externo (aguardando feedback, dependência de terceiros, decisão pendente). |

---

#### **Definition of Ready (DoR) - Backlog → A Fazer**

Uma tarefa só pode sair do Backlog e ir para "A Fazer" se atender **TODOS** os critérios abaixo:

- [ ] **Descrição clara:** O que precisa ser feito está descrito de forma objetiva
- [ ] **Critério de aceitação:** Como saber se a tarefa está concluída?
- [ ] **Estimativa de esforço:** Quanto tempo/complexidade? (ex: Pequena, Média, Grande)
- [ ] **Dependências resolvidas:** Todas as dependências de outras tarefas foram concluídas
- [ ] **Prioridade definida:** A tarefa tem uma prioridade clara (Alta, Média, Baixa)
- [ ] **Recursos disponíveis:** Tudo que é necessário para executar está disponível (acesso, informações, ferramentas)

**Exemplo de tarefa que passou pela DoR:**
```markdown
## [A Fazer] Criar endpoint de autenticação

**Descrição:** Implementar endpoint POST /api/auth/login que recebe email e senha e retorna JWT.

**Critério de Aceitação:**
- Endpoint responde com status 200 e token JWT válido para credenciais corretas
- Endpoint responde com status 401 para credenciais incorretas
- Token JWT expira em 24 horas

**Estimativa:** Média (2-4 horas)

**Dependências:** ✅ Banco de dados configurado, ✅ Biblioteca JWT instalada

**Prioridade:** Alta
```

---

#### **Critérios para Transição: A Fazer → Em Andamento**

Uma tarefa só pode ir para "Em Andamento" se:

- [ ] **Você tem tempo disponível:** Pelo menos 1-2 horas de trabalho focado
- [ ] **Limite de WIP respeitado:** Você tem no máximo 2 tarefas "Em Andamento" (Work In Progress)
- [ ] **Contexto carregado:** Você leu a descrição e entendeu o que precisa ser feito
- [ ] **Ambiente pronto:** Ferramentas, arquivos e dependências estão acessíveis

**Ação obrigatória ao fazer a transição:**
- Atualizar o status no dashboard
- Adicionar uma entrada no log: "Iniciando trabalho em [nome da tarefa]"

---

#### **Critérios para Transição: Em Andamento → Bloqueado**

Uma tarefa vai para "Bloqueado" quando:

- [ ] **Dependência externa:** Aguardando resposta, aprovação ou entrega de terceiros
- [ ] **Decisão pendente:** Precisa de uma decisão estratégica antes de continuar
- [ ] **Recurso indisponível:** Falta acesso, informação ou ferramenta crítica

**Ação obrigatória ao fazer a transição:**
- Documentar claramente **o que está bloqueando** e **quem/o que pode desbloquear**
- Adicionar uma entrada no log explicando o bloqueio
- Definir uma ação de follow-up (ex: "Cobrar resposta do cliente em 2 dias")

**Exemplo de tarefa bloqueada:**
```markdown
## [Bloqueado] Integrar API de pagamento

**Bloqueio:** Aguardando credenciais de API da equipe de infraestrutura.

**Quem pode desbloquear:** João (infra)

**Follow-up:** Cobrar João via Slack em 30/12/2025

**Bloqueado desde:** 29/12/2025
```

---

#### **Critérios para Transição: Bloqueado → Em Andamento**

Uma tarefa volta para "Em Andamento" quando:

- [ ] **Bloqueio resolvido:** A dependência foi atendida ou a decisão foi tomada
- [ ] **Contexto recuperado:** Você releu a tarefa e entendeu onde parou

**Ação obrigatória ao fazer a transição:**
- Atualizar o log explicando como o bloqueio foi resolvido
- Remover a descrição do bloqueio da tarefa

---

#### **Critérios para Transição: Em Andamento → Em Revisão**

Uma tarefa vai para "Em Revisão" quando:

- [ ] **Desenvolvimento concluído:** Todo o código/trabalho planejado foi implementado
- [ ] **Auto-revisão feita:** Você revisou seu próprio trabalho antes de pedir revisão
- [ ] **Código commitado:** Todas as mudanças estão no Git com mensagens claras
- [ ] **Testes básicos passando:** Você testou localmente e funciona

**Ação obrigatória ao fazer a transição:**
- Adicionar no log: "[Tarefa X] pronta para revisão"
- Se houver revisor, notificá-lo (ou agendar auto-revisão para o dia seguinte)

---

#### **Critérios para Transição: Em Revisão → Em Teste**

Uma tarefa vai para "Em Teste" quando:

- [ ] **Revisão aprovada:** Code review foi feito e aprovou (ou auto-revisão concluída)
- [ ] **Ajustes da revisão implementados:** Todos os comentários/sugestões foram endereçados
- [ ] **Código mergeado:** Se aplicável, branch foi mergeado na branch principal

**Ação obrigatória ao fazer a transição:**
- Adicionar no log: "[Tarefa X] passou na revisão, iniciando testes"
- Preparar ambiente de testes (se necessário)

**Transição alternativa:**
- **Em Revisão → Em Andamento:** Se a revisão identificar problemas que requerem retrabalho significativo

---

#### **Critérios para Transição: Em Teste → Em Homologação**

Uma tarefa vai para "Em Homologação" quando:

- [ ] **Todos os testes passaram:** Unit tests, integration tests e testes manuais estão OK
- [ ] **Bugs críticos corrigidos:** Nenhum bug bloqueante foi encontrado
- [ ] **Ambiente de homologação preparado:** Deploy feito em ambiente de staging/homologação
- [ ] **Documentação atualizada:** README, guias ou docs foram atualizados

**Ação obrigatória ao fazer a transição:**
- Adicionar no log: "[Tarefa X] testes concluídos, aguardando homologação"
- Notificar o stakeholder/cliente que a tarefa está pronta para validação

**Transição alternativa:**
- **Em Teste → Em Andamento:** Se testes identificarem bugs que requerem retrabalho

**Nota:** Para projetos individuais sem stakeholder externo, você pode pular "Em Homologação" e ir direto para "Concluído" após os testes.

---

#### **Critérios para Transição: Em Homologação → Concluído (DoD Final)**

Uma tarefa vai para "Concluído" quando:

- [ ] **Stakeholder aprovou:** Cliente/usuário validou e aceitou a entrega
- [ ] **Feedback incorporado:** Ajustes solicitados na homologação foram implementados
- [ ] **Deploy em produção:** Se aplicável, código foi deployado no ambiente de produção
- [ ] **Documentação final:** Toda documentação necessária está completa e atualizada
- [ ] **Sem débito técnico crítico:** Não deixou problemas graves para trás

**Ação obrigatória ao fazer a transição:**
- Adicionar no log: "[Tarefa X] concluída e aceita - [breve descrição do resultado]"
- Mover a tarefa para a seção "Concluído" do dashboard
- Arquivar a tarefa se a seção "Concluído" tiver mais de 10 itens
- Celebrar! 🎉

**Transição alternativa:**
- **Em Homologação → Em Andamento:** Se o stakeholder rejeitar e pedir mudanças significativas

---

#### **Fluxo Completo de Transições**

```
📦 Backlog
    ↓ (DoR atendida)
📋 A Fazer
    ↓ (Critérios de início atendidos)
🚧 Em Andamento
    ↓ (Desenvolvimento concluído)
🔍 Em Revisão
    ↓ (Revisão aprovada)
🧪 Em Teste
    ↓ (Testes passaram)
🎯 Em Homologação (opcional para projetos individuais)
    ↓ (Stakeholder aprovou)
✅ Concluído

🚫 Bloqueado (pode ocorrer em qualquer fase acima)
```

**Transições especiais:**
- **Bloqueado → [Fase anterior]:** Quando o bloqueio é resolvido, a tarefa volta para a fase onde estava
- **Bloqueado → A Fazer:** Se o bloqueio tornar a tarefa inviável, ela volta para "A Fazer" para ser repriorizada
- **Bloqueado → Backlog:** Se o bloqueio tornar a tarefa irrelevante ou precisar de redefinição completa
- **A Fazer → Backlog:** Se a tarefa perder prioridade ou precisar ser redetalhada
- **Qualquer fase → Em Andamento:** Se testes/revisão/homologação identificarem necessidade de retrabalho

---

#### **Limite de Work In Progress (WIP)**

**Regra de ouro:** No máximo **2 tarefas "Em Andamento"** por pessoa ao mesmo tempo.

**Por quê?**
- Reduz context switching (custo cognitivo de trocar de tarefa)
- Aumenta o foco e a qualidade do trabalho
- Garante que tarefas sejam finalizadas antes de iniciar novas

**Exceção:** Se uma tarefa estiver "Bloqueada", você pode iniciar outra enquanto aguarda o desbloqueio.

---

#### **Tipos de Cards (Classificação de Tarefas)**

Além dos **estados** (onde a tarefa está no fluxo), cada tarefa tem um **tipo** que define a natureza do trabalho. Isso ajuda na priorização, planejamento e análise de métricas.

| Tipo | Emoji | Descrição | Quando usar? | Prioridade Típica |
|:-----|:------|:----------|:-------------|:--------------------|
| **Feature** | 🎯 | Nova funcionalidade ou capacidade | Quando você está adicionando algo novo que o sistema não fazia antes. | Média a Alta |
| **Bug** | 🐛 | Correção de defeito ou comportamento incorreto | Quando algo que deveria funcionar não está funcionando como esperado. | Alta a Crítica |
| **Melhoria** | 🔧 | Otimização ou aprimoramento de algo existente | Quando você quer melhorar performance, UX ou qualidade de algo que já funciona. | Média |
| **Documentação** | 📚 | Criar ou atualizar documentação | Quando precisa escrever README, guias, comentários ou docs técnicas. | Baixa a Média |
| **Refatoração** | 🧹 | Melhorar código sem mudar comportamento | Quando o código funciona mas está confuso, duplicado ou difícil de manter. | Baixa a Média |
| **Pesquisa/Spike** | 🔬 | Investigação técnica ou prova de conceito | Quando você precisa explorar uma tecnologia, API ou abordagem antes de decidir. | Média |
| **Deploy** | 🚀 | Tarefa de implantação ou release | Quando você precisa fazer deploy, configurar ambiente ou lançar uma versão. | Alta |
| **Tarefa** | ✅ | Trabalho genérico que não se encaixa nas outras categorias | Quando é uma atividade administrativa, setup ou algo que não é código. | Variável |

---

#### **Critérios de DoD Específicos por Tipo**

Cada tipo de card pode ter critérios adicionais de Definition of Done:

**🎯 Feature:**
- [ ] Funcionalidade implementada e testada
- [ ] Testes unitários criados
- [ ] Documentação de uso atualizada
- [ ] UX validada (se aplicável)

**🐛 Bug:**
- [ ] Bug reproduzido e causa raiz identificada
- [ ] Correção implementada
- [ ] Teste de regressão criado para evitar recorrência
- [ ] Verificação de que a correção não quebrou outras funcionalidades

**🔧 Melhoria:**
- [ ] Melhoria implementada
- [ ] Métricas de antes/depois documentadas (se aplicável)
- [ ] Testes atualizados

**📚 Documentação:**
- [ ] Documentação escrita e revisada
- [ ] Exemplos práticos incluídos
- [ ] Links e referências verificados
- [ ] Ortografia e gramática revisadas

**🧹 Refatoração:**
- [ ] Código refatorado
- [ ] Todos os testes existentes ainda passam
- [ ] Comportamento externo não mudou
- [ ] Complexidade reduzida (medida por métricas ou revisão)

**🔬 Pesquisa/Spike:**
- [ ] Investigação concluída
- [ ] Descobertas documentadas
- [ ] Recomendação clara (usar X, não usar Y, precisa mais investigação)
- [ ] Próximos passos definidos

**🚀 Deploy:**
- [ ] Deploy executado com sucesso
- [ ] Ambiente de produção validado
- [ ] Rollback plan documentado
- [ ] Monitoramento ativo por 24h

**✅ Tarefa:**
- [ ] Atividade concluída conforme descrito
- [ ] Resultado documentado (se aplicável)

---

#### **Como Identificar Tipos no Dashboard**

**Formato recomendado para títulos de tarefas:**

```markdown
## [🎯 Feature] [Em Andamento] Criar sistema de autenticação
## [🐛 Bug] [Bloqueado] Corrigir erro de timeout na API
## [📚 Docs] [A Fazer] Documentar processo de deploy
## [🔬 Spike] [Em Teste] Investigar uso de Redis para cache
```

**Estrutura:** `[Tipo] [Estado] Título da Tarefa`

**Benefícios:**
- Identificação visual instantânea
- Facilita filtros e buscas
- Permite análise de métricas por tipo

---

#### **Priorização por Tipo**

Quando você tem múltiplas tarefas "A Fazer", use esta ordem de prioridade padrão:

1. **🐛 Bugs Críticos** - Bloqueiam usuários ou causam perda de dados
2. **🚀 Deploy** - Entregas agendadas ou releases
3. **🎯 Features de Alta Prioridade** - Funcionalidades críticas para o projeto
4. **🐛 Bugs Não-Críticos** - Problemas que não impedem o uso
5. **🔧 Melhorias** - Otimizações importantes
6. **🔬 Pesquisa/Spike** - Investigações necessárias para decisões
7. **🎯 Features de Média/Baixa Prioridade** - Funcionalidades secundárias
8. **🧹 Refatoração** - Melhorias de código
9. **📚 Documentação** - A menos que seja bloqueante para outros
10. **✅ Tarefas Genéricas** - Atividades administrativas

**Nota:** Esta é uma ordem padrão. O contexto do seu projeto pode exigir ajustes.

---

**Justificativa:** Um ciclo de vida robusto com DoR, DoD e tipificação clara garante qualidade, clareza e rastreabilidade. Os 8 estados e 8 tipos de cards cobrem 95%+ dos cenários reais de desenvolvimento individual.

**Critério de Sucesso:** 
- O usuário nunca fica em dúvida sobre qual estado ou tipo usar
- Tarefas não ficam presas em "Em Andamento" indefinidamente
- O dashboard reflete com precisão o estado e a natureza real do projeto
- É possível analisar métricas por tipo (ex: "Quantos bugs resolvi este mês?")

---

### **3. Rituais de Início e Fim de Sessão**

**Descrição:** Processos simples, rápidos e eficazes para "abrir" e "fechar" o contexto de trabalho, garantindo que o progresso seja capturado e o próximo passo esteja sempre claro.

#### **Por que Rituais são Importantes?**

Rituais resolvem três problemas críticos:

1. **Perda de Contexto:** Sem um ritual de início, você perde tempo tentando lembrar onde parou.
2. **Progresso Não Documentado:** Sem um ritual de fim, o trabalho feito não é registrado e pode ser esquecido.
3. **Paralisia de Decisão:** Sem definir "o que fazer a seguir", você perde tempo decidindo ao retomar.

---

#### **Ritual de Início de Sessão (Máximo 2 minutos)**

**Objetivo:** Carregar o contexto do projeto e iniciar o trabalho focado.

**Passos:**

1. **Abrir o Dashboard** (`STATUS_PROJETO.md`) no Cursor AI
   - Use `@STATUS_PROJETO.md` para referenciar rapidamente

2. **Ler a seção "Próximas Ações"**
   - Identifique a tarefa marcada como "AGORA"
   - Se não houver tarefa "AGORA", escolha a primeira da lista

3. **Atualizar o status da tarefa para "Em Andamento"**
   - Mova a tarefa da seção "A Fazer" para "Em Andamento"
   - Adicione timestamp: `- Iniciado em [DD/MM HH:MM]`

4. **Adicionar entrada no Log de Progresso**
   ```markdown
   ### [YYYY-MM-DD HH:MM] Iniciando sessão de trabalho
   
   **Foco desta sessão:** [Nome da tarefa]
   
   **Objetivo:** [O que você pretende alcançar nesta sessão]
   ```

5. **Abrir arquivos relevantes**
   - Use o Cursor AI para abrir os arquivos necessários para a tarefa
   - Se não souber quais arquivos, pergunte ao Cursor: "Quais arquivos preciso abrir para trabalhar em [tarefa]?"

**Checklist do Ritual de Início:**
- [ ] Dashboard aberto
- [ ] Tarefa "AGORA" identificada
- [ ] Status atualizado para "Em Andamento"
- [ ] Log de progresso atualizado
- [ ] Arquivos relevantes abertos
- [ ] Tempo total: < 2 minutos

**Exemplo Prático:**
```markdown
# Ritual de Início - 30/12/2025 14:00

1. Abri @STATUS_PROJETO.md
2. Tarefa AGORA: [🐛 Bug] Corrigir erro de timeout na API
3. Movi para "Em Andamento" - Iniciado em 30/12 14:00
4. Log atualizado: "Iniciando sessão - Foco: corrigir timeout"
5. Arquivos abertos: api/routes/auth.js, api/middleware/timeout.js
6. Pronto para trabalhar! ✅
```

---

#### **Ritual de Fim de Sessão (Máximo 2 minutos)**

**Objetivo:** Capturar o progresso, preservar o contexto e definir o próximo passo.

**Passos:**

1. **Atualizar o status da tarefa atual**
   - Se concluída: mover para "Concluído" (ou próxima fase do ciclo)
   - Se não concluída: manter em "Em Andamento" com nota do progresso
   - Se bloqueada: mover para "Bloqueado" com descrição do bloqueio

2. **Adicionar entrada detalhada no Log de Progresso**
   ```markdown
   ### [YYYY-MM-DD HH:MM] [Título da atividade]
   
   **O que foi feito:** [Descrição breve e objetiva]
   
   **Por que foi feito:** [Contexto e justificativa]
   
   **Próximos passos:** [O que fazer a seguir]
   ```

3. **Definir a próxima tarefa "AGORA"**
   - Escolha a próxima tarefa mais importante
   - Marque-a como "AGORA" na seção "Próximas Ações"
   - Se necessário, mova uma tarefa do "A Fazer" para "Próximas Ações"

4. **Commitar mudanças no Git** (se aplicável)
   - Faça commit do código com mensagem clara
   - Sincronize o dashboard também: `git add STATUS_PROJETO.md && git commit -m "Update dashboard"`

5. **Salvar e fechar**
   - Salve o dashboard
   - Feche o Cursor AI (ou deixe aberto se for retomar em breve)

**Checklist do Ritual de Fim:**
- [ ] Status da tarefa atualizado
- [ ] Log de progresso com entrada detalhada
- [ ] Próxima tarefa "AGORA" definida
- [ ] Código commitado no Git
- [ ] Dashboard salvo
- [ ] Tempo total: < 2 minutos

**Exemplo Prático:**
```markdown
# Ritual de Fim - 30/12/2025 16:30

1. Tarefa [🐛 Bug] Corrigir timeout - Status: Concluído ✅
2. Log atualizado:
   - O que: Aumentei timeout de 5s para 15s + retry com backoff
   - Por quê: Usuários reportavam erro 504 em horários de pico
   - Próximos passos: Monitorar por 48h
3. Próxima tarefa AGORA: [🎯 Feature] Implementar recuperação de senha
4. Git commit: "fix: increase API timeout and add retry logic"
5. Dashboard salvo e sincronizado
6. Sessão encerrada! 🎉
```

---

#### **Ritual de Retomada Após Pausa Longa (5-10 minutos)**

**Quando usar:** Quando você não mexe no projeto há mais de 3 dias.

**Passos:**

1. **Ler a seção "Visão Geral" do dashboard**
   - Relembrar o objetivo do projeto
   - Verificar o status geral

2. **Ler as últimas 5 entradas do Log de Progresso**
   - Reconstruir o contexto do que foi feito recentemente
   - Identificar decisões importantes

3. **Revisar a seção "Decisões Importantes"**
   - Relembrar escolhas arquiteturais
   - Verificar se há decisões pendentes

4. **Verificar tarefas "Bloqueadas"**
   - Ver se algum bloqueio foi resolvido
   - Atualizar follow-ups se necessário

5. **Seguir o Ritual de Início normal**

**Checklist do Ritual de Retomada:**
- [ ] Visão Geral lida
- [ ] Últimas 5 entradas do log revisadas
- [ ] Decisões Importantes revisadas
- [ ] Bloqueios verificados
- [ ] Ritual de Início executado
- [ ] Tempo total: < 10 minutos

---

#### **Automações Opcionais**

**Para reduzir ainda mais o atrito:**

1. **Git Hooks:**
   ```bash
   # .git/hooks/pre-commit
   # Lembrar de atualizar o dashboard antes de commitar
   if ! git diff --cached --name-only | grep -q "STATUS_PROJETO.md"; then
     echo "⚠️  Lembre-se de atualizar o STATUS_PROJETO.md!"
   fi
   ```

2. **Alias do Shell:**
   ```bash
   # ~/.bashrc ou ~/.zshrc
   alias start-session="cursor STATUS_PROJETO.md"
   alias end-session="git add STATUS_PROJETO.md && git commit -m 'Update dashboard'"
   ```

3. **Template de Log no Cursor AI:**
   - Crie um snippet no Cursor para gerar entradas de log rapidamente

---

**Justificativa:** Rituais curtos e eficazes garantem que o contexto seja preservado sem adicionar burocracia. A chave é manter cada ritual em menos de 2 minutos para que seja sustentável a longo prazo.

**Critério de Sucesso:**
- O usuário executa os rituais naturalmente, sem sentir que é um fardo
- O tempo de retomada do projeto é reduzido em pelo menos 50%
- O progresso é documentado consistentemente

---

### **4. Log de Progresso (Changelog)**

**Descrição:** Um registro cronológico simples, mas rico em contexto, das atividades e decisões do projeto, inspirado em Git commits e changelogs de software.

#### **Por que um Log de Progresso?**

O log resolve três problemas:

1. **Memória Falha:** Você não vai lembrar por que tomou uma decisão há 2 semanas.
2. **Contexto Perdido:** Sem registro, o raciocínio por trás das ações se perde.
3. **Rastreabilidade:** É impossível entender a evolução do projeto sem um histórico.

---

#### **Formato Padrão de Entrada**

```markdown
### [YYYY-MM-DD HH:MM] Título Curto e Descritivo

**O que foi feito:** Descrição breve e objetiva da ação realizada (1-2 frases).

**Por que foi feito:** Contexto, motivação e justificativa da decisão (1-2 frases).

**Impacto:** (Opcional) Resultado ou consequência da ação (1 frase).

**Próximos passos:** (Opcional) O que fazer a seguir (1 frase).
```

---

#### **Regras de Ouro do Log**

1. **Máximo 5 linhas por entrada** - Se precisar de mais, a informação deve ir para "Decisões Importantes" ou documentação separada.

2. **Foco em "O QUE" e "POR QUÊ", não em "COMO"** - Detalhes técnicos vão no Git commit, não no log.

3. **Entradas mais recentes no topo** - Ordem cronológica reversa para facilitar a leitura.

4. **Timestamp obrigatório** - Formato: `[YYYY-MM-DD HH:MM]`

5. **Título descritivo** - Deve ser possível entender o que aconteceu apenas lendo o título.

6. **Linguagem clara e objetiva** - Evite jargões desnecessários.

---

#### **Tipos de Entradas no Log**

##### **1. Início/Fim de Sessão**
```markdown
### [2025-12-30 14:00] Iniciando sessão de trabalho

**Foco desta sessão:** Corrigir bug de timeout na API de login.

**Objetivo:** Identificar causa raiz e implementar solução com retry.
```

##### **2. Tarefa Concluída**
```markdown
### [2025-12-30 16:30] Corrigido bug de timeout na API

**O que foi feito:** Aumentei o timeout de 5s para 15s e adicionei retry automático com backoff exponencial.

**Por que foi feito:** Usuários reportaram erro 504 em horários de pico. A causa raiz era timeout muito curto para queries complexas.

**Impacto:** Redução de 90% nos erros 504 em produção (monitorado por 48h).

**Próximos passos:** Considerar otimização de queries se o problema persistir.
```

##### **3. Bloqueio Identificado**
```markdown
### [2025-12-29 11:00] Tarefa de integração com email bloqueada

**O que foi feito:** Identifiquei que precisamos de credenciais SMTP do cliente para continuar.

**Por que foi feito:** A tarefa não pode avançar sem acesso ao servidor de email.

**Próximos passos:** Cobrar credenciais do João (cliente) via Slack até 02/01/2026.
```

##### **4. Decisão Técnica Importante**
```markdown
### [2025-12-28 15:00] Decidido usar JWT ao invés de sessions

**O que foi feito:** Após spike de 3h, decidimos usar JWT com refresh tokens.

**Por que foi feito:** Precisamos de autenticação stateless para escalar horizontalmente. Sessions com Redis adicionariam complexidade desnecessária.

**Impacto:** Maior complexidade inicial, mas melhor escalabilidade a longo prazo.

**Próximos passos:** Implementar JWT no backend (tarefa criada).
```

##### **5. Mudança de Prioridade**
```markdown
### [2025-12-27 09:00] Repriorizado feature de 2FA para depois do MVP

**O que foi feito:** Movi a tarefa de 2FA do "A Fazer" para o "Backlog".

**Por que foi feito:** Cliente pediu para focar em lançar o MVP em janeiro. 2FA pode esperar para v1.1.

**Impacto:** Reduz escopo do MVP em ~8 horas de trabalho.
```

##### **6. Bug Descoberto**
```markdown
### [2025-12-26 17:00] Descoberto bug crítico na validação de senha

**O que foi feito:** Identifiquei que senhas com caracteres especiais não estão sendo aceitas.

**Por que foi feito:** Testes manuais revelaram o problema. Causa raiz: regex de validação incorreta.

**Próximos passos:** Criar tarefa de bug com prioridade alta.
```

---

#### **Quando NÃO Adicionar ao Log**

- **Commits triviais:** "Fixed typo", "Updated README" → Isso vai no Git, não no log.
- **Trabalho em andamento:** Só registre quando algo concreto foi feito ou decidido.
- **Detalhes técnicos:** "Mudei o método X para usar Y" → Isso vai no commit message.

---

#### **Manutenção e Arquivamento**

**Quando arquivar:**
- Quando o log passar de 30 entradas (~2-3 meses de trabalho)
- Ao final de cada mês (para projetos longos)

**Como arquivar:**
1. Criar arquivo `LOG_[MES]_[ANO].md` (ex: `LOG_DEZEMBRO_2025.md`)
2. Mover entradas antigas para lá
3. Manter apenas as últimas 20-30 entradas no dashboard
4. Adicionar link no dashboard: `[Ver logs antigos: LOG_DEZEMBRO_2025.md]`

**Estrutura do arquivo de log arquivado:**
```markdown
# Log de Progresso - Dezembro 2025

## Projeto: Sistema de Autenticação

### [2025-12-30 16:30] Corrigido bug de timeout na API
...

### [2025-12-29 11:00] Tarefa de integração com email bloqueada
...

[... todas as entradas do mês ...]
```

---

#### **Integração com Git**

O log de progresso **complementa** o Git, não o substitui:

| Aspecto | Git Commits | Log de Progresso |
|:--------|:------------|:-----------------|
| **O quê** | Mudanças técnicas no código | Atividades e decisões do projeto |
| **Granularidade** | Linha por linha | Tarefa por tarefa |
| **Público** | Desenvolvedores | Qualquer stakeholder |
| **Linguagem** | Técnica | Negócio/contexto |
| **Quando** | A cada mudança de código | A cada sessão de trabalho |

**Exemplo de complementaridade:**

**Git commit:**
```
fix: increase API timeout from 5s to 15s and add retry logic

- Changed timeout constant in api/config.js
- Added exponential backoff retry in api/middleware/retry.js
- Updated tests to reflect new timeout
```

**Log de progresso:**
```markdown
### [2025-12-30 16:30] Corrigido bug de timeout na API

**O que foi feito:** Aumentei o timeout e adicionei retry automático.

**Por que foi feito:** Usuários reportavam erro 504 em horários de pico.

**Impacto:** Redução de 90% nos erros 504.
```

---

**Justificativa:** Um log simples, mas rico em contexto, é a chave para preservar o conhecimento do projeto. Ele funciona como um "segundo cérebro" que permite reconstruir o raciocínio por trás de cada decisão.

**Critério de Sucesso:**
- O usuário consegue reconstruir o contexto do projeto lendo apenas o log
- O log é atualizado naturalmente como parte dos rituais
- O log é útil para explicar o projeto para outras pessoas (ou para si mesmo no futuro)

---

### **5. Guia Completo da Metodologia (ENDFIRST_FLOW.md)**

**Descrição:** O documento central que explica todos os conceitos, princípios, processos e artefatos do ENDFIRST Flow, servindo como referência completa e autônoma.

#### **Estrutura do Guia Completo**

O guia será organizado em 10 seções principais:

##### **Seção 1: Introdução e Filosofia**

**Conteúdo:**
- O que é o ENDFIRST Flow?
- Por que ele existe? (problema que resolve)
- Para quem é? (desenvolvedor individual, projetos de software)
- Princípios fundamentais (pensar no resultado primeiro, simplicidade, contexto)
- Relação com o método ENDFIRST (11 pilares)

**Tamanho estimado:** 300-400 palavras

**Exemplo de conteúdo:**
```markdown
# ENDFIRST Flow: Metodologia de Acompanhamento de Projeto

## O que é?

O ENDFIRST Flow é uma metodologia leve e robusta para acompanhar projetos de desenvolvimento de software individual. Ele resolve o problema central de **perda de contexto** ao pausar e retomar o trabalho.

## Por que existe?

Desenvolvedores individuais enfrentam um desafio constante: ao retomar um projeto após uma pausa (horas, dias ou semanas), eles perdem tempo tentando lembrar:
- Onde pararam
- Por que tomaram certas decisões
- Qual é o próximo passo

O ENDFIRST Flow resolve isso com um sistema simples de dashboard, rituais e logs que preserva o contexto sem adicionar burocracia.

## Princípios Fundamentais

1. **Pensar no Resultado Primeiro:** Sempre saiba qual é o próximo passo antes de pausar o trabalho.
2. **Simplicidade Acima de Tudo:** Se um processo leva mais de 2 minutos, ele precisa ser simplificado.
3. **Contexto é Rei:** Preserve não apenas o "o que" foi feito, mas o "por que" foi feito.
4. **Agnóstico de Ferramenta:** Funciona com qualquer editor, mas otimizado para Cursor AI.
```

---

##### **Seção 2: Conceitos Centrais**

**Conteúdo:**
- Dashboard de Projeto
- Ciclo de Vida da Tarefa (8 estados)
- Tipos de Cards (8 tipos)
- Definition of Ready (DoR)
- Definition of Done (DoD)
- Work In Progress (WIP) Limit
- Log de Progresso
- Decisões Importantes

**Tamanho estimado:** 500-600 palavras

---

##### **Seção 3: Ciclo de Vida da Tarefa (Detalhado)**

**Conteúdo:**
- Descrição de cada um dos 8 estados
- Critérios de transição entre estados
- Fluxo completo de transições
- Exemplos práticos

**Tamanho estimado:** 800-1000 palavras

---

##### **Seção 4: Tipos de Cards e Priorização**

**Conteúdo:**
- Descrição dos 8 tipos de cards
- Quando usar cada tipo
- Critérios de DoD específicos por tipo
- Ordem de priorização padrão
- Como adaptar a priorização ao seu contexto

**Tamanho estimado:** 400-500 palavras

---

##### **Seção 5: Rituais (Início, Fim e Retomada)**

**Conteúdo:**
- Ritual de Início de Sessão (passo a passo)
- Ritual de Fim de Sessão (passo a passo)
- Ritual de Retomada Após Pausa Longa
- Checklists para cada ritual
- Automações opcionais

**Tamanho estimado:** 600-700 palavras

---

##### **Seção 6: Sistema de Log de Progresso**

**Conteúdo:**
- Formato padrão de entrada
- Regras de ouro do log
- Tipos de entradas (início/fim, tarefa concluída, bloqueio, decisão, etc.)
- Quando NÃO adicionar ao log
- Manutenção e arquivamento
- Integração com Git

**Tamanho estimado:** 400-500 palavras

---

##### **Seção 7: Integração com os 11 Pilares do ENDFIRST**

**Conteúdo:**
- Como o Flow se encaixa em cada pilar
- Quando usar o Flow durante a aplicação do ENDFIRST
- Exemplo prático: criação do próprio ENDFIRST Flow

**Tamanho estimado:** 300-400 palavras

**Exemplo de conteúdo:**
```markdown
## Integração com os 11 Pilares do ENDFIRST

O ENDFIRST Flow é uma **extensão natural** do método ENDFIRST, focada especificamente no **Pilar 6 (Execução)** e **Pilar 7 (Captura de Aprendizados)**.

| Pilar ENDFIRST | Como o Flow Ajuda |
|:---------------|:------------------|
| **Pilar 0: Estado Final** | O dashboard mantém o objetivo do projeto sempre visível. |
| **Pilar 1: Obstáculos** | Tarefas bloqueadas são rastreadas com clareza. |
| **Pilar 2: Recursos** | O log documenta recursos utilizados. |
| **Pilar 3: Escopo** | O backlog e "A Fazer" refletem o escopo calibrado. |
| **Pilar 4: Planejamento Reverso** | As tarefas são organizadas na ordem de execução. |
| **Pilar 5: Validação Externa** | Homologação é um estado explícito no ciclo de vida. |
| **Pilar 6: Execução** | **O Flow É O PILAR 6 EM AÇÃO.** |
| **Pilar 7: Aprendizados** | O log e decisões importantes capturam aprendizados. |
```

---

##### **Seção 8: Manutenção e Arquivamento**

**Conteúdo:**
- Quando arquivar tarefas concluídas
- Quando arquivar logs antigos
- Como manter o dashboard leve e útil
- Estratégias para projetos longos (6+ meses)

**Tamanho estimado:** 200-300 palavras

---

##### **Seção 9: Adaptações para Diferentes Contextos**

**Conteúdo:**
- Projetos pequenos (1 semana)
- Projetos médios (1 mês)
- Projetos grandes (6+ meses)
- Projetos colaborativos (adaptação para equipes)
- Projetos de pesquisa/escrita (não apenas software)

**Tamanho estimado:** 300-400 palavras

---

##### **Seção 10: Limitações e Evolução Futura**

**Conteúdo:**
- O que o Flow NÃO faz (e por quê)
- Limitações conhecidas
- Roadmap de versões futuras (v2.0, v3.0)
- Como contribuir com feedback

**Tamanho estimado:** 200-300 palavras

---

##### **Seção 11: Glossário de Termos**

**Conteúdo:**
- Definições de todos os termos técnicos usados no Flow
- Exemplos práticos para cada termo

**Tamanho estimado:** 300-400 palavras

**Exemplo:**
```markdown
## Glossário

**Backlog:** Lista de tarefas mapeadas mas não detalhadas. Ideias capturadas que ainda não estão prontas para serem trabalhadas.

**Definition of Ready (DoR):** Conjunto de critérios que uma tarefa deve atender antes de sair do Backlog e ir para "A Fazer".

**Definition of Done (DoD):** Conjunto de critérios que uma tarefa deve atender para ser considerada "Concluída".

**Work In Progress (WIP):** Número de tarefas que estão sendo trabalhadas simultaneamente. O limite recomendado é 2.

**Dashboard:** Arquivo único (STATUS_PROJETO.md) que centraliza todo o acompanhamento do projeto.

**Log de Progresso:** Registro cronológico das atividades e decisões do projeto.

**Decisões Importantes:** Registro permanente de decisões arquiteturais e estratégicas (inspirado em ADRs).

**Rituais:** Processos curtos (< 2 min) executados no início e fim de cada sessão de trabalho.
```

---

#### **Critérios de Qualidade do Guia Completo**

- [ ] **Completude:** Cobre todos os conceitos, processos e artefatos do Flow
- [ ] **Clareza:** Linguagem simples e objetiva, sem jargões desnecessários
- [ ] **Exemplos:** Pelo menos 2 exemplos práticos para cada conceito importante
- [ ] **Autonomia:** O usuário consegue implementar o Flow sem ajuda externa
- [ ] **Tamanho:** Entre 2.000-3.000 palavras (legível em 15-20 minutos)
- [ ] **Estrutura:** Seções claramente delimitadas com títulos descritivos
- [ ] **Navegação:** Índice no início com links para cada seção

---

**Justificativa:** Um guia completo e bem estruturado garante que o usuário tenha uma referência confiável para consultar sempre que tiver dúvidas. Ele serve como a "fonte de verdade" da metodologia.

**Critério de Sucesso:**
- O usuário consegue implementar o Flow lendo apenas este guia
- O guia responde 90%+ das dúvidas que surgem durante o uso
- O guia é consultado regularmente (não é esquecido após a primeira leitura)

---

### **6. Template de Dashboard (TEMPLATE_DASHBOARD.md)**

**Descrição:** Um arquivo Markdown pronto para copiar, colar e usar, que serve como ponto de partida para qualquer projeto usando o ENDFIRST Flow.

#### **Características do Template**

1. **Autoexplicativo:** Comentários em cada seção explicando o que preencher
2. **Utilizável em < 5 minutos:** Copiar, colar, preencher informações básicas e começar
3. **Cabe em uma tela:** Sem scroll excessivo (máximo 300-400 linhas)
4. **Facilmente editável:** Markdown puro, funciona em qualquer editor

#### **Estrutura do Template**

```markdown
# 📊 Dashboard do Projeto: [NOME DO PROJETO]

<!-- 
  INSTRUÇÕES:
  1. Substitua [NOME DO PROJETO] pelo nome real do seu projeto
  2. Preencha a seção "Visão Geral" com as informações básicas
  3. Adicione suas primeiras tarefas no Backlog
  4. Defina a primeira tarefa "AGORA" em "Próximas Ações"
  5. Delete estes comentários quando terminar o setup inicial
-->

**Objetivo:** [Descreva em 1-2 frases o que este projeto pretende alcançar]

**Status Geral:** 🟢 No Prazo | 🟡 Atenção | 🔴 Atrasado

**Início:** [DD/MM/YYYY]  
**Previsão de Conclusão:** [DD/MM/YYYY]  
**Última Atualização:** [DD/MM/YYYY HH:MM]

---

## 🎯 Próximas Ações

<!-- Mantenha no máximo 5 tarefas aqui. Use o formato: [Tipo] [Prioridade] Título (Estimativa) -->

### **AGORA** 👉
- [ ] [🎯 Feature] [Alta] [Descreva a próxima ação mais importante] (Xh)

### Próximas na Fila:
1. [ ] [Tipo] [Prioridade] [Descrição] (Xh)
2. [ ] [Tipo] [Prioridade] [Descrição] (Xh)
3. [ ] [Tipo] [Prioridade] [Descrição] (Xh)

---

## 📦 Backlog (0 tarefas)

<!-- Tarefas mapeadas mas não detalhadas. Adicione aqui ideias e tarefas futuras. -->

- [ ] [Tipo] [Prioridade] [Descrição breve] (Estimativa)

---

## 📋 A Fazer (0 tarefas)

<!-- Tarefas que passaram pela DoR e estão prontas para serem iniciadas. -->

---

## 🚧 Em Andamento (0 tarefas)

<!-- Máximo 2 tarefas aqui! Respeite o limite de WIP. -->

---

## 🔍 Em Revisão (0 tarefas)

<!-- Tarefas aguardando code review ou auto-revisão. -->

---

## 🧪 Em Teste (0 tarefas)

<!-- Tarefas sendo testadas (unit, integration, manual). -->

---

## 🎯 Em Homologação (0 tarefas)

<!-- Tarefas aguardando validação do cliente/stakeholder. Pode ser pulado em projetos individuais. -->

---

## ✅ Concluído (Últimas 10)

<!-- Tarefas finalizadas. Arquive quando passar de 10 itens. -->

---

## 🚫 Bloqueado (0 tarefas)

<!-- 
  Para cada tarefa bloqueada, documente:
  - O que está bloqueando
  - Quem pode desbloquear
  - Follow-up (quando cobrar)
  - Data do bloqueio
-->

---

## 📝 Log de Progresso

<!-- 
  Formato de entrada:
  ### [YYYY-MM-DD HH:MM] Título da Atividade
  **O que foi feito:** ...
  **Por que foi feito:** ...
  **Próximos passos:** (opcional)
-->

### [YYYY-MM-DD HH:MM] Projeto iniciado

**O que foi feito:** Criei o dashboard do projeto e defini o objetivo inicial.

**Por que foi feito:** Preciso de um sistema para acompanhar o progresso e não perder contexto.

**Próximos passos:** Adicionar as primeiras tarefas no Backlog e começar a trabalhar.

---

## 🎯 Decisões Importantes

<!-- 
  Formato:
  ### [DEC-XXX] Título da Decisão
  **Data:** ...
  **Contexto:** ...
  **Decisão:** ...
  **Alternativas consideradas:** ...
  **Consequências:** ...
  **Status:** ✅ Implementado | 🚧 Em andamento | ⏸️ Pausado
-->

### [DEC-001] [Título da primeira decisão importante]

**Data:** [DD/MM/YYYY]  
**Contexto:** [Por que esta decisão foi necessária?]  
**Decisão:** [O que foi decidido?]  
**Alternativas consideradas:** [Quais outras opções foram avaliadas?]  
**Consequências:** [Qual o impacto desta decisão?]  
**Status:** [Status atual]

---

## 📈 Métricas (Opcional)

<!-- Atualize semanalmente. Pode ser omitido em projetos pequenos. -->

**Tempo Investido:** 0 horas  
**Progresso:** 0% (0/0 tarefas concluídas)  
**Velocidade Média:** - tarefas/semana  
**Taxa de Bugs:** -%

---

<!-- 
  DICAS DE USO:
  - Atualize o dashboard no início e fim de cada sessão de trabalho
  - Mantenha a seção "Próximas Ações" sempre atualizada
  - Arquive tarefas concluídas quando passar de 10 itens
  - Arquive logs antigos mensalmente
  - Use emojis para identificação visual rápida
  - Respeite o limite de WIP (máximo 2 tarefas "Em Andamento")
-->
```

#### **Guia de Preenchimento Inicial (5 minutos)**

**Passo 1: Informações Básicas (1 min)**
- Nome do projeto
- Objetivo (1-2 frases)
- Data de início
- Previsão de conclusão

**Passo 2: Primeiras Tarefas (2 min)**
- Adicione 5-10 tarefas no Backlog
- Não precisa detalhar ainda, apenas capturar ideias

**Passo 3: Definir Primeira Ação (1 min)**
- Escolha a tarefa mais importante
- Mova para "Próximas Ações" e marque como "AGORA"

**Passo 4: Primeira Entrada no Log (1 min)**
- Registre a criação do dashboard

**Passo 5: Limpar Comentários (30s)**
- Delete os comentários de instrução
- Salve o arquivo

**Total: ~5 minutos**

---

#### **Variações do Template**

**Para projetos muito pequenos (< 1 semana):**
- Omitir seção "Métricas"
- Omitir seção "Decisões Importantes"
- Simplificar estados (apenas: Backlog, A Fazer, Em Andamento, Concluído)

**Para projetos de pesquisa/escrita:**
- Adaptar tipos de cards (ex: 📝 Capítulo, 🔬 Pesquisa, ✍️ Revisão)
- Adaptar estados (ex: Rascunho, Revisão, Finalizado)

---

**Justificativa:** Um template bem feito reduz drasticamente o atrito inicial. O usuário não precisa "inventar" a estrutura do dashboard, apenas preencher.

**Critério de Sucesso:**
- Um usuário novo consegue criar seu primeiro dashboard em menos de 5 minutos
- O template é claro o suficiente para não precisar de explicação adicional
- O template funciona "out of the box" para 90% dos projetos de software

---

### **7. Guia de Uso no Cursor AI (GUIA_CURSOR_AI.md)**

**Descrição:** Um guia prático e acionável que mostra como implementar o ENDFIRST Flow especificamente no Cursor AI, aproveitando os recursos únicos da ferramenta.

#### **Estrutura do Guia**

##### **Seção 1: Setup Inicial (5 minutos)**

**Conteúdo:**
- Como estruturar a pasta do projeto
- Onde colocar o `STATUS_PROJETO.md`
- Como configurar o Cursor AI para facilitar o acesso ao dashboard

**Exemplo:**
```markdown
## Setup Inicial

### Estrutura de Pastas Recomendada

```
meu-projeto/
├── STATUS_PROJETO.md          # Dashboard principal
├── docs/
│   └── DECISOES/               # Decisões arquivadas
├── logs/
│   ├── LOG_DEZEMBRO_2025.md   # Logs arquivados
│   └── TAREFAS_CONCLUIDAS.md  # Tarefas arquivadas
├── src/                        # Código fonte
├── tests/                      # Testes
└── README.md                   # Documentação do projeto
```

### Configuração do Cursor AI

1. **Adicione o dashboard aos favoritos:**
   - Abra `STATUS_PROJETO.md`
   - Clique com botão direito na aba
   - Selecione "Pin Tab"

2. **Configure atalho para abrir o dashboard:**
   - Use `Cmd/Ctrl + P` e digite "STATUS"
   - O Cursor AI vai sugerir o arquivo automaticamente

3. **Ative o Composer:**
   - Use `Cmd/Ctrl + K` para abrir o Composer
   - Isso facilita a atualização do dashboard com IA
```

---

##### **Seção 2: Usando o Símbolo @ para Referenciar o Dashboard**

**Conteúdo:**
- Como usar `@STATUS_PROJETO.md` no chat do Cursor
- Exemplos de prompts úteis
- Como pedir ao Cursor para atualizar o dashboard

**Exemplo:**
```markdown
## Usando o @ para Referenciar

O Cursor AI permite referenciar arquivos usando `@`. Isso é poderoso para trabalhar com o dashboard.

### Prompts Úteis

**Para iniciar uma sessão:**
```
@STATUS_PROJETO.md 

Olá! Vou começar a trabalhar agora. Qual é a tarefa marcada como "AGORA"? 
Me ajude a entender o contexto dela.
```

**Para atualizar o dashboard:**
```
@STATUS_PROJETO.md 

Acabei de concluir a tarefa [nome da tarefa]. 
Atualize o dashboard:
- Mova a tarefa para "Concluído"
- Adicione uma entrada no log explicando o que foi feito
- Defina a próxima tarefa "AGORA"
```

**Para retomar após uma pausa:**
```
@STATUS_PROJETO.md 

Faz 3 dias que não mexo neste projeto. 
Me ajude a retomar:
- Resuma o que foi feito recentemente
- Mostre as decisões importantes
- Indique qual tarefa devo trabalhar agora
```

**Para analisar o progresso:**
```
@STATUS_PROJETO.md 

Analise o progresso do projeto:
- Quantas tarefas foram concluídas esta semana?
- Há algum bloqueio crítico?
- Estamos no prazo?
```
```

---

##### **Seção 3: Rituais no Cursor AI (Passo a Passo)**

**Conteúdo:**
- Ritual de Início com screenshots/exemplos
- Ritual de Fim com screenshots/exemplos
- Atalhos e dicas específicas

**Exemplo:**
```markdown
## Ritual de Início no Cursor AI (2 minutos)

### Passo 1: Abrir o Dashboard
- **Atalho:** `Cmd/Ctrl + P` → digite "STATUS" → Enter
- Ou clique na aba pinada

### Passo 2: Ler "Próximas Ações"
- Role até a seção "🎯 Próximas Ações"
- Identifique a tarefa marcada como "AGORA 👉"

### Passo 3: Usar o Cursor para Atualizar
- Abra o Composer: `Cmd/Ctrl + K`
- Digite:
  ```
  Mova a tarefa "[nome]" de "A Fazer" para "Em Andamento"
  e adicione timestamp "Iniciado em [data/hora]"
  ```
- Revise a mudança e aceite

### Passo 4: Adicionar Log
- Use o Composer novamente:
  ```
  Adicione uma entrada no log:
  - Título: "Iniciando sessão de trabalho"
  - Foco: [nome da tarefa]
  - Objetivo: [o que pretendo alcançar]
  ```

### Passo 5: Abrir Arquivos Relevantes
- Pergunte ao Cursor:
  ```
  Quais arquivos preciso abrir para trabalhar em [tarefa]?
  ```
- Abra os arquivos sugeridos

**Total: ~2 minutos** ✅
```

---

##### **Seção 4: Integração com Git**

**Conteúdo:**
- Como commitar o dashboard junto com o código
- Boas práticas de commit messages
- Git hooks opcionais

**Exemplo:**
```markdown
## Integração com Git

### Commitando o Dashboard

**Sempre commite o dashboard junto com o código:**

```bash
# Após fazer mudanças no código
git add src/
git add STATUS_PROJETO.md
git commit -m "feat: add user authentication

- Implemented JWT-based auth
- Added login and register endpoints
- Updated dashboard with progress"
```

### Boas Práticas

1. **Commite o dashboard no fim de cada sessão**
2. **Use mensagens de commit descritivas**
3. **Sincronize o log do dashboard com os commits do Git**

### Git Hook Opcional

Crie `.git/hooks/pre-commit`:

```bash
#!/bin/bash
if ! git diff --cached --name-only | grep -q "STATUS_PROJETO.md"; then
  echo "⚠️  Você esqueceu de atualizar o STATUS_PROJETO.md!"
  echo "Deseja continuar mesmo assim? (y/n)"
  read answer
  if [ "$answer" != "y" ]; then
    exit 1
  fi
fi
```

Torne executável:
```bash
chmod +x .git/hooks/pre-commit
```
```

---

##### **Seção 5: Atalhos e Dicas Específicas do Cursor AI**

**Conteúdo:**
- Atalhos de teclado úteis
- Snippets para acelerar atualizações
- Truques para usar a IA do Cursor eficientemente

---

##### **Seção 6: Troubleshooting (Problemas Comuns)**

**Conteúdo:**
- "O Cursor não encontra meu dashboard" → Solução
- "O Composer não está atualizando corretamente" → Solução
- "O dashboard está ficando muito grande" → Solução
- "Esqueci de atualizar o dashboard por vários dias" → Solução

**Exemplo:**
```markdown
## Troubleshooting

### Problema: "O dashboard está ficando muito grande (>500 linhas)"

**Solução:**
1. Arquive tarefas concluídas antigas:
   - Mova as 20+ tarefas mais antigas para `logs/TAREFAS_CONCLUIDAS.md`
   - Mantenha apenas as últimas 10 no dashboard

2. Arquive logs antigos:
   - Mova entradas de log antigas para `logs/LOG_[MES]_[ANO].md`
   - Mantenha apenas as últimas 20-30 entradas no dashboard

3. Revise o Backlog:
   - Delete tarefas que não fazem mais sentido
   - Mova tarefas de baixíssima prioridade para um arquivo separado

### Problema: "Esqueci de atualizar o dashboard por vários dias"

**Solução:**
1. Use o histórico do Git para reconstruir o que foi feito:
   ```bash
   git log --oneline --since="3 days ago"
   ```

2. Peça ajuda ao Cursor:
   ```
   @STATUS_PROJETO.md
   
   Olhe os commits dos últimos 3 dias e atualize o dashboard:
   - Adicione entradas no log para cada commit importante
   - Atualize o status das tarefas baseado no que foi feito
   - Identifique a próxima tarefa "AGORA"
   ```

3. Execute o Ritual de Retomada completo
```

---

**Justificativa:** Um guia específico para o Cursor AI traduz a metodologia agnóstica em ações concretas, reduzindo o atrito e aumentando a adoção.

**Critério de Sucesso:**
- O usuário consegue implementar o Flow no Cursor AI sem travar
- O guia responde 90%+ das dúvidas específicas da ferramenta
- O usuário aproveita os recursos únicos do Cursor (IA, Composer, @) para tornar o Flow mais eficiente

---

### **8. Guia de Retomada de Contexto (GUIA_RETOMADA_CONTEXTO.md)**

**Descrição:** Um guia focado especificamente em como retomar projetos após pausas (horas, dias, semanas ou meses), minimizando o tempo de "reaquecimento".

#### **Estrutura do Guia**

##### **Seção 1: Por que Retomar é Difícil?**

**Conteúdo:**
- Ciência por trás da perda de contexto (memória de trabalho, context switching)
- O custo real de pausas longas (estudos mostram que pode levar 20-30 minutos para retomar)
- Como o ENDFIRST Flow resolve isso

---

##### **Seção 2: Checklist de Retomada Rápida (1 página)**

**Conteúdo:**
- Checklist visual e acionável para diferentes tipos de pausa

**Exemplo:**
```markdown
## Checklist de Retomada

### Pausa Curta (< 24 horas)

- [ ] Abrir `STATUS_PROJETO.md`
- [ ] Ler seção "Próximas Ações"
- [ ] Verificar última entrada do log
- [ ] Executar Ritual de Início normal

**Tempo estimado:** 2 minutos

---

### Pausa Média (1-3 dias)

- [ ] Abrir `STATUS_PROJETO.md`
- [ ] Ler "Visão Geral" (relembrar objetivo)
- [ ] Ler últimas 5 entradas do log
- [ ] Verificar tarefas "Bloqueadas" (algum desbloqueio?)
- [ ] Ler seção "Próximas Ações"
- [ ] Executar Ritual de Início normal

**Tempo estimado:** 5 minutos

---

### Pausa Longa (1-2 semanas)

- [ ] Abrir `STATUS_PROJETO.md`
- [ ] Ler "Visão Geral" completa
- [ ] Ler últimas 10 entradas do log
- [ ] Revisar "Decisões Importantes"
- [ ] Verificar todas as tarefas "Bloqueadas"
- [ ] Revisar tarefas "Em Andamento" (ainda fazem sentido?)
- [ ] Ler seção "Próximas Ações"
- [ ] Perguntar ao Cursor: "Me ajude a retomar este projeto"
- [ ] Executar Ritual de Início normal

**Tempo estimado:** 10 minutos

---

### Pausa Muito Longa (1+ mês)

- [ ] Abrir `STATUS_PROJETO.md`
- [ ] Ler "Visão Geral" completa
- [ ] Ler TODO o log de progresso (ou resumo mensal)
- [ ] Revisar TODAS as "Decisões Importantes"
- [ ] Revisar todas as tarefas em todos os estados
- [ ] Verificar se o objetivo do projeto ainda faz sentido
- [ ] Atualizar prioridades se necessário
- [ ] Perguntar ao Cursor: "Analise este projeto e me dê um resumo executivo"
- [ ] Considerar fazer um "Pilar 0" novo (redefinir estado final)
- [ ] Executar Ritual de Retomada Longa

**Tempo estimado:** 30-60 minutos
```

---

##### **Seção 3: Técnicas para Reconstruir o "Estado Mental"**

**Conteúdo:**
- Como usar o log para reconstruir o raciocínio
- Como usar decisões importantes para relembrar o "por quê"
- Como usar o Git para ver a evolução do código
- Como usar o Cursor AI para gerar resumos

**Exemplo:**
```markdown
## Técnicas de Reconstrução de Contexto

### Técnica 1: Leitura Reversa do Log

**Como fazer:**
1. Comece pela entrada mais recente do log
2. Leia de trás para frente até encontrar a última "grande decisão" ou "marco importante"
3. Isso reconstrói a narrativa do projeto

**Por que funciona:**
- O cérebro humano é melhor em lembrar eventos recentes
- Ler de trás para frente cria uma "linha do tempo mental"

---

### Técnica 2: Mapa Mental de Decisões

**Como fazer:**
1. Leia todas as entradas em "Decisões Importantes"
2. Crie um mapa mental (mental ou no papel) conectando as decisões
3. Identifique a "espinha dorsal" arquitetural do projeto

**Por que funciona:**
- Decisões importantes são os "pilares" do projeto
- Entender os pilares facilita entender os detalhes

---

### Técnica 3: Diff do Git

**Como fazer:**
```bash
# Ver o que mudou desde a última vez que você trabalhou
git log --since="2 weeks ago" --oneline

# Ver o diff de um commit específico
git show [commit-hash]

# Ver todos os arquivos modificados
git diff --name-only HEAD~10 HEAD
```

**Por que funciona:**
- O código é a "verdade objetiva" do que foi feito
- Ver as mudanças reais ajuda a reconstruir o contexto

---

### Técnica 4: Resumo Gerado por IA

**Como fazer:**
```
@STATUS_PROJETO.md

Analise este dashboard e gere um resumo executivo:
- Objetivo do projeto
- Progresso até agora (%)
- Últimas 3 atividades importantes
- Próximos 3 passos
- Bloqueios críticos
- Decisões arquiteturais principais

Formato: bullet points, máximo 10 linhas.
```

**Por que funciona:**
- A IA consegue processar todo o dashboard rapidamente
- Um resumo de 10 linhas é mais fácil de absorver que 500 linhas de dashboard
```

---

##### **Seção 4: Estratégias para Pausas Muito Longas (30+ dias)**

**Conteúdo:**
- Como lidar com projetos "congelados"
- Quando vale a pena "recomeçar do zero"
- Como arquivar projetos antigos

---

##### **Seção 5: Prevenção de Perda de Contexto**

**Conteúdo:**
- Como escrever logs que seu "eu futuro" vai agradecer
- Como documentar decisões de forma que elas façam sentido meses depois
- Como usar o dashboard para "deixar migalhas" para si mesmo

**Exemplo:**
```markdown
## Prevenção: Deixe Migalhas para Seu Eu Futuro

### Dica 1: Escreva Logs Pensando em "Eu Daqui a 1 Mês"

**Ruim:**
```markdown
### [2025-12-30] Mudei a API

**O que:** Mudei a API.
```

**Bom:**
```markdown
### [2025-12-30] Migrei de REST para GraphQL

**O que:** Substituí todos os endpoints REST por um único endpoint GraphQL.

**Por quê:** O cliente pediu para reduzir o número de requests. GraphQL permite buscar múltiplos recursos em uma única query.

**Impacto:** Redução de 60% no número de requests do frontend.

**Decisão relacionada:** Ver [DEC-003] sobre escolha de GraphQL vs REST.
```

**Por que o segundo é melhor:**
- Contexto completo (por que a mudança foi feita)
- Impacto mensurável
- Link para decisão relacionada (rastreabilidade)

---

### Dica 2: Use "Próximos Passos" Generosamente

Sempre que pausar o trabalho, deixe uma nota clara do que fazer a seguir:

```markdown
**Próximos passos:** 
1. Testar o endpoint /api/users com Postman
2. Se passar, criar PR para review
3. Se falhar, debugar o middleware de autenticação (suspeita: linha 45 de auth.js)
```

Isso elimina a paralisia de "por onde eu começo?" ao retomar.

---

### Dica 3: Documente "Armadilhas" e "Gotchas"

Se você encontrou um bug difícil ou uma configuração tricky, documente:

```markdown
### [2025-12-28] Descoberto bug no cache do Redis

**Armadilha:** O Redis estava cacheando tokens JWT expirados porque o TTL não estava sendo setado corretamente.

**Solução:** Adicionar `EX 86400` no comando SET do Redis.

**Onde:** arquivo `cache/redis.js`, linha 23.

**Nota para o futuro:** Se usuários reportarem "token inválido" aleatoriamente, verificar o TTL do Redis primeiro.
```

Isso economiza horas de debugging no futuro.
```

---

**Justificativa:** Retomar projetos é um dos maiores desafios de desenvolvedores individuais. Um guia focado nisso, com checklists e técnicas práticas, reduz drasticamente o tempo de "reaquecimento".

**Critério de Sucesso:**
- O tempo de retomada é reduzido em pelo menos 50%
- O usuário sente confiança ao retomar (não sente que "perdeu o fio da meada")
- O guia é consultado regularmente após pausas

---

### **9. Caso de Uso Completo (CASO_DE_USO_ENDFIRST_FLOW.md)**

**Descrição:** A documentação completa da aplicação dos 11 pilares do ENDFIRST para criar o próprio ENDFIRST Flow, servindo como prova de conceito e material para o Artigo 2.

#### **Estrutura do Caso de Uso**

##### **Seção 1: Introdução**

**Conteúdo:**
- Contexto: Por que o ENDFIRST Flow foi criado?
- Problema: Qual gap ele preenche?
- Abordagem: Como o método ENDFIRST foi aplicado para criar o Flow?

---

##### **Seção 2: Aplicação dos 11 Pilares**

**Conteúdo:**
- Narrativa completa de como cada pilar foi aplicado
- Todos os documentos intermediários (Pilares 0 a 7)
- Decisões tomadas em cada pilar
- Desafios enfrentados e como foram superados

**Estrutura:**
```markdown
## Pilar 0: Estado Final

### O que foi definido:
[Cópia do PILAR_0_ESTADO_FINAL.md]

### Insights:
- Definir métricas de sucesso claras foi crucial
- A ideia de ter 6 entregáveis (não 4) surgiu durante a validação

---

## Pilar 0.5: Mapa de Conhecimento

### O que foi mapeado:
[Cópia do PILAR_0.5_MAPA_CONHECIMENTO.md]

### Insights:
- Identificar 5 áreas de conhecimento ajudou a estruturar a pesquisa
- A decisão de usar o Banco de Referências para armazenar o conhecimento do Flow foi tomada aqui

---

[... continua para todos os 11 pilares ...]
```

---

##### **Seção 3: Aprendizados Capturados (Pilar 7)**

**Conteúdo:**
- O que funcionou bem?
- O que não funcionou?
- O que faria diferente na próxima vez?
- Insights acionáveis para outros projetos

**Exemplo:**
```markdown
## Aprendizados Capturados

### O que funcionou bem:

1. **Validação iterativa com o usuário:** Apresentar cada pilar individualmente para validação evitou retrabalho massivo no final.

2. **Aplicar o método para criar o método:** A meta-aplicação do ENDFIRST validou que o método realmente funciona na prática.

3. **Foco em robustez desde o início:** Não aceitar soluções "simplistas" (como 4 estados ao invés de 8) garantiu que o resultado final fosse realmente robusto.

### O que não funcionou:

1. **Tentar criar tudo de uma vez:** Inicialmente, tentei criar todos os pilares de uma vez e apresentar tudo junto. Isso foi rejeitado pelo usuário, que queria validar passo a passo.

2. **Subestimar a complexidade do Ciclo de Vida:** A primeira versão tinha apenas 4 estados, o que era insuficiente. Precisei refazer com 8 estados.

3. **Esquecer dos Tipos de Cards:** Inicialmente, não pensei em tipificar as tarefas (Feature, Bug, etc.), o que foi identificado como uma lacuna crítica.

### O que faria diferente:

1. **Começar com validação iterativa desde o início:** Não tentar "impressionar" com volume, mas focar em qualidade e validação constante.

2. **Pesquisar mais antes de propor:** Antes de propor 4 estados, deveria ter pesquisado metodologias ágeis para entender que 8 estados é o padrão.

3. **Documentar decisões em tempo real:** Algumas decisões foram tomadas "na hora" sem documentação adequada, o que dificultou a reconstrução do raciocínio depois.

### Insights acionáveis:

1. **"Simplicidade" não significa "simplista":** Um sistema simples de usar pode (e deve) ter complexidade interna bem pensada.

2. **Validação > Velocidade:** É melhor gastar 2x mais tempo validando do que ter que refazer tudo depois.

3. **Meta-aplicação é poderosa:** Usar o próprio método para melhorar o método é uma forma poderosa de validação e aprendizado.
```

---

##### **Seção 4: Métricas de Sucesso Alcançadas**

**Conteúdo:**
- Comparação entre as métricas definidas no Pilar 0 e os resultados reais
- Análise de desvios

---

##### **Seção 5: Reflexões sobre a Meta-Aplicação**

**Conteúdo:**
- O que significa aplicar o ENDFIRST para criar o ENDFIRST Flow?
- Insights filosóficos sobre metodologias auto-referentes
- Como isso valida (ou invalida) o método?

---

**Justificativa:** Um caso de uso completo serve como prova de conceito do método e como material rico para artigos, apresentações e ensino.

**Critério de Sucesso:**
- O caso de uso inspira confiança de que o método funciona
- O caso de uso serve como base para o Artigo 2
- O caso de uso tem pelo menos 3 insights acionáveis que podem ser aplicados em outros projetos

---

### **10. Atualização do Índice de Navegação (INDICE_DE_NAVEGACAO.md)**

**Descrição:** Adicionar a seção "ENDFIRST Flow" ao índice existente do pacote v11.5, facilitando a descoberta e navegação dos novos documentos.

#### **Conteúdo a Adicionar**

```markdown
## 🔄 ENDFIRST Flow (Metodologia de Acompanhamento de Projeto)

### Documentos Principais
- [ENDFIRST Flow - Guia Completo](METODO/flow/ENDFIRST_FLOW.md) - Documentação completa da metodologia
- [Template de Dashboard](METODO/flow/TEMPLATE_DASHBOARD.md) - Template pronto para usar
- [Guia de Uso no Cursor AI](METODO/flow/GUIA_CURSOR_AI.md) - Como implementar o Flow no Cursor AI
- [Guia de Retomada de Contexto](METODO/flow/GUIA_RETOMADA_CONTEXTO.md) - Como retomar projetos após pausas

### Caso de Uso
- [Caso de Uso Completo](METODO/flow/CASO_DE_USO_ENDFIRST_FLOW.md) - Aplicação do ENDFIRST para criar o Flow

### Pilares (Processo de Criação)
- [Pilar 0: Estado Final](METODO/casos_uso/GESTAO_PROJETO/PILAR_0_ESTADO_FINAL.md)
- [Pilar 0.5: Mapa de Conhecimento](METODO/casos_uso/GESTAO_PROJETO/PILAR_0.5_MAPA_CONHECIMENTO.md)
- [Pilar 1: Obstáculos](METODO/casos_uso/GESTAO_PROJETO/PILAR_1_OBSTACULOS.md)
- [Pilar 2: Recursos](METODO/casos_uso/GESTAO_PROJETO/PILAR_2_RECURSOS.md)
- [Pilar 3: Escopo](METODO/casos_uso/GESTAO_PROJETO/PILAR_3_ESCOPO.md)
- [Pilar 3.5: Análise de Riscos](METODO/casos_uso/GESTAO_PROJETO/PILAR_3.5_ANALISE_RISCOS.md)
- [Pilar 4: Planejamento Reverso](METODO/casos_uso/GESTAO_PROJETO/PILAR_4_PLANEJAMENTO_REVERSO.md)
- [Pilar 4.5: Roadmap](METODO/casos_uso/GESTAO_PROJETO/PILAR_4.5_ROADMAP.md)
- [Pilar 5: Validação Externa](METODO/casos_uso/GESTAO_PROJETO/PILAR_5_VALIDACAO.md)
- [Pilar 6: Execução](METODO/casos_uso/GESTAO_PROJETO/PILAR_6_EXECUCAO.md)
- [Pilar 7: Aprendizados](METODO/casos_uso/GESTAO_PROJETO/PILAR_7_APRENDIZADOS.md)

### Quick Start
1. Leia o [Guia Completo](METODO/flow/ENDFIRST_FLOW.md) (15 min)
2. Copie o [Template de Dashboard](METODO/flow/TEMPLATE_DASHBOARD.md) para seu projeto
3. Siga o [Guia de Uso no Cursor AI](METODO/flow/GUIA_CURSOR_AI.md) para setup
4. Execute seu primeiro Ritual de Início de Sessão
```

#### **Critérios de Qualidade**

- [ ] Links funcionam corretamente
- [ ] Descrições de 1 linha são claras e informativas
- [ ] Seção "Quick Start" guia o usuário pelos primeiros passos
- [ ] Integração harmoniosa com o índice existente

---

**Justificativa:** Um índice atualizado garante que os novos documentos sejam descobertos e usados. Sem isso, o Flow ficaria "perdido" no pacote.

**Critério de Sucesso:**
- O usuário encontra os documentos do Flow em menos de 10 segundos
- O índice é a primeira coisa consultada ao abrir o pacote no Cursor AI

---

## ❌ FORA DO ESCOPO (Versões Futuras)

### **1. Integração com APIs Externas**

**Descrição:** Conectar o dashboard com ferramentas como Jira, Trello, Notion, Linear, ou APIs de métricas (GitHub, GitLab).

**Por que está fora:** Adiciona complexidade técnica desnecessária para o MVP. O foco é em um sistema autônomo, simples e baseado em arquivos Markdown. Integrações requerem autenticação, sincronização, tratamento de erros de rede, etc.

**Quando considerar:** v2.0, após validar que o sistema básico funciona e há demanda clara dos usuários. Priorizar integrações baseadas em feedback real.

**Alternativa no MVP:** Usar o dashboard como fonte única de verdade e atualizar ferramentas externas manualmente quando necessário.

---

### **2. Geração Automática de Relatórios**

**Descrição:** Scripts para gerar relatórios de progresso, gráficos de burndown, velocity charts, ou estatísticas automaticamente a partir do dashboard.

**Por que está fora:** Automação prematura. O processo manual inicial ajuda a validar a utilidade do sistema e entender quais métricas realmente importam. Criar scripts de automação antes de saber o que automatizar é desperdício.

**Quando considerar:** v2.0, se houver demanda clara. Pode ser implementado como scripts Python que parsam o dashboard Markdown.

**Alternativa no MVP:** Atualizar a seção "Métricas" manualmente uma vez por semana. Isso leva ~2 minutos e é suficiente para projetos individuais.

---

### **3. Suporte a Múltiplos Colaboradores**

**Descrição:** Funcionalidades específicas para gestão de equipes, como:
- Atribuição de tarefas a pessoas específicas
- Sincronização de dashboards entre membros da equipe
- Resolução de conflitos em edições simultâneas
- Permissões e controle de acesso

**Por que está fora:** O foco inicial é no **desenvolvedor individual**, que é o principal caso de uso do Cursor AI. Adicionar suporte a equipes multiplica a complexidade por 10x (sincronização, conflitos, comunicação, etc.).

**Quando considerar:** v3.0, após dominar completamente o caso individual. Requer repensar a arquitetura (possivelmente migrar de Markdown para banco de dados).

**Alternativa no MVP:** Para projetos colaborativos, cada membro mantém seu próprio dashboard e sincroniza manualmente via reuniões ou ferramentas externas (Slack, email).

---

### **4. Múltiplos Templates de Dashboard**

**Descrição:** Variações do dashboard para diferentes tipos de projeto:
- Template para projetos de pesquisa/escrita
- Template para projetos de design
- Template para projetos de data science
- Template para projetos de infraestrutura

**Por que está fora:** Manter a simplicidade. Um único template robusto e adaptável é suficiente para a v1.0. Criar múltiplos templates antes de validar o template base é desperdício.

**Quando considerar:** v2.0, com base em feedback sobre adaptações necessárias. Criar templates específicos apenas se houver demanda clara de pelo menos 3 usuários diferentes.

**Alternativa no MVP:** O template base é flexível o suficiente para ser adaptado manualmente. Incluir seção no guia sobre "Como adaptar o template para seu contexto".

---

### **5. Aplicativo ou Plugin Nativo para Cursor AI**

**Descrição:** Criar uma extensão nativa do Cursor AI que:
- Automatize partes do Flow (ex: atualizar dashboard ao commitar)
- Adicione UI visual para o dashboard (ex: quadro Kanban interativo)
- Integre notificações e lembretes
- Sincronize com serviços externos

**Por que está fora:** Requer desenvolvimento de software complexo, conhecimento da API do Cursor AI (que pode não ser pública), e manutenção contínua. Fora do escopo de uma metodologia baseada em documentos.

**Quando considerar:** v3.0+, se o Flow se tornar amplamente adotado e houver recursos (tempo, dinheiro) para desenvolver e manter um plugin.

**Alternativa no MVP:** Usar os recursos nativos do Cursor AI (Composer, chat, @) para interagir com o dashboard. Isso já é muito poderoso.

---

### **6. Sistema de Notificações ou Lembretes**

**Descrição:** Alertas automáticos para:
- Lembrar o usuário de atualizar o dashboard
- Notificar sobre tarefas bloqueadas há muito tempo
- Alertar sobre deadlines próximos
- Sugerir quando fazer retrospectivas

**Por que está fora:** Adiciona dependência de ferramentas externas (cron jobs, serviços de notificação, etc.). O usuário deve desenvolver o hábito naturalmente, não depender de lembretes externos.

**Quando considerar:** v2.0, se o abandono gradual for um problema persistente após validação com usuários reais.

**Alternativa no MVP:** Incluir no guia dicas sobre como criar o hábito (ex: "Sempre atualize o dashboard antes de fechar o Cursor AI"). Confiar na disciplina do usuário.

---

### **7. Métricas Avançadas e Analytics**

**Descrição:** Análises sofisticadas como:
- Velocity (tarefas/sprint)
- Cycle time (tempo médio por tarefa)
- Lead time (tempo do backlog até conclusão)
- Previsão de conclusão baseada em dados históricos
- Análise de bottlenecks
- Heatmaps de produtividade

**Por que está fora:** Complexidade desnecessária para o MVP. Foco em funcionalidade básica primeiro. Métricas avançadas requerem volume significativo de dados históricos para serem úteis.

**Quando considerar:** v2.0, se houver interesse em otimização baseada em dados. Pode ser implementado como scripts de análise separados.

**Alternativa no MVP:** Métricas simples (tempo investido, progresso %, velocidade semanal) são suficientes e podem ser calculadas manualmente.

---

### **8. Versionamento Automático do Dashboard**

**Descrição:** Sistema que cria snapshots automáticos do dashboard em intervalos regulares, permitindo:
- Ver o estado do projeto em qualquer ponto no tempo
- Comparar versões (diff)
- Restaurar versões antigas
- Análise de evolução do projeto

**Por que está fora:** Git já faz isso se o usuário commitar regularmente. Não justifica desenvolvimento adicional.

**Quando considerar:** Talvez nunca, se o Git for suficiente. Reavaliar apenas se houver feedback de que o Git não está atendendo esta necessidade.

**Alternativa no MVP:** Commitar o dashboard regularmente no Git. Usar `git log` e `git diff` para ver histórico e mudanças.

---

### **9. Modo Offline/Sincronização**

**Descrição:** Suporte para trabalhar offline e sincronizar mudanças quando voltar online, especialmente útil para:
- Trabalho em aviões/trens
- Ambientes com internet instável
- Sincronização entre múltiplos dispositivos

**Por que está fora:** Markdown + Git já funciona offline. Sincronização é responsabilidade do Git, não do Flow.

**Quando considerar:** Não é necessário. Git resolve este problema.

**Alternativa no MVP:** Usar Git normalmente. Funciona offline por padrão.

---

### **10. Gamificação e Recompensas**

**Descrição:** Elementos de gamificação como:
- Pontos por tarefas concluídas
- Badges por conquistas (ex: "10 tarefas sem bugs")
- Streaks (dias consecutivos trabalhando)
- Leaderboards (para equipes)

**Por que está fora:** Pode ser distrativo e adicionar complexidade desnecessária. O foco deve ser em produtividade real, não em "joguinhos".

**Quando considerar:** v3.0+, se houver demanda clara e evidências de que gamificação aumenta a adoção. Requer pesquisa sobre eficácia.

**Alternativa no MVP:** A satisfação de ver o progresso real no dashboard é recompensa suficiente.

---

## 📊 Resumo do Escopo

| Categoria | Dentro do Escopo (v1.0) | Fora do Escopo (Futuro) |
|:----------|:------------------------|:------------------------|
| **Documentos** | 5 guias + 1 template + 1 caso de uso + índice | Templates múltiplos, relatórios automáticos |
| **Funcionalidades** | Dashboard, Rituais, Log, Ciclo de vida (8 estados), Tipos de cards (8 tipos) | Automações, Integrações, Notificações, Analytics avançado |
| **Público-alvo** | Desenvolvedor individual | Equipes colaborativas |
| **Plataforma** | Markdown + Cursor AI (agnóstico) | Plugin nativo, APIs externas, Apps móveis |
| **Métricas** | Básicas (tempo, progresso %, velocidade) | Avançadas (cycle time, lead time, previsões) |
| **Manutenção** | Manual (com automações opcionais via Git hooks) | Totalmente automatizada |

---

## 🎯 Princípio Norteador do Escopo (Reforço)

> **"Simplicidade acima de tudo. O ENDFIRST Flow v1.0 deve resolver 80% dos problemas com 20% da complexidade."**

**Teste de Escopo:**
Toda funcionalidade proposta deve passar por estas 3 perguntas:

1. **É absolutamente essencial para o problema central (perda de contexto)?**
   - Se não, vai para versões futuras.

2. **Pode ser implementado sem adicionar burocracia significativa?**
   - Se adiciona mais de 2 minutos ao fluxo de trabalho diário, vai para versões futuras.

3. **Funciona sem dependências externas complexas?**
   - Se requer APIs, servidores, ou ferramentas externas, vai para versões futuras.

---

## ✅ Checkpoint de Validação Final

Antes de avançar para o Pilar 3.5 (Análise de Riscos), valide:

- [ ] O escopo da v1.0 resolve o problema central (perda de contexto)?
- [ ] Tudo que está dentro do escopo é realmente essencial?
- [ ] As exclusões fazem sentido e estão bem justificadas?
- [ ] O escopo é viável de ser entregue em 3 dias de trabalho focado?
- [ ] Cada item dentro do escopo tem:
  - [ ] Descrição detalhada
  - [ ] Componentes/seções específicas
  - [ ] Critérios de qualidade
  - [ ] Exemplos práticos
  - [ ] Justificativa clara
  - [ ] Critérios de sucesso

---

## 🚀 Próximos Passos

Com o escopo calibrado e detalhado, o próximo passo é avançar para o **Pilar 3.5: Análise de Riscos**, onde aprofundaremos nos potenciais problemas que podem surgir dentro deste escopo definido e criaremos estratégias de mitigação robustas.

---

**Versão:** v3.0 (Revisão Completa e Robusta)  
**Data:** 30 de Dezembro de 2025  
**Autor:** Manus AI  
**Validado por:** Usuário (em processo)
