---
demanda_id: DEMANDA-METODO-007
title: TDD e Clean Code como Bloqueio Estrutural do Método
type: Método / Governança
classe: nenhuma
altera_funcionalidade: não
exige_f1: sim
status: f1_pending
created_at: 2026-01-20
created_by: CEO (Joubert Jr)
executor: Manus (Agent)
governed_by: /METODO/END_FIRST_V2.md
version: 1.0
---

# DEMANDA-METODO-007 — TDD e Clean Code como Bloqueio Estrutural do Método

**Versão:** 1.0  
**Data de Criação:** 20 de Janeiro de 2026  
**Solicitado por:** CEO (Joubert Jr)  
**Executor:** Manus (Agent)  
**Status:** F-1 PENDENTE DE APROVAÇÃO  
**Tipo:** Método / Governança  

---

## 🧠 CONTEXTO (POR QUE ESSA DEMANDA EXISTE)

### Fato observado (evidência real, não opinião)

- DEMANDA-PROD-004 seguiu END-FIRST v2
- F-1 existia e foi aprovada
- Gates funcionais e de robustez foram respeitados
- **Mesmo assim, TDD foi violado**
- **Mesmo assim, Clean Code foi violado**
- **O método não bloqueou**

### Conclusão inevitável

> O método governa o que é feito, mas não governa como o código nasce.

Isso cria um **vácuo estrutural:**
- Qualidade vira intenção
- TDD vira recomendação
- Clean Code vira cultura
- Nenhum deles vira regra executável

**Esta demanda existe para fechar esse vácuo.**

---

## 🎯 END — Estado Final Esperado

**"Nenhuma fase pode ser declarada PASS, integrada ao produto ou ao método, se código foi escrito antes de testes ou se critérios objetivos de Clean Code forem violados.**

**A ordem TDD (RED → GREEN → REFACTOR) e os critérios mínimos de Clean Code passam a ser regras formais do método END-FIRST, auditáveis, binárias e não negociáveis."**

### Resumo do END

> "Qualidade de código deixa de ser uma boa prática e passa a ser um bloqueio estrutural do método END-FIRST."

---

## 🧩 PROBLEMA QUE A DEMANDA RESOLVE

### Hoje (estado atual)

- F-1 governa o que provar
- Gates governam o que validar
- Robustez governa o que sobreviver
- ❌ **Nada governa como o código é produzido**

**Resultado:**
- Código pode nascer errado e "passar"
- Testes viram correção tardia
- Refatoração vira dívida

### Depois da DEMANDA-METODO-007

- Código não nasce sem teste
- Funções não crescem sem bloqueio
- Qualidade não depende de disciplina humana
- **Erro é bloqueado antes de existir**

---

## 🧱 PRINCÍPIOS CANÔNICOS INTRODUZIDOS

Esses princípios não são novos valores, são valores que passam a ter **força de lei no método:**

1. > "Código sem teste prévio não existe."

2. > "Teste que nasce depois do código não valida design."

3. > "Função grande demais é erro estrutural, não estilo."

4. > "Qualidade que depende de boa vontade não é método."

---

## 📐 ESCOPO DA DEMANDA (O QUE ELA MUDA)

### 1️⃣ END-FIRST v2 (documento central)

**Adicionar seção obrigatória:**

**"Governança de Qualidade de Código"**

Com regras como:
- Fase = FAIL se:
  - testes não precederam código
  - funções violam critérios objetivos
- Evidência de TDD passa a ser artefato válido
- Clean Code passa a ter critérios verificáveis (não subjetivos)

---

### 2️⃣ Template de F-1 (Planejamento Canônico)

**Adicionar seção obrigatória:**

**"Validação de TDD e Clean Code"**

Com critérios binários, por exemplo:
- TDD é obrigatório nesta demanda? (SIM / NÃO)
- Evidência RED → GREEN → REFACTOR existe?
- Critérios objetivos de Clean Code definidos?

**Sem essa seção preenchida:**
> F-1 é inválido.

---

### 3️⃣ .cursorrules

**Adicionar regras explícitas para o executor:**
- ❌ Não escrever código antes de teste
- ❌ Não declarar fase PASS sem evidência de TDD
- ❌ Não criar funções acima do limite definido
- ❌ Não misturar responsabilidades

**Cursor deixa de interpretar intenção e passa a obedecer contrato.**

---

## ✅ CRITÉRIOS DE ACEITAÇÃO

### PASS

A DEMANDA-METODO-007 só pode ser encerrada com PASS se:

1. ✅ **END-FIRST v2 tiver seção explícita de governança de TDD e Clean Code**
2. ✅ **Template de F-1 exigir validação formal de TDD/Clean Code**
3. ✅ **`.cursorrules` bloquear execução fora dessas regras**
4. ✅ **Seja possível responder objetivamente:**
   - "Este código nasceu com teste?"
   - "Este código respeita critérios objetivos?"

**Se qualquer resposta for "não sei" → FAIL.**

---

### FAIL

- ❌ Seção de governança de TDD/Clean Code ausente no END-FIRST v2
- ❌ Template de F-1 não exige validação de TDD/Clean Code
- ❌ `.cursorrules` não bloqueia violações
- ❌ Critérios de Clean Code permanecem subjetivos
- ❌ TDD permanece como recomendação (não bloqueio)

---

## 🚫 BLOQUEIOS ESTRUTURAIS (O QUE NÃO FAZER)

Para manter o método limpo:

- ❌ **Não implementar ferramenta**
- ❌ **Não escolher framework de teste**
- ❌ **Não definir linter específico**
- ❌ **Não mexer em código de produto**
- ❌ **Não criar automação de validação**

**Ela governa critérios, não implementações.**

---

## 📋 DO / DON'T

### DO (fazer)

- ✅ Definir critérios objetivos de Clean Code (tamanho, responsabilidade, complexidade)
- ✅ Tornar TDD obrigatório em F-1
- ✅ Bloquear PASS sem evidência de TDD
- ✅ Adicionar seção de governança ao END-FIRST v2
- ✅ Atualizar template de F-1
- ✅ Atualizar `.cursorrules` com bloqueios explícitos

### DON'T (não fazer)

- ❌ Escolher framework de teste específico
- ❌ Implementar ferramenta de validação
- ❌ Definir linter obrigatório
- ❌ Mexer em código de produto existente
- ❌ Criar automação de verificação
- ❌ Impor estilo de código subjetivo

---

## 📜 FRASES CANÔNICAS

> **"Qualidade não é uma expectativa. Qualidade é uma condição de passagem."**

> "Código sem teste prévio não existe."

> "Teste que nasce depois do código não valida design."

> "Função grande demais é erro estrutural, não estilo."

> "Qualidade que depende de boa vontade não é método."

---

## ✅ TODO CANÔNICO (F0-F6)

### F0 — Classificar Demanda

**END:** Demanda classificada como método/governança, não produto

**Critérios de PASS:**
- ✅ Tipo: Método / Governança
- ✅ Não altera funcionalidade de produto
- ✅ Não cria automação
- ✅ Governa critérios, não implementações

---

### F1 — Definir Critérios Objetivos de Clean Code

**END:** Critérios objetivos de Clean Code existem e são verificáveis

**Artefato esperado:** `/METODO/CLEAN_CODE_CRITERIA.md`

**Critérios de PASS:**
- ✅ Documento criado e versionado
- ✅ Critérios objetivos definidos (tamanho de função, responsabilidade, complexidade)
- ✅ Critérios são binários (não subjetivos)
- ✅ Exemplos de PASS/FAIL fornecidos

---

### F2 — Adicionar Governança de TDD ao END-FIRST v2

**END:** END-FIRST v2 tem seção explícita de governança de TDD e Clean Code

**Artefato esperado:** `/METODO/END_FIRST_V2.md` (atualizado)

**Critérios de PASS:**
- ✅ Seção "Governança de Qualidade de Código" adicionada
- ✅ TDD como regra formal (não recomendação)
- ✅ Critérios de Clean Code referenciados
- ✅ FAIL automático para violações

---

### F3 — Atualizar Template de F-1

**END:** Template de F-1 exige validação formal de TDD/Clean Code

**Artefato esperado:** `/METODO/TEMPLATE_DEMANDA_CANONICA.md` (atualizado)

**Critérios de PASS:**
- ✅ Seção "Validação de TDD e Clean Code" adicionada
- ✅ Campos obrigatórios: TDD obrigatório? (SIM/NÃO), Evidência RED→GREEN→REFACTOR, Critérios de Clean Code
- ✅ F-1 inválido sem essa seção preenchida

---

### F4 — Atualizar `.cursorrules`

**END:** `.cursorrules` bloqueia execução fora das regras de TDD/Clean Code

**Artefato esperado:** `.cursorrules` (atualizado)

**Critérios de PASS:**
- ✅ Regras explícitas adicionadas
- ✅ Bloqueios: não escrever código antes de teste, não declarar PASS sem evidência, não criar funções acima do limite
- ✅ Cursor opera sob contrato, não interpretação

---

### F5 — Criar Evidência de Aplicação Retroativa

**END:** Análise documentada de casos reais mostra onde o método deixou passar

**Artefato esperado:** `/EVIDENCIAS/aplicacao_retroativa_metodo_007.md`

**Critérios de PASS:**
- ✅ Análise de DEMANDA-PROD-004 documentada
- ✅ Demonstração de como nova regra teria bloqueado violações
- ✅ Comparativo método antigo vs novo

---

### F6 — Declarar PASS

**END:** Regra ativa, documentada, verificável e integrada ao método

**Artefato esperado:** `/DEMANDAS_MANUS/DEMANDA_METODO-007_F6_CONCLUSAO.md`

**Critérios de PASS:**
- ✅ Todos os artefatos criados e versionados
- ✅ END alcançado
- ✅ Bloqueios estruturais respeitados
- ✅ Método atualizado e integrado

---

## ❌ Fora de Escopo

- ❌ Implementar ferramenta de validação
- ❌ Escolher framework de teste
- ❌ Definir linter específico
- ❌ Mexer em código de produto
- ❌ Criar automação de verificação
- ❌ Migrar projetos existentes

**Razão:** Esta demanda define governança de qualidade de código, não implementações específicas de ferramentas.

---

## 📊 Histórico de Versões

- **v1.0** (2026-01-20): Versão inicial da demanda

---

## 🔗 Referências

- `/METODO/END_FIRST_V2.md` — Método END-FIRST v2
- `/METODO/TEMPLATE_DEMANDA_CANONICA.md` — Template canônico
- `.cursorrules` — Regras do Cursor
- `/DEMANDAS_MANUS/DEMANDA-PROD-004_*` — Evidência de violação de TDD/Clean Code

---

**Status:** F-1 PENDENTE DE APROVAÇÃO  
**Próximos passos:** Aguardar decisão do CEO para promover a F-1
