# Pilar 3: Calibragem de Escopo - Metodologia de Acompanhamento de Projeto ("ENDFIRST Flow")

**Data:** 30 de Dezembro de 2025  
**Versão:** v2.0

---

## 🎯 Definição do Escopo

A calibragem de escopo é crucial para garantir uma entrega de valor rápida e focada. Este pilar define claramente **o que entra** e **o que fica de fora** da versão 1.0 do ENDFIRST Flow, seguindo o princípio de **Produto Mínimo Viável (MVP)**.

---

## ✅ DENTRO DO ESCOPO (v1.0)

### **1. Dashboard de Projeto em Markdown**

**Descrição:** Um arquivo único `STATUS_PROJETO.md` que centraliza todo o acompanhamento do projeto.

**Componentes incluídos:**
- Seção de Visão Geral (nome, objetivo, status)
- Seção de Próximas Ações (3-5 tarefas prioritárias)
- Seção de Tarefas por Status (A Fazer, Em Andamento, Bloqueado, Concluído)
- Seção de Log de Progresso (changelog cronológico)
- Seção de Decisões Importantes (registro de escolhas críticas)
- Seção de Métricas (opcional: tempo investido, progresso %)

**Justificativa:** O dashboard é o coração do Flow. Sem ele, não há metodologia.

**Critério de Sucesso:** O usuário consegue entender o estado do projeto em menos de 30 segundos.

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

#### **Definition of Done (DoD) - Em Andamento → Concluído**

Uma tarefa só pode ser marcada como "Concluída" se atender **TODOS** os critérios abaixo:

- [ ] **Critério de aceitação atendido:** Tudo que foi definido na DoR foi entregue
- [ ] **Testado:** A funcionalidade foi testada e funciona conforme esperado
- [ ] **Documentado:** Se necessário, documentação foi atualizada (README, comentários, etc.)
- [ ] **Commitado:** Código foi commitado no Git com mensagem clara
- [ ] **Revisado:** Se aplicável, passou por code review ou auto-revisão
- [ ] **Sem débito técnico crítico:** Não deixou problemas graves para trás

**Ação obrigatória ao fazer a transição:**
- Adicionar uma entrada no log: "Concluído [nome da tarefa] - [breve descrição do resultado]"
- Mover a tarefa para a seção "Concluído" do dashboard
- Arquivar a tarefa se a seção "Concluído" tiver mais de 10 itens

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

#### **Exemplos Práticos de Cards**

**Exemplo 1: Feature**
```markdown
## [🎯 Feature] [Em Andamento] Implementar busca por filtros

**Descrição:** Adicionar filtros de data, categoria e status na tela de busca.

**Critério de Aceitação:**
- Usuário pode filtrar por data (range)
- Usuário pode filtrar por categoria (dropdown)
- Usuário pode filtrar por status (checkboxes)
- Filtros funcionam em combinação

**Estimativa:** Grande (6-8 horas)
**Prioridade:** Alta
**Iniciado em:** 30/12/2025 14:00
```

**Exemplo 2: Bug**
```markdown
## [🐛 Bug] [Em Teste] Corrigir erro 500 ao salvar perfil

**Descrição:** Ao salvar perfil com avatar grande (>2MB), API retorna erro 500.

**Causa Raiz:** Falta validação de tamanho de arquivo no backend.

**Solução:** Adicionar validação de tamanho (max 2MB) e retornar erro 400 com mensagem clara.

**Estimativa:** Pequena (1-2 horas)
**Prioridade:** Crítica
**Iniciado em:** 30/12/2025 10:00
**Concluído em:** 30/12/2025 11:30
```

**Exemplo 3: Spike**
```markdown
## [🔬 Spike] [Concluído] Investigar uso de WebSockets vs. Polling

**Descrição:** Avaliar qual abordagem usar para atualizações em tempo real.

**Descobertas:**
- WebSockets: Mais eficiente, mas requer infraestrutura adicional
- Polling: Mais simples, mas gera mais tráfego

**Recomendação:** Usar polling para MVP, migrar para WebSockets na v2.0.

**Próximos passos:** Implementar polling com intervalo de 5 segundos.

**Estimativa:** Média (3-4 horas)
**Prioridade:** Média
**Concluído em:** 29/12/2025
```

---

**Justificativa:** Um ciclo de vida robusto com DoR, DoD e tipificação clara garante qualidade, clareza e rastreabilidade. Os 8 estados e 8 tipos de cards cobrem 95%+ dos cenários reais de desenvolvimento individual.

**Critério de Sucesso:** 
- O usuário nunca fica em dúvida sobre qual estado ou tipo usar
- Tarefas não ficam presas em "Em Andamento" indefinidamente
- O dashboard reflete com precisão o estado e a natureza real do projeto
- É possível analisar métricas por tipo (ex: "Quantos bugs resolvi este mês?")

---

### **3. Rituais de Início e Fim de Sessão**

**Descrição:** Processos simples e rápidos para "abrir" e "fechar" o contexto de trabalho.

**Ritual de Início (máximo 2 minutos):**
1. Abrir o `STATUS_PROJETO.md` no Cursor AI
2. Ler a seção "Próximas Ações"
3. Escolher a tarefa "AGORA" e atualizar o status para "Em Andamento"

**Ritual de Fim (máximo 2 minutos):**
1. Atualizar o status da tarefa atual
2. Adicionar uma entrada no Log de Progresso (o que foi feito + por quê)
3. Definir a próxima tarefa "AGORA" para a próxima sessão

**Justificativa:** Rituais curtos têm maior chance de serem seguidos. Foco em capturar o essencial.

**Critério de Sucesso:** O usuário consegue executar cada ritual em menos de 2 minutos.

---

### **4. Log de Progresso (Changelog)**

**Descrição:** Um registro cronológico simples das atividades e decisões.

**Formato de entrada:**
```markdown
### [YYYY-MM-DD HH:MM] - Título da Atividade

**O que foi feito:** Descrição breve da ação realizada.

**Por que foi feito:** Contexto e justificativa da decisão.

**Próximos passos:** O que fazer a seguir (opcional).
```

**Regras:**
- Máximo 3-5 linhas por entrada
- Foco em "o que" e "por que", não em "como"
- Entradas mais recentes no topo

**Justificativa:** Um log simples é melhor que nenhum log. Inspirado em Git commits.

**Critério de Sucesso:** O usuário consegue reconstruir o contexto do projeto lendo apenas o log.

---

### **5. Guia Completo da Metodologia**

**Descrição:** O documento `ENDFIRST_FLOW.md` que explica todos os conceitos, princípios e processos.

**Seções incluídas:**
- Introdução e filosofia
- Princípios fundamentais
- Ciclo de vida da tarefa
- Rituais de início e fim
- Sistema de log de progresso
- Integração com os 11 pilares do ENDFIRST
- Manutenção e arquivamento
- Adaptações para diferentes tamanhos de projeto
- Limitações e evolução futura
- Glossário de termos

**Justificativa:** Documentação completa garante autonomia do usuário.

**Critério de Sucesso:** O usuário consegue implementar o Flow sem ajuda externa.

---

### **6. Template de Dashboard**

**Descrição:** O arquivo `TEMPLATE_DASHBOARD.md` pronto para copiar, colar e usar.

**Características:**
- Autoexplicativo (comentários em cada seção)
- Utilizável em menos de 5 minutos
- Cabe em uma tela (sem scroll excessivo)
- Facilmente editável em qualquer editor Markdown

**Justificativa:** Reduzir o atrito inicial é crítico para adoção.

**Critério de Sucesso:** Um usuário novo consegue criar seu primeiro dashboard em menos de 5 minutos.

---

### **7. Guia de Uso no Cursor AI**

**Descrição:** O documento `GUIA_CURSOR_AI.md` com instruções específicas para implementar o Flow no Cursor AI.

**Seções incluídas:**
- Como estruturar a pasta do projeto
- Como usar o símbolo `@` para referenciar o dashboard
- Passo a passo do ritual de início no Cursor AI
- Passo a passo do ritual de fim no Cursor AI
- Como usar o Composer para atualizar o dashboard
- Integração com Git
- Atalhos e dicas específicas
- Troubleshooting (problemas comuns)

**Justificativa:** Traduzir a teoria em prática acionável para a ferramenta principal.

**Critério de Sucesso:** O usuário consegue implementar o Flow no Cursor AI sem travar.

---

### **8. Guia de Retomada de Contexto**

**Descrição:** O documento `GUIA_RETOMADA_CONTEXTO.md` focado em retomar projetos após pausas.

**Seções incluídas:**
- Checklist de retomada (1 página)
- Como reconstruir o "estado mental" do projeto
- Técnicas para relembrar decisões passadas
- Como usar o log de progresso para retomar
- Estratégias para pausas longas (30+ dias)
- Fluxograma de decisão ("Por onde eu começo?")

**Justificativa:** Este é o problema central que motivou a criação do Flow.

**Critério de Sucesso:** O tempo de retomada é reduzido em pelo menos 50%.

---

### **9. Caso de Uso Completo**

**Descrição:** O documento `CASO_DE_USO_ENDFIRST_FLOW.md` narrando a criação do próprio Flow.

**Seções incluídas:**
- Narrativa completa da aplicação dos 11 pilares
- Todos os documentos intermediários (Pilares 0 a 7)
- Aprendizados capturados
- Métricas de sucesso alcançadas
- Reflexões sobre a meta-aplicação do método

**Justificativa:** Prova de conceito e material para o Artigo 2.

**Critério de Sucesso:** O caso de uso inspira confiança e demonstra o poder do método.

---

### **10. Atualização do Índice de Navegação**

**Descrição:** Adicionar a seção "ENDFIRST Flow" ao `INDICE_DE_NAVEGACAO.md` existente.

**Conteúdo:**
- Links diretos para todos os 5 documentos principais
- Descrição de 1 linha para cada documento
- Integração com a estrutura existente do índice

**Justificativa:** Facilitar a descoberta e navegação dos novos documentos.

**Critério de Sucesso:** O usuário encontra os documentos do Flow em menos de 10 segundos.

---

## ❌ FORA DO ESCOPO (Versões Futuras)

### **1. Integração com APIs Externas**

**Descrição:** Conectar o dashboard com ferramentas como Jira, Trello, Notion, ou APIs de métricas.

**Por que está fora:** Adiciona complexidade técnica desnecessária para o MVP. O foco é em um sistema autônomo e simples.

**Quando considerar:** v2.0, após validar que o sistema básico funciona.

---

### **2. Geração Automática de Relatórios**

**Descrição:** Scripts para gerar relatórios de progresso, gráficos de burndown, ou estatísticas automaticamente.

**Por que está fora:** Automação prematura. O processo manual inicial ajuda a validar a utilidade do sistema.

**Quando considerar:** v2.0, se houver demanda clara dos usuários.

---

### **3. Suporte a Múltiplos Colaboradores**

**Descrição:** Funcionalidades específicas para gestão de equipes, como atribuição de tarefas, sincronização entre dashboards, etc.

**Por que está fora:** O foco inicial é no desenvolvedor individual, que é o principal caso de uso do Cursor AI.

**Quando considerar:** v3.0, após dominar o caso individual.

---

### **4. Múltiplos Templates de Dashboard**

**Descrição:** Variações do dashboard para diferentes tipos de projeto (pesquisa, escrita, software, design).

**Por que está fora:** Manter a simplicidade. Um único template robusto e adaptável é suficiente para a v1.0.

**Quando considerar:** v2.0, com base em feedback sobre adaptações necessárias.

---

### **5. Aplicativo ou Plugin para Cursor AI**

**Descrição:** Criar uma extensão nativa do Cursor AI que automatize partes do Flow.

**Por que está fora:** Requer desenvolvimento de software e conhecimento da API do Cursor AI. Fora do escopo de uma metodologia baseada em documentos.

**Quando considerar:** v3.0+, se o Flow se tornar amplamente adotado.

---

### **6. Sistema de Notificações ou Lembretes**

**Descrição:** Alertas automáticos para lembrar o usuário de atualizar o dashboard ou executar rituais.

**Por que está fora:** Adiciona dependência de ferramentas externas. O usuário deve desenvolver o hábito naturalmente.

**Quando considerar:** v2.0, se o abandono gradual for um problema persistente.

---

### **7. Métricas Avançadas e Analytics**

**Descrição:** Análise de velocidade, tempo por tarefa, previsão de conclusão, etc.

**Por que está fora:** Complexidade desnecessária para o MVP. Foco em funcionalidade básica primeiro.

**Quando considerar:** v2.0, se houver interesse em otimização baseada em dados.

---

### **8. Versionamento Automático do Dashboard**

**Descrição:** Sistema que cria snapshots automáticos do dashboard em intervalos regulares.

**Por que está fora:** Git já faz isso se o usuário comitar regularmente. Não justifica desenvolvimento adicional.

**Quando considerar:** Talvez nunca, se o Git for suficiente.

---

## 📊 Resumo do Escopo

| Categoria | Dentro do Escopo (v1.0) | Fora do Escopo (Futuro) |
|:----------|:------------------------|:------------------------|
| **Documentos** | 5 guias + 1 template + 1 caso de uso | Templates múltiplos |
| **Funcionalidades** | Dashboard, Rituais, Log, Ciclo de vida | Automações, Integrações, Notificações |
| **Público-alvo** | Desenvolvedor individual | Equipes colaborativas |
| **Plataforma** | Markdown + Cursor AI | Plugin nativo, APIs externas |
| **Métricas** | Básicas (tempo, progresso %) | Avançadas (velocidade, previsões) |

---

## 🎯 Princípio Norteador do Escopo

> **"Simplicidade acima de tudo. O ENDFIRST Flow v1.0 deve resolver 80% dos problemas com 20% da complexidade."**

Toda funcionalidade proposta deve passar pelo teste:
- **É absolutamente essencial para o problema central (perda de contexto)?**
- **Pode ser implementado sem adicionar burocracia significativa?**
- **Funciona sem dependências externas complexas?**

Se a resposta for "não" para qualquer uma dessas perguntas, a funcionalidade fica para versões futuras.

---

## ✅ Checkpoint de Validação

Antes de avançar para o Pilar 3.5 (Análise de Riscos), valide:

- [ ] O escopo da v1.0 resolve o problema central (perda de contexto)?
- [ ] Tudo que está dentro do escopo é realmente essencial?
- [ ] As exclusões fazem sentido e estão bem justificadas?
- [ ] O escopo é viável de ser entregue em 3 dias?

---

## 🚀 Próximos Passos

Com o escopo calibrado, o próximo passo é avançar para o **Pilar 3.5: Análise de Riscos**, onde aprofundaremos nos potenciais problemas que podem surgir dentro deste escopo definido.
