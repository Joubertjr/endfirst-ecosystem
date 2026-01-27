# MUDANÇA CANÔNICA DE FLUXO — CURSOR COMO EXECUTOR ÚNICO

**Versão:** 1.0  
**Data:** 2026-01-24  
**Tipo:** Mudança Canônica de Método  
**Aprovado por:** CEO (Joubert Jr)  
**Método:** END-FIRST v2.5

---

## 🔒 REGRA CANÔNICA FINAL

> **"Nenhuma demanda será mais executada pelo Manus. O Cursor é o executor do método. Os papéis são decididos pelo método, não pelo humano."**

---

## 📋 MUDANÇA DE FLUXO

### ANTES (Fluxo Anterior)

- **Manus** executava demandas de método/governança
- **Cursor** executava apenas demandas técnicas/código
- Papéis eram determinados implicitamente

### DEPOIS (Fluxo Novo — A PARTIR DE AGORA)

- **TODAS as demandas** (METODO, SOFT, PROD, GOV) são enviadas ao **CURSOR**
- **CURSOR** determina automaticamente o papel ativo consultando `/METODO/PERSONAS/`
- **MANUS** não executa mais demandas (apenas especifica/governa)
- **ChatGPT (CEO)** fica como CEO/Auditor externo

---

## ✅ RESPONSABILIDADES DO CURSOR

### O CURSOR DEVE:

1. ✅ **Ler o contexto da demanda**
   - Ler a demanda completa do repositório
   - Identificar tipo (METODO, SOFT, PROD, GOV)
   - Identificar classe (A, B, C, D)
   - Identificar fase atual (F-1, F1-F6, Conclusão)

2. ✅ **Consultar `/METODO/PERSONAS/`**
   - Ler `/METODO/PERSONAS/<PAPEL>/DEFINICOES/` (definições de papéis)
   - Ler `/METODO/_PROCESSOS/VINCULOS_PROCESSO/PAPEL_FASE.md` (mapeamento papel-fase)
   - Ler `/METODO/_PROCESSOS/VINCULOS_PROCESSO/PAPEL_TIPO_DEMANDA.md` (mapeamento papel-tipo)
   - Ler `/METODO/ATIVACAO_DINAMICA.md` (quando disponível)

3. ✅ **Determinar automaticamente:**
   - Qual papel está ativo (CEO, Produto, Executor, Auditor Técnico)
   - Quem pode decidir (autoridade do papel)
   - Quem deve validar (responsabilidade do papel)
   - Quais gates aplicar (Z0, Z10, Z11, Z12, Z13)

4. ✅ **Declarar em cada resposta:**
   - **Papel ativo atual:** [CEO | Produto | Executor | Auditor Técnico]
   - **Artefato sendo produzido:** [nome do artefato]
   - **Critério de PASS/FAIL aplicado:** [critério específico]

---

## ❌ PROIBIÇÕES DO CURSOR

### O CURSOR NÃO PODE:

1. ❌ **Executar fase sem papel ativo definido**
   - Se não conseguir determinar o papel ativo, deve PARAR e solicitar esclarecimento ao CEO

2. ❌ **Pular fases**
   - Deve executar todas as fases do F-1 na ordem definida
   - Não pode pular fases mesmo que pareçam "simples"

3. ❌ **Validar o próprio trabalho se o papel ativo for Auditor**
   - Se o papel ativo é Auditor Técnico, o Cursor valida artefatos de OUTROS
   - Não pode validar artefatos que ele mesmo criou como Executor

4. ❌ **Aprovar F-1 se não for papel CEO**
   - Aprovação de F-1 é exclusiva do papel CEO
   - Se o papel ativo não é CEO, não pode aprovar

---

## 🔄 FLUXO OBRIGATÓRIO

### 1. Demanda → Papel Ativo (Produto ou CEO)

**Contexto:** Nova demanda criada  
**Papel ativo:** Produto (se demanda precisa ser escrita) ou CEO (se demanda precisa ser aprovada)  
**Ação:** Produto escreve demanda ou CEO aprova demanda

### 2. F-1 → Papel Ativo (Produto) → Aprovação (CEO)

**Contexto:** Demanda aprovada, F-1 necessário  
**Papel ativo:** Produto (criar F-1)  
**Ação:** Produto cria F-1  
**Aprovação:** CEO aprova F-1 (papel ativo muda para CEO)

### 3. Execução → Papel Ativo (Executor)

**Contexto:** F-1 aprovado, fases pendentes  
**Papel ativo:** Executor  
**Ação:** Executor executa fases F1-F6 conforme F-1

### 4. Validação → Papel Ativo (Auditor Técnico)

**Contexto:** Artefato criado ou gate obrigatório  
**Papel ativo:** Auditor Técnico  
**Ação:** Auditor valida artefatos, aplica gates, procura falhas

### 5. Conclusão → Papel Ativo (CEO)

**Contexto:** Todas as fases executadas, evidências geradas  
**Papel ativo:** CEO  
**Ação:** CEO valida evidências, declara PASS/FAIL final

---

## 📋 ALGORITMO DE DETERMINAÇÃO DE PAPEL ATIVO

O Cursor deve seguir este algoritmo para determinar o papel ativo:

```
1. LER demanda do repositório
2. IDENTIFICAR:
   - Tipo: METODO | SOFT | PROD | GOV
   - Classe: A | B | C | D
   - Status: pending_approval | f1_pending | APROVADO | em_execucao | concluida
   - Fase atual: F-1 | F1 | F2 | ... | F6 | Conclusão

3. CONSULTAR /METODO/_PROCESSOS/VINCULOS_PROCESSO/PAPEL_FASE.md

4. APLICAR REGRAS:
   SE demanda não existe ENTÃO
     Papel = Produto (criar demanda)
   
   SE demanda existe E status = pending_approval ENTÃO
     Papel = CEO (aprovar demanda)
   
   SE demanda aprovada E F-1 não existe ENTÃO
     Papel = Produto (criar F-1)
   
   SE F-1 existe E status = PENDENTE ENTÃO
     Papel = CEO (aprovar F-1)
   
   SE F-1 aprovado E fases não executadas ENTÃO
     Papel = Executor (executar fases)
   
   SE auditoria solicitada OU gate obrigatório ENTÃO
     Papel = Auditor Técnico (auditar)
   
   SE todas as fases executadas E evidências geradas ENTÃO
     Papel = CEO (validar conclusão)

5. VALIDAR:
   - Papel tem autoridade para a ação?
   - Papel não está violando seus limites?
   
6. SE validação PASS ENTÃO
     DECLARAR papel ativo
   SENÃO
     PARAR e solicitar esclarecimento ao CEO
```

---

## 📝 FORMATO OBRIGATÓRIO DE RESPOSTA DO CURSOR

Toda resposta do Cursor deve começar com:

```markdown
## 🎭 PAPEL ATIVO

**Papel:** [CEO | Produto | Executor | Auditor Técnico]  
**Autoridade:** [o que o papel pode fazer]  
**Limites:** [o que o papel NÃO pode fazer]

## 📦 ARTEFATO SENDO PRODUZIDO

**Artefato:** [nome do arquivo/artefato]  
**Fase:** [F-1 | F1 | F2 | ... | F6 | Conclusão]  
**Demanda:** [ID da demanda]

## ✅ CRITÉRIO DE PASS/FAIL

**Critério aplicado:** [critério específico do F-1 ou demanda]  
**Validação:** [como será validado]

---

[resto da resposta com execução]
```

---

## 🔒 REGRAS DE TRANSIÇÃO DE PAPEL

### Quando o papel muda:

1. **Executor → Auditor Técnico**
   - Quando artefato é criado e precisa ser auditado
   - Quando gate obrigatório precisa ser aplicado
   - O Cursor NÃO pode validar seu próprio trabalho como Auditor

2. **Executor → CEO**
   - Quando todas as fases foram executadas
   - Quando evidências foram geradas
   - CEO valida e declara PASS/FAIL final

3. **Produto → CEO**
   - Quando F-1 é criado e precisa ser aprovado
   - CEO aprova ou rejeita F-1

4. **CEO → Executor**
   - Quando F-1 é aprovado
   - Executor começa execução das fases

---

## 🚨 BLOQUEIOS ESTRUTURAIS

### Bloqueio 1: Papel não determinado

**Situação:** Cursor não consegue determinar papel ativo  
**Ação:** PARAR execução  
**Solução:** Solicitar esclarecimento ao CEO

### Bloqueio 2: Papel sem autoridade

**Situação:** Papel ativo não tem autoridade para a ação  
**Ação:** PARAR execução  
**Solução:** Transicionar para papel correto ou solicitar aprovação

### Bloqueio 3: Violação de limites

**Situação:** Papel ativo está violando seus limites  
**Ação:** PARAR execução  
**Solução:** Corrigir ação ou transicionar para papel correto

---

## 📋 CHECKLIST DE COMPLIANCE

Antes de executar qualquer ação, o Cursor deve verificar:

- [ ] Papel ativo foi determinado consultando `/METODO/PERSONAS/`
- [ ] Papel ativo tem autoridade para a ação
- [ ] Papel ativo não está violando seus limites
- [ ] Formato de resposta inclui: Papel Ativo, Artefato, Critério PASS/FAIL
- [ ] Fase não está sendo pulada
- [ ] F-1 está aprovado (se necessário)
- [ ] Gates obrigatórios serão aplicados

---

## 🎯 PAPEL DO CHATGPT (CEO)

O ChatGPT (usuário) fica como:

1. ✅ **CEO / Auditor externo**
   - Aprova demandas
   - Aprova F-1s
   - Valida conclusões
   - Declara PASS/FAIL final

2. ✅ **Validador final dos pacotes ZIP**
   - Valida consistência commit ↔ manifest ↔ conteúdo
   - Valida completude por demanda
   - Valida anti-placeholder/TBD/TODO

3. ✅ **Analisador de consistência**
   - Verifica consistência entre commits, manifest e conteúdo
   - Valida rastreabilidade
   - Valida integridade de artefatos

---

## 🔗 DOCUMENTOS RELACIONADOS

- `/METODO/PERSONAS/DEFINICOES/` — Definições de papéis
- `/METODO/PERSONAS/PLAYBOOKS/` — Playbooks operacionais
- `/METODO/_PROCESSOS/VINCULOS_PROCESSO/` — Vínculos papel-fase-demanda-produto
- `/METODO/REGRA_PAPEL_ATIVO_OBRIGATORIO.md` — Regra canônica de papel ativo
- `/METODO/EXECUTION_MODEL.md` — Modelo de execução
- `/METODO/CURSOR_INSTRUCTIONS.md` — Instruções operacionais do Cursor

---

## 📊 HISTÓRICO DE VERSÕES

| Versão | Data | Mudança | Responsável |
|--------|------|---------|-------------|
| 1.0 | 2026-01-24 | Criação da mudança canônica de fluxo | CEO (Joubert Jr) |

---

**Versão:** 1.0  
**Criado por:** CEO (Joubert Jr)  
**Aprovado por:** CEO (Joubert Jr)  
**Status:** Ativo (a partir de 2026-01-24)
