# ⚖️ Pilar 3: Calibração com a Realidade

**Versão:** 1.0
**Data:** 19 de Dezembro de 2025

---

## ❓ O Que É?

O **Pilar 3** é o momento da verdade. É onde a sua visão ambiciosa (Pilar 0) colide com a dura realidade dos seus obstáculos (Pilar 1) e recursos (Pilar 2). É o ponto de checagem mais crítico do método, onde você ajusta o plano para torná-lo **desafiador, porém alcançável**.

**Princípio Fundamental:**
> "A realidade é negociável, mas não ignorável. O sucesso não vem de ter um plano perfeito, mas de ter um plano que sobrevive ao contato com a realidade."

Este pilar é sobre tomar decisões difíceis e pragmáticas **antes** de escrever a primeira linha de código.

---

## 🧠 Por Que Funciona?

1.  **Previne o Fracasso por Exaustão:** A principal causa de abandono de projetos é a tentativa de alcançar um objetivo irrealista com recursos insuficientes. A calibração ajusta a equação `Visão vs Realidade` para que ela seja positiva.
2.  **Transforma o Plano em Ação:** Um plano não calibrado é apenas um sonho. Um plano calibrado é um mapa que pode ser seguido.
3.  **Otimiza o Uso de Recursos:** Força você a alocar seus recursos limitados nos problemas mais importantes, em vez de desperdiçá-los em funcionalidades secundárias.
4.  **Reduz o Risco:** É muito mais barato e rápido ajustar um plano em um documento do que mudar a direção de um projeto em andamento.

---

## 🛠️ Como Aplicar

### **Passo 1: Crie o Documento**

No seu diretório de projeto (`PROJETOS/meu_projeto/`), crie o arquivo `03_CALIBRACAO.md`.

### **Passo 2: A Análise Central**

O coração deste pilar é a comparação direta entre os **Obstáculos Críticos** (Pilar 1) e os **Gaps de Recursos** (Pilar 2). Crie uma tabela para visualizar essa relação.

### **Passo 3: Tome Decisões de Ajuste**

Para cada conflito identificado, você tem 3 opções:

1.  **Aumentar Recursos:** Você pode obter mais tempo, dinheiro ou conhecimento?
2.  **Reduzir o Obstáculo:** Você pode encontrar uma solução mais simples ou uma abordagem alternativa?
3.  **Ajustar o Estado Final:** Você precisa reduzir o escopo, estender o prazo ou diminuir a qualidade esperada?

Seja brutalmente honesto. Na maioria das vezes, a resposta correta é a número 3.

### **Passo 4: Use o Template**

Copie e cole este template em seu arquivo `03_CALIBRACAO.md` e preencha-o.

```markdown
# Calibração com a Realidade - [Nome do Projeto]

**Versão:** 1.0
**Data:** [Data de criação]

---

## 1. Análise de Viabilidade (Obstáculos vs Recursos)

*Esta tabela cruza os obstáculos e gaps de recursos mais críticos identificados nos pilares anteriores.*

| Obstáculo/Gap Crítico | Impacto no Projeto | Recursos Disponíveis | Conflito/Viabilidade | Decisão Preliminar |
|---|---|---|---|---|
| **Disponibilidade Limitada (10h/semana)** | Atraso em todas as frentes | Apenas 180h totais | **🔴 Conflito Alto:** Impossível entregar o escopo completo no prazo. | Reduzir escopo do MVP. |
| **Custo da API Gemini** | Risco de inviabilidade financeira | Orçamento de $500/mês | **🟠 Conflito Médio:** Orçamento apertado, requer otimização. | Implementar caching e monitoramento. |
| **Falta de Experiência com Temporal** | Atraso na Fase 2, risco de má implementação | Tempo para estudo (20h) | **🟡 Conflito Baixo:** Mitigável com plano de capacitação. | Manter plano de estudo. |
| [...] | ... | ... | ... | ... |

---

## 2. Decisões de Ajuste

*Com base na análise acima, documente as decisões de ajuste tomadas.*

### Decisão 1: Redução do Escopo do MVP

-   **Razão:** O conflito entre a disponibilidade de tempo e o escopo original é o maior risco do projeto.
-   **Ação:** O escopo do MVP será reduzido de 8 para 5 Requisitos Funcionais. Os RF-06, RF-07 e RF-08 serão movidos para a Fase 2.
-   **Impacto:** O MVP será mais enxuto, mas entregará o core da proposta de valor. O prazo de 8 semanas se torna realista.
-   **Alternativas Consideradas:** Tentar obter mais tempo (inviável), estender o prazo (afetaria a motivação).

### Decisão 2: Mitigação Ativa de Custos

-   **Razão:** O custo da API é um risco financeiro real.
-   **Ação:** O RNF de monitoramento de custos será elevado para prioridade máxima no MVP. Uma camada de cache com Redis será implementada desde o início.
-   **Impacto:** Aumento de 1 semana no desenvolvimento do MVP, mas reduz o risco financeiro a longo prazo.

### Decisão 3: [...]

---

## 3. Estado Final Ajustado (v1.1)

*Se o Estado Final foi alterado, documente a nova versão aqui. Se não houve mudanças, declare isso explicitamente.*

**Mudanças em Relação à v1.0:**

-   **Escopo:** O MVP agora consiste em 5 RFs, com os 3 restantes movidos para a Fase 2.
-   **Prazo:** O prazo do MVP é mantido em 8 semanas, mas o prazo do Beta é estendido para 12 semanas para acomodar os RFs movidos.
-   **Métricas:** A métrica de "Horas Economizadas" será medida apenas na Fase 2, não no MVP.

*(Copie e cole o Estado Final do Pilar 0 e aplique as mudanças)*

---

## 4. Próximo Passo Obrigatório: Análise de Riscos

Com o plano agora calibrado, o próximo passo é aprofundar a análise das opções técnicas através do **Pilar 3.5: Análise de Riscos e Trade-offs**.
```

---

## ✅ Checklist de Qualidade do Pilar 3

- [ ] A análise de viabilidade é honesta e baseada nos dados dos Pilares 1 e 2?
- [ ] Você tomou decisões difíceis em vez de apenas desejar que os problemas desapareçam?
- [ ] As decisões de ajuste são claras, com justificativas e impactos documentados?
- [ ] O Estado Final foi formalmente atualizado para refletir as mudanças?
- [ ] Você se sente mais confiante de que o plano, agora ajustado, é alcançável?

---

## 🔗 Relação com Outros Pilares

-   **Pilar 3.5 (Análise de Riscos):** Este pilar é a porta de entrada para o 3.5. Após calibrar o "o quê", o Pilar 3.5 irá definir o "como".
-   **Pilar 4 (Caminho Reverso):** O plano calibrado é o que será usado para traçar os marcos do caminho reverso. Um caminho reverso baseado em um plano não calibrado é inútil.
-   **Pilar 6 (Execução):** As decisões tomadas aqui (ex: redução de escopo) irão guiar diretamente o backlog de tarefas da execução.

---

## 🎓 Exemplo no Projeto @google_Store

No projeto, a calibração foi crucial. Percebeu-se que implementar todos os 12 RFs e 8 RNFs de uma vez era inviável. A decisão foi criar um **Roadmap em Fases (Pilar 4.5)**, com um MVP focado no core (upload, busca, análise) e um stack tecnológico simplificado (Redis em vez de Dragonfly, BullMQ em vez de Temporal). Esta decisão tornou o projeto executável.

**Veja o caso de uso completo em:** `contexto/casos_uso/CASO_USO_GOOGLE_STORE.md`

---

## 🎓 Exemplo Prático de Matriz de Decisão

| Critério | Peso | Abordagem A: Serverless (Vercel) | Abordagem B: Monolito (VPS) | Abordagem C: Microserviços (K8s) |
|---|---|---|---|---|
| Custo Inicial | 30% | 5 (1.5) | 4 (1.2) | 1 (0.3) |
| Escalabilidade | 25% | 4 (1.0) | 2 (0.5) | 5 (1.25) |
| Complexidade de Deploy | 25% | 5 (1.25) | 4 (1.0) | 1 (0.25) |
| Time-to-Market | 20% | 5 (1.0) | 3 (0.6) | 1 (0.2) |
| **TOTAL** | **100%** | **4.75** ⭐ | **3.30** | **2.00** |

**Decisão:** Abordagem A (Serverless) é a vencedora para o MVP, pois otimiza custo, simplicidade e velocidade.

---

**Próximo Passo:** Com o plano geral calibrado, é hora de aprofundar nas decisões técnicas com o **[Pilar 3.5: Análise de Riscos e Trade-offs](PILAR_3.5_ANALISE_RISCOS.md)**. 🚀
