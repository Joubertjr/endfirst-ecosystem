# Sistema de Pesquisa de Contexto e Banco de Referências

**Data:** 09/12/2025  
**Objetivo:** Integrar pesquisa sistemática ao ENDFIRST Method

---

## 🎯 VISÃO GERAL

**Problema:** ENDFIRST v7.0 não especifica quando/como levantar referências

**Solução:** Sistema de 3 Momentos + Banco de Referências

**Componentes:**
1. **Pilar 1.5: Pesquisa de Contexto** (NOVO)
2. **Pilar 3A Expandido:** Pesquisa de Validação
3. **Banco de Referências:** Repositório organizado

---

## PILAR 1.5: PESQUISA DE CONTEXTO ⭐ **NOVO**

### **Objetivo**

Descobrir o que é possível alcançar ANTES de definir resultado esperado.

### **Quando**

**Entre Pilar 1 (Identidade) e Pilar 2 (Estado Final)**

**Por quê:**
- Pilar 1 define QUEM você é
- Pilar 1.5 descobre O QUE é possível
- Pilar 2 define O QUE você quer (baseado no possível)

### **Perguntas-Chave**

1. **Benchmarks:** Que resultados outros alcançaram?
2. **Abordagens:** Que abordagens funcionam?
3. **Gaps:** O que falta / não foi feito?
4. **Contexto:** Que contexto preciso entender?

### **Processo de 4 Etapas**

**Etapa 1: Definir Escopo**
- O que preciso pesquisar?
- Exemplo: "Benchmarks de crescimento no Medium para iniciantes"

**Etapa 2: Pesquisar**
- Fontes: Medium, Google Scholar, benchmarks públicos
- Tempo: 1-2h (máximo)
- Foco: Descobrir o possível (não validar)

**Etapa 3: Extrair Insights**
- Que benchmarks são realistas?
- Que abordagens funcionam?
- Que gaps existem?

**Etapa 4: Documentar**
- Salvar em `/research/[tema]/context_[data].md`
- Formato: Benchmarks + Abordagens + Gaps + Fontes

### **Exemplo: Artigo 1**

**Etapa 1: Escopo**
- "Benchmarks de crescimento no Medium para iniciantes (2024)"

**Etapa 2: Pesquisar**
- Artigos sobre "How to get first 100 followers on Medium"
- Benchmarks públicos
- Casos de sucesso

**Etapa 3: Insights**
- **Benchmarks realistas:**
  - Iniciante sem promoção: 20-100 views/artigo
  - Iniciante com promoção: 100-500 views/artigo
  - Taxa conversão: 10-15% (views → seguidores)
- **Abordagens que funcionam:**
  - Publicar em publicações grandes (Better Humans)
  - Subtítulo forte + quebras visuais
  - Experiência pessoal (não só pesquisa)
- **Gaps:**
  - Poucos artigos sobre planejamento reverso científico
  - Nenhum com GPS Principle

**Etapa 4: Documentar**
- Salvar em `/research/medium_growth/context_2024-12.md`

**Resultado:**
- Pilar 2 define meta realista: "200-300 views, 5-10 seguidores"
- Não: "1.000 seguidores" (irrealista)

---

## PILAR 3A EXPANDIDO: PESQUISA DE VALIDAÇÃO

### **Objetivo**

Validar premissas com fontes primárias confiáveis.

### **Quando**

**Pilar 3 (Calibração) - Etapa A (Calibração de Premissas)**

### **Processo de 3 Etapas** (Já existe, mas expandido)

**Etapa 1: Identificar Premissas**
- Liste todas as suposições não validadas
- Exemplo: "92% das resoluções falham"

**Etapa 2: Buscar Evidências**
- **NOVO:** Consultar Banco de Referências PRIMEIRO
- Se não encontrar: Pesquisar fonte primária
- Usar Hierarquia de Evidências (7 níveis)

**Etapa 3: Validar ou Rejeitar**
- Aceitar: Evidência nível 1-3
- Rejeitar: Evidência nível 4-7 ou não encontrada
- **NOVO:** Adicionar ao Banco se validado

### **Fluxo com Banco de Referências**

```
Premissa: "92% das resoluções falham"
  ↓
Consultar Banco: /references/goal_setting/
  ↓
Encontrado? 
  → SIM: Usar citação pronta (30 seg)
  → NÃO: Pesquisar fonte primária (2h)
      ↓
      Validar (nível 1-3?)
        → SIM: Adicionar ao Banco + Usar
        → NÃO: Rejeitar + Buscar alternativa
```

### **Exemplo: Artigo 1**

**SEM Banco:**
- Premissa: "92% falham"
- Pesquisar fonte primária (2h)
- Encontrar: Norcross (1988) - 37 anos
- Rejeitar
- Pesquisar alternativa (2h)
- Encontrar: Oscarsson (2020) - "45-81%"
- **Total:** 4h

**COM Banco:**
- Premissa: "92% falham"
- Consultar `/references/goal_setting/`
- Encontrar: `oscarsson_resolutions_2020.md`
- Ler: "45-81% falham (Oscarsson 2020, 67 citações)"
- Usar citação pronta
- **Total:** 5 min

**Economia:** -3h55min

---

## BANCO DE REFERÊNCIAS: ESTRUTURA COMPLETA

### **Objetivo**

Repositório organizado de referências validadas, reutilizáveis em ciclos futuros.

### **Estrutura de Diretórios**

```
/references/
├── behavioral_science/
│   ├── kahneman_planning_fallacy.md
│   ├── baumeister_decision_fatigue.md
│   ├── gollwitzer_implementation_gap.md
│   └── oettingen_mental_contrasting.md
├── goal_setting/
│   ├── norcross_resolutions_1988.md
│   ├── oscarsson_resolutions_2020.md
│   ├── harkin_monitoring_2016.md
│   └── locke_goal_setting_theory.md
├── learning/
│   ├── kolb_learning_cycle.md
│   ├── kaizen_toyota.md
│   └── after_action_review_army.md
├── motivation/
│   ├── deci_self_determination.md
│   ├── pink_drive.md
│   └── frankl_logotherapy.md
├── copywriting/
│   ├── cialdini_influence.md
│   └── ladeira_90_lessons.md
├── benchmarks/
│   ├── medium_growth_2024.md
│   ├── linkedin_engagement_2024.md
│   ├── better_humans_acceptance.md
│   └── substack_conversion_rates.md
└── frameworks/
    ├── amazon_working_backwards.md
    ├── toyota_hoshin_kanri.md
    └── okr_google.md
```

### **Template de Arquivo**

```markdown
# [Título do Estudo/Conceito]

**Autor:** [Nome]  
**Ano:** [Ano]  
**Citações:** [Número]  
**Tipo:** [Meta-análise / Estudo / Framework / Benchmark]  
**Nível de Evidência:** [1-7]

---

## Citação Completa

[Formato APA ou similar]

---

## Resumo (1 Parágrafo)

[Resumo conciso do conceito/descoberta principal]

---

## Descoberta-Chave

[Frase de 1 linha que resume o insight principal]

---

## Quando Usar

- [Contexto 1]
- [Contexto 2]
- [Contexto 3]

---

## Citação Pronta (Copyable)

> "[Citação textual]" ([Autor], [Ano])

---

## Link para Fonte

[URL da fonte primária]

---

## Tags

#[tag1] #[tag2] #[tag3]

---

## Adicionado ao Banco

**Data:** [Data]  
**Por:** [Quem adicionou]  
**Usado em:** [Lista de artigos/projetos que usaram]
```

### **Exemplo: kahneman_planning_fallacy.md**

```markdown
# Planning Fallacy

**Autor:** Daniel Kahneman & Amos Tversky  
**Ano:** 1979  
**Citações:** 15.000+  
**Tipo:** Estudo  
**Nível de Evidência:** 2 (Estudo peer-reviewed, 100+ citações)

---

## Citação Completa

Kahneman, D., & Tversky, A. (1979). Intuitive prediction: Biases and corrective procedures. TIMS Studies in Management Science, 12, 313-327.

---

## Resumo

Planning Fallacy é a tendência de subestimar o tempo, custos e riscos de ações futuras, enquanto superestimamos benefícios. Ocorre porque focamos no cenário ideal e ignoramos obstáculos históricos.

---

## Descoberta-Chave

"Pessoas consistentemente subestimam tempo necessário para completar tarefas, mesmo quando têm experiência prévia de atrasos."

---

## Quando Usar

- Explicar por que metas lineares falham
- Justificar necessidade de buffer (40%)
- Validar planejamento reverso
- Artigos sobre produtividade/planejamento

---

## Citação Pronta

> "Planning Fallacy: a tendência de subestimar tempo, custos e riscos de ações futuras." (Kahneman & Tversky, 1979)

---

## Link para Fonte

https://psycnet.apa.org/record/1980-09923-001

---

## Tags

#behavioral_science #planning #cognitive_bias #productivity

---

## Adicionado ao Banco

**Data:** 09/12/2024  
**Por:** ENDFIRST Team  
**Usado em:** Article 1 (Medium)
```

---

## PROCESSO DE USO DO BANCO

### **1. ANTES DE COMEÇAR CICLO**

**Checklist:**
- [ ] Consultei Banco para tema similar?
- [ ] Identifiquei referências reutilizáveis?
- [ ] Adicionei ao planejamento?

### **2. DURANTE PESQUISA**

**Fluxo:**
1. Preciso de referência sobre X
2. Consultar `/references/[categoria]/`
3. Encontrado?
   - SIM: Usar citação pronta
   - NÃO: Pesquisar + Adicionar ao Banco

### **3. APÓS CONCLUSÃO**

**Checklist:**
- [ ] Adicionei novas referências ao Banco?
- [ ] Atualizei "Usado em:" nas referências existentes?
- [ ] Organizei por categoria correta?

---

## INTEGRAÇÃO COM PILAR 7 (APRENDIZADO CONTÍNUO)

**Pilar 7 captura aprendizados sobre PROCESSO**  
**Banco captura REFERÊNCIAS reutilizáveis**

**Diferença:**

| Aspecto | Pilar 7 | Banco de Referências |
|:--------|:--------|:---------------------|
| **O que** | Aprendizados de processo | Referências científicas |
| **Quando** | Após cada ciclo | Durante pesquisa |
| **Formato** | Narrativa | Estruturado |
| **Uso** | Melhorar processo | Citar em conteúdo |

**Exemplo:**
- **Pilar 7:** "Validação leva 2-3x mais tempo que estimado"
- **Banco:** "Oscarsson (2020): 45-81% falham - citação pronta"

---

## MÉTRICAS DE SUCESSO

### **Banco de Referências:**

**Métrica 1: Cobertura**
- % de temas com referências no Banco
- Meta: 80% após 5 ciclos

**Métrica 2: Reutilização**
- % de referências reutilizadas (vs pesquisadas do zero)
- Meta: 50% após 3 ciclos

**Métrica 3: Economia de Tempo**
- Tempo economizado por reutilização
- Meta: -2h por ciclo

### **Pilar 1.5 (Pesquisa de Contexto):**

**Métrica 1: Realismo de Metas**
- % de metas alcançadas (vs definidas)
- Meta: 80% após calibração com benchmarks

**Métrica 2: Tempo de Pesquisa**
- Tempo gasto em Pesquisa de Contexto
- Meta: 1-2h (não mais)

---

## EXEMPLO COMPLETO: ARTIGO 2

### **COM SISTEMA (Fluxo Ideal):**

**Pilar 1:** Identidade → "Educador científico"

**Pilar 1.5:** Pesquisa de Contexto (1h)
- Consultar `/research/medium_growth/context_2024-12.md`
- Benchmarks já documentados
- Não precisa pesquisar novamente

**Pilar 2:** Estado Final → "200-300 views, 5-10 seguidores" (realista)

**Pilar 3A:** Validação (30 min)
- Consultar `/references/goal_setting/oscarsson_resolutions_2020.md`
- Citação pronta
- Não precisa pesquisar

**Pilar 5:** Escrita (6h)
- Consultar `/references/behavioral_science/kahneman_planning_fallacy.md`
- Consultar `/references/behavioral_science/gollwitzer_implementation_gap.md`
- Citações prontas
- Sem interrupções

**Total Pesquisa:** 1h30min (vs 6h no Artigo 1)

**Economia:** -4h30min

---

## CHECKLIST COMPLETO

### **Pilar 1.5: Pesquisa de Contexto (4 itens)** ⭐ **NOVO**
- [ ] Defini escopo de pesquisa?
- [ ] Pesquisei benchmarks realistas?
- [ ] Identifiquei abordagens que funcionam?
- [ ] Documentei em `/research/[tema]/`?

### **Banco de Referências (3 itens)** ⭐ **NOVO**
- [ ] Consultei Banco antes de pesquisar?
- [ ] Adicionei novas referências ao Banco?
- [ ] Organizei por categoria correta?

---

## LIÇÃO-CHAVE

> **"Pesquisa sem sistema é trabalho dobrado. Pesquisa com sistema é investimento que se paga em cada ciclo."**

---

**SISTEMA COMPLETO** ✅  
**Pronto para integrar ao ENDFIRST v8.0** ✅
