---
document_id: ONTOLOGY_DECISIONS
type: canonical
owner: CEO (Joubert Jr)
status: approved
approved_by: CEO
approved_at: 2026-01-08
governed_by: /METODO/PILAR_ENDFIRST.md
---

# Ontology Decisions

**Versão:** 1.0  
**Data:** 8 de Janeiro de 2026  
**Tipo:** Canônico (Ontologia Operacional)  
**Status:** Aprovado pelo CEO

---

## 🎯 OBJETIVO

Este documento consolida **decisões ontológicas** do ENDFIRST Ecosystem em **frases normativas** e **verdades operacionais**.

**Função:**
> Congelar aprendizado, não inovação.

**Princípio:**
> Nada de teoria. Nada de formalismo. Apenas regras já vividas.

---

## 📜 VERDADES ESTRUTURAIS

### 1. Sobre Aprovação

**"PR não é mecanismo de aprovação."**

PR (Pull Request) é mecanismo técnico de revisão de código. Aprovação é decisão governada registrada em APPROVAL_LOG.md. Os dois não são a mesma coisa.

**Consequência:** Commit pode estar em master e ainda não estar aprovado formalmente. Aprovação exige registro explícito no log.

---

**"Aprovação sem hash não existe."**

Toda aprovação deve referenciar um commit Git válido. Não existe aprovação "no ar" ou "prometida para depois".

**Consequência:** `commit: TBD` é proibido. Aprovação só pode apontar para commits existentes.

---

**"Documento aprovado sem log é inexistente."**

Se um documento não está registrado em APPROVAL_LOG.md, ele não está oficialmente aprovado, independente de quem disse que está.

**Consequência:** APPROVAL_LOG.md é fonte única de verdade para aprovações.

---

### 2. Sobre Commits

**"Checklist existe para impedir estados inválidos."**

COMMIT_GOVERNANCE_CHECKLIST.md não é burocracia. É proteção estrutural contra commits "quase conformes" que passam tecnicamente mas quebram governança.

**Consequência:** Se checklist não fecha, commit não pode ser considerado aprovado.

---

**"Commit aprovado sem log não existe."**

Análogo a "documento aprovado sem log". Se APPROVAL_LOG.md não foi atualizado no commit, a aprovação não aconteceu.

**Consequência:** Aprovação e mudança devem ser atômicas (mesmo commit).

---

**"TBD é proibido."**

`commit: TBD` significa "rastreabilidade quebrada". Não é permitido em nenhuma circunstância.

**Consequência:** Toda entrada no APPROVAL_LOG deve ter hash real desde o início.

---

### 3. Sobre Documentos

**"Documento sem YAML frontmatter não é governado."**

Metadados obrigatórios (document_id, type, status, approved_by, approved_at, governed_by) são a interface de governança. Sem eles, o documento não entra no sistema.

**Consequência:** Documentos sem YAML são tratados como rascunhos ou não governados.

---

**"Documento Tipo A governa outros documentos."**

Documentos canônicos (Tipo A) são soberanos. Outros documentos devem referenciar explicitamente qual canônico os governa.

**Consequência:** Hierarquia de governança é explícita, não implícita.

---

**"README é documento vivo, não promessa implícita."**

README deve separar "Estado Atual" (o que existe) de "Visão Futura" (o que ainda não existe). Não pode narrar futuro sem contrato explícito.

**Consequência:** README não mente sobre o estado do sistema.

---

### 4. Sobre Governança

**"Governança não depende de autoridade."**

Sistema de governança deve funcionar por regras verificáveis, não por quem tem autoridade para decidir.

**Consequência:** CEO pode ser bloqueado por checklist se commit não estiver conforme.

---

**"Governança não depende de memória."**

Decisões devem estar registradas em documentos, não na cabeça das pessoas.

**Consequência:** Se não está documentado, não aconteceu.

---

**"Governança não depende de boa vontade."**

Sistema deve impedir erros por design, não confiar que pessoas vão lembrar de fazer certo.

**Consequência:** Checklists, regras e validações automáticas são obrigatórios.

---

### 5. Sobre Ontologia

**"Ontologia operacional é executável, não declarativa."**

Ontologia não é um glossário bonito. É um conjunto de regras que impedem estados inválidos.

**Consequência:** Documentos como COMMIT_GOVERNANCE_CHECKLIST.md e APPROVAL_LOG_RULES.md são ontologia, mesmo sem se chamar "ontology".

---

**"Cada novo documento cria semântica."**

Todo documento governado adiciona significado ao sistema. Decisões novas devem ser ancoradas conscientemente.

**Consequência:** Crescimento de documentos deve ser intencional, não acidental.

---

**"Ontologia congela aprendizado, não inovação."**

Este documento (ONTOLOGY_DECISIONS.md) registra regras já vividas, não teorias futuras.

**Consequência:** Só entra aqui o que já foi testado e validado na prática.

---

## 🧠 ENTIDADES FUNDAMENTAIS

### Documento
**Definição:** Arquivo .md com YAML frontmatter obrigatório.

**Tipos:**
- **Canônico (A):** Governa outros documentos
- **Operacional (B):** Define processos
- **Exemplo (C):** Exemplifica templates

**Estados:**
- `approved` — Oficialmente aprovado
- `pending` — Aguardando aprovação
- `obsolete` — Obsoleto (não usar)

---

### Commit
**Definição:** Mudança atômica no repositório Git.

**Propriedades:**
- Hash (7+ caracteres)
- Mensagem (Conventional Commits)
- Autor
- Data

**Relação com Aprovação:** Aprovação deve referenciar commit existente.

---

### Aprovação
**Definição:** Decisão formal registrada em APPROVAL_LOG.md.

**Propriedades obrigatórias:**
- document_id
- type (A/B/C)
- status (approved/pending/obsolete)
- approved_by (nome)
- approved_at (YYYY-MM-DD)
- reason (justificativa)
- governed_by (path)
- commit (hash)

**Invariante:** Aprovação sem hash não existe.

---

### Checklist
**Definição:** Lista de verificações obrigatórias antes de declarar conformidade.

**Função:** Impedir estados inválidos.

**Exemplos:**
- COMMIT_GOVERNANCE_CHECKLIST.md
- Checklist B1-B11 do ENDFIRST_SPEC

---

## 🔗 RELAÇÕES FUNDAMENTAIS

### "governado por"
**Definição:** Documento A governa documento B.

**Propriedade:** Transitiva (se A governa B e B governa C, então A governa C indiretamente).

**Exemplo:**
```
PILAR_ENDFIRST.md (A)
    ↓ governa
ENDFIRST_SPEC.md (B)
    ↓ governa
ENDFIRST_SPEC_EF-2026-001 (C)
```

---

### "aprovado por"
**Definição:** Pessoa X aprovou documento Y.

**Propriedade:** Não transitiva (aprovação não se propaga).

**Registro:** APPROVAL_LOG.md

---

### "registrado em"
**Definição:** Aprovação de documento X está registrada em commit Y.

**Propriedade:** Bidirecional (commit → log, log → commit).

**Invariante:** Hash deve existir em ambos os lados.

---

## 🚫 ANTI-ESTADOS (IMPOSSÍVEIS POR DEFINIÇÃO)

### "Commit aprovado sem log"
**Definição:** Commit que altera documentos governados mas não atualiza APPROVAL_LOG.md.

**Status:** PROIBIDO

**Bloqueio:** COMMIT_GOVERNANCE_CHECKLIST.md

---

### "Aprovação com TBD"
**Definição:** Entrada no APPROVAL_LOG com `commit: TBD`.

**Status:** PROIBIDO

**Bloqueio:** APPROVAL_LOG_RULES.md Regra 1

---

### "Documento aprovado sem YAML"
**Definição:** Documento sem metadados obrigatórios mas marcado como aprovado.

**Status:** IMPOSSÍVEL

**Motivo:** Sem YAML, documento não entra no sistema de governança.

---

### "README que mente"
**Definição:** README que afirma existência de algo que não existe.

**Status:** PROIBIDO

**Bloqueio:** README v11.8+ (Estado Atual vs Visão Futura)

---

## 🔄 MECANISMOS DE CORREÇÃO

### Correção de TBD
**Gatilho:** Detectar `commit: TBD` no APPROVAL_LOG.

**Ação:**
1. Identificar commit real que aprovou o documento
2. Substituir TBD por hash real
3. Criar commit de correção
4. Registrar correção no histórico do log

**Exemplo:** Commit 5c294f0 corrigiu TBD do commit 2d47fab.

---

### Correção de Contagem
**Gatilho:** Total de documentos não bate com realidade.

**Ação:**
1. Contar arquivos .md no repositório
2. Atualizar estatísticas no APPROVAL_LOG
3. Criar commit de correção
4. Registrar correção no histórico do log

**Exemplo:** Commit 4b8957a corrigiu contagem de 17 para 14.

---

### Correção de Commit Não Conforme
**Gatilho:** Commit falha no COMMIT_GOVERNANCE_CHECKLIST.

**Ação:**
1. Identificar itens que falharam
2. Corrigir inconsistências
3. Criar commit de correção
4. Validar novamente com checklist

**Exemplo:** Commit 2d47fab falhou (TBD presente), corrigido por 5c294f0.

---

## 📊 INVARIANTES GLOBAIS

### Invariante 1: Rastreabilidade Bidirecional
**Definição:** Se APPROVAL_LOG referencia commit X, então commit X deve conter mudanças no documento aprovado.

**Verificação:**
```bash
git show [HASH] -- path/to/document.md
```

---

### Invariante 2: Consistência YAML ↔ Log
**Definição:** Metadados no YAML frontmatter devem estar sincronizados com APPROVAL_LOG.

**Verificação:** Comparar campos `status`, `approved_by`, `approved_at`, `governed_by`.

---

### Invariante 3: Totalização Correta
**Definição:** Total de documentos = Aprovados + Pendentes + Obsoletos.

**Verificação:**
```bash
find . -name "*.md" | wc -l
```

---

### Invariante 4: Hierarquia Acíclica
**Definição:** Relação "governado por" não pode ter ciclos.

**Exemplo inválido:**
```
A governa B
B governa C
C governa A  ← CICLO (proibido)
```

---

## 🧪 CASOS DE TESTE (VALIDAÇÃO)

### Teste 1: TBD é detectado
**Input:** Criar entrada com `commit: TBD`

**Resultado esperado:** Checklist falha, commit não é aprovado

**Status:** ✅ VALIDADO (commit 2d47fab)

---

### Teste 2: Contagem incorreta é detectada
**Input:** Afirmar "17 documentos" quando existem 14

**Resultado esperado:** Auditoria identifica discrepância

**Status:** ✅ VALIDADO (commit 4b8957a)

---

### Teste 3: Commit sem log é bloqueado
**Input:** Alterar documento sem atualizar APPROVAL_LOG

**Resultado esperado:** Checklist falha (item "APPROVAL_LOG atualizado?")

**Status:** ✅ VALIDADO (design do checklist)

---

## 📚 DOCUMENTOS RELACIONADOS

**Canônicos (Tipo A):**
- PILAR_ENDFIRST.md — Meta-pilar soberano
- ENDFIRST_DOCUMENT_GOVERNANCE.md — Governança documental
- ONTOLOGY_DECISIONS.md — Este documento

**Operacionais (Tipo B):**
- COMMIT_GOVERNANCE_CHECKLIST.md — Checklist de conformidade
- APPROVAL_LOG_RULES.md — Regras anti-TBD
- APPROVAL_LOG.md — Log de aprovações

**Exemplos (Tipo C):**
- ENDFIRST_SPEC_EF-2026-001 — LLM Orchestrator
- ENDFIRST_SPEC_EF-2026-002 — Governança Documental

---

## 🔒 REGRA DE ATUALIZAÇÃO

**Este documento só pode ser atualizado quando:**

1. **Gatilho formal dispara** (ver ONTOLOGY_DECISIONS_TRIGGER.md)
2. **Todos os 5 critérios são cumpridos:**
   - Houve confusão real
   - Gerou risco sistêmico
   - É transversal (não local)
   - Cria fronteira clara (X ≠ Y)
   - Já está em uso
3. **CEO aprova a entrada**

**Proibido adicionar:**
- ❌ Teoria sem validação prática
- ❌ Formalismo sem necessidade operacional
- ❌ Conceitos que não foram testados
- ❌ Ontologia "preventiva"
- ❌ Glossário de termos

**Motivo:** Ontologia congela aprendizado, não inovação.

**Processo completo:** Ver `/METODO/ONTOLOGY_DECISIONS_TRIGGER.md`

---

**Versão:** 1.0  
**Criado:** 8 de Janeiro de 2026  
**Criado por:** Manus (Agent)  
**Aprovado por:** CEO (Joubert Jr)  
**Status:** Canônico (Tipo A)
