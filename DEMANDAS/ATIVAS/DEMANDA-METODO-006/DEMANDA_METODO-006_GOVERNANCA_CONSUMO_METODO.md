---
demanda_id: DEMANDA-METODO-006
title: Governança de Consumo, Atualização e Onboarding do Método
type: Método / Governança
classe: nenhuma
altera_funcionalidade: não
exige_f1: sim
status: f1_pending
created_at: 2026-01-20
created_by: CEO (Joubert Jr)
executor: Manus (Agent)
governed_by: /METODO/END_FIRST_V2.md
version: 1.1
updated_at: 2026-01-20
---

# DEMANDA-METODO-006 — Governança de Consumo, Atualização e Onboarding do Método

**Versão:** 1.1  
**Data de Criação:** 20 de Janeiro de 2026  
**Última atualização:** 20 de Janeiro de 2026  
**Solicitado por:** CEO (Joubert Jr)  
**Executor:** Manus (Agent)  
**Status:** F-1 PENDENTE DE APROVAÇÃO  
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

> "Consumo declarado precisa ser rastreável por marcador textual mínimo."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

**Artefatos conceituais mínimos (grep-friendly):**

1. ✅ **METHOD_CONSUMPTION_DECLARATION** existe com campos obrigatórios:
   - `method_name` (ex: "END-FIRST")
   - `method_version` (ex: "v2.5")
   - `adopted_at` (data)
   - `source_of_truth_ref` (ex: tag/commit do repositório do método)
   - `exceptions` (opcional: lista de regras dispensadas)

2. ✅ **METHOD_CHANGELOG** existe com entradas estruturadas:
   - `change_id` (identificador único)
   - `version` (versão do método)
   - `date` (data da mudança)
   - `scope` (retroativo / prospectivo)
   - `summary` (descrição da mudança)
   - `impact` (quem precisa agir)

3. ✅ **ONBOARDING_DEFINITION** existe com checklist binário:
   - Lista de artefatos obrigatórios para leitura
   - Critérios de "onboarding completo" (ex: "consegue criar demanda", "consegue executar F1-F6")
   - Nenhuma dependência de explicação verbal

4. ✅ **TOOL_CONTRACT** existe para ferramentas (Cursor/agentes):
   - Lista de documentos que a ferramenta DEVE consultar
   - Lista de ações que a ferramenta NUNCA executa sem referência explícita
   - Lista de registros que a ferramenta SEMPRE cria (ex: log de decisões)

5. ✅ **VERSIONING_MECHANISM** define:
   - Como versões do método são identificadas
   - Como projetos sabem qual versão estão usando
   - Como verificar se estão desatualizados

**Marcadores textuais mínimos (grep-friendly):**
- Consumo declarado deve ser rastreável por marcador textual mínimo (ex: `method: END-FIRST v2.5`)
- Mudanças do método devem ter marcador de escopo (ex: `scope: retroactive` ou `scope: prospective`)
- Onboarding completo deve ter marcador de status (ex: `onboarding_status: complete`)

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

- ❌ Impor README/Cursor Rules como parte obrigatória do método
- ❌ Criar automação obrigatória de atualização
- ❌ Definir estrutura de pastas como norma do método
- ❌ Obrigar atualização automática de projetos
- ❌ Mudar projetos existentes agora
- ❌ Proibir README/Cursor Rules como implementação operacional opcional

**Esclarecimento importante:**
- ✅ README e Cursor Rules **podem** ser usados como implementação operacional de "declaração de consumo"
- ✅ Desde que atendam aos marcadores canônicos mínimos (grep-friendly)
- ❌ O método **não** impõe README/Rules como única forma válida

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

- ❌ Impor README/Cursor Rules como norma obrigatória do método
- ❌ Criar automação obrigatória de sincronização
- ❌ Definir estrutura de diretórios como parte do método
- ❌ Migrar projetos existentes automaticamente
- ❌ Criar ferramentas de atualização automática obrigatória
- ❌ Proibir uso de README/Cursor Rules como implementação operacional

**Razão:** Esta demanda define governança de consumo e atualização do método (artefatos conceituais e marcadores), não implementações específicas obrigatórias de projeto. README/Rules são permitidos como implementação operacional opcional.

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
**Status:** F-1 PENDENTE DE APROVAÇÃO  
**Tipo:** Método / Governança  
**Impacto:** Global / Estrutural (todos os projetos que usam END-FIRST)  

---

## 🔗 Referências

- `/METODO/END_FIRST_V2.md` — Método END-FIRST v2
- `/METODO/GOVERNANCA_GATES.md` — Governança de gates
- `/METODO/TEMPLATE_DEMANDA_CANONICA.md` — Template usado para criar esta demanda

---

## 📊 HISTÓRICO DE VERSÕES

- **v1.0** (2026-01-20): Versão inicial da demanda
- **v1.1** (2026-01-20): Ajustes conforme validação do CEO:
  1. Binarização de critérios de aceitação (artefatos conceituais + marcadores grep-friendly)
  2. Correção de DON'T/Fora de Escopo (README/Rules permitidos como implementação operacional)
  3. Higiene do frontmatter (multi-linha)
  4. Adicionada frase canônica: "Consumo declarado precisa ser rastreável por marcador textual mínimo"
