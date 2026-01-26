---
demanda_id: DEMANDA-METODO-010
title: Governança de Produtos dentro do Método
type: método / governança
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-METODO-010 — Governança de Produtos dentro do Método

**Tipo:** Método / Governança  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existe um documento canônico em `/METODO/GOVERNANCA_PRODUTOS.md`
- ✅ O documento define a estrutura obrigatória de produtos dentro do método
- ✅ A regra "produto vive dentro do método" está explícita e governada
- ✅ Qualquer executor (humano ou IA) consegue criar um produto seguindo o contrato

**Resultado esperado do sistema:**

> "Existe um contrato formal que define como produtos são criados, versionados e governados dentro do repositório endfirst-ecosystem, em `/PRODUTOS/<nome>/`."

---

## 🚫 Regras Canônicas

**Governança de Produtos:**

> "Produto não nasce fora do método. Produto sem governança é software sem rastreabilidade."

**Estrutura Obrigatória:**

> "Todo produto DEVE seguir a estrutura canônica. Produto fora da estrutura é FAIL estrutural."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Documento `/METODO/GOVERNANCA_PRODUTOS.md` criado
- ✅ Estrutura mínima de produto definida:
  ```
  /PRODUTOS/<produto>/
    README.md
    DEMANDAS/
    planejamento/
    EVIDENCIAS/
    CONTEXTO/
    OUTPUTS/
  ```
- ✅ Regra explícita: "produto não nasce fora do método"
- ✅ Critérios de PASS/FAIL para criação de produto definidos
- ✅ Versionamento de produto definido

### FAIL

- ❌ Documento não existe
- ❌ Estrutura de produto não está definida
- ❌ Regra de governança não está explícita
- ❌ Critérios de PASS/FAIL não estão definidos

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um contrato formal que defina como produtos devem ser criados e governados dentro do repositório `endfirst-ecosystem`. Isso gera:

1. **Falta de rastreabilidade:** Produtos podem ser criados sem seguir o método
2. **Inconsistência estrutural:** Cada produto pode ter uma estrutura diferente
3. **Perda de governança:** Não há critério binário para validar se um produto está conforme

### Impacto

Sem governança de produtos:
- Produtos podem ser criados fora do método
- Rastreabilidade é perdida
- Qualidade não é garantida
- Versionamento é inconsistente

---

## 🚫 DO / DON'T

### ✅ DO

- **Definir estrutura canônica de produto**
- **Estabelecer regra: produto vive dentro do método**
- **Criar critérios binários de PASS/FAIL**
- **Definir versionamento de produto**
- **Especificar pastas obrigatórias**

### ❌ DON'T

- **Criar produto fora de `/PRODUTOS/`**
- **Permitir produto sem estrutura canônica**
- **Permitir produto sem README.md**
- **Permitir produto sem DEMANDAS/**
- **Permitir produto sem versionamento**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- Nenhum

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. `/METODO/GOVERNANCA_PRODUTOS.md`
   - Definir estrutura canônica de produto
   - Definir regra de governança
   - Definir critérios de PASS/FAIL
   - Definir versionamento

### Validações

1. Documento criado e commitado
2. Estrutura de produto definida
3. Regra de governança explícita
4. Critérios binários definidos

---

## ❌ Fora de Escopo

- Criação de produtos específicos (isso será feito em demandas de produto)
- Implementação de software para gerenciar produtos
- Migração de produtos existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Produto sem governança é software sem rastreabilidade. Governança de produtos é condição de passagem para qualquer produto no método END-FIRST."
