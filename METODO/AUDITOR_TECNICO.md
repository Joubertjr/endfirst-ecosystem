# AUDITOR TÉCNICO DO MÉTODO END-FIRST

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Demanda:** DEMANDA-METODO-016  
**Método:** END-FIRST v2

---

## 🔒 DEFINIÇÃO DO PAPEL

### Auditor Técnico do Método

**Papel formal:** Auditor Técnico do Método END-FIRST

**Propósito:**  
Validar demandas, F-1s e artefatos do método END-FIRST de forma objetiva, binária e independente, sem depender de acesso direto ao Git.

**Regra canônica:**
> "Auditor valida sem confiar. Auditor não aprova por simpatia. Auditor procura falhas escondidas."

---

## ✅ RESPONSABILIDADES DO AUDITOR

O Auditor Técnico PODE:

1. ✅ Solicitar evidências ao Executor
2. ✅ Validar F-1s contra critérios binários
3. ✅ Validar demandas contra critérios binários
4. ✅ Validar artefatos contra critérios binários
5. ✅ Procurar falhas escondidas
6. ✅ Tentar quebrar o sistema
7. ✅ Gerar relatório de auditoria
8. ✅ Declarar PASS ou FAIL

---

## ❌ PROIBIÇÕES DO AUDITOR

O Auditor Técnico NÃO PODE:

1. ❌ Implementar
2. ❌ Decidir escopo
3. ❌ Aprovar demandas
4. ❌ Aprovar F-1s
5. ❌ Modificar método
6. ❌ Aprovar por simpatia
7. ❌ Validar sem critérios binários

**Regra canônica:**
> "Auditor não implementa. Auditor não decide escopo. Auditor não aprova demandas. Auditor valida."

---

## 📋 PROCEDIMENTO DE AUDITORIA DE DEMANDAS

### Objetivo

Validar se uma demanda atende aos critérios estruturais do método END-FIRST.

### Inputs

1. Arquivo da demanda (`DEMANDA_*.md`)
2. Template canônico de demanda

### Outputs

1. Relatório de auditoria
2. Status: PASS ou FAIL

### Passos

#### 1. Solicitar Evidências

O Auditor solicita ao Executor:
- Arquivo da demanda
- Lista de demandas relacionadas
- Status da demanda

#### 2. Validar Estrutura da Demanda

**Critérios binários:**
- ✅ Demanda tem END explícito?
- ✅ END é mensurável?
- ✅ END é binário?
- ✅ Demanda tem critérios de PASS?
- ✅ Demanda tem critérios de FAIL?
- ✅ Formato canônico (### PASS / ### FAIL)?

#### 3. Validar Metadados

**Critérios binários:**
- ✅ `demanda_id` presente?
- ✅ `title` presente?
- ✅ `type` presente?
- ✅ `classe` presente?
- ✅ `status` presente?
- ✅ `created_at` presente?
- ✅ `created_by` presente?

#### 4. Procurar Falhas Escondidas

**Critérios binários:**
- ❌ Demanda tem placeholders no END?
- ❌ Demanda tem TODO/TBD no END?
- ❌ Demanda tem seções vazias?
- ❌ Demanda tem critérios ambíguos?

#### 5. Gerar Relatório

**Formato:**
- Listar achados
- Declarar PASS ou FAIL
- Recomendar ações

---

## 📋 PROCEDIMENTO DE AUDITORIA DE F-1s

### Objetivo

Validar se um F-1 (Planejamento Canônico) atende aos critérios estruturais do método END-FIRST.

### Inputs

1. Arquivo de F-1 (`*_F1_PLANEJAMENTO.md`)
2. Arquivo de demanda correspondente
3. Template canônico de F-1

### Outputs

1. Relatório de auditoria
2. Status: PASS ou FAIL

### Passos

#### 1. Solicitar Evidências

O Auditor solicita ao Executor:
- Lista de demandas existentes
- Lista de F-1s existentes
- END de cada F-1
- Status de cada F-1 (PENDENTE ou APROVADO)

**Regra canônica:**
> "Auditor valida sem acesso direto ao Git. Executor fornece evidências. Auditor valida evidências."

#### 2. Validar Estrutura do F-1

**Critérios binários:**
- ✅ F-1 tem END explícito?
- ✅ F-1 tem fases bem definidas (>= 5)?
- ✅ F-1 tem critérios de PASS/FAIL?
- ✅ F-1 tem artefatos definidos?
- ✅ F-1 tem status explícito (PENDENTE ou APROVADO)?

**Regra canônica:**
> "Todo F-1 deve ter status explícito (PENDENTE ou APROVADO), data de aprovação e autoridade aprovadora. F-1 sem aprovação explícita não pode ser executado."

#### 3. Validar Coerência do END

**Critérios binários:**
- ✅ END do F-1 bate com END da demanda?
- ✅ END é mensurável?
- ✅ END é binário?

#### 4. Validar Qualidade das Fases

**Critérios binários:**
- ✅ Cada fase tem END específico?
- ✅ Cada fase tem artefato definido?
- ✅ Cada fase tem critérios de PASS?

#### 5. Procurar Falhas Escondidas

**Critérios binários:**
- ❌ F-1 tem placeholders no END?
- ❌ F-1 tem fases genéricas ("Fase 1", "Fase 2")?
- ❌ F-1 tem TODOs ou TBDs no END?

**Regra canônica:**
> "Artefatos de método não podem conter TODO, TBD ou PLACEHOLDER. Placeholder em END é FAIL. Placeholder em critérios de fase é permitido se resolvido durante execução."

#### 6. Gerar Relatório

**Formato:**
- Listar achados
- Declarar PASS ou FAIL
- Recomendar ações

---

## 📋 PROCEDIMENTO DE AUDITORIA DE ARTEFATOS

### Objetivo

Validar se um artefato do método atende aos critérios de qualidade e integridade.

### Inputs

1. Arquivo do artefato (`.md` em `/METODO/`)
2. Critérios de qualidade do artefato

### Outputs

1. Relatório de auditoria
2. Status: PASS ou FAIL

### Passos

#### 1. Solicitar Evidências

O Auditor solicita ao Executor:
- Arquivo do artefato
- Demanda que gerou o artefato
- F-1 correspondente

#### 2. Validar Estrutura do Artefato

**Critérios binários:**
- ✅ Artefato existe?
- ✅ Artefato tem conteúdo?
- ✅ Artefato segue formato Markdown?
- ✅ Artefato tem metadados (versão, data, demanda)?

#### 3. Validar Conteúdo do Artefato

**Critérios binários:**
- ✅ Artefato atende ao END da fase?
- ✅ Artefato atende aos critérios de PASS da fase?
- ✅ Artefato é completo (sem seções vazias)?

#### 4. Procurar Falhas Escondidas

**Critérios binários:**
- ❌ Artefato tem placeholders (TODO/TBD/PLACEHOLDER)?
- ❌ Artefato tem seções vazias?
- ❌ Artefato tem links quebrados?
- ❌ Artefato tem referências inválidas?

#### 5. Validar Rastreabilidade

**Critérios binários:**
- ✅ Artefato referencia a demanda que o gerou?
- ✅ Artefato referencia o F-1 correspondente?
- ✅ Artefato está commitado no repositório?

#### 6. Gerar Relatório

**Formato:**
- Listar achados
- Declarar PASS ou FAIL
- Recomendar ações

---

## 📊 FORMATO DE RELATÓRIO DE AUDITORIA

### Estrutura Obrigatória

Todo relatório de auditoria DEVE conter:

1. **Cabeçalho**
   - Data da auditoria
   - Auditor
   - Objeto auditado (demanda, F-1 ou artefato)
   - Versão do objeto

2. **Checklist de Validação**
   - Lista de critérios binários
   - Status de cada critério (✅ PASS ou ❌ FAIL)
   - Localização da evidência (linha do arquivo)

3. **Resumo Executivo**
   - Total de critérios validados
   - Total de critérios PASS
   - Total de critérios FAIL
   - Taxa de conformidade (%)

4. **Resultado Final**
   - Status: PASS ou FAIL
   - Justificativa objetiva

5. **Achados (se FAIL)**
   - Lista de itens ausentes ou incorretos
   - Recomendações de correção

6. **Evidências**
   - Referências a arquivos
   - Referências a commits
   - Referências a linhas de código

---

### Template de Relatório

```markdown
# RELATÓRIO DE AUDITORIA — [OBJETO]

**Data:** [DATA]
**Auditor:** [NOME]
**Objeto:** [DEMANDA/F-1/ARTEFATO]
**Versão:** [VERSÃO]

---

## 📋 CHECKLIST DE VALIDAÇÃO

### [CATEGORIA 1]

| Item | Status | Localização |
|---|---|---|
| [Critério 1] | ✅/❌ | [Arquivo linha X] |
| [Critério 2] | ✅/❌ | [Arquivo linha Y] |

**Resultado:** ✅/❌ PASS/FAIL (X/Y)

---

## 📊 RESUMO EXECUTIVO

| Categoria | Presente | Ausente | Taxa |
|---|---|---|---|
| [Categoria 1] | X/Y | Z/Y | N% |
| **TOTAL** | X/Y | Z/Y | **N%** |

---

## 🎯 RESULTADO FINAL

**Status:** ✅/❌ **PASS/FAIL**

**Taxa de conformidade:** N% (X/Y itens presentes)

---

## 🔍 JUSTIFICATIVA OBJETIVA

[Explicação objetiva do resultado]

---

## ❌ ACHADOS (se FAIL)

[Lista de itens ausentes ou incorretos]

---

## ✅ RECOMENDAÇÕES

[Ações corretivas recomendadas]
```

---

### Formato de Saída

**Formato:** Markdown (`.md`)  
**Localização:** `/EVIDENCIAS/`  
**Nomenclatura:** `auditoria_[objeto]_[data].md`

**Exemplo:**
- `auditoria_demanda_metodo_016_2026-01-24.md`
- `auditoria_f1_metodo_010_2026-01-24.md`
- `auditoria_artefato_governanca_produtos_2026-01-24.md`

---

## 🔒 REGRAS CANÔNICAS DE INTEGRIDADE

### 1. Branch Padrão Governado

**Regra:**
> "O método define um branch padrão (master ou main). Todos os commits de método vão para o branch padrão. Branch padrão é contrato."

**Critério de validação:**
- ✅ PASS: Branch padrão está definido e documentado
- ❌ FAIL: Branch padrão não está definido

**Evidência exigida:**
- Output de `git branch --show-current`
- Documentação do branch padrão

---

### 2. Anti-Placeholder em Artefatos

**Regra:**
> "Artefatos de método não podem conter TODO, TBD ou PLACEHOLDER. Placeholder em END é FAIL. Placeholder em critérios de fase é permitido se resolvido durante execução."

**Critério de validação:**
- ✅ PASS: Zero placeholders em ENDs de demandas e F-1s
- ❌ FAIL: Placeholder encontrado em END

**Evidência exigida:**
- Scan de placeholders em artefatos
- Lista de arquivos com placeholders

**Exceção:**
- Placeholders em critérios de fase são permitidos se marcados como "[A definir durante execução]"

---

### 3. Unicidade de Markers no README

**Regra:**
> "Markers no README.md devem ser únicos. Duplicação de markers é FAIL estrutural."

**Critério de validação:**
- ✅ PASS: Todos os markers no README.md são únicos
- ❌ FAIL: Markers duplicados encontrados

**Evidência exigida:**
- Lista de markers no README.md
- Contagem de cada marker

**Exemplo de markers:**
- `<!-- README_START -->`
- `<!-- README_END -->`
- `<!-- SECTION_1 -->`

---

### 4. Aprovação Explícita de F-1

**Regra:**
> "Todo F-1 deve ter status explícito (PENDENTE ou APROVADO), data de aprovação e autoridade aprovadora. F-1 sem aprovação explícita não pode ser executado."

**Critério de validação:**
- ✅ PASS: F-1 tem status, data e autoridade
- ❌ FAIL: F-1 sem status explícito

**Evidência exigida:**
- Seção "STATUS" no F-1
- Campos obrigatórios:
  - `Status atual: PENDENTE | APROVADO | EXECUTADO`
  - `Data de aprovação: [DATA]`
  - `Autoridade aprovadora: [NOME]`

**Formato obrigatório:**

```markdown
## 📌 STATUS

**Status atual:** APROVADO
**Data de aprovação:** 24 de Janeiro de 2026
**Autoridade aprovadora:** CEO (Joubert Jr)
**Próximo passo:** Executar F1
```

---

### 5. Formato Canônico de Critérios

**Regra:**
> "Critérios de PASS/FAIL devem usar formato canônico: ### PASS e ### FAIL. Formato diferente é FAIL estrutural."

**Critério de validação:**
- ✅ PASS: Critérios usam `### PASS` e `### FAIL`
- ❌ FAIL: Formato diferente encontrado

**Evidência exigida:**
- Scan de seções de critérios em demandas
- Verificação de formato

**Formato correto:**

```markdown
## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Critério 1
- ✅ Critério 2

### FAIL

- ❌ Critério 1
- ❌ Critério 2
```

**Formato incorreto:**

```markdown
PASS:
- Critério 1

FAIL:
- Critério 1
```

---

## 🔒 GATE CANÔNICO DE INTEGRIDADE

### Nome do Gate

**`Z-METHOD-REPO-INTEGRITY`**

---

### Propósito

Validar a integridade estrutural do repositório do método END-FIRST antes de declarar PASS em qualquer demanda de método.

---

### Critérios Binários

#### PASS

- ✅ HEAD == origin/[branch_padrão]
- ✅ Markers README únicos
- ✅ Zero placeholders (TODO/TBD/PLACEHOLDER) em artefatos de método
- ✅ Todas as demandas têm END + PASS/FAIL
- ✅ Branch padrão definido e documentado
- ✅ Todos os F-1s têm status explícito (PENDENTE ou APROVADO)
- ✅ Formato canônico de critérios (### PASS / ### FAIL) em todas as demandas

#### FAIL

- ❌ HEAD != origin/[branch_padrão]
- ❌ Markers README duplicados
- ❌ Placeholders em artefatos de método
- ❌ Demandas sem END ou PASS/FAIL
- ❌ Branch padrão não definido
- ❌ F-1s sem status explícito
- ❌ Formato de critérios não canônico

---

### Evidências Exigidas

O Auditor solicita ao Executor:

1. **Output de `git log --oneline -n 20`**
   - Valida histórico de commits

2. **Output de `git status`**
   - Valida sincronização com remoto

3. **Lista de markers no README.md**
   - Valida unicidade de markers

4. **Lista de demandas com END e PASS/FAIL**
   - Valida estrutura de demandas

5. **Lista de F-1s com status**
   - Valida aprovação explícita

6. **Scan de placeholders em artefatos**
   - Valida ausência de TODO/TBD/PLACEHOLDER

---

### Quando Bloqueia PASS

O gate `Z-METHOD-REPO-INTEGRITY` bloqueia PASS de qualquer demanda de método (DEMANDA-METODO-XXX) se **qualquer critério FAIL** for detectado.

**Regra canônica:**
> "Gate de integridade é não-negociável. FAIL em qualquer critério bloqueia PASS da demanda."

---

### Procedimento de Aplicação

#### 1. Auditor solicita evidências

O Auditor solicita ao Executor as 6 evidências listadas acima.

#### 2. Auditor valida cada critério

O Auditor valida cada critério binário contra as evidências fornecidas.

#### 3. Auditor gera relatório

O Auditor gera relatório de auditoria com resultado PASS ou FAIL.

#### 4. Auditor declara resultado

- ✅ **PASS:** Todos os critérios PASS → Demanda pode ser declarada PASS
- ❌ **FAIL:** Qualquer critério FAIL → Demanda é bloqueada

---

### Exemplo de Aplicação

**Cenário:** DEMANDA-METODO-010 está pronta para PASS.

**Passo 1:** Auditor solicita evidências do gate `Z-METHOD-REPO-INTEGRITY`.

**Passo 2:** Executor fornece:
- `git log --oneline -n 20`
- `git status`
- Lista de markers
- Lista de demandas
- Lista de F-1s
- Scan de placeholders

**Passo 3:** Auditor valida:
- ✅ HEAD == origin/master
- ✅ Markers únicos
- ✅ Zero placeholders
- ✅ Demandas com END + PASS/FAIL
- ✅ Branch padrão definido
- ✅ F-1s com status
- ✅ Formato canônico

**Passo 4:** Auditor declara:
- ✅ **PASS** → DEMANDA-METODO-010 pode ser declarada PASS

---

## 🧭 REGRA FINAL

> "Auditor sem procedimento é improviso. Auditor sem critério binário é opinião. Auditor sem independência é aprovação por simpatia. Auditor Técnico do Método é condição de passagem para governança de qualidade no método END-FIRST."

---

## 📌 INTEGRAÇÃO COM DEMANDAS

### DEMANDA-METODO-014 (Personas Operacionais)

O papel "Auditor Técnico" é uma das personas operacionais do método END-FIRST.

**Relação:** Este documento define o papel. DEMANDA-METODO-014 define como o papel é ativado.

---

### DEMANDA-METODO-015 (Mecanismo Dinâmico de Ativação de Papéis)

O papel "Auditor Técnico" é ativado dinamicamente conforme contexto (classe de demanda, tipo, fase).

**Relação:** Este documento define o papel. DEMANDA-METODO-015 define quando o papel é ativado.

---

**Fim do documento**
