---
id: DEMANDA_MANUS-002
title: Kanban canônico + Contrato de estados para execução do Cursor
end: "Qualquer pessoa consegue ver 'o que está acontecendo' sem falar com ninguém; e o sistema impede status inventado."
type: método
executor: manus
requested_by: CEO
status: ready
created_at: 2026-01-10
updated_at: 2026-01-10
governed_by: /METODO/PILAR_ENDFIRST.md
---

# DEMANDA_MANUS-002 — Kanban canônico + Contrato de estados

**Executor:** Manus (Agent)  
**Solicitado por:** CEO (Joubert Jr)  
**Tipo:** método  
**Status:** ready

---

## 🎯 END (RESULTADO ESPERADO)

**"Qualquer pessoa consegue ver 'o que está acontecendo' sem falar com ninguém; e o sistema impede status inventado."**

**Critério de sucesso:**
- [ ] CEO abre GitHub Projects e em 30s sabe: o que está em execução agora, o que está bloqueado e por quê, o que falta para concluir DEMANDA-001
- [ ] Sistema impede status inventado estruturalmente (não depende de disciplina humana)
- [ ] Cursor referencia card automaticamente em todo incremento (commit/PR/issue)
- [ ] Contrato de estados documentado e operacional (quem move o quê, entrada/saída explícita)
- [ ] Zero conversa humana necessária para entender estado atual

**Sem END explícito → demanda inválida.**

---

## 📋 CONTEXTO

**Por que esta demanda existe:**
- DEMANDA-001 (LLM Orchestrator) está em execução pelo Cursor
- Não existe visibilidade estrutural do progresso (dependeria de "perguntar ao Cursor")
- Status pode ser inventado ou desatualizado (viola OD-009: disciplina humana é falha de design)
- CEO precisa ver "o que está acontecendo" sem depender de comunicação humana

**O que já existe:**
- `/METODO/PILAR_ENDFIRST.md` (princípios END FIRST)
- `/METODO/ONTOLOGY_DECISIONS.md` (OD-009: processo > disciplina, OD-011: entendimento sem mudança é fuga)
- `/METODO/ROLES_AND_RESPONSIBILITIES.md` (papéis: CEO/Manus/Cursor)
- `/METODO/EXECUTION_MODEL.md` (modelo de execução)
- `/DEMANDAS/DEMANDA-001_LLM_ORCHESTRATOR.md` (demanda em execução)
- `/DEMANDAS/DEMANDA-001_RESULT.md` (resultado esperado com 7 provas observáveis)
- `/DEMANDAS/DEMANDA-001_ACCEPTANCE.md` (critérios de aceitação do CEO)

**O que está faltando:**
- Kanban canônico no GitHub Projects (colunas, regras, automações)
- Contrato de estados (quem move o quê, quando, por quê)
- Entrada/saída explícita para cada papel (Cursor/Manus/CEO)
- Gatilho estrutural: todo incremento referencia card (impede esquecimento)
- Instrumentação de visibilidade (fonte única de verdade no Git)

---

## 🔍 ESCOPO

**O que está DENTRO do escopo:**
- Definir Kanban canônico no GitHub Projects (colunas mínimas: BACKLOG / TODO / DOING / DONE / BLOCKED)
- Documentar contrato de estados (quem move cartões técnicos, de especificação, de decisão)
- Especificar entrada/saída do Cursor (entrada: DEMANDA liberada + acceptance congelado; saída: commits incrementais + evidência dos critérios)
- Aplicar OD-009 (se depender de "alguém lembrar de atualizar Kanban", está errado)
- Definir gatilho estrutural: todo incremento = issue/PR/commit referencia card
- Criar documento de instrumentação de visibilidade (como CEO vê estado sem conversa)
- Validar que CEO consegue em 30s saber: o que está em execução, o que está bloqueado, o que falta para DEMANDA-001

**O que está FORA do escopo:**
- Implementar automações no GitHub Actions (pode ser fase 2)
- Criar dashboards visuais externos ao GitHub (GitHub Projects é suficiente)
- Definir processo de retrospectiva ou métricas de performance (foco é visibilidade, não análise)
- Alterar estrutura de DEMANDA-001 (ela já está liberada e em execução)

---

## 📦 ENTREGÁVEIS

**Manus deve entregar:**
1. **Documento: KANBAN_CANONICO.md** (definição de colunas, regras, automações, contrato de estados)
2. **Documento: CONTRATO_ESTADOS.md** (quem move o quê, entrada/saída por papel, gatilhos estruturais)
3. **Documento: INSTRUMENTACAO_VISIBILIDADE.md** (como CEO vê estado sem conversa, fonte única de verdade)
4. **Atualização: EXECUTION_MODEL.md** (adicionar seção sobre Kanban e visibilidade)
5. **GitHub Project configurado** (ou especificação completa para CEO configurar)

**Formato esperado:**
- Documentos Markdown governados por `/METODO/PILAR_ENDFIRST.md`
- YAML frontmatter completo (type: operational, status: approved, approved_by: CEO)
- Linguagem normativa (DEVE, NÃO DEVE, PROIBIDO, OBRIGATÓRIO)
- Exemplos concretos (como Cursor referencia card, como CEO valida visibilidade)

**Localização no Git:**
- `/METODO/KANBAN_CANONICO.md`
- `/METODO/CONTRATO_ESTADOS.md`
- `/METODO/INSTRUMENTACAO_VISIBILIDADE.md`
- `/METODO/EXECUTION_MODEL.md` (atualizado)

---

## ⛔ RESTRIÇÕES

**Manus NÃO deve:**
- Criar processo que dependa de disciplina humana (viola OD-009)
- Criar documentação que "faz sentido" mas não muda comportamento agora (viola OD-011)
- Definir status inventados ou subjetivos (ex: "quase pronto", "em revisão conceitual")
- Criar Kanban sem gatilho estrutural (ex: "Cursor deve lembrar de atualizar")
- Documentar sem critério binário de validação (CEO precisa poder verificar em 30s)

**Manus DEVE:**
- Aplicar END FIRST: resultado antes de processo (Kanban serve ao END, não o contrário)
- Aplicar OD-009: processo > disciplina (sistema impede erro por design)
- Aplicar OD-011: entendimento sem mudança é fuga (todo documento muda comportamento pequeno agora)
- Garantir rastreabilidade 100% (todo card tem commit, todo commit tem card)
- Criar contrato de estados binário (estado X existe ↔ condição Y é verdadeira no Git)

---

## 🔗 DOCUMENTOS RELACIONADOS

- `/METODO/PILAR_ENDFIRST.md` (princípios fundacionais)
- `/METODO/ONTOLOGY_DECISIONS.md` (OD-009, OD-011)
- `/METODO/ROLES_AND_RESPONSIBILITIES.md` (papéis: CEO/Manus/Cursor)
- `/METODO/EXECUTION_MODEL.md` (modelo de execução)
- `/DEMANDAS/DEMANDA-001_LLM_ORCHESTRATOR.md` (primeira demanda em execução)
- `/DEMANDAS/DEMANDA-001_RESULT.md` (resultado esperado)
- `/DEMANDAS/DEMANDA-001_ACCEPTANCE.md` (critérios de aceitação)

---

## 📜 CRITÉRIO DE ENCERRAMENTO

**Esta demanda estará concluída quando:**
1. CEO abre GitHub Projects e em 30s sabe: o que está em execução, o que está bloqueado, o que falta para DEMANDA-001
2. Sistema impede status inventado (contrato de estados binário documentado e operacional)
3. Cursor referencia card em todo incremento (gatilho estrutural documentado)
4. Contrato de estados documentado (quem move o quê, entrada/saída explícita)
5. Instrumentação de visibilidade documentada (fonte única de verdade no Git)
6. Documentos aprovados pelo CEO e commitados no Git
7. EXECUTION_MODEL.md atualizado com seção sobre Kanban e visibilidade

**CEO validará:**
- [ ] END foi atingido (visibilidade sem conversa + sistema impede status inventado)
- [ ] Entregáveis estão no Git (4 documentos criados/atualizados)
- [ ] Qualidade está conforme esperado (linguagem normativa, exemplos concretos, critérios binários)
- [ ] Mudança comportamental imediata (a partir do próximo incremento, Cursor já referencia card)

---

## 📊 HISTÓRICO

| Data | Evento | Responsável |
|------|--------|-------------|
| 2026-01-10 | Demanda criada | CEO |
| 2026-01-10 | Demanda especificada por Manus | Manus |

---

**Versão:** 1.0  
**Criado:** 2026-01-10  
**Solicitado por:** CEO (Joubert Jr)  
**Executor:** Manus (Agent)
