# Pilar 0.5: Validação Incremental - O Sistema Imune a Erros

**Posição:** Entre Pilar 0 (Seleção Dinâmica) e Pilar 1 (Identidade)

**Problema que resolve:** A tendência de um sistema (ou agente) de entrar em "modo execução" e se desviar do objetivo do cliente por falta de feedback contínuo.

---

## O Que É?

A Validação Incremental é um **mecanismo de controle de qualidade obrigatório** que força o sistema a pausar e sincronizar com o cliente em checkpoints predefinidos. Não é uma "boa prática" ou uma "sugestão", mas uma **regra não negociável do método**.

Sua função é garantir que o que está sendo construído é **exatamente** o que o cliente quer, em todas as fases do processo.

---

## Por Que é Crítico?

Sem este pilar, o sistema depende da "disciplina" do agente para lembrar de validar. Isso é uma falha de design. A Validação Incremental remove a decisão do agente e a transforma em uma **regra automática do sistema**.

> **Analogia:** É o checklist de decolagem de um avião. O piloto não "decide" se vai usá-lo; ele é obrigado a seguir o checklist para garantir a segurança. Da mesma forma, o agente não "decide" se vai validar; o método o obriga a validar para garantir a qualidade e o alinhamento.

---

## Como Funciona: Regras e Gatilhos

A Validação Incremental opera com base em um sistema de **gatilhos automáticos**. Se uma condição é atendida, uma ação de validação é **obrigatoriamente** disparada.

| Gatilho (Condição) | Ação Obrigatória |
| :--- | :--- |
| **Início de Deliverable Grande** (>1.000 palavras ou >30 min de trabalho) | 1. Criar estrutura/outline.<br>2. **PAUSAR** e validar com o cliente.<br>3. Só continuar após aprovação. |
| **Progresso de Deliverable** (a cada 30-50% concluído) | 1. Apresentar o progresso parcial.<br>2. **PAUSAR** e pedir feedback.<br>3. Ajustar se necessário. |
| **Antes de Finalizar** (99% concluído) | 1. Apresentar o rascunho final.<br>2. **PAUSAR** para aprovação final.<br>3. Não marcar como "pronto" sem o "OK" do cliente. |
| **Feedback do Cliente** (a qualquer momento) | 1. **PAUSAR** todas as outras tarefas.<br>2. Analisar o feedback.<br>3. Ajustar o plano ou o método (Pilar 7).<br>4. Re-validar o ajuste. |

---

## O Fluxo de Trabalho Obrigatório

Isso transforma o fluxo de trabalho de um processo linear para um ciclo iterativo:

1.  **CRIAR ESTRUTURA**
2.  **VALIDAR ESTRUTURA (Checkpoint 1)**
3.  **ESCREVER 30-50%**
4.  **VALIDAR RASCUNHO PARCIAL (Checkpoint 2)**
5.  **COMPLETAR RASCUNHO**
6.  **VALIDAR RASCUNHO FINAL (Checkpoint 3)**
7.  **ENTREGAR VERSÃO FINAL**

Cada etapa de validação é um **portão de qualidade**. O processo não avança para a próxima etapa sem a aprovação explícita do cliente.

---

## Conclusão: De "Confie em Mim" para "Verifique Comigo"

O Pilar 0.5 muda a filosofia do sistema de:

- **Errado:** "Confie em mim, eu sei o que estou fazendo e vou te entregar algo ótimo no final."
- **Certo:** "Verifique comigo a cada passo, para que o que eu construa seja exatamente o que você precisa."

Ele garante que o cliente (o Agente Externo principal) esteja sempre no controle, transformando o processo de criação em uma verdadeira colaboração e tornando grandes desvios de rota impossíveis.
