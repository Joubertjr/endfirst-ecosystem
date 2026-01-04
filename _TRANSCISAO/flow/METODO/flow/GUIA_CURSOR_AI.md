# Guia de Uso do ENDFIRST Flow no Cursor AI

**Autor:** Manus AI  
**Data:** 30 de Dezembro de 2025  
**Versão:** 1.0

---

## Seção 1: Por que Cursor AI?

O ENDFIRST Flow funciona em qualquer editor de texto, mas ele é **otimizado para o Cursor AI** por 4 motivos:

1. **Chat com o Código:** Você pode conversar com o seu `STATUS_PROJETO.md` para obter resumos e insights.
2. **Comandos de IA:** Automatizar tarefas repetitivas com comandos customizados.
3. **Integração com Git:** Commitar o `STATUS_PROJETO.md` diretamente da interface.
4. **Edição Rápida:** A edição de Markdown é fluida e rápida.

---

## Seção 2: Setup Inicial (5 minutos)

1. **Crie o arquivo:** Na raiz do seu projeto, crie o arquivo `STATUS_PROJETO.md`.
2. **Copie o template:** Copie o conteúdo do `TEMPLATE_DASHBOARD.md` e cole no `STATUS_PROJETO.md`.
3. **Preencha a Visão Geral:**
   - Nome do projeto
   - Objetivo
   - Datas
4. **Crie o Backlog:** Adicione todas as tarefas que você consegue pensar na seção "Backlog".
5. **Planeje o primeiro Sprint:**
   - Mova 3-5 tarefas do Backlog para "A Fazer".
   - Defina o objetivo do Sprint #1.
   - Preencha a tabela de tarefas do sprint.
6. **Commit inicial:**
   ```bash
   git add STATUS_PROJETO.md
   git commit -m "feat: add project dashboard"
   ```

---

## Seção 3: Rituais no Cursor AI

### Ritual de Início de Sessão (3 min)

1. **Abra o `STATUS_PROJETO.md`**
2. **Use o Chat com o Código:**
   - Selecione todo o conteúdo do arquivo (`Ctrl+A`)
   - Abra o chat (`Ctrl+K`)
   - Pergunte:
     ```
     Resuma o status atual do projeto em 3 pontos: progresso do sprint, tarefa AGORA e previsão de conclusão.
     ```
3. **Defina a tarefa "AGORA"**
4. **Inicie o cronômetro** (Toggl, Clockify, etc.)

### Ritual de Fim de Sessão (5 min)

1. **Pare o cronômetro**
2. **Use o Chat com o Código para atualizar métricas:**
   - Selecione a seção "Sprint Atual e Métricas"
   - Abra o chat (`Ctrl+K`)
   - Diga:
     ```
     Atualize as métricas: a tarefa '[NOME DA TAREFA]' agora tem [X] horas de tempo real e está [Y]% concluída. Recalcule o progresso do sprint, velocidade e previsão de conclusão.
     ```
3. **Adicione entrada no Log de Progresso**
4. **Use a integração com Git do Cursor AI para commitar:**
   - Vá para a aba de Git
   - Adicione `STATUS_PROJETO.md`
   - Escreva a mensagem de commit: `docs: update project status`
   - Clique em "Commit"

---

## Seção 4: Prompts Úteis

### 1. Resumo do Projeto

**Prompt:**
```
Com base neste dashboard, resuma o status do projeto em 5 pontos: objetivo, progresso, próxima tarefa, maior risco e previsão de conclusão.
```

### 2. Análise de Sprint

**Prompt:**
```
Analise o sprint atual. Estamos no prazo? Qual o ritmo atual? Qual a previsão de conclusão? Há algum risco?
```

### 3. Reconstrução de Contexto

**Prompt:**
```
Estou voltando a este projeto após 3 dias. Com base no Log de Progresso e nas tarefas, o que eu estava fazendo e qual a próxima coisa que eu deveria fazer?
```

### 4. Planejamento de Sprint

**Prompt:**
```
Com base no Backlog e na velocidade atual de [X]h/tarefa, sugira 3-5 tarefas para o próximo sprint que somem no máximo 25h.
```

---

## Seção 5: Comandos Customizados (Avançado)

Você pode criar comandos customizados no Cursor AI para automatizar os rituais.

**Exemplo de comando `end-session`:**

1. **Abra as configurações de comandos (`Ctrl+Shift+P` > "Configure Custom Commands")**
2. **Adicione o comando:**
   ```json
   {
     "name": "end-session",
     "prompt": "Com base no texto selecionado (que é a tarefa AGORA), gere uma entrada para o Log de Progresso no formato [YYYY-MM-DD HH:MM] [Tarefa] Título. Pergunte o que foi feito e por quê.",
     "shortcut": "ctrl+alt+e"
   }
   ```
3. **Como usar:**
   - Selecione a tarefa "AGORA"
   - Pressione `Ctrl+Alt+E`
   - O Cursor vai gerar a entrada do log para você

---

## Seção 6: Troubleshooting

**1. O chat não entende meu dashboard.**
   - Verifique se o formato do seu dashboard segue o template.
   - Selecione a seção específica que você quer que a IA analise.

**2. Os comandos customizados não funcionam.**
   - Verifique se o JSON do comando está correto.
   - Reinicie o Cursor AI.

---

**Fim do Guia do Cursor AI.**
