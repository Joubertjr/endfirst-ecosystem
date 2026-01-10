import axios from 'axios';
import { LLMProviderAdapter } from './base';
import { LLMResponse } from '../../../shared/types';

export class OpenAIAdapter implements LLMProviderAdapter {
  id = 'openai';
  name = 'ChatGPT (OpenAI)';
  endpoint = 'https://api.openai.com/v1/chat/completions';

  async sendPrompt(prompt: string, apiKey: string): Promise<LLMResponse> {
    try {
      const response = await axios.post(
        this.endpoint,
        {
          model: 'gpt-4',
          messages: [
            {
              role: 'user',
              content: prompt,
            },
          ],
          temperature: 0.7,
        },
        {
          headers: {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json',
          },
          timeout: 30000,
        }
      );

      const content = response.data.choices[0]?.message?.content || 'Nenhuma resposta recebida';

      return {
        providerId: this.id,
        providerName: this.name,
        content,
        timestamp: new Date(),
      };
    } catch (error: any) {
      throw new Error(`OpenAI API Error: ${error.response?.data?.error?.message || error.message}`);
    }
  }
}

