// Tipos compartilhados entre main e renderer

export interface LLMProvider {
  id: string;
  name: string;
  apiKey: string;
  endpoint: string;
}

export interface LLMResponse {
  providerId: string;
  providerName: string;
  content: string;
  timestamp: Date;
}

// Tipos para configuração de APIs
export interface APIConfig {
  openai?: {
    apiKey: string;
  };
  gemini?: {
    apiKey: string;
  };
  anthropic?: {
    apiKey: string;
  };
}

export interface ProviderConfig {
  id: 'openai' | 'gemini' | 'anthropic';
  name: string;
  apiKey: string;
  endpoint: string;
  enabled: boolean;
}
