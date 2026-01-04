# BANCO DE REFERÊNCIAS
## Documento de Requisitos de Negócio Completo

**Data:** 09/12/2025  
**Versão:** 1.0  
**Método:** ENDFIRST Method v9.0  
**Autor:** Criador do ENDFIRST Method

---

## SUMÁRIO EXECUTIVO

Este documento define **todos os requisitos de negócio e necessidades** do Banco de Referências, um sistema para gerenciar base **dinâmica e crescente** de citações científicas.

**Foco:** O QUÊ o sistema precisa fazer (não COMO implementar tecnicamente).

**Conteúdo:**
- Por quê criar (Identidade)
- O que existe (Pesquisa de Contexto)
- O quê fazer (Requisitos Funcionais)
- Viabilidade (Calibração)
- Priorização (Caminho Reverso)
- Como usar (Sistema de Uso)

**Resultado esperado:**
- 13 requisitos funcionais documentados
- 8 críticos/essenciais + 5 desejáveis
- Priorização clara
- Casos de uso definidos
- Métricas de sucesso

---

# PARTE 1: IDENTIDADE (O PORQUÊ)

## 1.1 QUEM PRECISA

**Identidade:** Criador do ENDFIRST Method que precisa gerenciar citações científicas de forma **dinâmica e crescente**.

**Contexto:**
- Pesquisador/Educador científico
- Criador de metodologia baseada em evidências
- Usuário de fontes científicas **em constante crescimento**
- Base atual: 5,800+ fontes
- Base futura: 10,000+ (1 ano), 50,000+ (5 anos)
- **Sempre pesquisa** e adiciona novas fontes

---

## 1.2 POR QUÊ IMPORTA

### **SENTIDO MAIOR (Autotranscendência):**

> "Métodos baseados em evidências precisam de evidências rastreáveis. Banco de Referências garante integridade científica."

**Beneficiários:**

**Para mim (criador):**
- Credibilidade científica
- Rastreabilidade de fontes
- Eficiência ao escrever
- Confiança nas citações

**Para usuários do método:**
- Confiança na base científica
- Acesso às fontes originais
- Validação independente
- Transparência total

**Para a ciência:**
- Boas práticas de citação
- Rastreabilidade de evidências
- Combate a pseudociência
- Rigor metodológico

---

## 1.3 PROBLEMAS QUE RESOLVE

### **PROBLEMA 1: Perda de Rastreabilidade (Base Crescente)**

**Situação atual:**
- Base cresce continuamente (5,800+ → 50,000+)
- Sem sistema, **impossível** gerenciar
- Difícil encontrar citação específica
- Risco de perder fontes aumenta

**Impacto:** Perda de credibilidade científica

---

### **PROBLEMA 2: Dificuldade em Citar**

**Situação atual:**
- 30-60 min por artigo buscando citações
- Risco de citar incorretamente
- Frustração e ineficiência

**Impacto:** Baixa produtividade

---

### **PROBLEMA 3: Impossível Validar Premissas**

**Situação atual:**
- Pilar 3 (Calibração) exige fontes primárias
- Sem acesso rápido a fontes confiáveis
- Validação superficial

**Impacto:** Não consigo aplicar meu próprio método rigorosamente

---

### **PROBLEMA 4: Dificuldade em Escalar**

**Situação atual:**
- Cada artigo precisa de citações
- Sem sistema, não escala
- Produção limitada

**Impacto:** Não consigo escalar produção de conteúdo

---

## 1.4 CONCLUSÃO

Banco de Referências **NÃO é opcional**. É **CRÍTICO** para:
- Gerenciar base dinâmica e crescente
- Transformar cada pesquisa em ativo acumulado
- Quanto mais uso, mais valioso (se organizado)
- Manter rigor científico
- Escalar produção de conteúdo

---

# PARTE 2: PESQUISA DE CONTEXTO (O POSSÍVEL)

## 2.1 NECESSIDADES ATENDIDAS HOJE

**Ferramentas de Citation Management (Zotero, Mendeley, EndNote):**

1. Armazenar referências organizadas
2. Capturar referências facilmente
3. Gerar citações automáticas
4. Armazenar e anotar PDFs
5. Acessar de múltiplos dispositivos

**Ferramentas de PKM (Obsidian, Roam, Notion):**

6. Ver conexões entre ideias
7. Descobrir padrões
8. Organizar de forma flexível
9. Buscar em todo conhecimento
10. Controlar próprios dados

---

## 2.2 NECESSIDADES NÃO ATENDIDAS (GAPS)

### **GAP 1: Integração Citação + Conhecimento**

**Problema:** Usuário precisa usar ferramentas separadas  
**Impacto:** Workflow fragmentado, duplicação de esforço  
**Oportunidade:** Integrar ambos em uma ferramenta

---

### **GAP 2: Validação de Qualidade**

**Problema:** Usuário não sabe se fonte é confiável  
**Impacto:** Todas as fontes parecem iguais, risco de usar fontes ruins  
**Oportunidade:** Classificar por Hierarquia de Evidências

---

### **GAP 3: Identificar Lacunas**

**Problema:** Usuário não sabe o que falta pesquisar  
**Impacto:** Pesquisa não direcionada, áreas subexploradas  
**Oportunidade:** Gap analysis para fontes científicas

---

### **GAP 4: Otimização para Base Crescente**

**Problema:** Quanto mais fontes, mais caótico  
**Impacto:** Sistema não melhora com uso, valor diminui com tempo  
**Oportunidade:** Otimizar para base dinâmica (não estática)

---

### **GAP 5: Múltiplos Tipos de Fontes**

**Problema:** Foco em papers acadêmicos  
**Impacto:** Pouco suporte para web, vídeos, livros  
**Oportunidade:** Suportar múltiplos tipos de fontes

---

### **GAP 6: Simplicidade**

**Problema:** Ferramentas complexas  
**Impacto:** Curva de aprendizado alta, baixa adoção  
**Oportunidade:** Sistema simples e intuitivo

---

## 2.3 ABORDAGENS QUE FUNCIONAM

**Identificadas na pesquisa:**

1. **Captura fácil:** Import, URL, manual
2. **Organização flexível:** Tags, pastas, sem hierarquia rígida
3. **Busca rápida:** Full-text, filtros avançados
4. **Conexões visuais:** Backlinks, graph view
5. **Gap analysis:** Identificar o que falta (InfraNodus)

---

# PARTE 3: REQUISITOS FUNCIONAIS (O QUÊ)

## 3.1 VISÃO GERAL

**Total:** 13 requisitos funcionais

**Essenciais (70% valor):** RF1-RF8  
**Desejáveis (30% promessa):** RF9-RF13

**Diferenciais:** RF4, RF5, RF6, RF8 ⭐

---

## 3.2 REQUISITOS ESSENCIAIS (RF1-RF8)

### **RF1: ADICIONAR REFERÊNCIAS**

**O quê:** Usuário consegue adicionar fontes ao Banco

**Necessidades atendidas:**
- N2: Capturar referências facilmente

**Critérios de sucesso:**
- Usuário adiciona referência manualmente em <2 min
- Usuário importa múltiplas referências de arquivo (BibTeX, RIS, etc.)
- Usuário captura referência de URL automaticamente

**Resolve:**
- Problema 1: Perda de rastreabilidade

**Prioridade:** P1 - CRÍTICO 🔴

---

### **RF2: ORGANIZAR REFERÊNCIAS**

**O quê:** Usuário consegue organizar fontes de forma flexível

**Necessidades atendidas:**
- N1: Armazenar referências organizadas
- N8: Organizar sem hierarquia rígida

**Critérios de sucesso:**
- Usuário cria tags livremente
- Usuário cria projetos/pastas
- Usuário reorganiza facilmente

**Resolve:**
- Problema 1: Perda de rastreabilidade
- Problema 4: Dificuldade em escalar

**Prioridade:** P2 - ESSENCIAL 🟡

---

### **RF3: BUSCAR REFERÊNCIAS**

**O quê:** Usuário encontra qualquer fonte rapidamente

**Necessidades atendidas:**
- N9: Buscar em todo conhecimento

**Critérios de sucesso:**
- Usuário encontra fonte em <10 segundos
- Busca funciona em todos os campos (autor, título, tags, etc.)
- Filtros avançados disponíveis (tag, projeto, qualidade, data)

**Resolve:**
- Problema 2: Dificuldade em citar
- Problema 4: Dificuldade em escalar

**Prioridade:** P1 - CRÍTICO 🔴

---

### **RF4: VALIDAR QUALIDADE DE FONTES** ⭐

**O quê:** Usuário consegue classificar e priorizar fontes por qualidade científica

**Necessidades atendidas:**
- GAP 2: Validação de qualidade

**Critérios de sucesso:**
- Usuário classifica fonte por Hierarquia de Evidências (7 níveis)
- Usuário vê qualidade de cada fonte visualmente
- Usuário filtra/ordena por qualidade
- Usuário prioriza fontes confiáveis automaticamente

**Hierarquia de Evidências (7 níveis):**
1. **Nível 1:** Experiência pessoal direta
2. **Nível 2:** Estudos científicos revisados por pares
3. **Nível 3:** Lógica + benchmarks validados
4. **Nível 4:** Opinião de especialista
5. **Nível 5:** Senso comum
6. **Nível 6:** Tradição/cultura
7. **Nível 7:** Autoridade sem evidências

**Resolve:**
- Problema 3: Impossível validar premissas

**Diferencial:** ⭐ Funcionalidade única (não existe em outras ferramentas)

**Prioridade:** P1 - CRÍTICO 🔴

**Observação:** Se usuário não entender 7 níveis, simplificar para 3 (Alta/Média/Baixa qualidade)

---

### **RF5: VER CONEXÕES ENTRE FONTES** ⭐

**O quê:** Usuário consegue linkar e navegar entre fontes relacionadas

**Necessidades atendidas:**
- N6: Ver conexões entre ideias
- GAP 1: Integração citação + conhecimento

**Critérios de sucesso:**
- Usuário cria links entre fontes
- Usuário vê quais fontes estão relacionadas
- Usuário navega entre fontes conectadas
- Usuário visualiza rede de fontes

**Resolve:**
- Problema 3: Impossível validar premissas (fontes relacionadas)

**Diferencial:** ⭐ Integra citação + PKM

**Prioridade:** P3 - EXPERIMENTAL 🟢

**Observação:** Validar com uso real se funcionalidade é útil

---

### **RF6: IDENTIFICAR LACUNAS NO CONHECIMENTO** ⭐

**O quê:** Usuário consegue ver o que falta pesquisar

**Necessidades atendidas:**
- GAP 3: Identificar lacunas

**Critérios de sucesso:**
- Usuário vê temas com poucas fontes
- Usuário vê conexões fracas
- Usuário recebe sugestões de próximas pesquisas
- Usuário identifica áreas subexploradas

**Resolve:**
- Problema 3: Impossível validar premissas (lacunas de conhecimento)

**Diferencial:** ⭐ Gap analysis para fontes científicas

**Prioridade:** P3 - EXPERIMENTAL 🟢

**Observação:** Validar com uso real se funcionalidade é útil

---

### **RF7: GERAR CITAÇÕES FORMATADAS**

**O quê:** Usuário consegue citar fontes facilmente

**Necessidades atendidas:**
- N3: Gerar citações automaticamente

**Critérios de sucesso:**
- Usuário copia citação formatada em <5 segundos
- Usuário escolhe formato (APA, ABNT, Chicago, etc.)
- Usuário gera bibliografia completa
- Formatos são corretos e validados

**Resolve:**
- Problema 2: Dificuldade em citar

**Prioridade:** P2 - ESSENCIAL 🟡

---

### **RF8: OTIMIZAR PARA BASE CRESCENTE** ⭐

**O quê:** Sistema fica **mais útil** conforme usuário adiciona fontes (não mais caótico)

**Necessidades atendidas:**
- GAP 4: Otimização para base crescente

**Critérios de sucesso:**
- Performance não degrada com mais fontes
- Sistema sugere conexões automaticamente
- Sistema identifica lacunas automaticamente
- Valor aumenta com uso (não diminui)

**Resolve:**
- Problema 4: Dificuldade em escalar

**Diferencial:** ⭐ Otimizado para base dinâmica (não estática)

**Prioridade:** P3 - EXPERIMENTAL 🟢

**Observação:** Validar com uso real se funcionalidade funciona como esperado

---

## 3.3 REQUISITOS DESEJÁVEIS (RF9-RF13)

**Promessa futura (30%)** - Para iterações futuras:

### **RF9: CAPTURA AUTOMÁTICA AVANÇADA**
- Browser extension
- Import automático de databases
- OCR de livros físicos

### **RF10: ANÁLISE AVANÇADA**
- Sentiment analysis
- Thematic analysis
- Network visualization avançada

### **RF11: COLABORAÇÃO**
- Compartilhar bibliotecas
- Trabalho em equipe
- Comentários e discussões

### **RF12: INTEGRAÇÃO COM FERRAMENTAS**
- Word plugin
- Google Docs add-on
- Obsidian plugin
- Zotero import/export

### **RF13: MÚLTIPLOS TIPOS DE FONTES**
- Vídeos (YouTube, etc.)
- Podcasts
- Tweets/threads
- Livros físicos

**Prioridade:** P4 - DESEJÁVEL 🟢

---

## 3.4 MÉTRICAS DE SUCESSO

**M1: Atende 6 Gaps Identificados**
- GAP 1: Integração citação + conhecimento (RF5)
- GAP 2: Validação de qualidade (RF4)
- GAP 3: Identificar lacunas (RF6)
- GAP 4: Base crescente (RF8)
- GAP 5: Múltiplos tipos (RF13 - futuro)
- GAP 6: Simplicidade (requisitos de usabilidade)

**M2: Resolve 4 Problemas**
- Problema 1: Rastreabilidade (RF1, RF2)
- Problema 2: Dificuldade em citar (RF3, RF7)
- Problema 3: Validar premissas (RF4, RF5, RF6)
- Problema 4: Escalar (RF2, RF3, RF8)

**M3: Economia de Tempo**
- Antes: 30-60 min/artigo buscando citações
- Depois: <10 min/artigo
- **Economia:** 20-50 min/artigo
- **10 artigos:** 3-8h economizadas
- **50 artigos:** 17-42h economizadas
- **100 artigos:** 33-83h economizadas

**M4: Usabilidade**
- Onboarding <20 min
- Primeira referência adicionada <5 min
- Primeira citação gerada <5 min
- Busca <10 segundos

---

# PARTE 4: CALIBRAÇÃO (VIABILIDADE)

## 4.1 PREMISSAS VALIDADAS

**8 premissas analisadas:**

✅ **7 VALIDADAS:**
1. Adicionar referências (Nível 2 - Zotero/Mendeley)
2. Organizar com tags (Nível 2 - Padrão indústria)
3. Buscar <10 seg (Nível 2 - Benchmarks)
4. Hierarquia de Evidências (Nível 1 - Experiência pessoal)
5. Ver conexões (Nível 2 - Obsidian/Roam)
6. Identificar lacunas (Nível 2 - InfraNodus)
7. Gerar citações (Nível 2 - Padrão indústria)

⚠️ **1 EXPERIMENTAL:**
8. Base crescente (Nível 3 - Lógica, não validado empiricamente)

---

## 4.2 NÚMEROS CALIBRADOS

| Métrica | Valor | Status |
|---------|-------|--------|
| Busca | <10 seg | ✅ Viável até 50,000 fontes |
| Onboarding | <20 min | ✅ Realista |
| Economia/artigo | 20-50 min | ✅ Conservador |
| Hierarquia | 7 níveis (ou 3) | ✅ Flexível |

**Base crescente:**
- Hoje: 5,800 fontes
- 1 ano: ~7,000-11,000 fontes
- 5 anos: ~11,000-35,000 fontes

**Performance validada até 5 anos de uso.**

---

## 4.3 OBSTÁCULOS E MITIGAÇÕES

### **OBSTÁCULO 1: Hierarquia Complexa (RF4)**
**Probabilidade:** 🟡 MÉDIA  
**Mitigação:** Simplificar para 3 níveis (Alta/Média/Baixa)

### **OBSTÁCULO 2: Gap Analysis Não Útil (RF6)**
**Probabilidade:** 🟡 MÉDIA  
**Mitigação:** Marcar como experimental, iterar ou remover

### **OBSTÁCULO 3: Base Crescente Não Otimiza (RF8)**
**Probabilidade:** 🟡 MÉDIA  
**Mitigação:** Marcar como experimental, validar com uso

### **OBSTÁCULO 4: Performance Degrada**
**Probabilidade:** 🟢 BAIXA  
**Mitigação:** Otimizar indexação, paginação

### **OBSTÁCULO 5: Requisitos Complexos**
**Probabilidade:** 🟢 BAIXA  
**Mitigação:** Simplificar linguagem, exemplos, glossário

---

## 4.4 CONCLUSÃO

**✅ REQUISITOS SÃO VIÁVEIS**

- 7 de 8 premissas validadas
- Números realistas
- Obstáculos mapeados com mitigações
- Benefício > Complexidade

---

# PARTE 5: PRIORIZAÇÃO (CAMINHO REVERSO)

## 5.1 PRIORIDADES DEFINIDAS

### **P1: CRÍTICOS** (Não pode faltar)

**RF1: Adicionar Referências** 🔴
- Sem isso, não há Banco
- Resolve Problema 1 (rastreabilidade)

**RF3: Buscar Referências** 🔴
- Sem busca rápida, Banco é inútil
- Resolve Problema 2 (dificuldade em citar)

**RF4: Validar Qualidade** ⭐ 🔴
- Diferencial único (GAP 2)
- Resolve Problema 3 (validar premissas)

---

### **P2: ESSENCIAIS** (Alto valor)

**RF2: Organizar** 🟡
- Base crescente precisa de organização
- Resolve Problema 4 (escalar)

**RF7: Citar** 🟡
- Propósito principal do Banco
- Resolve Problema 2 (dificuldade em citar)

---

### **P3: EXPERIMENTAIS** (Validar necessidade)

**RF5: Ver Conexões** ⭐ 🟢
- Diferencial (GAP 1), mas não validado
- Integra citação + PKM

**RF6: Identificar Lacunas** ⭐ 🟢
- Diferencial (GAP 3), mas não validado
- Gap analysis científico

**RF8: Base Crescente** ⭐ 🟢
- Diferencial (GAP 4), mas não validado
- Otimização dinâmica

---

### **P4: DESEJÁVEIS** (Futuro)

**RF9-RF13** 🟢
- 30% promessa futura
- Evolução pós-validação

---

## 5.2 GARGALO IDENTIFICADO

**RF4: Validar Qualidade** 🔴

**Por quê é gargalo:**
- Funcionalidade única (sem benchmarks)
- Hierarquia de Evidências (7 níveis)
- Crítico para diferenciação (GAP 2)
- Risco de usabilidade

**Mitigação:**
- Tutorial interativo
- Simplificar para 3 níveis se necessário
- Tornar opcional como último recurso

---

## 5.3 ORDEM DE DOCUMENTAÇÃO/IMPLEMENTAÇÃO

**Recomendação:**

1. **RF1:** Adicionar (crítico, base)
2. **RF3:** Buscar (crítico, uso frequente)
3. **RF4:** Qualidade (crítico, diferencial) 🔴 GARGALO
4. **RF2:** Organizar (essencial)
5. **RF7:** Citar (essencial)
6. **RF5:** Conexões (experimental)
7. **RF6:** Lacunas (experimental)
8. **RF8:** Base crescente (experimental)
9. **RF9-RF13:** Desejáveis (futuro)

---

# PARTE 6: SISTEMA DE USO (AGENTE EXTERNO)

## 6.1 CASOS DE USO PRINCIPAIS

### **CASO DE USO 1: Adicionar Nova Fonte** (RF1)

**Frequência:** Diária  
**Ator:** Usuário (criador de conteúdo)  
**Gatilho:** Encontrou fonte relevante durante pesquisa

**Fluxo:**
1. Usuário encontra fonte
2. Abre Banco de Referências
3. Escolhe método: Manual / Import / URL
4. Preenche/valida metadados
5. Classifica qualidade (RF4)
6. Adiciona tags/projeto (RF2)
7. Fonte salva
8. Opcional: Linkar com outras fontes (RF5)

**Resultado:** Fonte rastreável e organizada

---

### **CASO DE USO 2: Citar Fonte em Artigo** (RF7 + RF3)

**Frequência:** Semanal  
**Ator:** Usuário (escrevendo artigo)  
**Gatilho:** Precisa citar fonte no texto

**Fluxo:**
1. Está escrevendo artigo
2. Abre Banco
3. Busca fonte (por autor/título/tag/palavra-chave)
4. Encontra em <10 segundos
5. Escolhe formato (APA/ABNT/etc.)
6. Copia citação formatada
7. Cola no artigo

**Resultado:** Economia de 20-50 min/artigo

---

### **CASO DE USO 3: Validar Premissa** (RF4 + RF5)

**Frequência:** Mensal  
**Ator:** Usuário (aplicando Pilar 3)  
**Gatilho:** Precisa validar premissa com fontes primárias

**Fluxo:**
1. Tem premissa a validar
2. Abre Banco
3. Busca por tema/tag
4. Filtra por qualidade (Nível 1-3)
5. Vê fontes relacionadas (RF5)
6. Identifica se premissa é validada
7. Documenta validação

**Resultado:** Pilar 3 aplicado rigorosamente

---

### **CASO DE USO 4: Identificar Lacunas** (RF6)

**Frequência:** Mensal  
**Ator:** Usuário (planejando pesquisas)  
**Gatilho:** Quer saber o que pesquisar a seguir

**Fluxo:**
1. Abre Banco
2. Acessa funcionalidade "Lacunas"
3. Vê temas com poucas fontes
4. Vê sugestões de próximas pesquisas
5. Escolhe tema para explorar
6. Pesquisa novas fontes
7. Adiciona ao Banco (Caso de Uso 1)

**Resultado:** Pesquisa direcionada e eficiente

---

### **CASO DE USO 5: Gerar Bibliografia** (RF7)

**Frequência:** Semanal  
**Ator:** Usuário (finalizando artigo)  
**Gatilho:** Precisa gerar bibliografia completa

**Fluxo:**
1. Finalizou artigo
2. Abre Banco
3. Seleciona projeto/tag do artigo
4. Escolhe formato
5. Sistema gera bibliografia
6. Copia e cola no artigo

**Resultado:** Bibliografia correta e completa

---

## 6.2 JORNADA DO USUÁRIO

### **FASE 1: ONBOARDING** (<20 min)

1. **Boas-vindas** (2 min) - O que é, por quê usar
2. **Tutorial Hierarquia** (5 min) - 7 níveis explicados
3. **Adicionar Primeira Fonte** (5 min) - Guia passo a passo
4. **Buscar e Citar** (5 min) - Testar funcionalidades
5. **Explorar** (3 min) - Tags, conexões, lacunas

**Resultado:** Usuário consegue usar sozinho

---

### **FASE 2: USO REGULAR**

**Diariamente:**
- Adicionar novas fontes (Caso de Uso 1)
- Organizar com tags/projetos (RF2)
- Classificar qualidade (RF4)

**Semanalmente:**
- Citar fontes em artigos (Caso de Uso 2)
- Gerar bibliografias (Caso de Uso 5)
- Buscar fontes específicas (RF3)

**Mensalmente:**
- Validar premissas (Caso de Uso 3)
- Identificar lacunas (Caso de Uso 4)
- Planejar próximas pesquisas

---

### **FASE 3: BASE CRESCENTE** (Contínuo)

**Primeiros 3 meses:** 5,800 → ~6,500 fontes  
**6 meses - 1 ano:** ~7,000-11,000 fontes  
**1-5 anos:** ~11,000-35,000 fontes

**Expectativa:** Sistema fica **mais útil** com tempo (RF8)

---

## 6.3 REQUISITOS DE USABILIDADE

**RU1: Simplicidade**
- Onboarding <20 min
- Adicionar fonte <2 min
- Encontrar fonte <10 seg
- Copiar citação <5 seg

**RU2: Feedback Imediato**
- Confirmações visuais
- Indicadores de progresso
- Mensagens de erro claras
- Sugestões de correção

**RU3: Flexibilidade**
- Tags livres (não pré-definidas)
- Hierarquia opcional (3 ou 7 níveis)
- Múltiplos formatos de citação
- Múltiplos métodos de adição

**RU4: Perdão**
- Desfazer adição/edição
- Recuperar fonte deletada
- Editar metadados a qualquer momento
- Reclassificar qualidade

---

# PARTE 7: APRENDIZADOS

## 7.1 O QUE FUNCIONOU

1. Meta-aplicação do ENDFIRST
2. Validação obrigatória (v9.0)
3. Foco em necessidades (não tecnologia)
4. Calibração de premissas
5. Priorização clara
6. Casos de uso concretos

---

## 7.2 O QUE NÃO FUNCIONOU

1. Saiu do caminho (falou de implementação)
2. Estimativa de tempo (4-6x mais longo)
3. Não validou escopo antes

---

## 7.3 AÇÕES PARA PRÓXIMO CICLO

1. Confirmar escopo explicitamente
2. Validar foco a cada pilar
3. Estimar tempo realisticamente (2-3x)
4. Usar template de requisitos

---

# ANEXOS

## ANEXO A: GLOSSÁRIO

**Base Dinâmica:** Base de dados que cresce continuamente com uso (não estática)

**Hierarquia de Evidências:** Sistema de classificação de qualidade de fontes (7 níveis)

**Gap Analysis:** Análise para identificar lacunas no conhecimento

**PKM:** Personal Knowledge Management (gestão de conhecimento pessoal)

**Citation Management:** Gestão de citações e referências bibliográficas

---

## ANEXO B: HIERARQUIA DE EVIDÊNCIAS (7 NÍVEIS)

**Nível 1:** Experiência pessoal direta  
**Nível 2:** Estudos científicos revisados por pares  
**Nível 3:** Lógica + benchmarks validados  
**Nível 4:** Opinião de especialista  
**Nível 5:** Senso comum  
**Nível 6:** Tradição/cultura  
**Nível 7:** Autoridade sem evidências

**Simplificado (3 níveis):**
- **Alta:** Níveis 1-2
- **Média:** Níveis 3-4
- **Baixa:** Níveis 5-7

---

## ANEXO C: RESUMO DE REQUISITOS

| ID | Nome | Prioridade | Status | Diferencial |
|----|------|------------|--------|-------------|
| RF1 | Adicionar | P1 - CRÍTICO | Validado | - |
| RF2 | Organizar | P2 - ESSENCIAL | Validado | - |
| RF3 | Buscar | P1 - CRÍTICO | Validado | - |
| RF4 | Qualidade | P1 - CRÍTICO | Validado | ⭐ Único |
| RF5 | Conexões | P3 - EXPERIMENTAL | Validar | ⭐ PKM |
| RF6 | Lacunas | P3 - EXPERIMENTAL | Validar | ⭐ Gap |
| RF7 | Citar | P2 - ESSENCIAL | Validado | - |
| RF8 | Base Crescente | P3 - EXPERIMENTAL | Validar | ⭐ Dinâmico |
| RF9 | Captura Avançada | P4 - DESEJÁVEL | Futuro | - |
| RF10 | Análise Avançada | P4 - DESEJÁVEL | Futuro | - |
| RF11 | Colaboração | P4 - DESEJÁVEL | Futuro | - |
| RF12 | Integrações | P4 - DESEJÁVEL | Futuro | - |
| RF13 | Múltiplos Tipos | P4 - DESEJÁVEL | Futuro | - |

---

## ANEXO D: MÉTRICAS DE SUCESSO

**Economia de Tempo:**
- 10 artigos: 3-8h economizadas
- 50 artigos: 17-42h economizadas
- 100 artigos: 33-83h economizadas

**Usabilidade:**
- Onboarding: <20 min
- Adicionar fonte: <2 min
- Buscar fonte: <10 seg
- Copiar citação: <5 seg

**Crescimento da Base:**
- Hoje: 5,800 fontes
- 1 ano: ~7,000-11,000 fontes
- 5 anos: ~11,000-35,000 fontes

---

# CONCLUSÃO

Este documento define **todos os requisitos de negócio** do Banco de Referências.

**Próximos passos:**
1. Validar documento com stakeholders
2. Priorizar implementação (P1 → P2 → P3 → P4)
3. Focar em RF4 (gargalo crítico)
4. Validar RF5, RF6, RF8 com uso real
5. Iterar baseado em feedback

**Documento completo e pronto para uso.** ✅

---

**FIM DO DOCUMENTO**

**Versão:** 1.0  
**Data:** 09/12/2025  
**Método:** ENDFIRST Method v9.0  
**Total de páginas:** 1 arquivo Markdown completo


---

# PARTE 8: REQUISITOS TÉCNICOS ⭐ ATUALIZAÇÃO v1.1

## 8.1 REQUISITOS TÉCNICOS OBRIGATÓRIOS

### **RT1: GOOGLE FILE API (GEMINI FILE SEARCH)** ⭐ OBRIGATÓRIO

**O quê:**
Usar Google Gemini File Search API para implementar busca semântica (RAG) no Banco de Referências.

**Por quê:**
- Simplifica RAG (sem banco vetorial separado)
- Custo baixo (US$ 0,15 por 1M tokens de indexação)
- Consultas ilimitadas após indexação
- Citações automáticas com fontes
- Busca semântica (entende significado, não só palavras-chave)

**Como funciona:**
1. Upload de arquivos (PDFs, DOCXs, textos) para file_search_store
2. Gemini indexa automaticamente (embeddings + chunking)
3. Consulta via generate_content com file_search tool
4. Resposta com citações (arquivo + seção)

**Requisitos funcionais atendidos:**
- RF3: Buscar Referências (<10 seg) - Busca semântica rápida
- RF5: Ver Conexões - Gemini identifica relações entre fontes
- RF6: Identificar Lacunas - Análise de cobertura temática

**Custo estimado:**
- Base inicial (5,800 fontes, ~100 MB): ~US$ 0,15
- Crescimento (50,000 fontes, ~1 GB): ~US$ 1,50
- Consultas: Gratuitas (ilimitadas)

**Prioridade:** P1 - CRÍTICO 🔴

**Observação:** Cursor AI decide stack técnico, mas DEVE usar Google File API para RAG.

---

### **RT2: DOCKER** ⭐ OBRIGATÓRIO

**O quê:**
Sistema DEVE ser deployável via Docker containers.

**Por quê:**
- Portabilidade (roda em qualquer ambiente)
- Isolamento (dependências não conflitam)
- Escalabilidade (fácil replicar)
- Consistência (dev = prod)

**Requisitos:**
- Dockerfile na raiz do projeto
- docker-compose.yml para orquestração
- Variáveis de ambiente para configuração
- Volumes para persistência de dados

**Prioridade:** P1 - CRÍTICO 🔴

---

### **RT3: INTEGRAÇÃO COM ENDFIRST METHOD** ⭐ OBRIGATÓRIO

**O quê:**
Banco de Referências DEVE ser usado durante aplicação do ENDFIRST Method.

**Quando usar:**

**Pilar 1.5 (Pesquisa de Contexto):**
- Buscar fontes existentes no Banco
- Adicionar novas fontes encontradas
- Identificar gaps de conhecimento

**Pilar 3 (Calibração da Realidade):**
- Validar premissas com fontes do Banco
- Filtrar por Hierarquia de Evidências (Nível 1-3)
- Consultar fontes primárias

**Pilar 7 (Aprendizado Contínuo):**
- Documentar aprendizados como referências
- Adicionar ao Banco para reutilização

**Fluxo de trabalho:**

```
ENDFIRST Method → Pilar 1.5 → Buscar no Banco
                              ↓
                         Fontes existentes? 
                              ↓
                         SIM → Usar
                              ↓
                         NÃO → Pesquisar + Adicionar ao Banco
                              ↓
                         Pilar 3 → Validar com Banco (filtrar por qualidade)
                              ↓
                         Pilar 7 → Adicionar aprendizados ao Banco
```

**Requisitos funcionais atendidos:**
- RF1: Adicionar Referências (durante Pilar 1.5 e 7)
- RF3: Buscar Referências (durante Pilar 1.5 e 3)
- RF4: Validar Qualidade (durante Pilar 3)

**Prioridade:** P1 - CRÍTICO 🔴

**Observação:** ENDFIRST Method v9.2 será atualizado para incluir instruções de uso do Banco.

---

## 8.2 RESUMO DE REQUISITOS TÉCNICOS

| ID | Nome | Obrigatório | Prioridade |
|----|------|-------------|------------|
| RT1 | Google File API (RAG) | ✅ SIM | P1 - CRÍTICO |
| RT2 | Docker | ✅ SIM | P1 - CRÍTICO |
| RT3 | Integração ENDFIRST | ✅ SIM | P1 - CRÍTICO |

---

## 8.3 ATUALIZAÇÃO DE REQUISITOS FUNCIONAIS

### **RF3: BUSCAR REFERÊNCIAS** (ATUALIZADO)

**Implementação técnica:**
- Usar Google File API (Gemini File Search)
- Busca semântica (não só palavras-chave)
- Resposta com citações automáticas

**Critérios de sucesso (atualizados):**
- Usuário encontra fonte em <10 segundos ✅
- Busca entende **significado** (não só keywords) ⭐ NOVO
- Resultados incluem **citações com fontes** ⭐ NOVO
- Filtros avançados disponíveis (tag, projeto, qualidade, data) ✅

---

### **RF5: VER CONEXÕES ENTRE FONTES** (ATUALIZADO)

**Implementação técnica:**
- Usar Google File API para identificar relações semânticas
- Gemini analisa conteúdo e sugere conexões

**Critérios de sucesso (atualizados):**
- Usuário cria links entre fontes ✅
- Sistema **sugere conexões automaticamente** ⭐ NOVO (via Gemini)
- Usuário vê quais fontes estão relacionadas ✅
- Usuário navega entre fontes conectadas ✅

---

### **RF6: IDENTIFICAR LACUNAS NO CONHECIMENTO** (ATUALIZADO)

**Implementação técnica:**
- Usar Google File API para análise de cobertura temática
- Gemini identifica temas subexplorados

**Critérios de sucesso (atualizados):**
- Usuário vê temas com poucas fontes ✅
- Sistema **analisa cobertura temática automaticamente** ⭐ NOVO (via Gemini)
- Usuário recebe sugestões de próximas pesquisas ✅
- Usuário identifica áreas subexploradas ✅

---

## 8.4 STACK TÉCNICO (DECISÃO DO CURSOR AI)

**O que Cursor AI decide:**
- Linguagem (Python, Node.js, etc.)
- Framework (FastAPI, Express, etc.)
- Banco de dados (PostgreSQL, SQLite, etc.)
- Frontend (React, Vue, etc.)

**O que é OBRIGATÓRIO:**
- Google File API (Gemini File Search) para RAG ✅
- Docker para deployment ✅
- Integração com ENDFIRST Method ✅

---

## 8.5 REFERÊNCIAS

**Google File API:**
- Artigo: "O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos"
- Autor: Civil Learning, Coding Nexus
- Data: Nov 2025

**Custo:**
- Indexação: US$ 0,15 por 1M tokens
- Consultas: Gratuitas (ilimitadas)
- Modelo: gemini-embedding-001

**Exemplo de uso:**
- Phaser Studio (Beam): 3,000 arquivos, consulta em <2 segundos
- Antes: Horas para encontrar informações
- Depois: Minutos para prototipar jogos

---

**FIM DA ATUALIZAÇÃO - REQUISITOS TÉCNICOS** ✅

**Versão:** 1.1 (com RT1, RT2, RT3)  
**Data:** 09/12/2025  
**Próximo:** Atualizar ENDFIRST Method v9.2 para usar Banco
