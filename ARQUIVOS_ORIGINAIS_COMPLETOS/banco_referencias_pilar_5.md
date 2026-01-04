# PILAR 5: AGENTE EXTERNO (O SISTEMA DE USO)
## Projeto: Banco de Referências - Requisitos de Negócio

**Data:** 09/12/2025  
**Versão do Método:** v9.0  
**Foco:** Definir COMO usuário interage com requisitos (fluxo de uso)

---

## OBJETIVO DO PILAR

Definir **sistema de uso** do Banco de Referências: fluxos de trabalho, casos de uso, e jornada do usuário.

**IMPORTANTE:** Foco em **O QUÊ** usuário faz (não COMO implementar tecnicamente).

---

## A. CASOS DE USO PRINCIPAIS

### **CASO DE USO 1: Adicionar Nova Fonte** (RF1)

**Ator:** Usuário (criador de conteúdo)  
**Gatilho:** Encontrou fonte relevante durante pesquisa  
**Objetivo:** Adicionar fonte ao Banco para uso futuro

**Fluxo principal:**
1. Usuário encontra fonte (paper, livro, site, etc.)
2. Usuário abre Banco de Referências
3. Usuário escolhe método de adição:
   - **Opção A:** Manual (preenche formulário)
   - **Opção B:** Import (arquivo BibTeX/RIS)
   - **Opção C:** URL (captura automática)
4. Usuário preenche/valida metadados (autor, título, ano, etc.)
5. Usuário classifica qualidade (Hierarquia de Evidências - RF4)
6. Usuário adiciona tags/projeto (RF2)
7. Fonte é salva no Banco
8. Usuário pode linkar com outras fontes (RF5 - opcional)

**Resultado:** Fonte rastreável e organizada

**Frequência:** Diária (sempre que pesquisa)

---

### **CASO DE USO 2: Citar Fonte em Artigo** (RF7)

**Ator:** Usuário (escrevendo artigo)  
**Gatilho:** Precisa citar fonte no texto  
**Objetivo:** Copiar citação formatada rapidamente

**Fluxo principal:**
1. Usuário está escrevendo artigo
2. Usuário precisa citar fonte
3. Usuário abre Banco de Referências
4. Usuário busca fonte (RF3):
   - Por autor
   - Por título
   - Por tag/projeto
   - Por palavra-chave
5. Usuário encontra fonte em <10 segundos
6. Usuário escolhe formato (APA, ABNT, Chicago, etc.)
7. Usuário copia citação formatada
8. Usuário cola no artigo

**Resultado:** Economia de 20-50 min/artigo

**Frequência:** Semanal (ao escrever artigos)

---

### **CASO DE USO 3: Validar Premissa com Fontes** (RF4 + RF5)

**Ator:** Usuário (aplicando Pilar 3 - Calibração)  
**Gatilho:** Precisa validar premissa com fontes primárias  
**Objetivo:** Encontrar fontes confiáveis sobre tema específico

**Fluxo principal:**
1. Usuário tem premissa a validar
2. Usuário abre Banco de Referências
3. Usuário busca por tema/tag (RF3)
4. Usuário filtra por qualidade (RF4):
   - Nível 1-3: Alta confiabilidade
   - Fontes primárias priorizadas
5. Usuário vê fontes relacionadas (RF5):
   - Conexões entre fontes
   - Rede de evidências
6. Usuário identifica se premissa é validada:
   - Múltiplas fontes confiáveis → Validada
   - Poucas fontes ou baixa qualidade → Não validada
7. Usuário documenta validação

**Resultado:** Pilar 3 aplicado rigorosamente

**Frequência:** Mensal (ao criar novos projetos)

---

### **CASO DE USO 4: Identificar Lacunas de Pesquisa** (RF6)

**Ator:** Usuário (planejando próximas pesquisas)  
**Gatilho:** Quer saber o que pesquisar a seguir  
**Objetivo:** Descobrir temas subexplorados

**Fluxo principal:**
1. Usuário abre Banco de Referências
2. Usuário acessa funcionalidade "Lacunas" (RF6)
3. Sistema mostra:
   - Temas com poucas fontes
   - Conexões fracas entre temas
   - Áreas subexploradas
4. Usuário vê sugestões de próximas pesquisas
5. Usuário escolhe tema para explorar
6. Usuário pesquisa novas fontes
7. Usuário adiciona fontes ao Banco (volta para Caso de Uso 1)

**Resultado:** Pesquisa direcionada e eficiente

**Frequência:** Mensal (planejamento de pesquisas)

---

### **CASO DE USO 5: Gerar Bibliografia Completa** (RF7)

**Ator:** Usuário (finalizando artigo)  
**Gatilho:** Precisa gerar bibliografia completa  
**Objetivo:** Criar lista de referências formatada

**Fluxo principal:**
1. Usuário finalizou artigo
2. Usuário abre Banco de Referências
3. Usuário seleciona projeto/tag do artigo (RF2)
4. Usuário escolhe formato (APA, ABNT, etc.)
5. Sistema gera bibliografia completa
6. Usuário copia bibliografia
7. Usuário cola no final do artigo

**Resultado:** Bibliografia correta e completa

**Frequência:** Semanal (ao finalizar artigos)

---

## B. JORNADA DO USUÁRIO

### **FASE 1: ONBOARDING** (<20 min)

**Objetivo:** Usuário entende e começa a usar Banco

**Etapas:**
1. **Boas-vindas** (2 min)
   - O que é Banco de Referências
   - Por quê usar
   - Benefícios principais

2. **Tutorial Hierarquia de Evidências** (5 min)
   - 7 níveis explicados
   - Exemplos claros
   - Por quê importa

3. **Adicionar Primeira Fonte** (5 min)
   - Guia passo a passo
   - Adicionar fonte de exemplo
   - Classificar qualidade

4. **Buscar e Citar** (5 min)
   - Buscar fonte adicionada
   - Copiar citação formatada
   - Testar formatos

5. **Explorar Funcionalidades** (3 min)
   - Tags e organização
   - Conexões (se disponível)
   - Lacunas (se disponível)

**Resultado:** Usuário consegue usar sozinho

---

### **FASE 2: USO REGULAR** (Diário/Semanal)

**Padrão de uso:**

**Diariamente:**
- Adicionar novas fontes encontradas (Caso de Uso 1)
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

**Evolução do uso:**

**Primeiros 3 meses:**
- Base: 5,800 → ~6,500 fontes
- Foco: Adicionar e organizar
- Valor: Rastreabilidade básica

**6 meses - 1 ano:**
- Base: ~7,000-11,000 fontes
- Foco: Conexões e lacunas
- Valor: Insights e descobertas

**1-5 anos:**
- Base: ~11,000-35,000 fontes
- Foco: Validação rigorosa
- Valor: Ativo acumulado valioso

**Expectativa:** Sistema fica **mais útil** com tempo (RF8)

---

## C. FLUXOS ALTERNATIVOS

### **FLUXO A: Usuário Não Entende Hierarquia de Evidências**

**Problema:** 7 níveis são complexos

**Solução:**
1. Oferecer tutorial interativo
2. Mostrar exemplos práticos
3. **SE ainda não entende:**
   - Simplificar para 3 níveis (Alta/Média/Baixa)
   - Manter 7 níveis como opção avançada

---

### **FLUXO B: Fonte Não Tem Metadados Completos**

**Problema:** Usuário não sabe autor/ano/etc.

**Solução:**
1. Permitir campos vazios (mínimo: título + URL)
2. Marcar como "incompleto"
3. Sugerir completar depois
4. Buscar metadados automaticamente (se possível)

---

### **FLUXO C: Usuário Quer Importar Base Existente**

**Problema:** Já tem fontes em Zotero/Mendeley/etc.

**Solução:**
1. Oferecer import de BibTeX/RIS/etc.
2. Mapear campos automaticamente
3. Pedir classificação de qualidade em lote:
   - Classificar todas de um tipo (ex: todos papers = Nível 2)
   - Ajustar individualmente depois

---

## D. REQUISITOS DE USABILIDADE

### **RU1: Simplicidade**

**O quê:** Interface clara e intuitiva

**Critérios:**
- Usuário completa onboarding em <20 min
- Usuário adiciona fonte em <2 min
- Usuário encontra fonte em <10 seg
- Usuário copia citação em <5 seg

---

### **RU2: Feedback Imediato**

**O quê:** Usuário sempre sabe o que está acontecendo

**Critérios:**
- Confirmação visual ao adicionar fonte
- Indicador de busca em andamento
- Mensagens de erro claras
- Sugestões de correção

---

### **RU3: Flexibilidade**

**O quê:** Usuário pode usar do jeito dele

**Critérios:**
- Tags livres (não pré-definidas)
- Hierarquia opcional (pode usar 3 ou 7 níveis)
- Múltiplos formatos de citação
- Múltiplos métodos de adição

---

### **RU4: Perdão**

**O quê:** Usuário pode desfazer erros

**Critérios:**
- Desfazer adição/edição
- Recuperar fonte deletada
- Editar metadados a qualquer momento
- Reclassificar qualidade

---

## E. REQUISITOS DE ACESSIBILIDADE

### **RA1: Documentação Clara**

**O quê:** Ajuda sempre disponível

**Critérios:**
- Tutorial interativo
- Documentação completa
- Exemplos práticos
- FAQ

---

### **RA2: Onboarding Guiado**

**O quê:** Usuário não fica perdido

**Critérios:**
- Passo a passo claro
- Tooltips contextuais
- Vídeos explicativos (opcional)
- Suporte via email/chat

---

## ✅ CHECKLIST PILAR 5 (8 ITENS)

- [x] Sistema de execução claro? → **SIM** (5 casos de uso + jornada)
- [x] Decisões automatizadas? → **SIM** (fluxos alternativos definidos)
- [x] If-then rules criadas? → **SIM** (3 fluxos alternativos)
- [x] Responsabilidade preservada? → **SIM** (usuário decide classificação, tags, etc.)
- [x] Otimizado para uso? → **SIM** (requisitos de usabilidade)
- [x] Ambiente facilita ação? → **SIM** (onboarding <20 min)
- [x] Fluxos de trabalho definidos? → **SIM** (5 casos de uso)
- [x] Jornada do usuário mapeada? → **SIM** (3 fases)

---

## 📊 RESUMO EXECUTIVO

### **SISTEMA DE USO DEFINIDO:**

**5 Casos de Uso Principais:**
1. Adicionar nova fonte (diário)
2. Citar fonte em artigo (semanal)
3. Validar premissa (mensal)
4. Identificar lacunas (mensal)
5. Gerar bibliografia (semanal)

**Jornada do Usuário:**
- Fase 1: Onboarding (<20 min)
- Fase 2: Uso regular (diário/semanal/mensal)
- Fase 3: Base crescente (contínuo)

**Fluxos Alternativos:**
- Hierarquia complexa → Simplificar
- Metadados incompletos → Permitir
- Base existente → Importar

**Requisitos de Usabilidade:**
- Simplicidade
- Feedback imediato
- Flexibilidade
- Perdão

---

**PILAR 5 COMPLETO** ✅

**AGUARDANDO VALIDAÇÃO DO USUÁRIO** 🔄

---

## ⚠️ REGRA DE VALIDAÇÃO OBRIGATÓRIA (v9.0)

**PARADA OBRIGATÓRIA:** Este pilar está completo, mas NÃO posso avançar para Pilar 7 sem validação explícita.

**Pergunta para o usuário:**

> **"Pilar 5 (Agente Externo - Sistema de Uso) completo. Aprova? (SIM/NÃO/AJUSTAR)"**

**Opções:**
- **SIM** → Avanço para Pilar 7 (Aprendizado Contínuo - último pilar)
- **NÃO** → Reviso Pilar 5 completo
- **AJUSTAR [aspecto]** → Ajusto aspecto específico

**Aguardando resposta...** ⏳
