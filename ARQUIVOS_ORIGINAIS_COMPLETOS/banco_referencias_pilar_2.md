## Projeto: Banco de Referências - Requisitos de Negócio

**Data:** 09/12/2025  
**Versão do Método:** v9.0  
**Foco:** O QUÊ o Banco precisa fazer (não COMO implementar)

---

## OBJETIVO DO PILAR

Definir **estado final específico e mensurável** do Banco de Referências: O QUÊ ele precisa fazer para atender necessidades identificadas.

---

## 1. QUANDO EXATAMENTE?

**Pergunta:** Quando o Banco de Referências estará "pronto"?

**Resposta:** Não há "pronto" final. É sistema **evolutivo**.

**Marcos:**
- **Versão 1.0 (MVP):** Atende 6 gaps críticos identificados
- **Versão 2.0:** Adiciona funcionalidades avançadas
- **Versão 3.0+:** Evolui baseado em uso real

**Foco deste documento:** Definir requisitos para **Versão 1.0 (MVP)**

---

## 2. COMO VOU SABER QUE ALCANCEI? (MÉTRICAS)

**Métrica 1: Atende 6 Gaps Identificados**
- [ ] GAP 1: Integra citação + conhecimento
- [ ] GAP 2: Valida qualidade de fontes
- [ ] GAP 3: Identifica lacunas
- [ ] GAP 4: Otimiza para base crescente
- [ ] GAP 5: Suporta múltiplos tipos
- [ ] GAP 6: Simples de usar

**Métrica 2: Resolve 4 Problemas do Pilar 1**
- [ ] Problema 1: Perda de rastreabilidade (base crescente)
- [ ] Problema 2: Dificuldade em citar (30-60 min/artigo)
- [ ] Problema 3: Impossível validar premissas (Pilar 3)
- [ ] Problema 4: Dificuldade em escalar (base dinâmica)

**Métrica 3: Economia de Tempo Mensurável**
- Antes: 30-60 min por artigo buscando citações
- Depois: <10 min por artigo
- **Economia:** 20-50 min por artigo

**Métrica 4: Usuário Consegue Usar Sozinho**
- Onboarding <15 min
- Primeira referência adicionada <5 min
- Primeira citação gerada <5 min

---

## 3. COMO É "BOM O SUFICIENTE"? (QUALIDADE)

**Regra 70/30:** Mínimo 70% valor aplicável, máximo 30% promessa futura.

### **70% VALOR APLICÁVEL (MVP - V1.0):**

**Funcionalidades ESSENCIAIS que DEVEM existir:**

**F1. Adicionar Referências**
- Usuário consegue adicionar referência manualmente
- Usuário consegue importar de arquivo (BibTeX, RIS, etc.)
- Usuário consegue capturar de URL

**F2. Organizar Referências**
- Usuário consegue usar tags
- Usuário consegue usar pastas/projetos
- Usuário consegue buscar por qualquer campo

**F3. Validar Qualidade (GAP 2)**
- Usuário consegue classificar fonte por Hierarquia de Evidências (7 níveis)
- Usuário consegue ver qualidade de cada fonte
- Usuário consegue priorizar fontes confiáveis

**F4. Ver Conexões (GAP 1)**
- Usuário consegue linkar referências entre si
- Usuário consegue ver quais fontes estão relacionadas
- Usuário consegue navegar entre fontes conectadas

**F5. Identificar Lacunas (GAP 3)**
- Usuário consegue ver temas com poucas fontes
- Usuário consegue ver conexões fracas
- Usuário consegue identificar o que falta pesquisar

**F6. Citar Facilmente**
- Usuário consegue copiar citação formatada
- Usuário consegue gerar bibliografia
- Usuário consegue escolher formato (APA, ABNT, etc.)

**F7. Buscar Rapidamente**
- Usuário consegue buscar por qualquer palavra
- Usuário consegue filtrar por tag, projeto, qualidade
- Usuário consegue encontrar em <10 segundos