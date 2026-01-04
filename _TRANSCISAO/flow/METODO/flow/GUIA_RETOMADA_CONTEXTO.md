# Guia de Retomada de Contexto

**Autor:** Manus AI  
**Data:** 30 de Dezembro de 2025  
**Versão:** 1.0

---

## Seção 1: O Problema da Perda de Contexto

A perda de contexto é o maior inimigo do desenvolvedor individual. Cada vez que você pausa um projeto, o "estado mental" que você construiu (variáveis, lógica, próximos passos) se dissipa.

Retomar o trabalho exige um esforço cognitivo para reconstruir esse estado mental. O objetivo deste guia é tornar esse processo **rápido, eficiente e indolor**.

---

## Seção 2: Checklists de Retomada por Tempo de Pausa

### Pausa Curta (< 24 horas)

**Tempo de retomada:** 3 minutos

**Checklist:**
1. ✅ Execute o **Ritual de Início de Sessão** completo (3 min).
   - Ler dashboard, verificar métricas, definir tarefa AGORA, iniciar cronômetro.

---

### Pausa Média (1-3 dias)

**Tempo de retomada:** 5-10 minutos

**Checklist:**
1. ✅ Execute o **Ritual de Início de Sessão** (3 min).
2. ✅ Leia as **últimas 5 entradas do Log de Progresso** (2 min).
   - Foco no "por quê" das últimas ações.
3. ✅ Revise os **últimos 3 commits no Git** (3 min).
   - `git log -p -3`
4. ✅ Use o prompt de **Reconstrução de Contexto** no Cursor AI (2 min).

---

### Pausa Longa (1-2 semanas)

**Tempo de retomada:** 15-20 minutos

**Checklist:**
1. ✅ Execute o **Ritual de Início de Sessão** (3 min).
2. ✅ Leia as **últimas 10-15 entradas do Log de Progresso** (5 min).
3. ✅ Leia a seção **"Decisões Importantes"** do dashboard (3 min).
4. ✅ Revise os **últimos 5-10 commits no Git** (5 min).
5. ✅ Use o prompt de **Reconstrução de Contexto** no Cursor AI (2 min).
6. ✅ Considere fazer uma **tarefa de "aquecimento"** (um bug pequeno ou refatoração) antes de pegar uma feature complexa.

---

### Pausa Muito Longa (1+ mês)

**Tempo de retomada:** 30-60 minutos

**Checklist:**
1. ✅ Execute o **Ritual de Início de Sessão** (3 min).
2. ✅ Leia o **dashboard completo**, seção por seção (10 min).
3. ✅ Leia o **Log de Progresso completo** do último mês (10 min).
4. ✅ Leia as **Decisões Importantes completas** (5 min).
5. ✅ Revise o **histórico do Git do último mês** (10 min).
6. ✅ Use o prompt de **Reconstrução de Contexto** no Cursor AI (2 min).
7. ✅ Crie uma **tarefa de Pesquisa/Spike** para re-explorar a arquitetura ou a parte do código que você vai trabalhar (30-60 min).
8. ✅ **NÃO comece a codificar imediatamente.** Use a primeira sessão apenas para reconstruir o contexto.

---

## Seção 3: 4 Técnicas de Reconstrução de Contexto

### Técnica 1: Leitura Ativa

Não leia passivamente. Ao ler o dashboard ou o log, faça anotações e perguntas a si mesmo:
- "Por que eu decidi usar X em vez de Y?"
- "Qual era o bug que eu estava tentando corrigir?"
- "Qual a próxima etapa lógica aqui?"

### Técnica 2: O Resumo da IA

Use o Cursor AI para criar um resumo para você. Selecione o dashboard e o log e use o prompt:

```
Estou voltando a este projeto após [X] dias. Com base neste dashboard e log, resuma em 5 pontos o que eu estava fazendo, qual era a próxima tarefa e qual o maior risco atual.
```

### Técnica 3: O Mapa Mental

Se o contexto for muito complexo, crie um mapa mental rápido (em papel ou em ferramentas como Miro/Excalidraw) com:
- O objetivo da tarefa atual no centro
- Ramos para: dependências, riscos, próximos passos, decisões tomadas

### Técnica 4: A Tarefa de Aquecimento

Comece com uma tarefa pequena e bem definida (um bug, uma refatoração, uma melhoria de documentação). Isso ajuda a "aquecer" o cérebro e a re-familiarizar-se com o código antes de atacar problemas complexos.

---

## Seção 4: Estratégias de Prevenção

Prevenir a perda de contexto é mais fácil do que remediar.

### 1. Ritual de Fim de Sessão Impecável

O passo mais importante para prevenir a perda de contexto é um **Ritual de Fim de Sessão bem feito**:
- **Log detalhado:** O "por quê" é mais importante que o "o que".
- **Próxima tarefa clara:** Deixe uma instrução clara para o seu "eu" do futuro.
- **Commit atômico:** Commits pequenos e bem descritos são mais fáceis de revisar.

### 2. Decisões Explícitas

Sempre que tomar uma decisão importante, registre na seção "Decisões Importantes". Isso evita o "por que eu fiz isso?" no futuro.

### 3. Código Limpo e Documentado

Código auto-explicativo e bem documentado é a melhor forma de preservar contexto.

---

**Fim do Guia de Retomada de Contexto.**
