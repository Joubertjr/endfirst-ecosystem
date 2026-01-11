---
document_id: CURSOR_INSTRUCTIONS
type: operational
owner: CEO (Joubert Jr)
status: approved
approved_by: CEO
approved_at: 2026-01-10
governed_by: /METODO/PILAR_ENDFIRST.md
version: 1.0
created_at: 2026-01-10
---

# CURSOR INSTRUCTIONS — Instruções Operacionais para Cursor

**Versão:** 1.0  
**Data:** 10 de Janeiro de 2026  
**Tipo:** Operacional (Tipo B)  
**Owner:** CEO (Joubert Jr)

---

## 🎯 OBJETIVO

Este documento contém **instruções operacionais diretas** para o Cursor (executor técnico) seguir durante a execução de incrementos.

**Regra:**
> Cursor DEVE ler este documento antes de iniciar qualquer incremento.

---

## 🔗 RASTREABILIDADE OBRIGATÓRIA (KANBAN)

### Regra absoluta

**Todo commit DEVE referenciar card do GitHub Projects.**

**Formato obrigatório:**
- `Refs #X` ou `[#X]` na mensagem de commit
- Onde `X` = número do card/issue

### Fluxo obrigatório

**1. Ao iniciar incremento:**
- Mover card de **TODO → DOING** no GitHub Projects
- Criar primeiro commit com `Refs #X`

**2. Durante execução:**
- Todo commit DEVE incluir `Refs #X`
- Manter card em **DOING**

**3. Ao concluir incremento:**
- Último commit DEVE incluir `Refs #X`
- Mover card de **DOING → DONE** no GitHub Projects

### Exemplo de commit correto

```
feat(ui): implementa seleção de resposta [#5]

- Adiciona estado de seleção (useState)
- Implementa feedback visual inequívoco
- Cria evidência em EVIDENCIAS/CRITERIO_03.md

Prova Critério 3:
- ✅ Seleção funcional
- ✅ Feedback visual claro
- ✅ Deseleção automática

Refs #5
```

### Exemplo de commit INCORRETO (proibido)

```
feat(ui): implementa seleção de resposta

- Adiciona estado de seleção
- Implementa feedback visual

❌ FALTA: Refs #X
❌ FALTA: Mover card no Kanban
```

---

## 📋 CHECKLIST PRÉ-COMMIT

Antes de fazer commit, verificar:

- [ ] Mensagem de commit inclui `Refs #X` ou `[#X]`
- [ ] Card está em **DOING** (se primeiro commit, mover de TODO → DOING)
- [ ] Commit referencia o card correto (número bate com incremento)
- [ ] Se último commit do incremento, mover card para **DONE**

---

## 🚨 PROIBIÇÕES ABSOLUTAS

**❌ Commit sem referência ao card**
- Todo commit sem `Refs #X` viola rastreabilidade 100%

**❌ Card em TODO com commits já feitos**
- Se commit existe, card DEVE estar em DOING ou DONE

**❌ Card em DOING após incremento concluído**
- Se incremento terminou, card DEVE estar em DONE

**❌ Múltiplos cards em DOING simultaneamente**
- Apenas 1 incremento por vez (WIP = 1)

---

## 📜 FONTE DAS REGRAS

**Documentos canônicos:**
- `/METODO/KANBAN_CANONICO.md` — Definição de colunas, regras, automações
- `/METODO/CONTRATO_ESTADOS.md` — Quem move o quê, transições de estado
- `/METODO/INSTRUMENTACAO_VISIBILIDADE.md` — Como CEO vê estado sem conversa

**Princípio:**
> "Quem não está no Kanban não existe. E quem inventa status está estruturalmente errado." (CEO, 2026-01-10)

---

## 🎯 MUDANÇA COMPORTAMENTAL IMEDIATA

**A partir de agora:**
- Cursor não faz commit sem `Refs #X`
- Cursor não deixa card em TODO com commits feitos
- Cursor não deixa card em DOING após concluir incremento
- Sistema impede status inventado (não depende de disciplina)

**Lei ativa:**
- OD-009: Processo > Disciplina (não depende de "lembrar")
- OD-011: Entendimento sem mudança é fuga (muda comportamento agora)
- Kanban Canônico: Status é consequência, não narrativa

---

## 🔄 FLUXO VISUAL

```
TODO → DOING → DONE
  ↓       ↓       ↓
Início  Commits  Fim
        (Refs #X)
```

**Regra:**
- TODO = Nada iniciado (sem commits)
- DOING = Execução ativa (commits com Refs #X)
- DONE = Concluído (último commit + card movido)

---

## 📞 DÚVIDAS?

**Se algo não está claro:**
- Execução PARA (não tenta adivinhar)
- Lê documentos canônicos (KANBAN_CANONICO.md, CONTRATO_ESTADOS.md)
- Pergunta ao CEO (não ao Manus)

**Princípio:**
> "Executor não avalia se 'está certo'. Executor segue estados, critérios e evidências. Se algo não está claro, execução PARA." (OD-011 estendida)

---

## 📊 HISTÓRICO DE VERSÕES

| Versão | Data | Mudanças |
|--------|------|----------|
| 1.0 | 2026-01-10 | Versão inicial: regras de rastreabilidade Kanban |

---

**Governado por:** `/METODO/PILAR_ENDFIRST.md`  
**Criado por:** Manus (Agent)  
**Aprovado por:** CEO (Joubert Jr)
