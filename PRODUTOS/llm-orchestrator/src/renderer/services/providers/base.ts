import { LLMResponse } from '../../../shared/types';

export interface LLMProviderAdapter {
  id: string;
  name: string;
  sendPrompt(prompt: string, apiKey: string): Promise<LLMResponse>;
}

export interface ProviderConfig {
  id: string;
  apiKey: string;
  endpoint: string;
}

