# VÍNCULOS: PAPEL ↔ TIPO DE DEMANDA

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Método:** END-FIRST v2

---

## 🔗 MAPEAMENTO PAPEL ↔ TIPO DE DEMANDA

| Tipo de Demanda | Papel Principal | Papel Secundário | Papel de Auditoria |
|---|---|---|---|
| **DEMANDA-METODO** | CEO | Produto | Auditor Técnico |
| **DEMANDA-SOFT** | Produto | Executor | Auditor Técnico |
| **DEMANDA-PROD** | Produto | Executor | Auditor Técnico |
| **DEMANDA-GOV** | CEO | Auditor Técnico | Auditor Técnico |

---

## 📋 REGRAS DE ATIVAÇÃO POR TIPO

### DEMANDA-METODO (Método)

**Papel principal:** CEO  
**Justificativa:** Demandas de método alteram o próprio método END-FIRST

**Responsabilidades:**
- ✅ CEO define END de mudanças no método
- ✅ CEO aprova mudanças estruturais
- ✅ Produto estrutura a demanda
- ✅ Executor implementa (se aplicável)
- ✅ Auditor Técnico valida integridade

**Gates obrigatórios:**
- ✅ `Z-METHOD-REPO-INTEGRITY`

---

### DEMANDA-SOFT (Software)

**Papel principal:** Produto  
**Justificativa:** Demandas de software implementam funcionalidades

**Responsabilidades:**
- ✅ Produto define END de funcionalidades
- ✅ Produto define critérios de PASS/FAIL
- ✅ Executor implementa código
- ✅ CEO aprova F-1 e valida conclusão
- ✅ Auditor Técnico valida qualidade técnica

**Gates obrigatórios:**
- ✅ `Z10` (Qualidade de Produto) OU dispensa explícita

---

### DEMANDA-PROD (Produto)

**Papel principal:** Produto  
**Justificativa:** Demandas de produto criam ou evoluem produtos

**Responsabilidades:**
- ✅ Produto define END de produtos
- ✅ Produto define critérios de aceitação
- ✅ Executor implementa produto
- ✅ CEO aprova F-1 e valida conclusão
- ✅ Auditor Técnico valida conformidade

**Gates obrigatórios:**
- ✅ `Z10` (Qualidade de Produto) OU dispensa explícita

---

### DEMANDA-GOV (Governança)

**Papel principal:** CEO  
**Justificativa:** Demandas de governança definem regras e processos

**Responsabilidades:**
- ✅ CEO define END de governança
- ✅ CEO aprova regras canônicas
- ✅ Auditor Técnico estrutura procedimentos
- ✅ Executor implementa (se aplicável)
- ✅ Auditor Técnico valida aplicação

**Gates obrigatórios:**
- ✅ `Z-METHOD-REPO-INTEGRITY`

---

## 🎯 RESPOSTA À PERGUNTA CANÔNICA

> "Dado o tipo de demanda, qual papel é o principal?"

**Algoritmo:**

```
SE tipo = DEMANDA-METODO ENTÃO
  Papel principal = CEO

SE tipo = DEMANDA-SOFT ENTÃO
  Papel principal = Produto

SE tipo = DEMANDA-PROD ENTÃO
  Papel principal = Produto

SE tipo = DEMANDA-GOV ENTÃO
  Papel principal = CEO
```

---

## 🔒 REGRA CANÔNICA

> "Tipo de demanda determina papel principal. Papel principal não pode ser ignorado."
