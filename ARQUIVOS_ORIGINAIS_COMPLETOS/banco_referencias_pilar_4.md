# PILAR 4: CAMINHO REVERSO (O COMO - REQUISITOS)
## Projeto: Banco de Referências - Requisitos de Negócio

**Data:** 09/12/2025  
**Versão do Método:** v9.0  
**Foco:** Priorizar requisitos do estado final até o presente

---

## OBJETIVO DO PILAR

Mapear caminho **do estado final (MVP pronto) até o presente**, priorizando requisitos por dependências e valor.

**IMPORTANTE:** Foco em **O QUÊ** fazer (requisitos de negócio), não **COMO** implementar tecnicamente.

---

## A. ESTADO FINAL (MARCO 0)

**MVP V1.0 completo e funcionando:**

✅ 8 Funcionalidades essenciais implementadas  
✅ Atende 6 gaps identificados  
✅ Resolve 4 problemas do Pilar 1  
✅ Economia de 20-50 min/artigo validada  
✅ Usuário consegue usar sozinho (<20 min onboarding)

---

## B. CAMINHO REVERSO (15 MARCOS)

### **MARCO 15: MVP V1.0 Pronto** 🎯
**O quê:** Sistema completo e validado  
**Depende de:** Marco 14  
**Valor:** 100%

---

### **MARCO 14: Validação com Usuário Real**
**O quê:** Testar todas funcionalidades com caso de uso real  
**Requisitos:**
- R14.1: Usuário consegue completar fluxo completo
- R14.2: Economia de tempo é mensurável
- R14.3: Onboarding <20 min validado

**Depende de:** Marco 13  
**Valor:** 95%

---

### **MARCO 13: Integração Completa**
**O quê:** Todas funcionalidades funcionam juntas  
**Requisitos:**
- R13.1: F1-F8 integradas
- R13.2: Fluxo de uso coerente
- R13.3: Dados consistentes entre funcionalidades

**Depende de:** Marcos 5-12  
**Valor:** 90%

---

### **MARCO 12: F8 - Base Crescente Implementada** ⭐
**O quê:** Sistema otimiza para base crescente  
**Requisitos:**
- R12.1: Sugestões automáticas de conexões
- R12.2: Performance não degrada com mais fontes
- R12.3: Lacunas identificadas automaticamente

**Status:** EXPERIMENTAL (validar com uso)  
**Depende de:** Marcos 4, 5, 11  
**Valor:** 85%

---

### **MARCO 11: F7 - Busca Rápida Implementada**
**O quê:** Usuário encontra qualquer fonte em <10 seg  
**Requisitos:**
- R11.1: Busca full-text
- R11.2: Filtros (tag, projeto, qualidade)
- R11.3: Resultados relevantes primeiro

**Depende de:** Marcos 2, 3  
**Valor:** 80%

---

### **MARCO 10: F6 - Citação Fácil Implementada**
**O quê:** Usuário copia citação formatada rapidamente  
**Requisitos:**
- R10.1: Copiar citação em formato escolhido (APA, ABNT, etc.)
- R10.2: Gerar bibliografia completa
- R10.3: Formatos corretos e validados

**Depende de:** Marco 2  
**Valor:** 75%

---

### **MARCO 9: F5 - Lacunas Identificadas** ⭐
**O quê:** Usuário vê o que falta pesquisar  
**Requisitos:**
- R9.1: Temas com poucas fontes identificados
- R9.2: Conexões fracas visualizadas
- R9.3: Sugestões de próximas pesquisas

**Status:** EXPERIMENTAL (validar com uso)  
**Depende de:** Marcos 3, 4  
**Valor:** 70%

---

### **MARCO 8: F4 - Conexões Visualizadas** ⭐
**O quê:** Usuário vê e navega entre fontes relacionadas  
**Requisitos:**
- R8.1: Linkar fontes entre si
- R8.2: Ver fontes relacionadas
- R8.3: Navegar entre conexões

**Status:** EXPERIMENTAL (validar com uso)  
**Depende de:** Marco 2  
**Valor:** 65%

---

### **MARCO 7: F3 - Qualidade Validada** 🔴 GARGALO
**O quê:** Usuário classifica e prioriza por qualidade  
**Requisitos:**
- R7.1: Classificar por Hierarquia de Evidências (7 níveis)
- R7.2: Ver qualidade de cada fonte
- R7.3: Priorizar fontes confiáveis
- R7.4: Tutorial interativo (se usuário não entender)

**Por quê gargalo:**
- Funcionalidade única (não existe em outras ferramentas)
- Requer definição clara dos 7 níveis
- Requer validação de usabilidade
- Crítico para diferenciação

**Depende de:** Marco 2  
**Valor:** 60%

---

### **MARCO 6: F2 - Organização Implementada**
**O quê:** Usuário organiza fontes facilmente  
**Requisitos:**
- R6.1: Tags
- R6.2: Pastas/Projetos
- R6.3: Busca por qualquer campo

**Depende de:** Marco 2  
**Valor:** 55%

---

### **MARCO 5: F1 - Adicionar Referências Implementada**
**O quê:** Usuário adiciona fontes facilmente  
**Requisitos:**
- R5.1: Adicionar manualmente (formulário)
- R5.2: Importar de arquivo (BibTeX, RIS, etc.)
- R5.3: Capturar de URL

**Depende de:** Marco 2  
**Valor:** 50%

---

### **MARCO 4: Modelo de Dados Definido**
**O quê:** Estrutura de dados clara  
**Requisitos:**
- R4.1: Campos de referência (autor, título, ano, etc.)
- R4.2: Metadados (tags, projeto, qualidade, etc.)
- R4.3: Relacionamentos (conexões entre fontes)
- R4.4: Suporta múltiplos tipos de fontes

**Depende de:** Marco 3  
**Valor:** 40%

---

### **MARCO 3: Requisitos Funcionais Priorizados**
**O quê:** Lista de requisitos ordenada por prioridade  
**Requisitos:**
- R3.1: Requisitos essenciais (MVP)
- R3.2: Requisitos experimentais
- R3.3: Requisitos futuros (V2.0+)
- R3.4: Dependências mapeadas

**Depende de:** Marco 2  
**Valor:** 30%

---

### **MARCO 2: Requisitos Funcionais Completos**
**O quê:** Documento com TODOS requisitos de negócio  
**Requisitos:**
- R2.1: 8 funcionalidades detalhadas
- R2.2: Necessidades atendidas mapeadas
- R2.3: Gaps resolvidos documentados
- R2.4: Métricas de sucesso definidas

**Depende de:** Marco 1  
**Valor:** 20%

---

### **MARCO 1: Requisitos de Negócio Validados** ⭐
**O quê:** Pilares 0-3 completos e validados  
**Requisitos:**
- R1.1: Identidade clara (por quê)
- R1.2: Necessidades identificadas (o possível)
- R1.3: Estado final definido (o quê)
- R1.4: Viabilidade validada (o realismo)

**Depende de:** PRESENTE  
**Valor:** 10%

---

### **MARCO 0: PRESENTE** (AGORA)
**O quê:** Pilares 0-3 completos  
**Status:** ✅ COMPLETO  
**Próximo:** Marco 1 (este pilar)

---

## C. DEPENDÊNCIAS MAPEADAS

### **Dependências Sequenciais:**

```
0 (PRESENTE) → 1 → 2 → 3 → 4 → 5,6,7,8,9,10,11 → 12 → 13 → 14 → 15 (MVP)
```

### **Dependências Paralelas:**

Marcos 5-11 podem ser desenvolvidos em **paralelo** após Marco 4:
- F1 (Adicionar) → Marco 5
- F2 (Organizar) → Marco 6
- F3 (Qualidade) → Marco 7 🔴 GARGALO
- F4 (Conexões) → Marco 8
- F5 (Lacunas) → Marco 9
- F6 (Citação) → Marco 10
- F7 (Busca) → Marco 11

Marco 12 (F8 - Base Crescente) depende de 4, 5, 11.

---

## D. GARGALO CRÍTICO

### **MARCO 7: F3 - Validação de Qualidade** 🔴

**Por quê é gargalo:**

1. **Funcionalidade única**
   - Não existe em outras ferramentas
   - Sem benchmarks para copiar
   - Requer design original

2. **Complexidade conceitual**
   - Hierarquia de Evidências (7 níveis)
   - Usuário pode não entender
   - Requer tutorial/onboarding

3. **Crítico para diferenciação**
   - Resolve GAP 2 (principal diferencial)
   - Sem isso, é só mais uma ferramenta de citação
   - Valor único do Banco

4. **Risco de usabilidade**
   - Se usuário não entender → baixa adoção
   - Se muito complexo → usuário desiste
   - Requer validação cuidadosa

**Mitigação:**

- **Plano A:** Tutorial interativo claro
- **Plano B:** Simplificar para 3 níveis (Alta/Média/Baixa)
- **Plano C:** Tornar opcional (usuário escolhe usar ou não)

---

## E. PRIORIZAÇÃO DE REQUISITOS

### **PRIORIDADE 1: CRÍTICOS (Não pode lançar sem)**

**R1.1-R1.4:** Requisitos de negócio validados ✅ (COMPLETO)  
**R2.1-R2.4:** Requisitos funcionais completos (ESTE PILAR)  
**R4.1-R4.4:** Modelo de dados definido  
**R5.1-R5.3:** Adicionar referências (F1)  
**R7.1-R7.4:** Validação de qualidade (F3) 🔴 GARGALO

**Justificativa:** Sem esses, não atende propósito básico.

---

### **PRIORIDADE 2: ESSENCIAIS (MVP incompleto sem)**

**R6.1-R6.3:** Organização (F2)  
**R10.1-R10.3:** Citação fácil (F6)  
**R11.1-R11.3:** Busca rápida (F7)

**Justificativa:** Necessários para uso prático, mas MVP pode funcionar sem.

---

### **PRIORIDADE 3: EXPERIMENTAIS (Validar com uso)**

**R8.1-R8.3:** Conexões (F4) ⭐  
**R9.1-R9.3:** Lacunas (F5) ⭐  
**R12.1-R12.3:** Base crescente (F8) ⭐

**Justificativa:** Diferenciais importantes, mas não validados. Podem ser V2.0 se não funcionarem.

---

### **PRIORIDADE 4: VALIDAÇÃO**

**R13.1-R13.3:** Integração completa  
**R14.1-R14.3:** Validação com usuário

**Justificativa:** Garantem qualidade, mas vêm depois de funcionalidades.

---

## F. TIMELINE ESTIMADA (SEM TECNOLOGIA)

**Fase 1: Requisitos (1-2 semanas)**
- Marco 1: Validar Pilares 0-3 ✅ COMPLETO
- Marco 2: Documentar requisitos completos (ESTE PILAR)
- Marco 3: Priorizar requisitos (ESTE PILAR)

**Fase 2: Design (2-4 semanas)**
- Marco 4: Definir modelo de dados
- Marcos 5-11: Detalhar cada funcionalidade
- Marco 7: Resolver gargalo (Hierarquia de Evidências)

**Fase 3: Implementação (8-16 semanas)**
- Desenvolver funcionalidades priorizadas
- Foco em P1 (críticos) primeiro
- P2 (essenciais) depois
- P3 (experimentais) por último

**Fase 4: Validação (2-4 semanas)**
- Marco 13: Integrar tudo
- Marco 14: Testar com usuário real
- Marco 15: MVP pronto

**Total:** 13-26 semanas (3-6 meses) ✅ Alinhado com Pilar 3

---

## ✅ CHECKLIST PILAR 4 (5 ITENS)

- [x] Marcos críticos mapeados? → **SIM** (15 marcos)
- [x] Dependências identificadas? → **SIM** (sequenciais + paralelas)
- [x] Gargalo crítico identificado? → **SIM** (Marco 7 - F3 Qualidade)
- [x] Cada etapa tem sentido claro? → **SIM** (requisitos de negócio, não tecnologia)
- [x] Caminho viável? → **SIM** (3-6 meses, alinhado com Pilar 3)

---

## 📊 RESUMO EXECUTIVO

### **CAMINHO MAPEADO:**

**15 marcos** do estado final (MVP) até presente  
**3 prioridades** definidas (Críticos, Essenciais, Experimentais)  
**1 gargalo** identificado (F3 - Validação de Qualidade)  
**Timeline:** 3-6 meses (alinhado com Pilar 3)

---

### **REQUISITOS PRIORIZADOS:**

**P1 - CRÍTICOS (5 requisitos):**
- R1: Requisitos validados ✅
- R2: Requisitos completos
- R4: Modelo de dados
- R5: Adicionar referências (F1)
- R7: Validação qualidade (F3) 🔴

**P2 - ESSENCIAIS (3 requisitos):**
- R6: Organização (F2)
- R10: Citação (F6)
- R11: Busca (F7)

**P3 - EXPERIMENTAIS (3 requisitos):**
- R8: Conexões (F4)
- R9: Lacunas (F5)
- R12: Base crescente (F8)

---

### **GARGALO CRÍTICO:**

**Marco 7: F3 - Validação de Qualidade**

**Por quê:**
- Funcionalidade única (sem benchmarks)
- Complexidade conceitual (7 níveis)
- Crítico para diferenciação (GAP 2)
- Risco de usabilidade

**Mitigação:**
- Tutorial interativo
- Simplificar se necessário (3 níveis)
- Tornar opcional como último recurso

---

**PILAR 4 COMPLETO** ✅

**AGUARDANDO VALIDAÇÃO DO USUÁRIO** 🔄

---

## ⚠️ REGRA DE VALIDAÇÃO OBRIGATÓRIA (v9.0)

**PARADA OBRIGATÓRIA:** Este pilar está completo, mas NÃO posso avançar para Pilar 5 sem validação explícita.

**Pergunta para o usuário:**

> **"Pilar 4 (Caminho Reverso - Requisitos Priorizados) completo. Aprova? (SIM/NÃO/AJUSTAR)"**

**Opções:**
- **SIM** → Avanço para Pilar 5 (Agente Externo - Sistema de uso)
- **NÃO** → Reviso Pilar 4 completo
- **AJUSTAR [aspecto]** → Ajusto aspecto específico

**Aguardando resposta...** ⏳
