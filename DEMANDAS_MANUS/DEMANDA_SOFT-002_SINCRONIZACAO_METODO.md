---
demanda_id: DEMANDA-SOFT-002
title: Sincronização Automática do Método
type: software / sincronização
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-SOFT-002 — Sincronização Automática do Método

**Tipo:** Software / Sincronização  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ O software sincroniza automaticamente o diretório `/METODO/` do repositório `endfirst-ecosystem`
- ✅ A sincronização ocorre sem quebrar o software
- ✅ O método atualiza sem necessidade de rebuild do Docker
- ✅ Qualquer atualização no repositório é refletida no software em tempo real

**Resultado esperado do sistema:**

> "O software sincroniza automaticamente o diretório `/METODO/` do repositório endfirst-ecosystem."

---

## 🚫 Regras Canônicas

**Sincronização Automática:**

> "Método muda. Software não quebra. Sincronização automática é condição de passagem."

**Método como Fonte Única:**

> "Método vive no repositório. Software consome método. Software que não sincroniza método não implementa END-FIRST."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Software sincroniza `/METODO/` automaticamente
- ✅ Sincronização ocorre sem quebrar software
- ✅ Método atualiza sem rebuild do Docker
- ✅ Atualização no repositório é refletida no software em tempo real
- ✅ Sincronização é auditável (log de sincronização)

### FAIL

- ❌ Software não sincroniza `/METODO/`
- ❌ Sincronização quebra software
- ❌ Método não atualiza sem rebuild
- ❌ Atualização não é refletida em tempo real
- ❌ Sincronização não é auditável

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um mecanismo de sincronização automática do método. Isso gera:

1. **Desatualização:** Software pode usar versão antiga do método
2. **Inconsistência:** Método no repositório e método no software podem divergir
3. **Necessidade de rebuild:** Atualização do método exige rebuild do Docker
4. **Perda de rastreabilidade:** Não é possível saber qual versão do método está sendo usada

### Impacto

Sem sincronização automática:
- Método fica desatualizado
- Inconsistência é inevitável
- Rebuild é necessário
- Rastreabilidade é perdida

---

## 🚫 DO / DON'T

### ✅ DO

- **Implementar sincronização automática de `/METODO/`**
- **Garantir que sincronização não quebra software**
- **Garantir que método atualiza sem rebuild**
- **Implementar log de sincronização**
- **Testar sincronização com atualização real**

### ❌ DON'T

- **Criar software que não sincroniza método**
- **Permitir que sincronização quebre software**
- **Exigir rebuild para atualizar método**
- **Permitir sincronização sem log**
- **Permitir desatualização do método**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- **Depende de:** DEMANDA-SOFT-001 (Plataforma END-FIRST)

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. **Mecanismo de Sincronização**
   - Script de sincronização
   - Configuração de volume Docker
   - Log de sincronização

2. **Testes**
   - Teste de sincronização automática
   - Teste de atualização sem rebuild
   - Teste de log de sincronização

### Validações

1. Sincronização automática funciona
2. Sincronização não quebra software
3. Método atualiza sem rebuild
4. Log de sincronização existe
5. Atualização é refletida em tempo real

---

## ❌ Fora de Escopo

- Sincronização de outros diretórios além de `/METODO/`
- Implementação de versionamento de método (isso será feito em demanda futura)
- Migração de dados existentes

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Método muda. Software não quebra. Sincronização automática é condição de passagem para qualquer software no método END-FIRST."
