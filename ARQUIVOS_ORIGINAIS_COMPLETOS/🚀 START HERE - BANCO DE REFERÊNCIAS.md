# 🚀 START HERE - BANCO DE REFERÊNCIAS

**Bem-vindo ao projeto Banco de Referências!**

Este documento é o **ponto de entrada** para Cursor AI desenvolver o sistema.

---

## 📋 O QUE VOCÊ VAI ENCONTRAR AQUI

### **1. Este arquivo (00_START_HERE.md)**
- Prompt de entrada para Cursor AI
- Regras de execução
- Ordem de leitura dos documentos

### **2. requisitos_completo.md**
- Documento completo de requisitos de negócio
- 13 requisitos funcionais (RF1-RF13)
- Priorização (P1-P4)
- Casos de uso
- Métricas de sucesso

### **3. blueprint_funcional.md**
- Arquitetura conceitual do sistema
- 5 camadas lógicas
- Analogia com Cody (code graph)
- Diferencial ENDFIRST

### **4. pilares/**
- Pilares 0-7 do planejamento ENDFIRST
- Processo completo de definição de requisitos
- Aprendizados capturados

---

## 🎯 PROMPT DE ENTRADA PARA CURSOR AI

**Copie e cole este bloco no Cursor AI:**

```
You are an autonomous software architect and senior engineer.

Your task:
Design and implement a system based STRICTLY on the following documents.

Rules:
- Do NOT change requirements.
- Do NOT add features not specified.
- Do NOT assume technical stack unless explicitly required.
- Focus on correctness, scalability, and clarity.
- Treat this as a long-term system (5+ years, growing dataset from 5,800 to 50,000+ references).
- Base dinâmica: Sistema DEVE ficar MAIS ÚTIL com crescimento (não mais caótico).

Goal:
Build the minimum viable system that fully satisfies P1 (CRÍTICO) and P2 (ESSENCIAL) requirements,
and prepares clean extension points for P3 (EXPERIMENTAL) and P4 (DESEJÁVEL).

Context:
This is the ENDFIRST Reference Bank — a cognitive system for managing scientific references
with quality validation (Hierarchy of Evidence), knowledge graph, and gap analysis.

NOT a citation manager.
NOT a simple database.
IT IS a decision support and intellectual production system.

Priority:
1. RF1 (Adicionar Referências) — CRÍTICO
2. RF3 (Buscar Referências) — CRÍTICO
3. RF4 (Validar Qualidade) — CRÍTICO + GARGALO
4. RF2 (Organizar) — ESSENCIAL
5. RF7 (Citar) — ESSENCIAL
6. RF5, RF6, RF8 — EXPERIMENTAL (extension points)
7. RF9-RF13 — DESEJÁVEL (futuro)

Gargalo identificado:
RF4 (Validar Qualidade) é funcionalidade ÚNICA (não existe em outras ferramentas).
- Hierarquia de Evidências (7 níveis ou 3 simplificados)
- Crítico para diferenciação
- Risco de usabilidade
- Mitigação: Tutorial interativo, simplificar se necessário

Below are the full documents.

Read in this order:
1. requisitos_completo.md (Business Requirements)
2. blueprint_funcional.md (Functional Architecture)
3. pilares/ (optional: ENDFIRST planning process)

👇 START READING
```

---

## 📖 ORDEM DE LEITURA RECOMENDADA

### **PARA CURSOR AI:**

**1. requisitos_completo.md** (OBRIGATÓRIO)
- Leia COMPLETO
- Entenda os 13 requisitos funcionais
- Priorize P1 e P2
- Identifique gargalo (RF4)

**2. blueprint_funcional.md** (OBRIGATÓRIO)
- Leia COMPLETO
- Entenda arquitetura conceitual (5 camadas)
- Analogia com Cody (code graph)
- Diferencial ENDFIRST

**3. pilares/** (OPCIONAL)
- Processo de planejamento ENDFIRST
- Aprendizados capturados
- Contexto adicional

---

## ⚠️ REGRAS CRÍTICAS PARA CURSOR AI

### **REGRA 1: RESPEITAR ESCOPO**
- Requisitos de negócio SÃO FIXOS
- NÃO adicionar features não especificadas
- NÃO mudar prioridades

### **REGRA 2: FOCO EM P1 E P2**
- P1 (CRÍTICO): RF1, RF3, RF4
- P2 (ESSENCIAL): RF2, RF7
- P3 (EXPERIMENTAL): RF5, RF6, RF8 → Extension points
- P4 (DESEJÁVEL): RF9-RF13 → Futuro

### **REGRA 3: BASE DINÂMICA**
- Sistema DEVE ficar MAIS ÚTIL com crescimento
- Performance NÃO PODE degradar com mais fontes
- 5,800 hoje → 50,000+ em 5 anos

### **REGRA 4: GARGALO (RF4)**
- Hierarquia de Evidências é CRÍTICO
- Funcionalidade ÚNICA (diferencial)
- Risco de usabilidade
- Simplificar se necessário (7 níveis → 3 níveis)

### **REGRA 5: MÉTRICAS DE SUCESSO**
- Busca: <10 segundos
- Adicionar fonte: <2 minutos
- Copiar citação: <5 segundos
- Onboarding: <20 minutos

---

## 🎯 OBJETIVO FINAL

**Sistema que:**
- ✅ Gerencia base dinâmica e crescente de referências científicas
- ✅ Valida qualidade de fontes (Hierarquia de Evidências)
- ✅ Permite ver conexões entre fontes (knowledge graph)
- ✅ Identifica lacunas no conhecimento (gap analysis)
- ✅ Facilita citação e geração de bibliografias
- ✅ Fica MAIS ÚTIL com uso (não mais caótico)

**Economia esperada:**
- 20-50 min/artigo
- 10 artigos = 3-8h economizadas
- 50 artigos = 17-42h economizadas
- 100 artigos = 33-83h economizadas

---

## 🔄 PRÓXIMOS PASSOS

**1. Cursor AI lê documentos** (requisitos + blueprint)

**2. Cursor AI propõe arquitetura**
- Entidades
- Relações
- Schema de dados
- Fluxos principais

**3. Usuário valida arquitetura**
- Alinhado com requisitos?
- Prioridades corretas?
- Gargalo considerado?

**4. Cursor AI implementa P1 e P2**
- RF1, RF3, RF4 (CRÍTICO)
- RF2, RF7 (ESSENCIAL)

**5. Validar com uso real**
- Adicionar primeiras fontes
- Testar busca
- Validar Hierarquia de Evidências

**6. Iterar P3 (EXPERIMENTAL)**
- RF5, RF6, RF8
- Validar se são úteis

**7. Futuro (P4)**
- RF9-RF13
- Após validar P1-P3

---

## 📚 CONTEXTO ADICIONAL

### **ENDFIRST Method**
Este projeto foi planejado usando **ENDFIRST Method v9.1** (metodologia de planejamento reverso).

**Pilares aplicados:**
- Pilar 0: Seleção Dinâmica
- Pilar 1: Identidade (por quê criar)
- Pilar 1.5: Pesquisa de Contexto (o que existe)
- Pilar 2: Estado Final (o quê fazer)
- Pilar 3: Calibração (viabilidade)
- Pilar 4: Caminho Reverso (priorização)
- Pilar 5: Agente Externo (sistema de uso)
- Pilar 7: Aprendizado Contínuo

**Resultado:**
- Requisitos claros e priorizados
- Gargalo identificado
- Métricas de sucesso definidas
- Casos de uso reais

---

## ✅ CHECKLIST ANTES DE COMEÇAR

**Cursor AI deve:**
- [ ] Ler requisitos_completo.md COMPLETO
- [ ] Ler blueprint_funcional.md COMPLETO
- [ ] Entender prioridades (P1 > P2 > P3 > P4)
- [ ] Identificar gargalo (RF4)
- [ ] Confirmar escopo com usuário
- [ ] Propor arquitetura ANTES de implementar
- [ ] Focar em P1 e P2 primeiro

**Usuário deve:**
- [ ] Validar arquitetura proposta
- [ ] Confirmar alinhamento com requisitos
- [ ] Validar prioridades
- [ ] Testar sistema com uso real
- [ ] Capturar aprendizados (Pilar 7)

---

## 🚀 COMECE AGORA!

**1. Abra Cursor AI**

**2. Carregue este diretório:**
```bash
cursor /caminho/para/endfirst-cursor-project/banco_referencias/
```

**3. Cole o prompt de entrada** (seção "PROMPT DE ENTRADA PARA CURSOR AI" acima)

**4. Deixe Cursor AI ler os documentos**

**5. Valide arquitetura proposta**

**6. Implemente P1 e P2**

**7. Teste e itere!**

---

**BOA SORTE!** 🎉

**Qualquer dúvida, consulte:**
- `requisitos_completo.md` (requisitos)
- `blueprint_funcional.md` (arquitetura)
- `pilares/` (processo de planejamento)
- `../method/` (ENDFIRST Method v9.1)

---

**FIM DO START HERE** ✅
