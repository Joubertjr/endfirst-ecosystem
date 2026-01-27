# VÍNCULOS: PAPEL ↔ TIPO DE PRODUTO

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Método:** END-FIRST v2

---

## 🔗 MAPEAMENTO PAPEL ↔ TIPO DE PRODUTO

| Tipo de Produto | Papel Principal | Papel Secundário | Papel de Validação |
|---|---|---|---|
| **Produto Digital** | Produto | Executor | CEO |
| **Artefato de Método** | CEO | Auditor Técnico | Auditor Técnico |
| **Software/Plataforma** | Produto | Executor | CEO |
| **Documento/Contrato** | Produto | Executor | CEO |

---

## 📋 REGRAS DE ATIVAÇÃO POR TIPO DE PRODUTO

### Produto Digital

**Papel principal:** Produto  
**Justificativa:** Produtos digitais requerem definição clara de valor e aceitação

**Responsabilidades:**
- ✅ Produto define valor do produto
- ✅ Produto define critérios de aceitação
- ✅ Executor implementa produto
- ✅ CEO valida se END foi atingido

**Exemplo:** Contratação Pública de TI (PROD-001)

---

### Artefato de Método

**Papel principal:** CEO  
**Justificativa:** Artefatos de método alteram o próprio método END-FIRST

**Responsabilidades:**
- ✅ CEO define END do artefato
- ✅ Auditor Técnico estrutura procedimentos
- ✅ Executor implementa (se aplicável)
- ✅ Auditor Técnico valida conformidade

**Exemplo:** Auditor Técnico (METODO-016)

---

### Software/Plataforma

**Papel principal:** Produto  
**Justificativa:** Software requer definição clara de funcionalidades e UX

**Responsabilidades:**
- ✅ Produto define funcionalidades
- ✅ Produto define UX esperada
- ✅ Executor implementa código
- ✅ CEO valida se END foi atingido

**Exemplo:** Plataforma END-FIRST (SOFT-001)

---

### Documento/Contrato

**Papel principal:** Produto  
**Justificativa:** Documentos requerem definição clara de conteúdo e estrutura

**Responsabilidades:**
- ✅ Produto define conteúdo esperado
- ✅ Produto define estrutura canônica
- ✅ Executor escreve documento
- ✅ CEO valida se END foi atingido

**Exemplo:** README Estratégico (METODO-008)

---

## 🎯 RESPOSTA À PERGUNTA CANÔNICA

> "Dado o tipo de produto, qual papel é o principal?"

**Algoritmo:**

```
SE tipo_produto = "Artefato de Método" ENTÃO
  Papel principal = CEO

SE tipo_produto EM ["Produto Digital", "Software/Plataforma", "Documento/Contrato"] ENTÃO
  Papel principal = Produto
```

---

## 🔒 REGRA CANÔNICA

> "Tipo de produto determina papel principal. Artefatos de método são sempre governados pelo CEO."
