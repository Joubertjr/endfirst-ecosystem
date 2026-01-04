# 🚀 Pilar 6: Execução e Monitoramento

**Versão:** 1.0
**Data:** 19 de Dezembro de 2025

---

## ❓ O Que É?

O **Pilar 6** é onde o planejamento encontra a ação. É o processo de transformar seu plano validado e detalhado em realidade, de forma iterativa e controlada. Não se trata de seguir o plano cegamente, mas de usá-lo como um mapa, ajustando a rota conforme necessário, sem nunca perder de vista o destino (o Estado Final).

**Princípio Fundamental:**
> "Um plano não é nada sem execução. A execução não é nada sem monitoramento. O sucesso está na dança entre seguir o plano e adaptar-se à realidade do caminho."

---

## 🧠 Por Que Funciona?

1.  **Foco na Entrega de Valor:** A execução é dividida em sprints ou iterações curtas, cada uma com um objetivo claro derivado do roadmap (Pilar 4.5). Isso garante que você esteja sempre trabalhando na coisa mais importante.
2.  **Cria um Ciclo de Feedback Rápido:** O monitoramento constante permite que você identifique desvios do plano rapidamente, possibilitando correções de curso ágeis antes que pequenos problemas se tornem grandes crises.
3.  **Mantém a Motivação:** Ver o progresso tangível a cada semana ou quinzena, através de dashboards e entregas, é um poderoso motivador para você e sua equipe.
4.  **Promove a Responsabilidade:** Um plano de execução claro, com tarefas, responsáveis e prazos, cria um ambiente de responsabilidade e transparência.

---

## 🛠️ Como Aplicar

### **Passo 1: Crie o Documento**

No seu diretório de projeto (`PROJETOS/meu_projeto/`), crie o arquivo `06_EXECUCAO.md`. Este será um documento vivo, que você atualizará semanalmente.

### **Passo 2: Quebre os Marcos em Tarefas**

Pegue o primeiro marco do seu roadmap (o MVP) e quebre-o em tarefas menores e acionáveis. Use uma ferramenta de gestão de projetos (Trello, Jira, Notion, ou mesmo um simples arquivo Markdown) para criar seu backlog.

### **Passo 3: Planeje seus Sprints**

Agrupe as tarefas em Sprints, que são blocos de tempo fixos (geralmente 1 ou 2 semanas). Para cada sprint, defina um objetivo claro.

**Exemplo:**
-   **Sprint 1 (2 semanas):** Objetivo: Implementar o RF-01 (Upload de Documentos) de ponta a ponta.
-   **Sprint 2 (2 semanas):** Objetivo: Implementar o RF-02 (Busca Semântica) e integrá-lo com a API Gemini.

### **Passo 4: Monitore o Progresso**

Defina um dia da semana para sua "Reunião de Monitoramento" (mesmo que seja só com você mesmo). Nesta reunião, atualize seu dashboard de progresso e seu log de decisões.

-   **Dashboard de Progresso:** Uma visão de alto nível de como você está em relação aos marcos.
-   **Log de Decisões:** Um registro de todas as decisões importantes tomadas durante a execução (ex: mudar uma biblioteca, alterar um endpoint de API).

### **Passo 5: Use o Template**

Copie e cole este template em seu arquivo `06_EXECUCAO.md` e mantenha-o atualizado.

```markdown
# Execução e Monitoramento - [Nome do Projeto]

**Versão:** [Atualize a cada semana, ex: Semana 3]
**Data:** [Data da atualização]

---

## 1. Dashboard de Progresso

*Visão de alto nível do andamento do projeto em relação aos marcos do Pilar 4.5.*

| Marco | Status | % Completo | Prazo Original | Prazo Estimado | Risco |
|---|---|---|---|---|---|
| **MVP** | 🚧 Em Andamento | 40% | 10 semanas | 11 semanas | 🟡 Médio |
| **Beta** | 📝 A Fazer | 0% | 22 semanas | 23 semanas | 🟢 Baixo |
| **Produção** | 📝 A Fazer | 0% | 38+ semanas | 39+ semanas | 🟢 Baixo |

**Comentário:** *O MVP está com um atraso estimado de 1 semana devido a uma complexidade inesperada na integração com a API de backup. O risco é médio, pois pode ser absorvido na folga do cronograma.*

---

## 2. Plano de Sprints (Fase Atual: MVP)

### Sprint 2 (Semana 3-4)

-   **Objetivo:** Implementar RF-02 (Busca Semântica) e integrá-lo com a API Gemini.
-   **Status:** 🚧 Em Andamento

| Tarefa | Responsável | Status | Link (PR, Task) |
|---|---|---|---|
| Criar endpoint da API de busca | Eu | ✅ Concluído | [#12](link) |
| Integrar com a API Gemini | Eu | 🚧 Em Andamento | [#14](link) |
| Criar UI da página de busca | Eu | 📝 A Fazer | [#15](link) |
| Escrever testes de integração | Eu | 📝 A Fazer | [#16](link) |

---

### Sprint 1 (Semana 1-2)

-   **Objetivo:** Implementar RF-01 (Upload de Documentos) de ponta a ponta.
-   **Status:** ✅ Concluído
-   **Retrospectiva Rápida:** *A implementação foi mais rápida que o esperado, mas os testes demoraram mais. Precisamos alocar mais tempo para testes no próximo sprint.*

---

## 3. Log de Decisões e Mudanças

*Registre todas as decisões técnicas e de produto importantes tomadas durante a execução.*

### Decisão #003: Mudar de Redis para Dragonfly

-   **Data:** 20/Dez/2025
-   **Contexto:** Durante os testes de carga do PoC, a latência do Redis começou a aumentar com múltiplas conexões.
-   **Decisão:** Migrar para Dragonfly, que é compatível com a API do Redis, mas oferece melhor performance multi-thread.
-   **Impacto:** +2 dias de setup na Fase 2, mas garante a escalabilidade futura.
-   **Alternativas Consideradas:** Otimizar o Redis (muito complexo), usar um serviço gerenciado mais caro (fora do orçamento).

### Decisão #002: [...]

### Decisão #001: [...]

---

## 4. Métricas Chave (KPIs)

*Monitore as métricas mais importantes para a fase atual.*

| Métrica | Valor Atual | Meta (MVP) | Status |
|---|---|---|---|
| Custo Acumulado | $45 | < $800 | 🟢 OK |
| Bugs Críticos Abertos | 1 | 0 | 🟡 Atenção |
| Cobertura de Testes | 65% | > 80% | 🟡 Atenção |
```

---

## ✅ Checklist de Qualidade do Pilar 6

- [ ] Você tem um backlog de tarefas claro para a fase atual?
- [ ] Você está trabalhando em sprints com objetivos definidos?
- [ ] Você está atualizando seu dashboard de progresso semanalmente?
- [ ] Todas as decisões importantes estão sendo registradas no Log de Decisões?
- [ ] Você está monitorando as métricas chave e agindo sobre os desvios?

---

## 🔗 Relação com Outros Pilares

-   **Pilar 4.5 (Roadmap):** É a fonte de verdade para o planejamento dos sprints e do backlog.
-   **Pilar 7 (Aprendizagem):** O Log de Decisões e as retrospectivas dos sprints são insumos valiosos para o Pilar 7. Cada decisão é um aprendizado em potencial.
-   **Pilar 0 (Estado Final):** Durante a execução, continue se perguntando: "Esta tarefa me aproxima do Estado Final?". Se a resposta for não, questione sua prioridade.

---

## 🎓 Exemplo no Projeto @google_Store

O roadmap do @google_Store definiu o MVP com 5 RFs. Na execução, isso foi quebrado em sprints de 2 semanas. No final do Sprint 1, a retrospectiva mostrou que a documentação da API do Google File Search estava desatualizada, causando um pequeno atraso. Essa informação foi registrada e o cronograma do Sprint 2 foi ajustado. Isso é o monitoramento em ação: identificar e reagir a desvios rapidamente.

**Veja o caso de uso completo em:** `contexto/casos_uso/CASO_USO_GOOGLE_STORE.md`

---

## 🆕 Definition of Done (DoD) (NOVO v10.8)

**Objetivo:** Corrigir a **Causa Raiz #3 (Ausência de um Contrato de Entrega)**.

Antes de iniciar a execução, é crucial definir o que significa "pronto". O **Definition of Done (DoD)** é um checklist que serve como um contrato claro entre o executor e o cliente (ou validador), garantindo que as expectativas estejam alinhadas. Ele deve ser criado com base no **Mapa de Conhecimento (Pilar 0.5)**.

### Template de Definition of Done (DoD)

```markdown
# Definition of Done (DoD) - [Nome do Projeto]

## Critérios de Entrega do Pacote Final

### 1. Documentação do Método
- [ ] Todos os pilares (0 a 7) estão documentados em arquivos separados.
- [ ] Cada pilar contém: conceito, justificativa, passo a passo, template, exemplo e checklist.
- [ ] O Pilar 0.5 (Mapa de Conhecimento) foi preenchido.

### 2. Captura de Conhecimento
- [ ] O documento `REFERENCIAS_E_FUNDAMENTOS.md` está completo.
- [ ] O documento `HISTORICO_COMPLETO.md` está completo.
- [ ] O documento `DECISOES_E_JUSTIFICATIVAS.md` está completo.
- [ ] O documento `APRENDIZADOS_ACUMULADOS.md` está completo.

### 3. Artefatos do Projeto
- [ ] As especificações técnicas estão completas.
- [ ] O código-fonte está funcional e testado.
- [ ] Os guias de usuário estão claros e completos.

### 4. Validação
- [ ] O pacote passou pela Validação de Completude (Pilar 5).
- [ ] Todos os itens do Mapa de Conhecimento (Pilar 0.5) foram entregues.
```

---

## 🎓 Exemplo Prático de Log de Decisões

### **Decisão #004: Mudar de Redis para Dragonfly**

- **Data:** 15/12/2025
- **Contexto:** Durante os testes de carga do MVP, a latência do cache com Redis estava acima de 50ms sob carga pesada.
- **Decisão:** Migrar a camada de cache de Redis para Dragonfly.
- **Justificativa:** Dragonfly oferece performance até 25x superior a Redis com a mesma API, resolvendo o problema de latência sem reescrever o código.
- **Alternativas Consideradas:** Otimizar o Redis (muito complexo), usar Memcached (API diferente).
- **Consequências:** Aumento de 2 dias no cronograma para migração e testes.

---

**Próximo Passo:** A execução gera dados e experiências. É hora de transformar isso em conhecimento duradouro com o **[Pilar 7: Aprendizagem Contínua](PILAR_7_APRENDIZAGEM.md)**. 🚀
