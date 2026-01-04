# Pilar 0.5: Mapa de Conhecimento - Metodologia de Acompanhamento de Projeto ("ENDFIRST Flow")

**Data:** 30 de Dezembro de 2025  
**Versão:** v2.0

---

## 🗺️ Mapa de Conhecimento

Este mapa delineia todo o conhecimento que precisa ser gerado, pesquisado e sintetizado para criar a metodologia **"ENDFIRST Flow"**. Ele serve como um guia para garantir que nenhum aspecto crítico seja esquecido durante o desenvolvimento.

---

## 🧠 Áreas de Conhecimento a Explorar

### **1. Metodologias Ágeis e Frameworks de Gestão**

**Conceitos-chave a estudar:**
- **Scrum:** Sprints, Daily Standups, Retrospectivas, Definition of Done
- **Kanban:** Fluxo contínuo, WIP limits, visualização de trabalho
- **XP (Extreme Programming):** Feedback rápido, simplicidade, coragem para mudanças
- **Lean:** Eliminação de desperdício, foco no valor, melhoria contínua

**Relevância para o ENDFIRST Flow:**
- Adaptar o conceito de "ciclo curto" para sessões de trabalho individuais
- Usar visualização de status (inspirado no Kanban) no dashboard
- Incorporar rituais de feedback (início/fim de sessão)

---

### **2. Sistemas de Produtividade Pessoal**

**Conceitos-chave a estudar:**
- **GTD (Getting Things Done):** Captura, clarificação, organização, reflexão, engajamento
- **Zettelkasten:** Sistema de notas interconectadas para preservar conhecimento
- **Pomodoro:** Ciclos de trabalho focado com pausas regulares
- **Eisenhower Matrix:** Priorização por urgência vs. importância

**Relevância para o ENDFIRST Flow:**
- O ritual de "captura" do GTD inspira o ritual de fim de sessão
- A ideia de "próxima ação" do GTD será central no dashboard
- O conceito de "revisão semanal" pode ser adaptado para projetos

---

### **3. Gestão Visual de Projetos**

**Conceitos-chave a estudar:**
- **Dashboards:** Princípios de design de informação, hierarquia visual
- **Quadros Kanban:** Colunas de status, cartões de tarefa
- **Burndown Charts:** Visualização de progresso ao longo do tempo
- **Status Indicators:** Semáforos, badges, progress bars

**Relevância para o ENDFIRST Flow:**
- O dashboard será o coração visual da metodologia
- Uso de emojis e formatação Markdown para criar hierarquia visual
- Seções claramente delimitadas para facilitar a leitura rápida

---

### **4. Gerenciamento de Contexto e Memória**

**Conceitos-chave a estudar:**
- **Second Brain (Tiago Forte):** Captura, organização, destilação, expressão
- **PKM (Personal Knowledge Management):** Sistemas para gerenciar conhecimento pessoal
- **Context Switching:** Custos cognitivos de trocar de contexto
- **Mental Models:** Como reconstruir o "estado mental" de um projeto

**Relevância para o ENDFIRST Flow:**
- O problema central que o Flow resolve é a perda de contexto
- O "Guia de Retomada de Contexto" será baseado nestes princípios
- O log de progresso funciona como um "segundo cérebro" do projeto

---

### **5. Versionamento e Histórico**

**Conceitos-chave a estudar:**
- **Git:** Commits, branches, changelog, histórico de decisões
- **Semantic Versioning:** Versionamento significativo (MAJOR.MINOR.PATCH)
- **Changelogs:** Formato "Keep a Changelog", entradas cronológicas
- **Decision Records (ADRs):** Documentação de decisões arquiteturais

**Relevância para o ENDFIRST Flow:**
- O log de progresso será inspirado em changelogs do Git
- A seção "Decisões Importantes" é inspirada em ADRs
- Cada entrada de log deve ter data, contexto e justificativa

---

## ❓ Perguntas-Chave a Serem Respondidas

Estas são as perguntas críticas que a metodologia precisa responder de forma clara e acionável:

| # | Pergunta | Por que é importante? | Onde será respondida? |
|:---|:---------|:----------------------|:----------------------|
| **1** | Como manter o contexto de um projeto entre sessões de trabalho no Cursor AI? | É o problema central que motivou a criação do Flow. | `GUIA_RETOMADA_CONTEXTO.md` + `GUIA_CURSOR_AI.md` |
| **2** | Qual a maneira mais simples e eficaz de registrar o progresso diário? | Precisa ser tão simples que não seja ignorado, mas robusto o suficiente para ser útil. | `ENDFIRST_FLOW.md` (seção "Log de Progresso") |
| **3** | Como visualizar o status geral do projeto de forma rápida e intuitiva? | O usuário precisa entender em 10 segundos o estado do projeto. | `TEMPLATE_DASHBOARD.md` |
| **4** | Qual o mínimo de "burocracia" necessária para um acompanhamento robusto? | Evitar que a metodologia se torne um fardo. | `ENDFIRST_FLOW.md` (seção "Princípios") |
| **5** | Como a metodologia pode ajudar a decidir "qual a próxima ação"? | Eliminar a paralisia de decisão ao retomar o trabalho. | `TEMPLATE_DASHBOARD.md` (seção "Próximas Ações") |
| **6** | Como integrar o "ENDFIRST Flow" com os 11 pilares do ENDFIRST? | Garantir coerência filosófica e prática. | `ENDFIRST_FLOW.md` (seção "Integração com ENDFIRST") |
| **7** | Como usar o versionamento (Git) como ferramenta de acompanhamento? | Git já está presente em 99% dos projetos de software. | `GUIA_CURSOR_AI.md` (seção "Git + Flow") |
| **8** | Como garantir que o dashboard não se torne gigante e inútil? | Evitar o "graveyard effect" onde o documento cresce até ser abandonado. | `ENDFIRST_FLOW.md` (seção "Manutenção e Arquivamento") |
| **9** | Como adaptar o Flow para projetos de diferentes tamanhos? | Um projeto de 1 semana vs. 6 meses precisa de abordagens diferentes. | `ENDFIRST_FLOW.md` (seção "Adaptações") |
| **10** | Como o Flow funciona para projetos colaborativos (não apenas individuais)? | Preparar para evolução futura, mesmo que o MVP seja individual. | `ENDFIRST_FLOW.md` (seção "Limitações e Futuro") |

---

## 📦 Deliverables a Serem Produzidos

| # | Deliverable | Formato | Tamanho Estimado | Prioridade |
|:---|:------------|:--------|:-----------------|:-----------|
| **1** | `ENDFIRST_FLOW.md` | Markdown | 2.000-3.000 palavras | **CRÍTICA** |
| **2** | `TEMPLATE_DASHBOARD.md` | Markdown (template) | 300-500 palavras | **CRÍTICA** |
| **3** | `GUIA_CURSOR_AI.md` | Markdown | 1.500-2.000 palavras | **CRÍTICA** |
| **4** | `GUIA_RETOMADA_CONTEXTO.md` | Markdown | 1.000-1.500 palavras | **ALTA** |
| **5** | `CASO_DE_USO_ENDFIRST_FLOW.md` | Markdown | 3.000-4.000 palavras | **ALTA** |
| **6** | Atualização do `INDICE_DE_NAVEGACAO.md` | Markdown | 50-100 palavras (adição) | **MÉDIA** |

**Total estimado:** ~8.000-11.000 palavras de documentação nova.

---

## 🗄️ Gestão do Conhecimento Gerado

### **Uso do Banco de Referências**

Todo o conhecimento gerado durante a criação do ENDFIRST Flow será armazenado no **Banco de Referências** do método ENDFIRST. Esta será uma aplicação prática do próprio sistema que estamos criando.

**Estrutura no Banco:**

```
BANCO_REFERENCIAS/
├── projetos/
│   ├── 01_METODO_ENDFIRST/          # Primeiro projeto (a metodologia base)
│   ├── 02_GOOGLE_STORE_V2.1/        # Segundo projeto (exemplo de software)
│   └── 03_ENDFIRST_FLOW/            # Terceiro projeto (este que estamos criando)
│       ├── requisitos/
│       │   ├── RF_001_dashboard.md
│       │   ├── RF_002_rituais.md
│       │   └── ...
│       ├── referencias/
│       │   ├── metodologias_ageis.md
│       │   ├── gestao_contexto.md
│       │   └── ...
│       └── decisoes/
│           ├── DEC_001_formato_dashboard.md
│           └── ...
```

**Por que isso é importante:**

1. **Praticamos o que pregamos:** Usamos o Banco de Referências para gerenciar o próprio projeto de criação do Flow.
2. **Conhecimento preservado:** Todas as pesquisas, decisões e aprendizados ficam documentados e recuperáveis.
3. **Exemplo prático:** Demonstra como usar o Banco para projetos de metodologia (não apenas software).
4. **Rastreabilidade:** Cada decisão de design do Flow terá sua justificativa documentada.

**Quando será implementado:**

A estrutura do projeto no Banco de Referências será criada durante o **Pilar 6 (Execução)** e consolidada no **Pilar 7 (Captura de Aprendizados)**.

---

## 🎯 Critérios de Completude do Mapa

Este mapa de conhecimento será considerado completo quando:

- ✅ Todas as 5 áreas de conhecimento foram exploradas e sintetizadas
- ✅ Todas as 10 perguntas-chave têm respostas claras e acionáveis
- ✅ Todos os 6 deliverables foram criados e validados
- ✅ O usuário consegue usar o Flow sem consultar documentação externa

---

## 🚀 Próximos Passos

Com o mapa de conhecimento completo, o próximo passo é avançar para o **Pilar 1: Identificar os Obstáculos** que podem impedir a criação desta metodologia.
