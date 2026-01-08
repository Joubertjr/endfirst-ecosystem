# PROMPT PARA CURSOR — DEMANDA-001: LLM Orchestrator v1

**Versão:** 1.0  
**Data:** 7 de Janeiro de 2026  
**Tipo:** Contrato de Resultado (não solução)

---

## 🎯 OBJETIVO (RESULTADO ESPERADO)

Implementar aplicação desktop macOS que permite **validação cruzada de prompts com múltiplas LLMs**.

**Governado por:** ENDFIRST_SPEC_EF-2026-001 (VALIDADA pelo CEO em 07/01/2026)

**Referência canônica:** `/METODO/examples/ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md`

---

## 📋 RESULTADO ESTRUTURAL (5 VERDADES)

**No final, deve ser verdade que:**

1. ✅ Consigo enviar um prompt para múltiplas LLMs simultaneamente e receber respostas comparáveis
2. ✅ Consigo selecionar a melhor resposta entre as LLMs baseado em critério próprio
3. ✅ A resposta selecionada passa por validação cruzada de outras LLMs em ordem configurável
4. ✅ Reduzo erro e viés nas decisões baseadas em LLMs através de validação entre pares
5. ✅ Mantenho contexto preservado durante todo o fluxo de refinamento iterativo

---

## 🔒 CRITÉRIOS DE ACEITAÇÃO (VERIFICÁVEIS)

**A implementação só pode ser considerada DONE quando:**

- [ ] **Critério 1:** Consigo enviar um prompt para 1-4 LLMs simultaneamente
  - **Teste:** Enviar para 2 LLMs e receber 2 respostas

- [ ] **Critério 2:** Respostas são exibidas lado a lado em interface visual
  - **Teste:** Ver 4 respostas na tela ao mesmo tempo

- [ ] **Critério 3:** Consigo selecionar uma resposta como "melhor"
  - **Teste:** Clicar em resposta e ver marcação visual

- [ ] **Critério 4:** Resposta selecionada inicia validação cruzada automaticamente
  - **Teste:** Selecionar e ver fluxo de revisão

- [ ] **Critério 5:** Ordem de validação muda baseada na LLM inicial
  - **Teste:** Selecionar ChatGPT e verificar ordem Gemini→Manus→Claude

- [ ] **Critério 6:** Contexto é preservado durante refinamentos
  - **Teste:** Fazer 3 rodadas de revisão e verificar que contexto anterior está presente

- [ ] **Critério 7:** Sistema roda localmente no macOS
  - **Teste:** Abrir e usar sem conexão com servidor externo

---

## 🎯 ESCOPO (DENTRO/FORA)

### ✅ Dentro do escopo (DEVE implementar)

- ✔️ Envio de prompt para múltiplas LLMs (1-4) simultaneamente
- ✔️ Comparação visual de respostas lado a lado
- ✔️ Seleção de melhor resposta (manual)
- ✔️ Validação cruzada automatizada (ordem configurável)
- ✔️ Preservação de contexto durante refinamentos
- ✔️ Execução local (macOS)
- ✔️ Gerenciamento de APIs (cadastro, configuração)
- ✔️ Interface visual intuitiva
- ✔️ Suporte para 4 LLMs (ChatGPT, Gemini, Manus, Claude)

### ❌ Fora do escopo (NÃO DEVE implementar)

- ❌ Suporte para Windows ou Linux
- ❌ Mais de 4 LLMs na versão inicial
- ❌ Treinamento de modelos próprios
- ❌ Hospedagem em nuvem
- ❌ Compartilhamento de conversas entre usuários
- ❌ Integração com outras ferramentas (Notion, Slack, etc.)
- ❌ Análise estatística automática de qual LLM é "melhor"
- ❌ Seleção automática de melhor resposta
- ❌ Histórico persistente de conversas
- ❌ Controle automático de custos

---

## 🚫 ANTI-RESULTADOS (NÃO PODE ACONTECER)

**Mesmo se todos os critérios técnicos passarem, NÃO PODE:**

- ❌ Sistema funciona, mas usuário não confia nas respostas (falta transparência)
- ❌ Comparação existe, mas não ajuda a decidir (falta critério de seleção)
- ❌ Processo automatizado existe, mas ninguém usa (complexidade excessiva)
- ❌ Validação cruzada existe, mas adiciona mais confusão que clareza
- ❌ Sistema reduz erro de LLM, mas introduz erro de orquestração (bug no fluxo)

---

## 🟡 INCERTEZAS ACEITÁVEIS (DECISÕES PERMITIDAS)

### Incerteza 1: Stack tecnológico exato
- ✅ **OK:** Escolher entre Electron+React, SwiftUI ou Tauri baseado em teste rápido (< 2 dias)
- ❌ **NÃO OK:** Gastar mais de 2 dias decidindo stack sem prototipar

### Incerteza 2: UX/UI detalhado
- ✅ **OK:** Começar com wireframe simples e iterar baseado em uso real
- ❌ **NÃO OK:** Tentar criar interface "perfeita" antes de testar fluxo básico

### Incerteza 3: Gerenciamento de tokens/custos
- ✅ **OK:** Versão v1 não controla custos automaticamente, apenas alerta
- ❌ **NÃO OK:** Ignorar completamente (deve estar no roadmap futuro)

### Incerteza 4: Performance com 4 LLMs simultâneas
- ✅ **OK:** Testar com casos reais e otimizar se necessário
- ❌ **NÃO OK:** Assumir que vai funcionar sem testar

### Incerteza 5: Formato de armazenamento de configurações
- ✅ **OK:** Usar JSON simples no início e migrar depois se necessário
- ❌ **NÃO OK:** Criar banco de dados complexo antes de validar necessidade

### Incerteza 6: Critérios de seleção de "melhor resposta"
- ✅ **OK:** Começar com seleção manual e adicionar critérios depois baseado em uso
- ❌ **NÃO OK:** Tentar criar algoritmo de seleção automática antes de entender padrões

### Incerteza 7: Número de LLMs suportadas
- ✅ **OK:** Começar com 4 LLMs e adicionar depois
- ❌ **NÃO OK:** Tentar suportar todas as LLMs do mercado desde o início

---

## 🔗 DEPENDÊNCIAS

### Dependências técnicas:
- APIs de ChatGPT, Gemini, Manus e Claude ativas e acessíveis
- Credenciais/tokens de API configuradas e válidas
- macOS 12+ (sistema operacional)
- Conexão com internet (para chamadas de API)

### Dependências organizacionais:
- Orçamento para custos de APIs de LLMs
- Aprovação para uso de múltiplas LLMs (se necessário)

---

## 📖 ONTOLOGIA (TERMOS CRÍTICOS)

### "Validação cruzada"
Processo onde resposta selecionada é enviada para outras LLMs em ordem configurável para validação, refinamento e detecção de erro/viés.

### "Ordem configurável"
Sequência de LLMs que recebem a resposta para validação, determinada pela LLM inicial selecionada.

**Exemplo:**
- Se ChatGPT for selecionada → Ordem: Gemini → Manus → Claude
- Se Gemini for selecionada → Ordem: Manus → Claude → ChatGPT
- Se Manus for selecionada → Ordem: Claude → ChatGPT → Gemini
- Se Claude for selecionada → Ordem: ChatGPT → Gemini → Manus

### "Contexto preservado"
Histórico de prompts e respostas mantido durante todo o fluxo de refinamento, permitindo que LLMs subsequentes tenham acesso às interações anteriores.

---

## 🛡️ ANTI-GAMING / INTEGRIDADE

**Como evitar que critérios sejam "passados" sem resultado real:**

- Sistema não pode considerar "sucesso" se usuário não interagiu com as respostas
- Validação cruzada não pode ser considerada "completa" se LLMs não receberam contexto anterior
- Comparação lado a lado não pode ser considerada "funcional" se respostas não são visíveis simultaneamente

---

## 📋 TAREFA (PASSO A PASSO)

### Passo 1: Definir stack tecnológico (< 2 dias)
**Ação:** Testar viabilidade de Electron+React, SwiftUI ou Tauri

**Critério de decisão:** Qual permite prototipar mais rápido

**Entrega:** Decisão documentada com justificativa

---

### Passo 2: Criar wireframe básico (< 1 dia)
**Ação:** Desenhar interface simples com:
- Área de input de prompt
- Seleção de LLMs (1-4)
- Área de comparação de respostas (lado a lado)
- Botão de seleção de melhor resposta
- Visualização de fluxo de validação cruzada

**Entrega:** Wireframe visual (pode ser sketch simples)

---

### Passo 3: Implementar MVP (< 1 semana)
**Ação:** Implementar funcionalidades core:
- Envio de prompt para múltiplas LLMs
- Exibição de respostas lado a lado
- Seleção de melhor resposta
- Validação cruzada automatizada
- Preservação de contexto

**Entrega:** Aplicação funcional que passa nos 7 critérios de aceitação

---

### Passo 4: Testar com casos reais (< 2 dias)
**Ação:** Usar sistema para validar prompts reais e verificar se critérios são satisfeitos

**Entrega:** Relatório de testes com evidências (screenshots, logs)

---

### Passo 5: Iterar baseado em uso (contínuo)
**Ação:** Ajustar UX/UI, performance e funcionalidades baseado em feedback real

**Entrega:** Versões iterativas com melhorias documentadas

---

## ✅ VALIDAÇÃO (Definition of Done)

### V1 — Critérios de aceitação passam
- [ ] Todos os 7 critérios de aceitação foram testados e passaram

### V2 — Escopo respeitado
- [ ] Nenhuma funcionalidade fora do escopo foi implementada
- [ ] Todas as funcionalidades dentro do escopo foram implementadas

### V3 — Anti-resultados evitados
- [ ] Sistema é transparente (usuário confia nas respostas)
- [ ] Comparação ajuda a decidir (critério de seleção claro)
- [ ] Processo não é complexo demais (usuário usa)
- [ ] Validação cruzada não adiciona confusão
- [ ] Não há erro de orquestração (fluxo funciona corretamente)

### V4 — Incertezas resolvidas dentro das fronteiras
- [ ] Stack foi escolhido baseado em teste rápido (< 2 dias)
- [ ] UX/UI começou simples e iterou baseado em uso
- [ ] Custos são alertados (não controlados automaticamente)
- [ ] Performance foi testada com casos reais
- [ ] Configurações usam JSON simples
- [ ] Seleção de melhor resposta é manual
- [ ] Suporte para 4 LLMs (não mais)

### V5 — Dependências satisfeitas
- [ ] APIs de ChatGPT, Gemini, Manus e Claude estão integradas
- [ ] Sistema roda no macOS 12+
- [ ] Conexão com internet funciona

---

## 🚫 O QUE NÃO FAZER

### ❌ Não implementar funcionalidades fora do escopo
**Exemplo:** Não criar versão Windows, não adicionar mais de 4 LLMs, não criar histórico persistente.

### ❌ Não gastar tempo excessivo em decisões
**Exemplo:** Não gastar mais de 2 dias escolhendo stack, não tentar criar interface "perfeita" antes de testar.

### ❌ Não ignorar anti-resultados
**Exemplo:** Não criar sistema que funciona mas ninguém usa, não criar validação cruzada que adiciona confusão.

### ❌ Não fingir que critérios passaram
**Exemplo:** Não marcar critério como DONE sem testar, não assumir que performance funciona sem testar.

---

## 📊 MÉTRICAS DE SUCESSO

### M1 — Tempo de implementação
**Objetivo:** MVP funcional em < 1 semana (após escolha de stack)

### M2 — Taxa de validação
**Objetivo:** 100% dos critérios de aceitação passam nos testes

### M3 — Uso real
**Objetivo:** CEO usa o sistema para validar prompts reais em < 24h após entrega

### M4 — Confiança
**Objetivo:** CEO confia nas respostas e usa o sistema regularmente

---

## 🎯 REGRA MÃE

**"Qualquer mudança no resultado esperado deve gerar nova versão da ENDFIRST_SPEC e passar pelo ritual novamente."**

**Proibido:**
- Implementar funcionalidades fora do escopo sem atualizar a Spec
- Mudar resultado esperado sem versionar

**Permitido:**
- Resolver incertezas dentro das fronteiras definidas (OK se... / NÃO OK se...)
- Iterar UX/UI baseado em uso real (dentro do escopo)

---

## 📜 DECLARAÇÃO FINAL

Este prompt é o **contrato de resultado** entre CEO e Cursor.

**Governança:** ENDFIRST_SPEC_EF-2026-001 (VALIDADA)

**Próximo passo:** Implementar MVP que passa nos 7 critérios de aceitação.

---

**Versão:** 1.0  
**Data:** 7 de Janeiro de 2026  
**Governado por:** ENDFIRST_SPEC_EF-2026-001  
**Referência:** `/METODO/examples/ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md`
