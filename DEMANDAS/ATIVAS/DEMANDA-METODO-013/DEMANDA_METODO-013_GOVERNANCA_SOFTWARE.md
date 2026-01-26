---
demanda_id: DEMANDA-METODO-013
title: Governança de Software que implementa o Método
type: método / governança
classe: A
altera_funcionalidade: não
exige_f1: sim
status: backlog
created_at: 2026-01-23
created_by: CEO (Joubert Jr)
executor: Manus
---

# DEMANDA-METODO-013 — Governança de Software que implementa o Método

**Tipo:** Método / Governança  
**Classe:** A (ver `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`)  
**Altera Funcionalidade:** Não  
**Exige F-1:** Sim  
**Status:** BACKLOG

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Após a conclusão desta demanda:

- ✅ Existe um documento canônico em `/METODO/GOVERNANCA_SOFTWARE.md`
- ✅ O documento define como um software pode implementar END-FIRST sem quebrar o método
- ✅ As regras de consumo de `/METODO/` estão explícitas
- ✅ Qualquer executor consegue criar software que implementa o método seguindo o contrato

**Resultado esperado do sistema:**

> "Existe um contrato que define como um software pode implementar END-FIRST sem quebrar o método."

---

## 🚫 Regras Canônicas

**Governança de Software:**

> "Software não redefine método. Software consome método. Software que redefine regras é FAIL estrutural."

**Consumo de Método:**

> "Software DEVE consumir `/METODO/` do repositório. Software que não consome método não implementa END-FIRST."

**Execução Governada:**

> "Software só executa demandas aprovadas. Software que executa demanda não aprovada é FAIL estrutural."

**Evidência Obrigatória:**

> "Software DEVE registrar evidência de execução. Software sem evidência não é auditável."

---

## ✅ Critérios de Aceitação (Binários)

### PASS

- ✅ Documento `/METODO/GOVERNANCA_SOFTWARE.md` criado
- ✅ Regras de consumo de `/METODO/` definidas:
  - Software consome `/METODO/`
  - Software não redefine regras
  - Software só executa demandas aprovadas
  - Software registra evidência
- ✅ Critérios de PASS/FAIL para software definidos
- ✅ Exemplo de software conforme fornecido

### FAIL

- ❌ Documento não existe
- ❌ Regras de consumo não estão definidas
- ❌ Critérios de PASS/FAIL não estão definidos
- ❌ Exemplo não está fornecido

---

## 🔒 Gates Obrigatórios

**Baseado na classificação da demanda:**

- **Classe A:** Z10 obrigatório (Qualidade de Produto) OU dispensa explícita registrada

---

## 🧠 Problemas Observados

### Contexto

Atualmente, não existe um contrato formal que defina como um software pode implementar END-FIRST sem quebrar o método. Isso gera:

1. **Risco de redefinição:** Software pode redefinir regras do método
2. **Falta de rastreabilidade:** Software pode executar demandas não aprovadas
3. **Perda de auditoria:** Software pode não registrar evidência
4. **Inconsistência de implementação:** Cada software pode implementar o método de forma diferente

### Impacto

Sem governança de software:
- Método pode ser quebrado por software
- Rastreabilidade é perdida
- Auditoria é impossível
- Qualidade não é garantida

---

## 🚫 DO / DON'T

### ✅ DO

- **Definir regras de consumo de `/METODO/`**
- **Estabelecer regra: software consome método**
- **Criar critérios binários de PASS/FAIL**
- **Definir obrigatoriedade de evidência**
- **Fornecer exemplo de software conforme**

### ❌ DON'T

- **Criar software que redefine método**
- **Permitir software que não consome `/METODO/`**
- **Permitir software que executa demanda não aprovada**
- **Permitir software sem registro de evidência**
- **Permitir software que quebra governança**

---

## 🧱 Bloqueios Estruturais

### Bloqueios Técnicos

- Nenhum

### Bloqueios de Método

- **Depende de:** DEMANDA-METODO-010 (Governança de Produtos)

### Bloqueios de Governança

- Nenhum

---

## 📋 TODO Canônico

### Artefatos a serem criados

1. `/METODO/GOVERNANCA_SOFTWARE.md`
   - Definir regras de consumo de `/METODO/`
   - Definir regra: software consome método
   - Definir critérios de PASS/FAIL
   - Definir obrigatoriedade de evidência
   - Fornecer exemplo de software conforme

### Validações

1. Documento criado e commitado
2. Regras de consumo definidas
3. Critérios binários definidos
4. Obrigatoriedade de evidência explícita
5. Exemplo fornecido

---

## ❌ Fora de Escopo

- Criação de software específico (isso será feito em demandas de software)
- Implementação de software para gerenciar método
- Migração de software existente

---

## 📌 Status

**Status atual:** BACKLOG  
**Próximo passo:** Aguardando aprovação do CEO para criação do F-1

---

## 🧭 Regra Final

> "Software que redefine método não implementa END-FIRST. Software que não consome método não é governado. Governança de software é condição de passagem para qualquer software no método END-FIRST."
