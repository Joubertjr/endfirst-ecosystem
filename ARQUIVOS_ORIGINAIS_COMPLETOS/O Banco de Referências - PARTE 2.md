# O Banco de Referências - PARTE 2

**Status:** Rascunho - Checkpoint 2 (66%)

---

## 3. Critérios de Aplicabilidade

### 3.1 Quando Implementar um Banco de Referências

A implementação de um Banco de Referências é recomendada quando o projeto atende a pelo menos dois dos seguintes critérios:

| Critério | Descrição | Threshold |
| :--- | :--- | :--- |
| **Duração Temporal** | Projetos de longa duração onde o conhecimento acumulado ao longo do tempo é crítico. | > 2 semanas |
| **Multiplicidade de Agentes** | Projetos com múltiplos colaboradores (humanos ou IA) que precisam compartilhar contexto. | ≥ 2 agentes |
| **Complexidade Estrutural** | Projetos com múltiplos deliverables, fases interdependentes ou arquitetura modular. | ≥ 5 componentes principais |
| **Evolução Metodológica** | Projetos onde o método, framework ou abordagem evolui continuamente. | ≥ 3 versões do método |
| **Dependência de Histórico** | Projetos onde decisões futuras dependem fortemente do histórico de decisões passadas. | Alta dependência |
| **Rotatividade de Agentes** | Projetos onde agentes entram e saem frequentemente, exigindo onboarding rápido. | > 20% de rotatividade |

### 3.2 Quando NÃO Implementar

A implementação de um Banco de Referências é desnecessária ou contraproducente nos seguintes cenários:

1. **Projetos Triviais:** Tarefas simples, de curta duração (< 2 dias), sem necessidade de documentação histórica.
2. **Projetos Descartáveis:** Protótipos ou experimentos onde o conhecimento não será reutilizado.
3. **Projetos com Contexto Estável:** Projetos onde o contexto, método e requisitos não mudam ao longo do tempo.
4. **Projetos Individuais de Curta Duração:** Trabalhos solo que serão concluídos em uma única sessão sem interrupções.

### 3.3 Matriz de Decisão

Para facilitar a decisão, utilize a seguinte matriz:

```
SCORE = (Duração × 1) + (Agentes × 2) + (Complexidade × 1.5) + (Evolução × 2) + (Histórico × 1) + (Rotatividade × 1.5)

SE SCORE ≥ 10 → Implementar Banco de Referências (Alta Prioridade)
SE 5 ≤ SCORE < 10 → Considerar Implementação (Média Prioridade)
SE SCORE < 5 → Não Implementar (Baixa Prioridade)
```

**Exemplo de Cálculo (Projeto ENDFIRST):**
- Duração: 6 meses = 6 pontos × 1 = **6**
- Agentes: 2 (humano + IA) = 2 × 2 = **4**
- Complexidade: 10 componentes = 10 × 1.5 = **15**
- Evolução: 10 versões do método = 10 × 2 = **20**
- Histórico: Alta dependência = 5 × 1 = **5**
- Rotatividade: 50% (IA muda de sessão) = 5 × 1.5 = **7.5**

**SCORE TOTAL = 57.5 → Alta Prioridade**

---

## 4. Requisitos de Implementação

### 4.1 Requisitos Funcionais

Uma implementação válida de um Banco de Referências DEVE atender aos seguintes requisitos funcionais, independentemente da tecnologia ou plataforma utilizada:

| ID | Requisito | Descrição | Critério de Validação |
| :--- | :--- | :--- | :--- |
| **RF-01** | **Centralização** | Deve existir um único repositório autoritativo para cada categoria de artefato. | Não há duplicatas ou versões conflitantes em locais diferentes. |
| **RF-02** | **Curadoria** | Deve incluir apenas artefatos validados e versões finais. Rascunhos e versões obsoletas devem ser excluídos ou marcados claramente. | Todos os artefatos possuem status explícito (final, rascunho, obsoleto). |
| **RF-03** | **Anotação** | Cada artefato deve possuir metadados descritivos: título, propósito, versão, data, autor, relevância. | É possível entender a função de um artefato sem abri-lo. |
| **RF-04** | **Acessibilidade Programática** | O banco deve ser consultável por agentes computacionais (IA, scripts) de forma automatizada. | Uma IA pode ler o índice e localizar artefatos sem intervenção humana. |
| **RF-05** | **Versionamento** | O banco (ou seus artefatos) deve rastrear mudanças ao longo do tempo. | É possível identificar o que mudou entre a versão N e N+1. |
| **RF-06** | **Indexação** | Deve existir um índice ou catálogo que liste todos os artefatos e suas localizações. | Um novo agente pode navegar pelo banco usando apenas o índice. |

### 4.2 Requisitos Não-Funcionais

Além dos requisitos funcionais, a implementação deve considerar os seguintes atributos de qualidade:

| ID | Atributo | Descrição | Métrica |
| :--- | :--- | :--- | :--- |
| **RNF-01** | **Escalabilidade** | O banco deve suportar crescimento contínuo sem degradação de desempenho. | Tempo de busca < 5s mesmo com 1.000+ artefatos. |
| **RNF-02** | **Manutenibilidade** | Deve ser fácil adicionar, atualizar ou remover artefatos. | Tempo para adicionar um novo artefato < 2 minutos. |
| **RNF-03** | **Portabilidade** | O banco deve ser independente de plataforma ou ferramenta específica. | Pode ser migrado entre sistemas sem perda de informação. |
| **RNF-04** | **Resiliência** | O banco deve ter backup ou redundância para prevenir perda de dados. | Recovery Point Objective (RPO) < 24 horas. |

### 4.3 Critérios de Validação da Implementação

Para validar se uma implementação atende aos requisitos, execute os seguintes testes:

**Teste 1: Teste de Onboarding**
- Um novo agente (humano ou IA) deve conseguir entender o estado do projeto em < 10 minutos consultando apenas o Banco de Referências.

**Teste 2: Teste de Localização**
- Um agente deve conseguir localizar qualquer artefato crítico em < 2 minutos usando o índice do banco.

**Teste 3: Teste de Consistência**
- Não deve haver conflitos de versão ou informações contraditórias entre artefatos do banco.

**Teste 4: Teste de Automação**
- Uma IA deve conseguir ler o índice e acessar artefatos sem intervenção humana.

---

**FIM DO CHECKPOINT 2 (Seções 3-4 concluídas)**
