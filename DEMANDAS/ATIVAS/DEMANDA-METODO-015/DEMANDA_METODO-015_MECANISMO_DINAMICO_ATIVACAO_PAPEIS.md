---
demanda_id: DEMANDA-METODO-015
title: Mecanismo Dinâmico de Ativação de Papéis
type: método / meta-governança
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-METODO-015 — Mecanismo Dinâmico de Ativação de Papéis

**Tipo:** Método / Meta-Governança  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

**END (exato):**

> "Dado um contexto (produto + tipo de demanda + classe + fase), o método determina automaticamente qual papel está ativo, quais decisões são permitidas, quais perguntas são obrigatórias e quais evidências bloqueiam PASS — de forma auditável e sem depender de explicação humana."

**Nota:** Esta demanda usa a ontologia de personas em `/METODO/PERSONAS/` e os vínculos em `/METODO/PERSONAS/VINCULOS_PROCESSO/` como base.

---

## 🚫 Regras Canônicas

**Papel Dinâmico:**

> "Papel muda conforme contexto. Contexto determina papel. Papel sem contexto é improviso."

**Determinismo Obrigatório:**

> "Mesmo contexto DEVE produzir mesmo papel ativo. Não-determinismo é alucinação."

**Anti-Alucinação por Papel:**

> "Executor não decide escopo. CEO não implementa. Auditor não aprova por simpatia. Papel fora de limite é FAIL estrutural."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Existe um artefato canônico no método com:
  - Papéis (CEO, Produto, Executor, Auditor)
  - Autoridade de cada papel
  - Proibições de cada papel
  - Checklist obrigatório por papel
  - Evidências obrigatórias por papel

- ✅ Existe um artefato canônico com regras de ativação dinâmica:
  - Matriz de contexto → perfil ativo
  - INPUTS: Classe (A/B/C/D), Tipo (Método/Produto/Software), Fase (F-1, F1-F6), Produto alvo, Risco
  - OUTPUT: Papel ativo, Checklist obrigatório, Bloqueios ativados

- ✅ Para 3 cenários reais, o método produz o mesmo "perfil ativo" sempre (determinístico):
  - Cenário 1: Classe A + Produto + F4
  - Cenário 2: Classe C + UX + F1
  - Cenário 3: Método + F-1

- ✅ "Executor" não consegue justificar decisão fora do papel sem gerar FAIL (regra explícita)

### FAIL

- ❌ Artefato de papéis não existe
- ❌ Artefato de ativação dinâmica não existe
- ❌ Método não é determinístico (mesmo contexto produz papéis diferentes)
- ❌ Executor pode decidir fora do papel sem FAIL
- ❌ Papel sem limite explícito

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um mecanismo formal que determine automaticamente qual papel está ativo em cada contexto. Isso gera:

1. **Alucinação de papel:** Executor decide escopo, CEO implementa, Auditor aprova por simpatia
2. **Improviso:** Papel muda sem critério binário
3. **Não-determinismo:** Mesmo contexto produz papéis diferentes
4. **Perda de governança:** Não há critério para validar se um papel está agindo conforme

### Impacto

Sem mecanismo dinâmico:
- Papel vira "habilidade implícita" (memória humana)
- Governança é perdida
- Alucinação é inevitável
- Qualidade não é garantida

---

## 🚫 DO / DON'T

### ✅ DO

- **Definir papéis canônicos:** CEO, Produto, Executor, Auditor
- **Definir autoridade de cada papel**
- **Definir proibições de cada papel**
- **Criar matriz de ativação dinâmica:** contexto → papel ativo
- **Garantir determinismo:** mesmo contexto = mesmo papel
- **Criar regra anti-alucinação:** papel fora de limite = FAIL

### ❌ DON'T

- **Permitir papel sem limite explícito**
- **Permitir executor decidir escopo**
- **Permitir CEO implementar**
- **Permitir auditor aprovar por simpatia**
- **Permitir não-determinismo**
- **Permitir improviso de papel**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- **Depende de:** DEMANDA-METODO-014 (Personas Operacionais)

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. **Matriz de Papéis Canônicos**
   - `/METODO/PAPEIS_CANONICOS.md`
   - Definição de cada papel (CEO, Produto, Executor, Auditor)
   - Autoridade de cada papel
   - Proibições de cada papel
   - Checklist obrigatório por papel
   - Evidências obrigatórias por papel

2. **Mecanismo de Ativação Dinâmica**
   - `/METODO/ATIVACAO_DINAMICA_PAPEIS.md`
   - Matriz de contexto → perfil ativo
   - INPUTS: Classe, Tipo, Fase, Produto, Risco
   - OUTPUT: Papel ativo, Checklist, Bloqueios
   - Regras de ativação
   - Exemplos de ativação

3. **Validação de Determinismo**
   - 3 cenários reais testados
   - Prova de determinismo (mesmo contexto = mesmo papel)

### Validações

1. Artefato de papéis criado e commitado
2. Artefato de ativação dinâmica criado e commitado
3. Determinismo validado (3 cenários)
4. Regra anti-alucinação explícita
5. Papel fora de limite = FAIL

---

## 🔍 LIMITES POR PAPEL

### CEO
**Pode:**
- Validar END
- Decidir PASS/FAIL
- Priorizar demandas
- Definir regra canônica

**NÃO pode:**
- Implementar
- Escrever código
- Executar fases

---

### Produto (Chefe de Produto)
**Pode:**
- Converter problema em demanda
- Definir aceitação binária
- Recortar escopo

**NÃO pode:**
- Reescrever método
- Implementar
- Decidir PASS/FAIL final

---

### Executor (Cursor/Dev)
**Pode:**
- Executar estritamente o F-1 aprovado
- Gerar evidência
- Implementar

**NÃO pode:**
- Decidir escopo
- Mudar END
- Aprovar demanda

---

### Auditor (Manus/QA)
**Pode:**
- Procurar falhas escondidas
- Validar binariamente
- Tentar quebrar

**NÃO pode:**
- Aprovar por simpatia
- Implementar
- Decidir escopo

---

## 📊 INPUTS E OUTPUTS DO MECANISMO

### INPUTS (Contexto)

1. **Classe da demanda:** A, B, C, D
2. **Tipo:** Método, Produto, Software
3. **Fase:** F-1, F1, F2, F3, F4, F5, F6
4. **Produto alvo:** (ex: Contratação TI)
5. **Risco:** (ex: execução longa, persistência, auditabilidade)

### OUTPUT (Perfil Ativo)

1. **Papel ativo:** Qual papel está ativo agora
2. **Checklist obrigatório:** Quais perguntas são obrigatórias
3. **Bloqueios ativados:** Quais evidências bloqueiam PASS

---

## ❌ Fora de Escopo

- Definição de personas de produto (isso é DEMANDA-METODO-014)
- Implementação de software para gerenciar papéis
- Migração de papéis existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Papel sem contexto é improviso. Contexto sem papel é alucinação. Mecanismo dinâmico de ativação de papéis é condição de passagem para governança de execução no método END-FIRST."
