import React, { useState, useEffect } from 'react';
import { LLMResponse, ProviderConfig } from '../../shared/types';
import { orchestrationService } from '../services/orchestration';
import '../../types/electron';

interface PromptInputProps {
  onResponsesReceived: (responses: Array<{ success: boolean; response?: LLMResponse; error?: string; providerId: string }>) => void;
}

export const PromptInput: React.FC<PromptInputProps> = ({ onResponsesReceived }) => {
  const [prompt, setPrompt] = useState('');
  const [availableProviders, setAvailableProviders] = useState<ProviderConfig[]>([]);
  const [selectedProviders, setSelectedProviders] = useState<Set<string>>(new Set());
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadProviders();
  }, []);

  const loadProviders = async () => {
    if (window.electronAPI?.config) {
      const providers = await window.electronAPI.config.getAllProviders();
      const enabledProviders = providers.filter((p) => p.enabled && p.apiKey);
      setAvailableProviders(enabledProviders);
      
      // Selecionar todos os providers disponíveis por padrão
      setSelectedProviders(new Set(enabledProviders.map((p) => p.id)));
    }
  };

  const handleProviderToggle = (providerId: string) => {
    setSelectedProviders((prev) => {
      const newSet = new Set(prev);
      if (newSet.has(providerId)) {
        newSet.delete(providerId);
      } else {
        newSet.add(providerId);
      }
      return newSet;
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!prompt.trim()) {
      setError('Por favor, digite um prompt');
      return;
    }

    if (selectedProviders.size === 0) {
      setError('Selecione pelo menos um provider');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const providersToUse = availableProviders.filter((p) => selectedProviders.has(p.id));
      const results = await orchestrationService.sendToMultipleProviders(prompt, providersToUse);
      
      onResponsesReceived(results);
    } catch (err: any) {
      setError(err.message || 'Erro ao enviar prompt');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'system-ui' }}>
      <h2 style={{ marginTop: 0 }}>Enviar Prompt</h2>

      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '16px' }}>
          <label style={{ display: 'block', marginBottom: '8px', fontWeight: '500' }}>
            Prompt:
          </label>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Digite seu prompt aqui..."
            rows={6}
            style={{
              width: '100%',
              padding: '12px',
              border: '1px solid #ddd',
              borderRadius: '4px',
              fontSize: '14px',
              fontFamily: 'inherit',
              resize: 'vertical',
            }}
            disabled={loading}
          />
        </div>

        <div style={{ marginBottom: '16px' }}>
          <label style={{ display: 'block', marginBottom: '8px', fontWeight: '500' }}>
            Selecionar LLMs ({selectedProviders.size} selecionada{selectedProviders.size !== 1 ? 's' : ''}):
          </label>
          {availableProviders.length === 0 ? (
            <p style={{ color: '#d32f2f', fontSize: '14px' }}>
              Nenhum provider configurado. Configure suas APIs na aba Configuração.
            </p>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {availableProviders.map((provider) => (
                <label
                  key={provider.id}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    cursor: loading ? 'not-allowed' : 'pointer',
                    padding: '8px',
                    borderRadius: '4px',
                    backgroundColor: selectedProviders.has(provider.id) ? '#e3f2fd' : 'transparent',
                  }}
                >
                  <input
                    type="checkbox"
                    checked={selectedProviders.has(provider.id)}
                    onChange={() => handleProviderToggle(provider.id)}
                    disabled={loading}
                    style={{ marginRight: '8px', cursor: loading ? 'not-allowed' : 'pointer' }}
                  />
                  <span>{provider.name}</span>
                </label>
              ))}
            </div>
          )}
        </div>

        {error && (
          <div
            style={{
              padding: '12px',
              backgroundColor: '#ffebee',
              color: '#d32f2f',
              borderRadius: '4px',
              marginBottom: '16px',
              fontSize: '14px',
            }}
          >
            {error}
          </div>
        )}

        <button
          type="submit"
          disabled={loading || selectedProviders.size === 0 || availableProviders.length === 0}
          style={{
            padding: '12px 24px',
            backgroundColor: loading || selectedProviders.size === 0 ? '#ccc' : '#1976d2',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            fontSize: '16px',
            fontWeight: '500',
            cursor: loading || selectedProviders.size === 0 ? 'not-allowed' : 'pointer',
            opacity: loading || selectedProviders.size === 0 ? 0.6 : 1,
          }}
        >
          {loading ? 'Enviando...' : `Enviar para ${selectedProviders.size} LLM${selectedProviders.size !== 1 ? 's' : ''}`}
        </button>
      </form>
    </div>
  );
};

