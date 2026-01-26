---
demanda_id: DEMANDA-METODO-012
title: Versionamento Cruzado (Método x Produto x Execução)
type: método / governança
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-METODO-012 — Versionamento Cruzado (Método x Produto x Execução)

**Tipo:** Método / Governança  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existe um documento canônico em `/METODO/VERSIONAMENTO_CRUZADO.md`
- ✅ O documento define os campos obrigatórios de versionamento para outputs
- ✅ Todo output gerado por um produto registra: versão do método, versão do produto, versão do contexto e id da execução
- ✅ Qualquer executor consegue gerar outputs com versionamento cruzado seguindo o contrato

**Resultado esperado do sistema:**

> "Todo output gerado por um produto registra: versão do método, versão do produto, versão do contexto e id da execução."

---

## 🚫 Regras Canônicas

**Versionamento Cruzado:**

> "Output sem versionamento cruzado é output sem rastreabilidade. Rastreabilidade é condição de passagem."

**Campos Obrigatórios:**

> "Todo OUTPUT DEVE conter: versão do método, versão do produto, versão do contexto e id da execução. Output sem esses campos é FAIL estrutural."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Documento `/METODO/VERSIONAMENTO_CRUZADO.md` criado
- ✅ Campos obrigatórios definidos:
  - `metodo_version` (ex: `END-FIRST v2.5`)
  - `produto_version` (ex: `contratacao-ti v1.2`)
  - `contexto_version` (ex: `lei-14133 v2.0`)
  - `execucao_id` (ex: `exec-2026-01-23-001`)
- ✅ Formato de versionamento definido
- ✅ Critérios de PASS/FAIL para versionamento definidos
- ✅ Exemplo de output com versionamento cruzado fornecido

### FAIL

- ❌ Documento não existe
- ❌ Campos obrigatórios não estão definidos
- ❌ Formato de versionamento não está explícito
- ❌ Critérios de PASS/FAIL não estão definidos
- ❌ Exemplo não está fornecido

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um contrato formal que defina como outputs devem registrar versionamento cruzado. Isso gera:

1. **Falta de rastreabilidade:** Não é possível saber qual versão do método, produto e contexto foi usada em um output
2. **Impossibilidade de auditoria:** Não é possível auditar a origem de um output
3. **Perda de reprodutibilidade:** Não é possível reproduzir um output com as mesmas versões
4. **Inconsistência de versionamento:** Cada produto pode ter um formato de versionamento diferente

### Impacto

Sem versionamento cruzado:
- Outputs não são rastreáveis
- Auditoria é impossível
- Reprodutibilidade é perdida
- Qualidade não é garantida

---

## 🚫 DO / DON'T

### ✅ DO

- **Definir campos obrigatórios de versionamento**
- **Estabelecer regra: versionamento cruzado é obrigatório**
- **Criar critérios binários de PASS/FAIL**
- **Definir formato de versionamento**
- **Fornecer exemplo de output com versionamento cruzado**

### ❌ DON'T

- **Criar OUTPUT sem versionamento cruzado**
- **Permitir OUTPUT sem versão do método**
- **Permitir OUTPUT sem versão do produto**
- **Permitir OUTPUT sem versão do contexto**
- **Permitir OUTPUT sem id da execução**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- **Depende de:** DEMANDA-METODO-010 (Governança de Produtos)
- **Depende de:** DEMANDA-METODO-011 (Governança de Contexto)

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. `/METODO/VERSIONAMENTO_CRUZADO.md`
   - Definir campos obrigatórios de versionamento
   - Definir formato de versionamento
   - Definir critérios de PASS/FAIL
   - Fornecer exemplo de output com versionamento cruzado

### Validações

1. Documento criado e commitado
2. Campos obrigatórios definidos
3. Formato de versionamento explícito
4. Critérios binários definidos
5. Exemplo fornecido

---

## ❌ Fora de Escopo

- Implementação de software para gerenciar versionamento
- Migração de outputs existentes
- Criação de outputs específicos

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Output sem versionamento cruzado é output sem rastreabilidade. Versionamento cruzado é condição de passagem para qualquer output no método END-FIRST."
