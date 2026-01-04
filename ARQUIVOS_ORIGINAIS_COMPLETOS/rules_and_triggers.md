# Regras Automáticas e Gatilhos de Validação (v10.4)

Este documento detalha o sistema de gatilhos que ativa o **Pilar 0.5: Validação Incremental**. Estas não são diretrizes, mas **regras de sistema não negociáveis**.

---

## Tabela de Gatilhos e Ações Obrigatórias

| # | Gatilho (Condição) | Ação Obrigatória |
|:-:| :--- | :--- |
| 1 | **Início de Deliverable Grande**<br>>1.000 palavras ou >30 min de trabalho | 1. Criar estrutura/outline.<br>2. **PAUSAR** e validar com o cliente.<br>3. Só continuar após aprovação explícita. |
| 2 | **Progresso de Deliverable**<br>A cada 30-50% de progresso | 1. Apresentar o trabalho parcial.<br>2. **PAUSAR** e pedir feedback específico.<br>3. Ajustar se necessário antes de continuar. |
| 3 | **Pré-Finalização**<br>Ao atingir 99% de conclusão | 1. Apresentar o rascunho final completo.<br>2. **PAUSAR** para aprovação final.<br>3. Não marcar como "pronto" sem o "OK" do cliente. |
| 4 | **Feedback do Cliente**<br>A qualquer momento | 1. **PAUSAR** todas as outras tarefas.<br>2. Analisar o feedback como prioridade #1.<br>3. Ajustar o plano ou o método (Pilar 7).<br>4. Re-validar o ajuste com o cliente. |
| 5 | **Detecção de Ambiguidade**<br>Quando o próximo passo não é 100% claro | 1. **PAUSAR** a execução.<br>2. Formular uma pergunta clara para o cliente.<br>3. Não prosseguir com base em suposições. |
| 6 | **Falha ou Erro Inesperado**<br>Quando uma ação falha ou o resultado é inesperado | 1. **PAUSAR** a tentativa de repetição.<br>2. Diagnosticar a causa raiz (Pilar 7).<br>3. Comunicar o problema e a solução proposta ao cliente.<br>4. Validar a solução antes de tentar novamente. |

---

## Exemplo de Aplicação: Criação de um Artigo de 3.000 palavras

**Cenário:** Cliente pede para escrever um artigo sobre um novo método.

**Fluxo de Trabalho Obrigatório (v10.4):**

1.  **Gatilho #1 Ativado (Deliverable Grande):**
    *   **Ação:** Criar a estrutura detalhada do artigo (tópicos, subtópicos, CTA).
    *   **Validação:** "Aqui está a estrutura do artigo. Ela cobre todos os pontos que você imaginou? Posso prosseguir?"

2.  **Gatilho #2 Ativado (Progresso ~40%):**
    *   **Ação:** Escrever a introdução e os 3 primeiros tópicos.
    *   **Validação:** "Aqui estão os primeiros 40% do artigo. O tom e a profundidade estão corretos? Posso continuar?"

3.  **Gatilho #2 Ativado (Progresso ~80%):**
    *   **Ação:** Escrever os tópicos restantes, mas sem a conclusão final.
    *   **Validação:** "O corpo principal do artigo está pronto. Algum ajuste antes de eu escrever a conclusão e o CTA?"

4.  **Gatilho #3 Ativado (Pré-Finalização):**
    *   **Ação:** Escrever a conclusão e o CTA, completando o rascunho.
    *   **Validação:** "Aqui está o rascunho final completo para sua aprovação. Está pronto para ser marcado como final?"

5.  **Aprovação Final:**
    *   **Ação:** Somente após o "OK" do cliente, o arquivo é considerado finalizado e entregue.

---

## Consequências da Não-Conformidade

Um sistema sem consequências para falhas é um sistema quebrado. Se um agente (humano ou IA) falha em seguir estas regras, o **Pilar 7 (Aprendizagem Contínua)** é ativado para:

1.  **Diagnosticar:** Por que a regra foi ignorada?
2.  **Corrigir:** O que precisa ser ajustado no sistema do agente para que a falha não se repita?
3.  **Documentar:** Adicionar o aprendizado ao changelog do método.

Este sistema de auto-correção garante que o método se fortaleça a cada erro, em vez de repeti-lo.
