# 🚧 Pilar 1: Identificação de Obstáculos

**Versão:** 1.0
**Data:** 19 de Dezembro de 2025

---

## ❓ O Que É?

O **Pilar 1** é o primeiro passo prático após definir o destino. Consiste em **identificar e listar TODOS os obstáculos** que estão entre você e o estado final definido no Pilar 0. É um exercício de honestidade radical e pensamento crítico.

**Princípio Fundamental:**
> "Um problema bem definido é um problema meio resolvido. Não se pode desviar de um obstáculo que você se recusa a ver."

Nesta fase, o objetivo **NÃO é resolver** os problemas, mas sim trazê-los à luz.

---

## 🧠 Por Que Funciona?

1.  **Transforma o Medo em Ação:** O medo do desconhecido é paralisante. Ao nomear os obstáculos, você transforma uma ansiedade vaga em uma lista de problemas concretos e gerenciáveis.
2.  **Cria um Plano de Ação Realista:** Um plano que ignora os obstáculos é apenas um desejo. A lista de obstáculos é a base para um plano de ação robusto e realista.
3.  **Foca a Aquisição de Recursos:** Ao saber quais são os obstáculos, você sabe exatamente quais recursos (conhecimento, ferramentas, dinheiro) precisa adquirir (Pilar 2).
4.  **Evita Surpresas Desagradáveis:** A maioria dos projetos falha por causa de obstáculos imprevistos. Este pilar força a antecipação, reduzindo o risco de surpresas no meio do caminho.

---

## 🛠️ Como Aplicar

### **Passo 1: Crie o Documento**

No seu diretório de projeto (`PROJETOS/meu_projeto/`), crie o arquivo `01_OBSTACULOS.md`.

### **Passo 2: Brainstorm Amplo**

Com o Estado Final (Pilar 0) em mente, pergunte-se: **"O que pode me impedir de chegar lá?"**. Faça um brainstorm e liste tudo que vier à mente, sem filtros. Use as seguintes categorias para guiar seu pensamento:

-   **Técnicos:** Lacunas na tecnologia, complexidade da arquitetura, integrações difíceis, performance.
-   **Financeiros:** Custos de ferramentas, orçamento insuficiente, fluxo de caixa.
-   **De Tempo:** Prazos apertados, sua disponibilidade, dependências externas.
-   **De Conhecimento:** Habilidades que você não possui, falta de experiência em uma área específica.
-   **De Recursos:** Falta de ferramentas, equipe insuficiente, infraestrutura inadequada.
-   **De Mercado:** Concorrência, falta de demanda, timing errado.
-   **Pessoais:** Procrastinação, falta de motivação, medo de falhar.

### **Passo 3: Use o Template**

Copie e cole este template em seu arquivo `01_OBSTACULOS.md` e preencha-o.

```markdown
# Obstáculos - [Nome do Projeto]

**Versão:** 1.0
**Data:** [Data de criação]

---

## 1. Lista de Obstáculos

### Obstáculos Técnicos
1.  **[Nome do Obstáculo]:** [Descrição detalhada]
    *Ex: **Complexidade da Busca Semântica:** Não tenho experiência em implementar um sistema RAG do zero, especialmente a parte de chunking e embedding de documentos.*
2.  **[...]:** [...]

### Obstáculos Financeiros
1.  **[Nome do Obstáculo]:** [Descrição detalhada]
    *Ex: **Custo da API Gemini:** O custo por token pode escalar rapidamente e ultrapassar o orçamento de $500/mês se o uso for alto.*
2.  **[...]:** [...]

### Obstáculos de Tempo
1.  **[Nome do Obstáculo]:** [Descrição detalhada]
    *Ex: **Disponibilidade Limitada:** Tenho apenas 10h/semana para dedicar ao projeto, o que pode tornar o prazo de 8 semanas para o MVP irrealista.*
2.  **[...]:** [...]

### Obstáculos de Conhecimento
1.  **[Nome do Obstáculo]:** [Descrição detalhada]
    *Ex: **Falta de Experiência com Temporal:** Nunca usei Temporal para orquestração de workflows, a curva de aprendizado pode ser alta.*
2.  **[...]:** [...]

*(Continue para todas as categorias relevantes)*

---

## 2. Matriz de Priorização de Obstáculos

*Avalie cada obstáculo com base no seu impacto (o quão prejudicial ele é se não for resolvido) e na sua probabilidade de ocorrência.*

| Obstáculo | Impacto (1-5) | Probabilidade (1-5) | Score (I x P) | Prioridade |
|---|---|---|---|---|
| Custo da API Gemini | 5 | 4 | 20 | 🔴 Crítico |
| Disponibilidade Limitada | 5 | 5 | 25 | 🔴 Crítico |
| Falta de Experiência com Temporal | 3 | 5 | 15 | 🟠 Alto |
| Complexidade da Busca Semântica | 4 | 3 | 12 | 🟠 Alto |
| [...] | ... | ... | ... | ... |

**Legenda:**
- **🔴 Crítico (16-25):** Deve ser resolvido ou mitigado no Pilar 3.
- **🟠 Alto (10-15):** Requer um plano de mitigação claro.
- **🟡 Médio (5-9):** Deve ser monitorado.
- **🟢 Baixo (1-4):** Pode ser ignorado por enquanto.

---

## 3. Resumo dos Obstáculos Críticos

*Liste os 3-5 obstáculos com maior score e descreva por que eles são críticos.*

### 1. Disponibilidade Limitada (Score 25)
> Este é o maior risco, pois afeta diretamente a capacidade de execução. Se não for mitigado, todos os prazos serão comprometidos.

### 2. Custo da API Gemini (Score 20)
> Risco existencial para o projeto. Se os custos saírem do controle, o projeto se torna financeiramente inviável.

### 3. [...]
> [...]
```

---

## ✅ Checkpoints de Validação

- [ ] Você identificou pelo menos 5 obstáculos?
- [ ] Você classificou os obstáculos por impacto e probabilidade?
- [ ] Você identificou o obstáculo CRÍTICO?

---

## 🏁 Definition of Done (DoD)

"O Pilar 1 está pronto quando: (1) Pelo menos 5 obstáculos foram identificados, (2) Eles foram classificados por impacto e probabilidade, (3) O obstáculo CRÍTICO foi identificado."

---

## 🏆 Critérios de Qualidade

- **Especificidade:** Os obstáculos são específicos e concretos, não vagos?
- **Relevância:** Eles estão diretamente no caminho para o Estado Final?
- **Honestidade:** Você foi honesto sobre os obstáculos internos (suas próprias limitações)?

---

## ✅ Checklist de Qualidade do Pilar 1

- [ ] Você listou pelo menos 10-15 obstáculos?
- [ ] Você considerou todas as categorias (técnico, financeiro, tempo, conhecimento, etc.)?
- [ ] Os obstáculos são específicos e não vagos? (Ex: "Falta de dinheiro" vs "Orçamento de $500/mês é insuficiente para cobrir custos de API e infra")
- [ ] A matriz de priorização foi preenchida honestamente?
- [ ] Os obstáculos críticos estão claramente identificados e justificados?

---

## 🔗 Relação com Outros Pilares

-   **Pilar 0 (Estado Final):** A clareza do estado final é essencial para identificar os obstáculos REAIS.
-   **Pilar 2 (Recursos):** Esta lista de obstáculos irá direcionar exatamente quais recursos você precisa adquirir ou desenvolver.
-   **Pilar 3 (Calibração):** Os obstáculos críticos são o principal insumo para a fase de calibração, onde você decidirá se precisa ajustar o escopo, o prazo ou o orçamento.

---

## 🎓 Exemplo no Projeto @google_Store

No início do projeto, um obstáculo crítico identificado foi a **"Falta de um Plano de Rollout em Fases"**. O plano inicial era construir tudo de uma vez, o que foi identificado como um risco altíssimo. Isso levou diretamente à criação do **Pilar 4.5 (Roadmap de Implementação)** na v10.6 do método.

**Veja o caso de uso completo em:** `contexto/casos_uso/CASO_USO_GOOGLE_STORE.md`

---

## 🎓 Exemplos Práticos de Vieses Cognitivos

### **1. Viés de Otimismo (Planning Fallacy)**

- **O que é:** A tendência de subestimar o tempo, os custos e os riscos de ações futuras.
- **Exemplo:** "Eu consigo fazer essa feature em 2 dias", quando na verdade leva 5 dias.
- **Como combater:** Multiplique suas estimativas por 1.5 ou 2. Peça estimativas de terceiros.

### **2. Viés de Confirmação**

- **O que é:** A tendência de procurar, interpretar e lembrar de informações que confirmam suas crenças existentes.
- **Exemplo:** "Eu acho que a tecnologia X é a melhor, então só vou ler artigos que falam bem dela."
- **Como combater:** Procure ativamente por informações que contradizem sua hipótese. Use o Pilar 5 (Validação Externa).

### **3. Efeito Dunning-Kruger**

- **O que é:** A tendência de pessoas com baixo conhecimento em uma área superestimarem sua habilidade.
- **Exemplo:** "Eu li um artigo sobre marketing, agora sou um especialista e posso criar a estratégia sozinho."
- **Como combater:** Seja humilde, consulte especialistas e use o Pilar 5.

---

**Próximo Passo:** Com os obstáculos identificados e priorizados, você está pronto para o **[Pilar 2: Análise de Recursos](PILAR_2_RECURSOS.md)**. 🚀
