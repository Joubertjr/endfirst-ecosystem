# Pesquisa: Estrutura de Projeto para Cursor AI

**Data:** 09/12/2025  
**Fonte:** Documentação oficial + Comunidade

---

## 🎯 DESCOBERTAS-CHAVE

### **1. TIPOS DE RULES**

Cursor suporta 4 tipos:

**A. Project Rules** (`.cursor/rules/`)
- Armazenado em `.cursor/rules/`
- Versionado com código
- Escopo: Projeto específico

**B. User Rules**
- Global ao ambiente Cursor
- Usado pelo Agent (Chat)

**C. Team Rules**
- Gerenciado via dashboard
- Disponível em planos Team/Enterprise
- Pode ser enforced (obrigatório)

**D. AGENTS.md**
- Instruções em Markdown
- Alternativa simples a `.cursor/rules`

---

## 📋 BEST PRACTICES (OFICIAL)

### **Limites e Estrutura:**
1. ✅ **Manter rules <500 linhas**
2. ✅ **Dividir rules grandes em múltiplos composáveis**
3. ✅ **Fornecer exemplos concretos**
4. ✅ **Evitar orientação vaga**
5. ✅ **Reusar rules quando repetir prompts**

### **Formato RULE.md:**
```markdown
---
description: "Descrição da rule"
alwaysApply: false
---

...conteúdo da rule
```

**Metadata:**
- `alwaysApply: true` → Aplicado em toda sessão de chat
- `alwaysApply: false` → Agent decide quando aplicar

---

## 🏗️ ESTRUTURA DE PROJETO (COMUNIDADE)

### **Recomendações da Comunidade:**

**1. Contexto é Crítico**
- Cursor tem limite de 20.000 tokens
- Não pode alimentar codebase inteiro
- Precisa organizar contexto eficientemente

**2. Descrições em Arquivos**
- Adicionar descrições curtas no topo de cada arquivo
- Ajuda Cursor (e humano) a entender rapidamente

**3. Estrutura Clara:**
```
project/
├── .cursor/
│   └── rules/
│       ├── base.md
│       ├── frontend.md
│       └── backend.md
├── docs/
│   ├── PROJECT_STRUCTURE.md
│   ├── TECH_STACK.md
│   └── CONVENTIONS.md
└── src/
```

**4. Documentação de Projeto:**
- `PROJECT_STRUCTURE.md` - Estrutura de pastas
- `TECH_STACK.md` - Dependências e tecnologias
- `CONVENTIONS.md` - Convenções de código

---

## 💡 INSIGHTS PARA ENDFIRST

### **O que aplicar:**

**1. Usar `.cursorrules` (não `.cursor/rules/`)**
- Mais simples para projeto único
- Arquivo único na raiz
- Limite: <500 linhas

**2. Estrutura de Documentação:**
```
endfirst-cursor-project/
├── .cursorrules (instruções do método)
├── README.md (guia rápido)
├── method/ (documentação modular)
├── context/ (contexto reutilizável)
├── templates/ (templates prontos)
└── output/ (resultados gerados)
```

**3. Princípios:**
- ✅ Descrições claras em cada arquivo
- ✅ Contexto organizado (não tudo em um arquivo)
- ✅ Exemplos concretos (não vago)
- ✅ Modular (fácil de navegar)

---

## 🚫 O QUE EVITAR

1. ❌ `.cursorrules` >500 linhas
2. ❌ Orientação vaga ("seja criativo")
3. ❌ Tudo em um arquivo gigante
4. ❌ Sem exemplos concretos

---

## 📊 BENCHMARKS

**Tamanho ideal de .cursorrules:**
- Mínimo: 200 linhas (funcional)
- Ideal: 300-400 linhas (completo sem ser excessivo)
- Máximo: 500 linhas (limite recomendado)

**Estrutura de pastas:**
- 4-6 pastas principais
- 15-25 arquivos totais
- Cada arquivo <200 linhas

---

## ✅ VALIDAÇÃO

**Descobertas validadas:**
1. ✅ `.cursorrules` é formato oficial
2. ✅ Limite de 500 linhas é real
3. ✅ Estrutura modular é best practice
4. ✅ Contexto organizado é crítico

**Pronto para aplicar no ENDFIRST** ✅
