import axios from 'axios';
import { LLMProviderAdapter } from './base';
import { LLMResponse } from '../../../shared/types';

export class GeminiAdapter implements LLMProviderAdapter {
  id = 'gemini';
  name = 'Gemini (Google)';
  endpoint = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent';

  async sendPrompt(prompt: string, apiKey: string): Promise<LLMResponse> {
    try {
      const response = await axios.post(
        `${this.endpoint}?key=${apiKey}`,
        {
          contents: [
            {
              parts: [
                {
                  text: prompt,
                },
              ],
            },
          ],
        },
        {
          headers: {
            'Content-Type': 'application/json',
          },
          timeout: 30000,
        }
      );

      const content =
        response.data.candidates?.[0]?.content?.parts?.[0]?.text || 'Nenhuma resposta recebida';

      return {
        providerId: this.id,
        providerName: this.name,
        content,
        timestamp: new Date(),
      };
    } catch (error: any) {
      throw new Error(`Gemini API Error: ${error.response?.data?.error?.message || error.message}`);
    }
  }
}

