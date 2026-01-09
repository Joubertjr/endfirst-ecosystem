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

