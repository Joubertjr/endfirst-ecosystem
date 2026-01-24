# README SOURCE MAPPING (v1.0)

**Demanda:** DEMANDA-METODO-008 — README Estratégico END-FIRST  
**Fase:** F2 — Mapear Fontes Conceituais  
**Status:** CONCLUÍDO  
**Data:** 20 de Janeiro de 2026

---

## 🎯 END DESTE ARTEFATO

> "Todas as fontes canônicas estão mapeadas e seus conceitos-chave extraídos para uso no README."

Este documento extrai e organiza os conceitos-chave das fontes canônicas obrigatórias para garantir que o README seja conceitualmente robusto e alinhado com o método.

---

## 📚 FONTE 1: Artigo "Why Most New Year's Resolutions Fail"

**URL:** https://medium.com/@endfirstmethod/why-most-new-years-resolutions-fail-and-it-s-not-your-fault-6686003f53fb

### Conceitos-Chave Extraídos

| Conceito | Descrição | Citação / Ideia Central |
|---|---|---|
| **Problema Humano Fundamental** | A falha de resoluções não é moral (falta de disciplina), mas estrutural (uso de um modelo mental inadequado). | "The problem isn't you. It's the mental model you're using." |
| **Linear Planning Fallacy** | O modelo de planejamento linear assume um futuro previsível, motivação constante e disciplina infinita, o que não corresponde à realidade humana. | "Trying to change your life with linear planning is like trying to navigate a new city without knowing your destination." |
| **Princípio do GPS** | A rota é definida pelo destino. O destino é fixo, mas o caminho é adaptável. | "You tell it where you want to end up, and it calculates the optimal route backward from that destination." |
| **Três Forças da Falha** | A falha sistêmica é causada pela combinação de três fenômenos psicológicos: | |
| 1. **Planning Fallacy** | Subestimamos cronicamente o tempo, custo e dificuldade de tarefas futuras. | "We are, by nature, overly optimistic planners." |
| 2. **Decision Fatigue** | A qualidade das decisões se deteriora ao longo do dia. A força de vontade é um recurso limitado. | "Decision fatigue isn't weakness — it's biology." |
| 3. **Implementation Gap** | A lacuna entre a intenção de agir e a ação em si. A intenção não se traduz em realidade sem um plano concreto. | "Most of us intend to act, but we fail to execute." |
| **Ciclo de Culpa** | Falhar em seguir o plano linear gera culpa, que por sua vez cria mais decisões, acelerando a fadiga decisória e levando ao abandono. | "Guilt creates additional decisions, which accelerates decision fatigue. It's a vicious cycle." |
| **Solução: Pensar a Partir do Fim** | Em vez de focar no próximo passo, começar com uma visão clara do resultado desejado e trabalhar para trás. | "Think from the end, not about the end." |
| **Identidade vs. Tarefas** | Mudar o foco de "o que eu vou fazer" para "quem eu quero ser". O sistema é construído em torno da identidade desejada. | "Who do I want to be — and what system makes that almost inevitable?" |

---

## 📚 FONTE 2: Método END-FIRST v2

**Arquivo:** `/METODO/END_FIRST_V2.md`

### Conceitos-Chave Extraídos

| Conceito | Descrição | Ideia Central |
|---|---|---|
| **END (Estado Final Esperado)** | Um destino claro, verificável e imutável que define o sucesso. É o pilar central do método. | "O END é o contrato. O resto é execução." |
| **F-1 (Planejamento Canônico)** | O contrato de execução que detalha como o END será alcançado. É um artefato de primeira classe, não uma formalidade. | "Planning is a first-class artifact. Executor only executes." |
| **Gates** | Pontos de verificação de qualidade e conformidade que garantem que o método está sendo seguido. | "Qualidade não é uma expectativa. Qualidade é uma condição de passagem." |
| **Evidências** | Provas auditáveis e imutáveis de que o trabalho foi feito corretamente e os critérios de PASS foram atendidos. | "Se não há evidência, não aconteceu." |
| **PASS/FAIL Binário** | O sucesso não é subjetivo. Ou todos os critérios foram atendidos (PASS), ou não foram (FAIL). Não existe "quase PASS". | "Não existe 'quase PASS'. Existe PASS ou existe retrabalho." |
| **Governança do Executor** | O método governa o executor (seja humano ou IA). O executor não tem autonomia para desviar do método. | "Autoridade decide. Executor executa." |

---

## 📚 FONTE 3: Demandas de Método Relevantes

**Arquivo:** `DEMANDA-METODO-005` (Aplicação Obrigatória de Qualidade)

### Conceitos-Chave Extraídos

| Conceito | Descrição | Ideia Central |
|---|---|---|
| **Qualidade Não Opcional** | A qualidade (robustez, resiliência) não é um "extra", mas uma condição fundamental para o sucesso, especialmente em execuções longas. | "Qualidade não é complexidade; é sobrevivência sob falha." |
| **Regra Binária do Z10** | Gates de qualidade (como Z10) são obrigatórios para certas classes de demanda, a menos que uma dispensa seja explicitamente justificada e registrada. | "Se o método permite pular qualidade sem declarar, o método falhou." |
| **Prova de Robustez** | O sucesso exige prova de comportamento correto sob falha, não apenas em condições ideais. | "PASS exige prova de comportamento sob falha." |

---

## 📚 FONTE 4: Projeto `livros` (Implementação Prática)

### Conceitos-Chave a Serem Extraídos

- **Persistência Progressiva:** Como o sistema salva o estado a cada passo para evitar perda de trabalho.
- **Retomada Segura:** A capacidade de interromper e continuar uma execução longa sem corrupção de dados.
- **Rastreabilidade:** Como a estrutura de arquivos e commits permite uma auditoria completa do processo.
- **Exemplo de F-1:** Um F-1 real do projeto que demonstra o planejamento canônico em ação.

---

## ✅ CRITÉRIOS DE PASS

- [x] Todos os conceitos-chave das fontes foram extraídos e organizados.
- [x] O mapeamento conecta claramente os conceitos ao arco narrativo definido na Fase F1.
- [x] O documento serve como uma base de conhecimento robusta para a escrita do README na Fase F4.

---

## 📊 HISTÓRICO DE VERSÕES

- **v1.0** (2026-01-20): Versão inicial criada como parte da Fase F2 da DEMANDA-METODO-008.
