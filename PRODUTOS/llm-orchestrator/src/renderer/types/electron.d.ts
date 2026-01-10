import { ProviderConfig } from '../../shared/types';

declare global {
  interface Window {
    electronAPI: {
      platform: string;
      config: {
        saveProvider: (config: ProviderConfig) => Promise<{ success: boolean; error?: string }>;
        getProvider: (id: string) => Promise<ProviderConfig | undefined>;
        getAllProviders: () => Promise<ProviderConfig[]>;
        removeProvider: (id: string) => Promise<{ success: boolean; error?: string }>;
        validateAPIKey: (apiKey: string) => Promise<boolean>;
      };
    };
  }
}

export {};

