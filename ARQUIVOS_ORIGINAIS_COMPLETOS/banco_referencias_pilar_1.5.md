# PILAR 1.5: PESQUISA DE CONTEXTO (O POSSÍVEL)
## Projeto: Banco de Referências - Requisitos de Negócio

**Data:** 09/12/2025  
**Versão do Método:** v9.0

---

## OBJETIVO DO PILAR

Descobrir **o que é possível** antes de definir requisitos. Pesquisar soluções existentes, identificar benchmarks, e mapear gaps.

---

## ETAPA 1: DEFINIR ESCOPO DE PESQUISA

**Pergunta:** O que preciso pesquisar?

**Resposta:** Soluções de gestão de referências bibliográficas E gestão de conhecimento pessoal (PKM).

**Escopo:**
1. Citation management software (Zotero, Mendeley, EndNote, etc.)
2. Personal Knowledge Management tools (Obsidian, Roam, Notion, etc.)
3. Funcionalidades padrão da indústria
4. Gaps existentes
5. Abordagens que funcionam

---

## ETAPA 2: PESQUISAR (1-2H MÁXIMO)

**Fontes consultadas:**
1. Wikipedia - Comparison of reference management software
2. Nodus Labs - Best PKM Tools 2024 (Obsidian vs Roam vs Notion vs Evernote)

**Tempo investido:** ~1h

---

## ETAPA 3: EXTRAIR INSIGHTS

### **A. SOLUÇÕES EXISTENTES (2 CATEGORIAS)**

#### **CATEGORIA 1: CITATION MANAGEMENT**

**Foco:** Citações formais, bibliografias, papers acadêmicos

**Principais ferramentas:**
- **Zotero:** Gratuito, open source, 300 MB storage, multi-plataforma
- **Mendeley:** Gratuito até 2 GB, proprietary, sincronização automática
- **EndNote:** US$ 299.95, mais antigo (1988), versão web gratuita
- **JabRef:** Gratuito, open source, Java, BibTeX/BibLaTeX
- **Citavi:** US$ 89-1947, dados locais ou cloud
- **RefWorks:** Assinatura institucional, web-based
- **Paperpile:** US$ 2.99/mês, integração Google Docs
- **Papers:** US$ 3-5/mês, web + desktop + mobile

**Funcionalidades comuns:**
1. Armazenamento de referências e PDFs
2. Import/Export múltiplos formatos (BibTeX, RIS, EndNote)
3. Browser extensions (captura automática)
4. Geração de citações e bibliografias
5. Integração com Word/Google Docs/LaTeX
6. Busca full-text
7. Tags e organização por pastas
8. Sincronização cloud
9. Mobile apps
10. Anotações em PDFs

---

#### **CATEGORIA 2: PKM (PERSONAL KNOWLEDGE MANAGEMENT)**

**Foco:** Conexões entre ideias, descoberta de insights, pensamento em rede

**Principais ferramentas:**
- **Obsidian:** Local-first, Markdown, graph view, backlinks, plugins
- **Roam Research:** Networked thinking, backlinks automáticos, não-hierárquico
- **Notion:** Workspace flexível, databases relacionais, colaboração
- **LogSeq:** Similar Obsidian, local-first, open source
- **Evernote:** Captura simples, busca poderosa, arquivamento
- **Mem AI:** AI-driven, organização automática, sugestões contextuais

**Funcionalidades comuns:**
1. Backlinks (links bidirecionais)
2. Graph view (visualização de rede)
3. Wiki-style links
4. Tags e organização flexível
5. Full-text search
6. Markdown support
7. Plugins e extensibilidade
8. Local storage (privacidade)
9. Sincronização opcional

**Funcionalidades avançadas (InfraNodus):**
1. **Network visualization:** Mapas visuais de ideias
2. **Gap analysis:** Identificar lacunas no conhecimento ⭐
3. **Sentiment analysis:** Analisar tom
4. **Thematic analysis:** Identificar temas principais
5. **Clusters:** Agrupar conceitos relacionados

---

### **B. BENCHMARKS REALISTAS**

#### **Armazenamento:**
- Gratuito: 300 MB (Zotero) a 2 GB (Mendeley)
- Pago: Ilimitado ou muito grande

#### **Preços:**
- **Gratuito:** Zotero, JabRef, LogSeq, Obsidian (base)
- **Baixo:** US$ 2.99-5/mês (Paperpile, Papers, Mem)
- **Alto:** US$ 89-299+ (Citavi, EndNote)

#### **Funcionalidades esperadas pelos usuários:**
1. Import/Export múltiplos formatos
2. Busca full-text rápida
3. Tags e organização
4. Sincronização multi-dispositivo
5. Mobile apps
6. Integrações (Word, Google Docs, etc.)
7. Backlinks (se PKM)
8. Graph view (se PKM)

---

### **C. ABORDAGENS QUE FUNCIONAM**

#### **1. Markdown como Base**
- Formato portável e durável
- Legível por humanos
- Versionável (Git)
- Não depende de vendor

#### **2. Local-First com Sync Opcional**
- Dados no computador do usuário
- Privacidade garantida
- Sincronização opcional para conveniência

#### **3. Graph View**
- Visualização de conexões entre notas/fontes
- Descoberta de padrões
- Navegação intuitiva

#### **4. Backlinks Automáticos**
- Conexões bidirecionais
- Descoberta serendipitosa
- Contexto rico

#### **5. Extensibilidade**
- Plugins da comunidade
- API aberta
- Customização

#### **6. Gap Analysis** ⭐
- Identificar lacunas no conhecimento
- Sugerir áreas para explorar
- Guiar pesquisas futuras

---

### **D. GAPS IDENTIFICADOS**

#### **Gap 1: Citation Management ≠ PKM**
**Problema:**
- Citation management foca em citações formais
- PKM foca em conexões entre ideias
- **Ferramentas separadas** (Zotero + Obsidian)
- Workflow fragmentado
- Duplicação de esforço

**Oportunidade:**
- Integrar citation management + PKM
- Rastreabilidade + Conexões

---

#### **Gap 2: Falta de Validação Científica**
**Problema:**
- Ferramentas não classificam qualidade de fontes
- Não usam Hierarquia de Evidências
- Não rastreiam fontes primárias vs secundárias
- Não validam credibilidade

**Oportunidade:**
- Integrar Hierarquia de Evidências (7 níveis)
- Classificar fontes automaticamente
- Priorizar fontes primárias

---

#### **Gap 3: Base Estática vs Dinâmica**
**Problema:**
- Citation management assume base **estática** (papers já publicados)
- Não otimizado para base **crescente** (sempre adicionando novas fontes)
- Não identifica lacunas para pesquisar

**Oportunidade:**
- Otimizar para base dinâmica e crescente
- Gap analysis para identificar o que falta
- Sugerir próximas pesquisas

---

#### **Gap 4: Foco em Papers Acadêmicos**
**Problema:**
- Maioria focada em papers científicos (PDFs)
- Pouco suporte para outros tipos de fontes
- Limitado para conteúdo web, vídeos, podcasts, livros

**Oportunidade:**
- Suportar múltiplos tipos de fontes
- Flexibilidade

---

#### **Gap 5: Complexidade Desnecessária**
**Problema:**
- Curva de aprendizado alta
- Muitas funcionalidades desnecessárias
- Interface complexa

**Oportunidade:**
- Simplicidade
- Foco no essencial
- Onboarding fácil

---

## ETAPA 4: DOCUMENTAR

### **RESUMO EXECUTIVO**

**O QUE EXISTE:**
1. **Citation Management** (Zotero, Mendeley, EndNote): Foco em citações formais
2. **PKM** (Obsidian, Roam, Notion): Foco em conexões entre ideias
3. **Análise Avançada** (InfraNodus): Gap analysis, network visualization

**O QUE FUNCIONA:**
1. Markdown como base (portável, durável)
2. Local-first com sync opcional (privacidade)
3. Graph view (visualização de rede)
4. Backlinks automáticos (descoberta)
5. Gap analysis (identificar lacunas) ⭐

**O QUE FALTA:**
1. **Integração** citation management + PKM
2. **Validação científica** (Hierarquia de Evidências)
3. **Base dinâmica** otimizada (crescimento contínuo)
4. **Gap analysis** para fontes científicas
5. **Simplicidade** (foco no essencial)

**OPORTUNIDADE:**
Criar Banco de Referências que **combina**:
- Citation management (rastreabilidade formal)
- PKM (conexões e insights)
- Validação científica (Hierarquia de Evidências)
- Gap analysis (identificar o que falta pesquisar)
- Base dinâmica (otimizada para crescimento)

---

## ✅ CHECKLIST PILAR 1.5 (4 ITENS)

- [x] Defini escopo de pesquisa? → **SIM** (Citation management + PKM)
- [x] Pesquisei benchmarks realistas (1-2h)? → **SIM** (~1h, 2 fontes principais)
- [x] Identifiquei abordagens que funcionam? → **SIM** (6 abordagens: Markdown, Local-first, Graph view, Backlinks, Extensibilidade, Gap analysis)
- [x] Documentei insights principais? → **SIM** (2 categorias, benchmarks, abordagens, 5 gaps)

---

## 📊 INSIGHTS-CHAVE

### **Insight 1: Duas Categorias Separadas**
- Citation management e PKM são **mundos diferentes**
- Usuários precisam de **ambos**
- Oportunidade de **integração**

### **Insight 2: Gap Analysis é Diferencial**
- InfraNodus mostra que gap analysis é poderoso
- Identificar **o que falta** é tão importante quanto **o que tem**
- Aplicável a fontes científicas

### **Insight 3: Base Dinâmica é Diferente**
- Citation management assume base estática
- ENDFIRST Method precisa de base **dinâmica**
- Sempre adicionando, sempre crescendo

### **Insight 4: Validação Científica é Gap**
- Nenhuma ferramenta usa Hierarquia de Evidências
- Oportunidade de **diferenciação**
- Crítico para rigor científico

### **Insight 5: Simplicidade é Valorizada**
- Ferramentas complexas têm curva de aprendizado alta
- Oportunidade de **simplicidade**
- Foco no essencial

---

**PILAR 1.5 COMPLETO** ✅

**AGUARDANDO VALIDAÇÃO DO USUÁRIO** 🔄

---

## ⚠️ REGRA DE VALIDAÇÃO OBRIGATÓRIA (v9.0)

**PARADA OBRIGATÓRIA:** Este pilar está completo, mas NÃO posso avançar para Pilar 2 sem validação explícita.

**Pergunta para o usuário:**

> **"Pilar 1.5 (Pesquisa de Contexto) completo. Aprova? (SIM/NÃO/AJUSTAR)"**

**Opções:**
- **SIM** → Avanço para Pilar 2 (Estado Final)
- **NÃO** → Reviso Pilar 1.5 completo
- **AJUSTAR [aspecto]** → Ajusto aspecto específico

**Aguardando resposta...** ⏳
