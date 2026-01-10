import axios from 'axios';
import { LLMProviderAdapter } from './base';
import { LLMResponse } from '../../../shared/types';

export class AnthropicAdapter implements LLMProviderAdapter {
  id = 'anthropic';
  name = 'Claude (Anthropic)';
  endpoint = 'https://api.anthropic.com/v1/messages';

  async sendPrompt(prompt: string, apiKey: string): Promise<LLMResponse> {
    try {
      const response = await axios.post(
        this.endpoint,
        {
          model: 'claude-3-opus-20240229',
          max_tokens: 1024,
          messages: [
            {
              role: 'user',
              content: prompt,
            },
          ],
        },
        {
          headers: {
            'x-api-key': apiKey,
            'anthropic-version': '2023-06-01',
            'Content-Type': 'application/json',
          },
          timeout: 30000,
        }
      );

      const content = response.data.content?.[0]?.text || 'Nenhuma resposta recebida';

      return {
        providerId: this.id,
        providerName: this.name,
        content,
        timestamp: new Date(),
      };
    } catch (error: any) {
      throw new Error(`Anthropic API Error: ${error.response?.data?.error?.message || error.message}`);
    }
  }
}

