const Store = require('electron-store');

interface ProviderConfig {
  id: 'openai' | 'gemini' | 'anthropic';
  name: string;
  apiKey: string;
  endpoint: string;
  enabled: boolean;
}

interface StoreSchema {
  providers: ProviderConfig[];
}

const store = new Store({
  name: 'llm-orchestrator-config',
  defaults: {
    providers: [],
  },
});

const configService = {
  // Salvar configuração de um provider
  saveProvider(config: ProviderConfig): void {
    const providers = (store.get('providers', []) as ProviderConfig[]) || [];
    const index = providers.findIndex((p: ProviderConfig) => p.id === config.id);
    
    if (index >= 0) {
      providers[index] = config;
    } else {
      providers.push(config);
    }
    
    store.set('providers', providers);
  },

  // Obter configuração de um provider
  getProvider(id: string): ProviderConfig | undefined {
    const providers = (store.get('providers', []) as ProviderConfig[]) || [];
    return providers.find((p: ProviderConfig) => p.id === id);
  },

  // Obter todas as configurações
  getAllProviders(): ProviderConfig[] {
    return (store.get('providers', []) as ProviderConfig[]) || [];
  },

  // Remover configuração de um provider
  removeProvider(id: string): void {
    const providers = (store.get('providers', []) as ProviderConfig[]) || [];
    const filtered = providers.filter((p: ProviderConfig) => p.id !== id);
    store.set('providers', filtered);
  },

  // Validar formato de API key básico
  validateAPIKey(apiKey: string): boolean {
    // Validação básica: não vazio e tem pelo menos 20 caracteres
    if (!apiKey || typeof apiKey !== 'string') {
      return false;
    }
    return apiKey.trim().length >= 20;
  },
};

module.exports = { configService };
