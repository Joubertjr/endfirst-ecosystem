---
demanda_id: DEMANDA-METODO-006
title: Governança de Consumo, Atualização e Onboarding do Método
type: Método / Governança
classe: nenhuma
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-20
created_by: CEO (Joubert Jr)
executor: Manus (Agent)
governed_by: /METODO/END_FIRST_V2.md
version: 1.0
---

# DEMANDA-METODO-006 — Governança de Consumo, Atualização e Onboarding do Método

**Versão:** 1.0  
**Data de Criação:** 20 de Janeiro de 2026  
**Solicitado por:** CEO (Joubert Jr)  
**Executor:** Manus (Agent)  
**Status:** BACKLOG  
**Tipo:** Método / Governança  

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Para qualquer projeto que utilize a metodologia END-FIRST (ex.: projeto do livro):

#### 1️⃣ O método é sempre a fonte de verdade ativa

- Existe uma única fonte canônica do método
- Projetos não redefinem, não resumem e não reinterpretam o método
- O método governa projetos; projetos não governam o método

**📌 Um observador externo consegue identificar qual método está em uso sem perguntar a ninguém.**

---

#### 2️⃣ O consumo do método é explícito e rastreável

- Todo projeto declara explicitamente:
  - que consome o método
  - qual versão conceitual do método está usando
- Não existe consumo implícito, tácito ou "por costume"

**📌 Se um projeto não declara consumo do método, ele não está autorizado a usar END-FIRST.**

---

#### 3️⃣ Atualizações do método não dependem de memória humana

- O método possui mecanismo canônico de atualização de conhecimento
- Mudanças relevantes no método:
  - são registradas
  - são comunicáveis
  - são rastreáveis
- Nenhum executor precisa "lembrar" o que mudou

**📌 Se alguém precisa avisar manualmente "o método mudou", o método falhou.**

---

#### 4️⃣ Onboarding é governado pelo método, não por explicação

- Existe uma definição clara de:
  - o que significa "estar onboardado no método"
  - quais artefatos são obrigatórios para onboarding
- Onboarding não depende de conversa, contexto prévio ou explicação verbal

**📌 Um agente novo (humano ou Cursor) consegue operar apenas lendo o método.**

---

#### 5️⃣ Ferramentas (Cursor, agentes) operam sob contrato metodológico

- Ferramentas não decidem como usar o método
- O método define:
  - o que a ferramenta deve respeitar
  - quando deve consultar o método
  - o que é proibido executar sem referência explícita

**📌 A ferramenta é executora. O método é autoridade.**

---

#### 6️⃣ Atualizações do método não quebram projetos silenciosamente

- O método deixa claro:
  - o que é retroativo
  - o que é apenas prospectivo
- Projetos conseguem saber:
  - se precisam agir
  - ou se permanecem válidos

**📌 Nenhuma mudança de método gera ambiguidade operacional.**

---

#### 7️⃣ O método explica como ele mesmo evolui

- Existe clareza sobre:
  - como o método muda
  - como esse conhecimento é preservado
  - como versões anteriores permanecem compreensíveis

**📌 O método não vira "versão oral" nem "estado mental do CEO".**

---

### 🧭 Resumo do END (Canônico)

> "Todo projeto que usa END-FIRST consome o método como contrato explícito, versionável e auditável. Atualizações do método são rastreáveis, onboarding é governado, e ferramentas executam sob autoridade metodológica — não por memória humana."

---

## 🚫 Regras Canônicas

**Método / Governança:**

> "Método governa projetos; projetos não governam método."

> "Se é preciso explicar o método, ele não está completo."

> "Conhecimento que depende de memória humana não é método."

> "Ferramenta executa regras; não interpreta intenção."

> "Usar o método sem declarar consumo é violação estrutural."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Existe mecanismo canônico de declaração de consumo do método por projetos
- ✅ Existe mecanismo canônico de versionamento conceitual do método
- ✅ Existe mecanismo canônico de comunicação de atualizações do método
- ✅ Existe definição clara de "onboarding completo" no método
- ✅ Existe contrato metodológico para ferramentas (Cursor, agentes)
- ✅ Existe distinção clara entre mudanças retroativas e prospectivas
- ✅ Existe documentação de como o método evolui

### FAIL

- ❌ Projeto usa END-FIRST sem declarar consumo explícito
- ❌ Atualização do método depende de "avisar manualmente"
- ❌ Onboarding depende de explicação verbal ou contexto prévio
- ❌ Ferramenta interpreta intenção sem referência explícita ao método
- ❌ Mudança de método gera ambiguidade operacional

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe:** Nenhuma (demanda de método/governança)
- **Todas:** Z12 (Auditoria Canônica) obrigatório

**Referência:** `/METODO/GOVERNANCA_GATES.md`

---

## 🧠 Problemas Observados

**Contexto (não tarefas):**

Durante a execução de projetos que utilizam END-FIRST (ex.: projeto do livro), foram observados os seguintes problemas:

1. **Consumo implícito do método**
   - Projetos usam END-FIRST sem declarar explicitamente
   - Não há rastreabilidade de qual versão do método está em uso

2. **Atualizações dependem de memória humana**
   - Mudanças no método exigem "avisar manualmente"
   - Não há mecanismo canônico de comunicação de atualizações

3. **Onboarding depende de explicação**
   - Novos executores (humanos ou Cursor) precisam de contexto prévio
   - Não há definição clara de "onboarding completo"

4. **Ferramentas interpretam intenção**
   - Cursor/agentes decidem como usar o método
   - Não há contrato metodológico explícito

5. **Ambiguidade em mudanças de método**
   - Não está claro o que é retroativo vs prospectivo
   - Projetos não sabem se precisam agir ou permanecem válidos

**Causa raiz identificada:**

> "O método END-FIRST não possui governança explícita de consumo, atualização e onboarding. Projetos e ferramentas operam por memória humana, não por contrato metodológico."

---

## 🚫 DO / DON'T

### DO (fazer)

- ✅ Definir mecanismo de declaração de consumo do método
- ✅ Definir versionamento conceitual do método
- ✅ Definir mecanismo de comunicação de atualizações
- ✅ Definir critérios de onboarding completo
- ✅ Definir contrato metodológico para ferramentas
- ✅ Distinguir mudanças retroativas de prospectivas
- ✅ Documentar como o método evolui

### DON'T (não fazer)

- ❌ Definir README específico de projeto
- ❌ Definir Cursor Rules específicas de projeto
- ❌ Criar automação de atualização
- ❌ Definir estrutura de pastas de projeto
- ❌ Obrigar atualização automática de projetos
- ❌ Mudar projetos existentes agora

---

## 🧱 Bloqueios Estruturais

- 🔒 **Nenhuma execução autorizada:** Status BACKLOG não autoriza execução
- 🔒 **F-1 obrigatório:** Demanda exige planejamento canônico antes de execução
- 🔒 **Aprovação do CEO:** F-1 deve ser aprovado pelo CEO antes de execução
- 🔒 **Escopo de método:** Governar critérios, não implementar soluções específicas

---

## 📋 TODO Canônico

**Status BACKLOG:** Nenhuma ação autorizada até promoção para F-1

**Quando promovida para F-1, fases esperadas:**

- [ ] F0: Classificar tipos de consumo de método (projeto, ferramenta, humano)
- [ ] F1: Definir mecanismo de declaração de consumo
- [ ] F2: Definir versionamento conceitual do método
- [ ] F3: Definir mecanismo de comunicação de atualizações
- [ ] F4: Definir critérios de onboarding completo
- [ ] F5: Definir contrato metodológico para ferramentas
- [ ] F6: Integrar ao método END-FIRST v2

---

## ❌ Fora de Escopo

- ❌ Implementar README de projeto específico
- ❌ Implementar Cursor Rules de projeto específico
- ❌ Criar automação de sincronização
- ❌ Definir estrutura de diretórios de projeto
- ❌ Migrar projetos existentes
- ❌ Criar ferramentas de atualização automática

**Razão:** Esta demanda define governança de consumo e atualização do método, não implementações específicas de projeto.

---

## 📌 Status

**Status atual:** BACKLOG

**Próximos passos possíveis (quando CEO decidir):**
1. Promover para F-1 PENDENTE DE APROVAÇÃO
2. Criar planejamento canônico (F-1)
3. Aguardar aprovação do CEO
4. Executar fases F1-F6

**Bloqueio ativo:** Status BACKLOG não autoriza execução

---

## 🧭 Regra Final

**Frase canônica de fechamento:**

> "Método que depende de memória humana não governa — apenas sugere."

---

## 📊 Metadados

**Versão:** 1.0  
**Criado em:** 2026-01-20  
**Autor:** CEO (Joubert Jr)  
**Executor:** Manus (Agent)  
**Status:** BACKLOG  
**Tipo:** Método / Governança  
**Impacto:** Global / Estrutural (todos os projetos que usam END-FIRST)  

---

## 🔗 Referências

- `/METODO/END_FIRST_V2.md` — Método END-FIRST v2
- `/METODO/GOVERNANCA_GATES.md` — Governança de gates
- `/METODO/TEMPLATE_DEMANDA_CANONICA.md` — Template usado para criar esta demanda
