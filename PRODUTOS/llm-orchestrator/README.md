# LLM Orchestrator

**Produto:** LLM Orchestrator  
**Demanda:** DEMANDA-001_LLM_ORCHESTRATOR  
**Spec:** ENDFIRST_SPEC_EF-2026-001  
**Status:** 🚧 Em desenvolvimento

---

## Stack Tecnológica

**Escolhida:** Electron + React + TypeScript

**Decisão:** Baseada em menor atrito + entrega mais rápida dos critérios

**Tecnologias:**
- **Electron:** Framework para aplicações desktop cross-platform
- **React:** Biblioteca para interface de usuário
- **TypeScript:** Superset do JavaScript com tipagem estática
- **Node.js:** Runtime JavaScript

**Por quê esta stack:**
- Ecosistema maduro para desenvolvimento desktop macOS
- Grande quantidade de bibliotecas para APIs HTTP
- Facilidade de integração com múltiplas APIs de LLM
- Desenvolvimento rápido com componentes React reutilizáveis
- TypeScript garante type safety ao trabalhar com múltiplas APIs diferentes

---

## Providers de LLM Suportados

### 1. ChatGPT (OpenAI)
- **Endpoint:** `https://api.openai.com/v1/chat/completions`
- **Documentação:** https://platform.openai.com/docs/api-reference
- **Autenticação:** Bearer token (API key)
- **Modelo:** gpt-4 ou gpt-3.5-turbo (configurável)

### 2. Gemini (Google)
- **Endpoint:** `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent`
- **Documentação:** https://ai.google.dev/docs
- **Autenticação:** API key (query parameter ou header)
- **Modelo:** gemini-pro (configurável)

### 3. Claude (Anthropic)
- **Endpoint:** `https://api.anthropic.com/v1/messages`
- **Documentação:** https://docs.anthropic.com/claude/reference
- **Autenticação:** x-api-key header
- **Modelo:** claude-3-opus, claude-3-sonnet, claude-3-haiku (configurável)

**Nota sobre 4º Provider:**
- Inicialmente suportamos 3 providers reais
- Arquitetura modular permite adicionar 4º provider facilmente no futuro
- Ordem de validação cruzada ajustada para 3 providers:
  - ChatGPT → Gemini → Claude
  - Gemini → Claude → ChatGPT
  - Claude → ChatGPT → Gemini

---

## Como Rodar Localmente

### Pré-requisitos
- macOS 12+
- Node.js 18+ (recomendado: usar nvm)
- npm ou yarn

### Instalação

```bash
# Navegar para o diretório do produto
cd PRODUTOS/llm-orchestrator

# Instalar dependências
npm install

# Executar em modo desenvolvimento (compila main + inicia Vite + abre Electron)
npm run dev

# Ou compilar e executar em produção
npm run build
npm start
```

**Nota:** No modo desenvolvimento, o aplicativo:
- Compila o main process do Electron (TypeScript → JavaScript)
- Inicia o servidor Vite para o renderer process (React)
- Aguarda o Vite estar pronto e abre a janela Electron
- Auto-reload quando há mudanças no código

### Configuração de APIs

1. Abra o aplicativo
2. Vá para a aba "Configuração"
3. Adicione suas chaves de API:
   - **OpenAI API Key:** Obtenha em https://platform.openai.com/api-keys
   - **Google Gemini API Key:** Obtenha em https://makersuite.google.com/app/apikey
   - **Anthropic API Key:** Obtenha em https://console.anthropic.com/
4. As credenciais são salvas localmente no macOS (electron-store)
   - **Nota:** Migração para Keychain será feita antes da aceitação final do Critério 7

### Estrutura do Projeto

```
/PRODUTOS/llm-orchestrator/
├── PLAN.md                    # Plano de execução detalhado
├── README.md                  # Este arquivo
├── package.json               # Dependências e scripts
├── src/
│   ├── main/                  # Processo principal Electron
│   ├── renderer/              # Aplicação React
│   │   ├── components/        # Componentes UI
│   │   ├── services/          # Serviços (orquestração, APIs)
│   │   └── utils/             # Utilitários
│   └── shared/                # Código compartilhado
└── tests/                     # Testes
```

---

## Funcionalidades Principais

- ✅ Envio de prompt para múltiplas LLMs simultaneamente (1-3)
- ✅ Comparação visual lado a lado de respostas
- ✅ Seleção manual de melhor resposta
- ✅ Validação cruzada automatizada entre LLMs
- ✅ Preservação de contexto durante refinamentos iterativos
- ✅ Execução local no macOS (sem servidor externo)

---

## Status de Desenvolvimento

**Última atualização:** Verificar commits no Git

**Incrementos concluídos:**
- Ver PLAN.md para detalhes do progresso

---

## Referências

- **Plano de Execução:** [PLAN.md](./PLAN.md)
- **Demanda:** [/DEMANDAS/DEMANDA-001_LLM_ORCHESTRATOR.md](../../DEMANDAS/DEMANDA-001_LLM_ORCHESTRATOR.md)
- **Spec:** [/METODO/examples/ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md](../../METODO/examples/ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md)
- **Critérios de Aceitação:** [/DEMANDAS/DEMANDA-001_ACCEPTANCE.md](../../DEMANDAS/DEMANDA-001_ACCEPTANCE.md)

