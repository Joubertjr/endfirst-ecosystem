---
document_id: TEMPLATE_RESULT
type: operational
owner: CEO (Joubert Jr)
status: approved
approved_by: CEO
approved_at: 2026-01-08
governed_by: /METODO/PILAR_ENDFIRST.md
---

# Template — RESULT (Resultado Final de Demanda)

**Versão:** 1.0  
**Data:** 8 de Janeiro de 2026  
**Tipo:** Operacional (Template)  
**Status:** Aprovado pelo CEO

---

## 🎯 OBJETIVO

Este template define o **RESULTADO FINAL** de uma demanda.

**RESULTADO é uma entidade de primeira classe no sistema ENDFIRST.**

**Regra absoluta (OD-010):**
> Nenhum backlog pode existir antes da definição formal do RESULTADO.

---

## 📋 QUANDO USAR

**Obrigatório para:**
- Toda demanda (Cursor ou Manus)
- Antes de criar backlog
- Antes de organizar execução
- Antes de definir processo

**Momento:**
- Após DEMANDA-XXX.md ser criada
- Antes de qualquer planejamento de execução
- Como pré-condição para backlog

---

## 📄 ESTRUTURA OBRIGATÓRIA

### Frontmatter YAML

```yaml
---
document_id: DEMANDA-XXX_RESULT
type: result
related_demand: DEMANDA-XXX
product: [nome do produto]
owner: CEO (Joubert Jr)
status: approved
approved_by: CEO
approved_at: YYYY-MM-DD
governed_by: /METODO/PILAR_ENDFIRST.md
immutable_during_execution: true
---
```

**Campos obrigatórios:**
- `document_id`: DEMANDA-XXX_RESULT
- `type`: result
- `related_demand`: DEMANDA-XXX
- `product`: Nome do produto
- `owner`: CEO (Joubert Jr)
- `status`: approved
- `approved_by`: CEO
- `approved_at`: Data de aprovação
- `governed_by`: /METODO/PILAR_ENDFIRST.md
- `immutable_during_execution`: true

---

### Seção 1: RESULTADO FINAL (Obrigatória)

**Pergunta-mãe:**
> "O que existe quando esta demanda termina?"

**Resposta obrigatória:**
- Descrição clara e observável do resultado
- Não é intenção, não é processo, não é plano
- É o que pode ser visto, tocado, executado, provado

**Formato:**
```markdown
## 🎯 RESULTADO FINAL

Quando DEMANDA-XXX for concluída, o seguinte RESULTADO existirá:

[Descrição clara e observável do resultado]

**Critério de encerramento:**
> Esta demanda está encerrada quando [condição observável].
```

---

### Seção 2: PROVAS OBSERVÁVEIS (Obrigatória)

**Pergunta-mãe:**
> "Como provar que o resultado existe?"

**Resposta obrigatória:**
- Lista de provas observáveis (não interpretáveis)
- Cada prova é binária (existe ou não existe)
- Cada prova é verificável por qualquer pessoa

**Formato:**
```markdown
## ✅ PROVAS OBSERVÁVEIS

Para provar que o RESULTADO existe, as seguintes provas devem ser apresentadas:

1. **[Nome da prova 1]**
   - O que observar: [descrição]
   - Como verificar: [passo a passo]
   - Critério: [binário - passa/falha]

2. **[Nome da prova 2]**
   - O que observar: [descrição]
   - Como verificar: [passo a passo]
   - Critério: [binário - passa/falha]

[...]
```

---

### Seção 3: ARTEFATOS ENTREGÁVEIS (Obrigatória)

**Pergunta-mãe:**
> "O que será commitado no Git quando terminar?"

**Resposta obrigatória:**
- Lista de artefatos que existirão no Git
- Localização exata de cada artefato
- Formato de cada artefato

**Formato:**
```markdown
## 📦 ARTEFATOS ENTREGÁVEIS

Quando DEMANDA-XXX for concluída, os seguintes artefatos existirão no Git:

1. **[Nome do artefato 1]**
   - Localização: `/caminho/para/artefato`
   - Formato: [tipo de arquivo]
   - Conteúdo: [descrição do conteúdo]

2. **[Nome do artefato 2]**
   - Localização: `/caminho/para/artefato`
   - Formato: [tipo de arquivo]
   - Conteúdo: [descrição do conteúdo]

[...]
```

---

### Seção 4: CRITÉRIOS DE NÃO-RESULTADO (Opcional)

**Pergunta-mãe:**
> "O que NÃO é o resultado?"

**Resposta opcional:**
- Lista de coisas que NÃO são o resultado
- Esclarece fronteiras
- Evita ambiguidade

**Formato:**
```markdown
## ❌ CRITÉRIOS DE NÃO-RESULTADO

O RESULTADO **NÃO** inclui:

- ❌ [Coisa que não é resultado 1]
- ❌ [Coisa que não é resultado 2]
- [...]

**Nota:** Estes itens estão explicitamente fora do escopo desta demanda.
```

---

### Seção 5: RELAÇÃO COM ACCEPTANCE (Obrigatória)

**Pergunta-mãe:**
> "Como este RESULT se relaciona com ACCEPTANCE?"

**Resposta obrigatória:**
- RESULT define O QUE existe
- ACCEPTANCE define COMO CEO julga
- RESULT é pré-condição para ACCEPTANCE

**Formato:**
```markdown
## 🔗 RELAÇÃO COM ACCEPTANCE

**RESULT vs ACCEPTANCE:**
- **RESULT** (este documento): Define O QUE existe quando termina
- **ACCEPTANCE** (`DEMANDA-XXX_ACCEPTANCE.md`): Define COMO CEO julga sucesso

**Hierarquia:**
```
RESULT (O QUE existe)
   ↓
ACCEPTANCE (COMO julgar)
   ↓
DECISÃO FINAL (CEO)
```

**Nota:** ACCEPTANCE é parte do RESULTADO, mas não é tudo.
```

---

## 🚨 REGRAS ABSOLUTAS

### Regra 1: RESULT antes de backlog

**Obrigatório:**
- ✅ RESULT.md criado e aprovado
- ✅ Só então backlog pode ser criado

**Proibido:**
- ❌ Criar backlog antes de RESULT
- ❌ Organizar tarefas antes de RESULT
- ❌ Planejar execução antes de RESULT

**Violação:** OD-010

---

### Regra 2: RESULT é imutável durante execução

**Obrigatório:**
- ✅ RESULT congelado após aprovação
- ✅ Mudanças só em nova demanda

**Proibido:**
- ❌ Mudar RESULT durante execução
- ❌ "Ajustar" resultado durante desenvolvimento
- ❌ "Descobrir" resultado durante execução

**Violação:** OD-007

---

### Regra 3: RESULT é observável, não interpretável

**Obrigatório:**
- ✅ RESULT é verificável por qualquer pessoa
- ✅ RESULT é binário (existe ou não existe)

**Proibido:**
- ❌ RESULT que depende de interpretação
- ❌ RESULT que depende de "quase"
- ❌ RESULT que depende de "mais ou menos"

**Violação:** OD-009

---

## 📝 EXEMPLO COMPLETO

Ver: `/DEMANDAS/DEMANDA-001_RESULT.md`

---

## 🔗 DOCUMENTOS RELACIONADOS

- `/METODO/ONTOLOGY_DECISIONS.md` (OD-010)
- `/METODO/PILAR_ENDFIRST.md` (Meta-pilar)
- `/DEMANDAS/DEMANDA-XXX_ACCEPTANCE.md` (Critérios de aceitação)
- `/DEMANDAS/DEMANDA-XXX.md` (Demanda original)

---

## 📜 DECLARAÇÃO DO CEO

> "RESULTADO é uma entidade de primeira classe no sistema ENDFIRST. Não é texto, não é intenção, não é explicação. É um objeto governável. Backlog não cria resultado. Resultado cria backlog."

**Data:** 2026-01-08  
**Responsável:** CEO (Joubert Jr)
