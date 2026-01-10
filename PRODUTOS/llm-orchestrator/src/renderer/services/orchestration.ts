import { LLMResponse } from '../../shared/types';
import { LLMProviderAdapter } from './providers/base';
import { OpenAIAdapter } from './providers/openai';
import { GeminiAdapter } from './providers/gemini';
import { AnthropicAdapter } from './providers/anthropic';

export interface ProviderConfig {
  id: 'openai' | 'gemini' | 'anthropic';
  apiKey: string;
  enabled: boolean;
}

const adapterMap: Record<string, () => LLMProviderAdapter> = {
  openai: () => new OpenAIAdapter(),
  gemini: () => new GeminiAdapter(),
  anthropic: () => new AnthropicAdapter(),
};

export class OrchestrationService {
  /**
   * Envia prompt para múltiplas LLMs simultaneamente
   * @param prompt Texto do prompt
   * @param providers Lista de providers selecionados
   * @returns Array de respostas (sucesso ou erro)
   */
  async sendToMultipleProviders(
    prompt: string,
    providers: ProviderConfig[]
  ): Promise<Array<{ success: boolean; response?: LLMResponse; error?: string; providerId: string }>> {
    const enabledProviders = providers.filter((p) => p.enabled && p.apiKey);

    if (enabledProviders.length === 0) {
      throw new Error('Nenhum provider habilitado ou configurado');
    }

    // Criar adaptadores para os providers selecionados
    const adapters = enabledProviders.map((provider) => {
      const adapterFactory = adapterMap[provider.id];
      if (!adapterFactory) {
        throw new Error(`Provider ${provider.id} não suportado`);
      }
      return {
        adapter: adapterFactory(),
        apiKey: provider.apiKey,
        providerId: provider.id,
      };
    });

    // Enviar requests em paralelo
    const promises = adapters.map(async ({ adapter, apiKey, providerId }) => {
      try {
        const response = await adapter.sendPrompt(prompt, apiKey);
        return {
          success: true,
          response,
          providerId,
        };
      } catch (error: any) {
        return {
          success: false,
          error: error.message || 'Erro desconhecido',
          providerId,
        };
      }
    });

    // Aguardar todas as respostas (sucesso ou erro)
    return Promise.all(promises);
  }
}

export const orchestrationService = new OrchestrationService();

