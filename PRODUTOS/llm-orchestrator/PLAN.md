# Plano de Execução - DEMANDA-001: LLM Orchestrator

**Documento:** PLAN.md  
**Demanda:** DEMANDA-001_LLM_ORCHESTRATOR  
**Spec:** ENDFIRST_SPEC_EF-2026-001  
**Executor:** Cursor  
**Status:** ⚠️ Ajustado conforme feedback CEO - Aguardando autorização para início

---

## Confirmação de Leitura dos Documentos

✅ **Documentos lidos na ordem obrigatória:**
1. `/METODO/EXECUTOR_ONBOARDING_PROCESS.md` - Processo de onboarding compreendido
2. `/METODO/EXECUTION_MODEL.md` - Papéis e responsabilidades compreendidos
3. `/DEMANDAS/DEMANDA-001_LLM_ORCHESTRATOR.md` - Demanda compreendida
4. `/METODO/examples/ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md` - Spec validada compreendida
5. `/DEMANDAS/DEMANDA-001_ACCEPTANCE.md` - Critérios de aceitação final compreendidos

**Princípios fundamentais internalizados:**
- Git é fonte única de verdade
- Executor executa, não decide
- Entrega via commit estruturado e push
- Sem contexto humano, sem END fora do Git

---

## Decisões Técnicas Críticas (Antes de Codar)

### Stack Tecnológica Escolhida: **Electron + React + TypeScript**

**Decisão:** Electron + React + TypeScript  
**Razão:** Menor atrito + entrega mais rápida dos critérios
- Ecosistema maduro para desenvolvimento desktop macOS
- Grande quantidade de bibliotecas para APIs HTTP
- Facilidade de integração com múltiplas APIs
- Desenvolvimento rápido com componentes React
- TypeScript para type safety com múltiplas APIs

**Timebox:** Máximo 2-4 horas para setup inicial (Incremento 1)  
**Regra CEO:** Se escolha de stack virar projeto dentro do projeto, já começamos errado.

---

### Providers de LLM Identificados (Resolvendo Ambiguidade "Manus")

**Status:** ⚠️ Ambiguidade identificada e resolvida

**Providers Reais com APIs Documentadas:**
1. **ChatGPT** (OpenAI API)
   - Endpoint: `https://api.openai.com/v1/chat/completions`
   - Documentação: https://platform.openai.com/docs/api-reference
   - Autenticação: Bearer token (API key)

2. **Gemini** (Google Gemini API)
   - Endpoint: `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent`
   - Documentação: https://ai.google.dev/docs
   - Autenticação: API key

3. **Claude** (Anthropic API)
   - Endpoint: `https://api.anthropic.com/v1/messages`
   - Documentação: https://docs.anthropic.com/claude/reference
   - Autenticação: x-api-key header

4. **Manus - RESOLVIDO:**
   - **Problema:** "Manus" é o nome do Chefe de Produto (agente), não um provider de API
   - **Solução:** Iniciar com **3 providers reais** (ChatGPT, Gemini, Claude)
   - **4º slot:** Deixar como "Provider Custom" ou "Stub Provider" com contrato claro para extensão futura
   - **Impacto:** Validação cruzada funcionará com 3 LLMs inicialmente; ordem de rotação ajustada

**Ordem de Validação Cruzada (Ajustada para 3 providers):**
- ChatGPT selecionado → Gemini → Claude → (loop)
- Gemini selecionado → Claude → ChatGPT → (loop)
- Claude selecionado → ChatGPT → Gemini → (loop)

**Nota:** Se necessário adicionar 4º provider real no futuro, será extensão simples graças à arquitetura modular.

---

## Incrementos de Execução

### INCREMENTO 1: Setup Inicial e Fundação (Timebox: 2-4 horas)
**Objetivo:** Configurar projeto Electron+React+TypeScript e estrutura base

**Ações:**
- ✅ Decisão prévia: Electron + React + TypeScript (já decidido acima)
- Criar projeto Electron com React template
- Configurar TypeScript
- Estrutura de pastas básica:
  ```
  /PRODUTOS/llm-orchestrator/
  ├── src/
  │   ├── main/              # Processo principal Electron
  │   ├── renderer/          # React app
  │   │   ├── components/
  │   │   ├── services/
  │   │   └── utils/
  │   └── shared/            # Código compartilhado
  ├── package.json
  └── README.md
  ```
- Testar execução local no macOS
- Documentar stack escolhida no README.md

**Entregável:**
- Projeto Electron+React configurado
- Aplicativo roda localmente (janela Electron abre)
- README.md com instruções de setup e stack documentada

**Prova de Critério 7 (parcial):** Aplicativo abre e roda localmente no macOS

**Commit:** `feat(setup): configuração inicial Electron+React+TypeScript`

---

### INCREMENTO 2: Gerenciamento de APIs
**Objetivo:** Implementar cadastro e configuração de APIs (3 providers)

**Ações:**
- Criar interface de configuração de APIs
- Implementar armazenamento local de credenciais (electron-store - migrar para Keychain antes da aceitação final)
- Criar módulo de configuração para 3 providers:
  - OpenAI (ChatGPT)
  - Google Gemini
  - Anthropic (Claude)
- Validar formato de credenciais (não precisa validar conexão ainda)

**Entregável:**
- Interface de configuração funcional
- Credenciais salvas localmente (electron-store - migrar para Keychain antes da aceitação final do Critério 7)
- Módulo de configuração modular para adicionar providers

**Prova de Critério 7:** Interface de configuração funciona localmente, credenciais salvas no macOS

**Commit:** `feat(config): gerenciamento de APIs e credenciais`

---

### INCREMENTO 3: Envio Simultâneo para Múltiplas LLMs
**Objetivo:** Enviar prompt para 1-3 LLMs simultaneamente e receber respostas

**Ações:**
- Criar abstração de provider (interface comum)
- Implementar adaptadores:
  - OpenAIAdapter (ChatGPT)
  - GeminiAdapter (Google)
  - AnthropicAdapter (Claude)
- Implementar serviço de orquestração que envia requests paralelos
- Criar interface React: input de prompt e seleção de LLMs
- Implementar exibição de respostas recebidas
- Adicionar tratamento de erros básico

**Entregável:**
- Módulo de integração com 3 APIs funcionando
- Interface funcional: input de prompt + seleção de LLMs + exibição de respostas
- Abstração permite adicionar 4º provider facilmente
- Envio paralelo implementado

**Prova de Critério 1 (parcial):**
- ✅ Enviar prompt selecionando 1 LLM → receber 1 resposta
- ✅ Enviar prompt selecionando 2 LLMs → receber 2 respostas distintas
- ✅ Enviar prompt selecionando 3 LLMs → receber 3 respostas distintas
- ✅ Verificar que todas as respostas foram recebidas (sucesso ou erro)

**Checklist de Prova do Critério 1:**
```
[ ] 1. Configurar pelo menos 2 providers na aba Configuração
[ ] 2. Ir para aba Início
[ ] 3. Digitar um prompt de teste (ex: "Explique o que é TypeScript em 2 frases")
[ ] 4. Selecionar 1 LLM (checkbox)
[ ] 5. Clicar em "Enviar para 1 LLM"
[ ] 6. Verificar: 1 resposta aparece na seção "Respostas Recebidas"
[ ] 7. Repetir com 2 LLMs selecionadas
[ ] 8. Verificar: 2 respostas distintas aparecem
[ ] 9. Repetir com 3 LLMs selecionadas (se 3 estiverem configuradas)
[ ] 10. Verificar: 3 respostas distintas aparecem
[ ] 11. Verificar: Cada resposta mostra provider name e conteúdo diferente
[ ] 12. Verificar: Timestamps estão presentes
```

**Commit:** `feat(orchestration): INCREMENTO 3 - envio simultâneo para múltiplas LLMs`

---

### INCREMENTO 4: Comparação Visual Lado a Lado
**Objetivo:** Exibir respostas de múltiplas LLMs simultaneamente

**Ações:**
- Criar layout de grid/columns (3 colunas máximo inicialmente)
- Implementar componentes de visualização de resposta por LLM
- Adicionar headers identificando cada LLM (nome, logo, timestamp)
- Implementar scroll independente por resposta
- Ajustar responsividade

**Entregável:**
- Interface visual com múltiplas colunas funcionando
- Todas as respostas visíveis simultaneamente

**Prova de Critério 2:** Enviar prompt para 3 LLMs e verificar que 3 respostas são exibidas simultaneamente na tela

**Prova de Critério 1 (completo):** Enviar para 1, 2 e 3 LLMs e receber número correto de respostas

**Commit:** `feat(ui): comparação visual lado a lado de respostas`

---

### INCREMENTO 6: Seleção de Melhor Resposta
**Objetivo:** Permitir seleção manual de uma resposta como "melhor"

**Ações:**
- Implementar botão/clique para selecionar resposta
- Adicionar feedback visual (highlight, borda, checkmark)
- Deselecionar outras respostas quando uma é selecionada
- Armazenar qual resposta foi selecionada

**Entregável:**
- Seleção funcional com feedback visual claro

**Prova de Critério 3:** Clicar em resposta e verificar marcação visual (highlight/borda/checkmark)

**Commit:** `feat(ui): seleção de melhor resposta com feedback visual`

---

### INCREMENTO 7: Validação Cruzada Automatizada
**Objetivo:** Iniciar validação cruzada automaticamente quando resposta é selecionada

**Ações:**
- Implementar lógica de ordem de validação (ajustada para 3 providers):
  - ChatGPT → Gemini → Claude
  - Gemini → Claude → ChatGPT
  - Claude → ChatGPT → Gemini
- Criar interface de visualização do fluxo de validação
- Implementar envio automático da resposta selecionada para próxima LLM
- Exibir respostas de validação em área dedicada ou sequencial

**Entregável:**
- Fluxo de validação cruzada automatizado
- Interface de progresso/status

**Prova de Critério 4:** Selecionar resposta e verificar que validação inicia automaticamente

**Prova de Critério 5:** Selecionar cada uma das 3 LLMs e verificar ordem correta de validação

**Commit:** `feat(cross-validation): validação cruzada automatizada com ordem configurável`

---

### INCREMENTO 8: Preservação de Contexto
**Objetivo:** Manter histórico de prompts e respostas durante refinamentos

**Ações:**
- Criar estrutura de contexto (histórico de mensagens)
- Implementar gerenciamento de contexto incluindo:
  - Prompt original
  - Todas as respostas iniciais
  - Resposta selecionada
  - Histórico de validações cruzadas
- Enviar contexto completo para cada LLM na sequência
- Criar interface para visualizar histórico
- Implementar limite de tokens com resumo automático se necessário

**Entregável:**
- Sistema de gerenciamento de contexto completo
- Histórico preservado durante todo o fluxo
- Interface de visualização de histórico

**Prova de Critério 6:** Executar 3 rodadas de validação e verificar que cada LLM recebe contexto completo (prompt + resposta selecionada + histórico)

**Commit:** `feat(context): preservação de contexto durante refinamentos iterativos`

---

### INCREMENTO 9: Polimento e Validação Final
**Objetivo:** Garantir qualidade e aderência completa aos critérios

**Ações:**
- Testar todos os fluxos end-to-end
- Corrigir bugs encontrados
- Melhorar UX/UI baseado em uso real
- Adicionar tratamento de erros robusto
- Otimizar performance
- Validar todos os 7 critérios de aceitação

**Entregável:**
- Sistema completo e funcional
- Todos os 7 critérios passando
- Tratamento de erros implementado

**Prova de Todos os Critérios:** Executar checklist completo

**Commit:** `feat(polish): validação final e tratamento de erros`

---

## Como Cada Critério Será Provado

### Critério 1: Envio para 1-4 LLMs simultaneamente
**Status:** Ajustado para 1-3 LLMs (3 providers reais)  
**Prova:** 
- Enviar prompt selecionando 1 LLM → receber 1 resposta
- Enviar prompt selecionando 2 LLMs → receber 2 respostas
- Enviar prompt selecionando 3 LLMs → receber 3 respostas
- Verificar que todas as respostas são distintas e completas

**Incremento:** 4 (parcial), 5 (completo)

---

### Critério 2: Respostas lado a lado
**Prova:** 
- Enviar prompt para 3 LLMs
- Verificar que 3 respostas são exibidas simultaneamente na tela
- Verificar que todas são visíveis sem scroll horizontal excessivo
- Verificar identificação clara de cada LLM (nome/logo)

**Incremento:** 5

---

### Critério 3: Seleção de melhor resposta
**Prova:** 
- Clicar em uma resposta
- Verificar marcação visual imediata (highlight/borda/checkmark)
- Verificar que outras respostas perdem seleção
- Clicar em outra resposta e verificar que seleção muda

**Incremento:** 6

---

### Critério 4: Validação cruzada automática
**Prova:** 
- Selecionar uma resposta
- Verificar que validação cruzada inicia automaticamente (sem clique adicional)
- Verificar que interface mostra progresso/fluxo de validação
- Verificar que primeira LLM da ordem recebe a resposta

**Incremento:** 7

---

### Critério 5: Ordem baseada na LLM inicial
**Status:** Ajustado para 3 providers  
**Prova:** 
- Selecionar resposta do ChatGPT → verificar ordem: Gemini → Claude
- Selecionar resposta do Gemini → verificar ordem: Claude → ChatGPT
- Selecionar resposta do Claude → verificar ordem: ChatGPT → Gemini
- Verificar que ordem é seguida exatamente

**Incremento:** 7

---

### Critério 6: Contexto preservado
**Prova:** 
- Enviar prompt inicial
- Selecionar melhor resposta
- Executar 3 rodadas de validação cruzada
- Para cada LLM na sequência, inspecionar payload enviado e verificar:
  - Prompt original está presente
  - Resposta selecionada está presente
  - Histórico de validações anteriores está presente
- Verificar na interface que histórico completo é visível

**Incremento:** 8

---

### Critério 7: Sistema roda localmente no macOS
**Prova:** 
- Executar aplicativo sem servidor externo (exceto APIs de LLMs)
- Verificar que interface funciona offline (sem chamadas para backend próprio)
- Verificar que credenciais são salvas localmente (inspecionar keychain/storage)
- Verificar que aplicativo funciona sem conexão com internet para UI
- Verificar que aplicativo só faz chamadas diretas para APIs de LLMs

**Incrementos:** 1 (parcial), 2 (parcial), 9 (completo)

---

## Regra de Ouro de Execução

Cada incremento só "existe" se terminar com:
- ✅ Algo rodando local
- ✅ Prova de pelo menos 1 critério (ou parte do critério)
- ✅ Commit + push

---

## Estrutura de Arquivos

```
/PRODUTOS/llm-orchestrator/
├── PLAN.md                    # Este arquivo (plano de execução)
├── README.md                  # Documentação: stack, providers, como rodar
├── package.json               # Dependências Node.js
├── src/
│   ├── main/                  # Processo principal Electron
│   │   ├── main.ts
│   │   └── preload.ts
│   ├── renderer/              # React app
│   │   ├── App.tsx
│   │   ├── components/
│   │   │   ├── PromptInput.tsx
│   │   │   ├── LLMSelector.tsx
│   │   │   ├── ResponsePanel.tsx
│   │   │   └── CrossValidationFlow.tsx
│   │   ├── services/
│   │   │   ├── orchestration.ts
│   │   │   ├── providers/
│   │   │   │   ├── base.ts
│   │   │   │   ├── openai.ts
│   │   │   │   ├── gemini.ts
│   │   │   │   └── anthropic.ts
│   │   │   └── context.ts
│   │   └── utils/
│   └── shared/
│       └── types.ts
└── tests/                     # Testes (se necessário)
```

---

## Riscos e Mitigações

**Risco 1:** APIs com formatos/rate limits diferentes  
**Mitigação:** Abstração de provider (base.ts) + adaptadores específicos

**Risco 2:** Performance com 3 chamadas simultâneas  
**Mitigação:** Timeout configurável, tratamento assíncrono, otimizar se necessário

**Risco 3:** Limite de tokens no contexto  
**Mitigação:** Resumo automático ou truncamento inteligente do histórico

**Risco 4:** Ambiguidade "Manus API"  
**Mitigação:** ✅ RESOLVIDO - Iniciar com 3 providers reais, deixar 4º slot como extensão futura

---

## Notas Importantes

- ⚠️ **Não alterar** documentos em `/METODO/` ou `/DEMANDAS/`
- ✅ **Criar código** apenas em `/PRODUTOS/llm-orchestrator/`
- ✅ **Commits estruturados** seguindo formato: `tipo: descrição`
- ✅ **Entrega via Git** - fazer push após cada incremento funcional
- ✅ **Sem perguntas** - executar conforme spec, não reinterpretar
- ✅ **Timebox rígido** - Incremento 1 máximo 4 horas
- ✅ **Providers claros** - 3 providers reais identificados, sem ambiguidade

---

**Status do Plano:** ✅ Ajustado conforme feedback CEO  
**Próximo passo:** Aguardar autorização para iniciar Incremento 1

