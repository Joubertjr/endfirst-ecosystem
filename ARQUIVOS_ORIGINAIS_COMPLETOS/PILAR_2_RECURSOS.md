# 💰 Pilar 2: Análise de Recursos

**Versão:** 1.0
**Data:** 19 de Dezembro de 2025

---

## ❓ O Que É?

O **Pilar 2** é o contraponto ao Pilar 1. Após listar tudo que pode dar errado (obstáculos), agora você vai **inventariar tudo que você tem a seu favor**. É um exercício de reconhecimento de seus ativos, muitas vezes subestimados.

**Princípio Fundamental:**
> "Você é mais rico do que pensa. A criatividade não está na ausência de recursos, mas no uso inteligente dos que você já possui."

Recursos não são apenas dinheiro. Incluem tempo, conhecimento, ferramentas, contatos e sua própria energia.

---

## 🧠 Por Que Funciona?

1.  **Combate a Sensação de Impotência:** Após a lista de obstáculos do Pilar 1, é comum sentir-se sobrecarregado. O Pilar 2 reequilibra a balança, mostrando que você tem armas para lutar.
2.  **Direciona a Solução de Problemas:** Ao cruzar a lista de obstáculos com a de recursos, você começa a ver soluções. "Tenho o obstáculo X, mas tenho o recurso Y que pode resolvê-lo."
3.  **Identifica Gaps Críticos:** A análise revela quais recursos essenciais estão faltando, permitindo que você crie um plano para adquiri-los antes que se tornem um bloqueio.
4.  **Promove a Criatividade:** A escassez de um recurso (ex: dinheiro) força o uso criativo de outros (ex: conhecimento, network) para atingir o mesmo objetivo.

---

## 🛠️ Como Aplicar

### **Passo 1: Crie o Documento**

No seu diretório de projeto (`PROJETOS/meu_projeto/`), crie o arquivo `02_RECURSOS.md`.

### **Passo 2: Inventário Completo**

Liste todos os recursos que você possui, divididos nas seguintes categorias:

-   **Tempo:** Quantas horas por semana/mês você pode dedicar? Qual a duração total do projeto?
-   **Financeiro:** Orçamento total, orçamento mensal, acesso a crédito, possíveis fontes de receita.
-   **Conhecimento/Skills:** O que você sabe fazer? Linguagens de programação, metodologias, design, marketing, etc. Seja específico sobre seu nível (básico, intermediário, avançado).
-   **Ferramentas/Infraestrutura:** Software, hardware, acesso a APIs, contas em serviços (AWS, Vercel, etc.).
-   **Pessoas/Network:** Quem você conhece que pode ajudar? Mentores, especialistas, ex-colegas, comunidades online.
-   **Ativos Existentes:** Projetos anteriores, código reutilizável, documentos, templates, reputação, marca pessoal.

### **Passo 3: Use o Template**

Copie e cole este template em seu arquivo `02_RECURSOS.md` e preencha-o.

```markdown
# Análise de Recursos - [Nome do Projeto]

**Versão:** 1.0
**Data:** [Data de criação]

---

## 1. Inventário de Recursos

### Tempo
-   **Disponibilidade Semanal:** [ex: 15 horas]
-   **Duração Total do Projeto:** [ex: 12 semanas]
-   **Total de Horas Disponíveis:** [ex: 180 horas]
-   **Flexibilidade:** [ex: Alta, posso trabalhar nos fins de semana se necessário]

### Financeiro
-   **Orçamento Total:** [ex: $2.000]
-   **Orçamento Mensal:** [ex: $500/mês]
-   **Fonte:** [ex: Recursos próprios]
-   **Custos Fixos Atuais:** [ex: $100/mês (infraestrutura existente)]

### Conhecimento/Skills
-   **Python (Avançado):** Mais de 5 anos de experiência, confortável com FastAPI.
-   **React (Intermediário):** Criei 3 projetos, mas não conheço as features do React 19.
-   **PostgreSQL (Básico):** Sei fazer CRUD, mas não tenho experiência com otimização.
-   **Metodologia ENDFIRST (Avançado):** Criador do método.

### Ferramentas/Infraestrutura
-   **Software:** Cursor AI, VS Code, Docker, Git.
-   **Contas:** Vercel Pro, Neon PostgreSQL (Free Tier), conta OpenAI com acesso à API Gemini.
-   **Hardware:** MacBook Pro M3 Max.

### Pessoas/Network
-   **Mentores:** [Nome do Mentor 1] (Especialista em Arquitetura), [Nome do Mentor 2] (Especialista em Marketing).
-   **Comunidades:** Acesso à comunidade de desenvolvedores X, Y, Z.
-   **Contatos:** [Nome do Contato 1] (Pode ajudar com design), [Nome do Contato 2] (Pode testar o beta).

### Ativos Existentes
-   **Código:** Biblioteca de componentes React reutilizáveis de projeto anterior.
-   **Documentação:** Especificação técnica do @google_Store v2.0.
-   **Marca:** Blog no Medium com 500+ seguidores.

---

## 2. Análise de Gaps de Recursos

*Cruze os **Obstáculos Críticos** (do Pilar 1) com seu inventário de recursos para identificar os gaps mais importantes.*

| Obstáculo Crítico | Recurso Necessário | Recurso Disponível? | Gap | Plano de Aquisição/Mitigação |
|---|---|---|---|---|
| **Falta de Experiência com Temporal** | Conhecimento em Temporal | ❌ Não | **Alto** | **Plano:** Dedicar 20h (2 semanas) para fazer um curso online e criar um PoC. |
| **Custo da API Gemini** | Orçamento ou Otimização | ⚠️ Parcial | **Médio** | **Plano:** Implementar caching agressivo (usando Dragonfly) e criar um dashboard de monitoramento de custos desde o MVP. |
| **Disponibilidade Limitada** | Mais tempo ou escopo menor | ❌ Não | **Crítico** | **Plano:** Este gap será tratado no Pilar 3 (Calibração), provavelmente reduzindo o escopo do MVP. |
| [...] | ... | ... | ... | ... |

---

## 3. Resumo dos Gaps Críticos

*Liste os 2-3 gaps de recursos mais perigosos para o projeto.*

### 1. Gap de Tempo
> O gap entre o tempo necessário (estimado) e o tempo disponível é o maior risco. A única solução é reduzir o escopo ou estender o prazo.

### 2. Gap de Conhecimento em Orquestração
> A falta de conhecimento em Temporal pode atrasar significativamente a Fase 2. O plano de capacitação é essencial para mitigar este risco.
```

---

## ✅ Checklist de Qualidade do Pilar 2

- [ ] Você foi honesto e detalhado sobre seus recursos?
- [ ] Você considerou recursos além do dinheiro (tempo, conhecimento, network)?
- [ ] A análise de gaps está diretamente ligada aos obstáculos críticos do Pilar 1?
- [ ] Para cada gap crítico, você tem um plano de aquisição ou mitigação claro?
- [ ] Você se sente mais confiante e preparado após este exercício?

---

## 🔗 Relação com Outros Pilares

-   **Pilar 1 (Obstáculos):** A análise de gaps só é eficaz se for baseada nos obstáculos reais do projeto.
-   **Pilar 3 (Calibração):** Este pilar é o segundo grande insumo para a calibração. A comparação `Obstáculos vs Recursos` é o coração do Pilar 3.
-   **Pilar 4 (Caminho Reverso):** O plano de aquisição de recursos (ex: aprender uma nova skill) se torna um dos primeiros marcos no seu caminho reverso.

---

## 🎓 Exemplo no Projeto @google_Store

No projeto, um gap de conhecimento identificado foi a falta de experiência com ferramentas de orquestração complexas como Temporal. O plano de mitigação foi usar uma solução mais simples (BullMQ) no MVP e dedicar tempo para aprender Temporal apenas na Fase 2, quando o requisito se tornaria crítico. Isso é um exemplo perfeito de uso inteligente de recursos.

**Veja o caso de uso completo em:** `contexto/casos_uso/CASO_USO_GOOGLE_STORE.md`

---

## 🎓 Exemplo Prático de Análise de Gaps

| Recurso Necessário | Disponível? | Gap | Plano de Aquisição |
|---|---|---|---|
| Conhecimento em Temporal | ❌ | Alto | Fazer o curso "Temporal 101" (2 semanas) |
| Orçamento para API Gemini | 🟡 Parcial | Médio | Implementar um sistema de cache (Dragonfly) para reduzir chamadas à API |
| Especialista em Marketing | ❌ | Alto | Contratar um freelancer por 5h/semana na fase de lançamento |
| Tempo de desenvolvimento | 🟡 Parcial | Médio | Reduzir o escopo do MVP (Pilar 3) para caber nas 10h/semana disponíveis |

---

**Próximo Passo:** Com uma visão clara de seus obstáculos e recursos, você está pronto para o momento da verdade: **[Pilar 3: Calibração com a Realidade](PILAR_3_CALIBRACAO.md)**. 🚀
