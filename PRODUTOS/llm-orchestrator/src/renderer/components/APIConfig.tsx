import React, { useState, useEffect } from 'react';
import { ProviderConfig } from '../../shared/types';
import '../types/electron';

interface ProviderFormData {
  id: 'openai' | 'gemini' | 'anthropic';
  name: string;
  apiKey: string;
  endpoint: string;
}

const PROVIDER_INFO: Record<string, { name: string; endpoint: string; placeholder: string }> = {
  openai: {
    name: 'ChatGPT (OpenAI)',
    endpoint: 'https://api.openai.com/v1/chat/completions',
    placeholder: 'sk-...',
  },
  gemini: {
    name: 'Gemini (Google)',
    endpoint: 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent',
    placeholder: 'AIza...',
  },
  anthropic: {
    name: 'Claude (Anthropic)',
    endpoint: 'https://api.anthropic.com/v1/messages',
    placeholder: 'sk-ant-...',
  },
};

export const APIConfig: React.FC = () => {
  const [providers, setProviders] = useState<ProviderConfig[]>([]);
  const [formData, setFormData] = useState<Record<string, ProviderFormData>>({
    openai: { id: 'openai', name: PROVIDER_INFO.openai.name, apiKey: '', endpoint: PROVIDER_INFO.openai.endpoint },
    gemini: { id: 'gemini', name: PROVIDER_INFO.gemini.name, apiKey: '', endpoint: PROVIDER_INFO.gemini.endpoint },
    anthropic: { id: 'anthropic', name: PROVIDER_INFO.anthropic.name, apiKey: '', endpoint: PROVIDER_INFO.anthropic.endpoint },
  });
  const [validation, setValidation] = useState<Record<string, { valid: boolean; message: string }>>({});
  const [savedStatus, setSavedStatus] = useState<Record<string, 'idle' | 'saving' | 'success' | 'error'>>({
    openai: 'idle',
    gemini: 'idle',
    anthropic: 'idle',
  });

  useEffect(() => {
    loadProviders();
  }, []);

  const loadProviders = async () => {
    if (window.electronAPI?.config) {
      const allProviders = await window.electronAPI.config.getAllProviders();
      setProviders(allProviders);

      // Preencher formulários com dados salvos
      allProviders.forEach((provider) => {
        setFormData((prev) => ({
          ...prev,
          [provider.id]: {
            id: provider.id,
            name: provider.name,
            apiKey: provider.apiKey,
            endpoint: provider.endpoint,
          },
        }));
      });
    }
  };

  const validateAPIKey = async (id: string, apiKey: string): Promise<boolean> => {
    if (!apiKey.trim()) {
      setValidation((prev) => ({
        ...prev,
        [id]: { valid: false, message: 'API Key não pode estar vazia' },
      }));
      return false;
    }

    if (window.electronAPI?.config) {
      const isValid = await window.electronAPI.config.validateAPIKey(apiKey);
      setValidation((prev) => ({
        ...prev,
        [id]: isValid
          ? { valid: true, message: 'Formato válido' }
          : { valid: false, message: 'API Key deve ter pelo menos 20 caracteres' },
      }));
      return isValid;
    }

    return false;
  };

  const handleAPIKeyChange = async (id: string, value: string) => {
    setFormData((prev) => ({
      ...prev,
      [id]: { ...prev[id], apiKey: value },
    }));

    // Validar após um pequeno delay
    setTimeout(() => {
      validateAPIKey(id, value);
    }, 500);
  };

  const handleSave = async (id: string) => {
    if (!window.electronAPI?.config) {
      return;
    }

    const form = formData[id];
    const isValid = await validateAPIKey(id, form.apiKey);

    if (!isValid) {
      setSavedStatus((prev) => ({ ...prev, [id]: 'error' }));
      return;
    }

    setSavedStatus((prev) => ({ ...prev, [id]: 'saving' }));

    const config: ProviderConfig = {
      id: form.id,
      name: form.name,
      apiKey: form.apiKey,
      endpoint: form.endpoint,
      enabled: true,
    };

    const result = await window.electronAPI.config.saveProvider(config);

    if (result.success) {
      setSavedStatus((prev) => ({ ...prev, [id]: 'success' }));
      setTimeout(() => {
        setSavedStatus((prev) => ({ ...prev, [id]: 'idle' }));
      }, 2000);
      await loadProviders();
    } else {
      setSavedStatus((prev) => ({ ...prev, [id]: 'error' }));
    }
  };

  const renderProviderForm = (id: 'openai' | 'gemini' | 'anthropic') => {
    const info = PROVIDER_INFO[id];
    const form = formData[id];
    const status = savedStatus[id];
    const validationResult = validation[id];
    const isSaved = providers.some((p) => p.id === id && p.apiKey === form.apiKey);

    return (
      <div key={id} style={{ marginBottom: '24px', padding: '16px', border: '1px solid #ddd', borderRadius: '8px' }}>
        <h3 style={{ marginTop: 0 }}>{info.name}</h3>
        <div style={{ marginBottom: '12px' }}>
          <label style={{ display: 'block', marginBottom: '4px', fontWeight: '500' }}>
            API Key:
          </label>
          <input
            type="password"
            value={form.apiKey}
            onChange={(e) => handleAPIKeyChange(id, e.target.value)}
            placeholder={info.placeholder}
            style={{
              width: '100%',
              padding: '8px',
              border: `1px solid ${validationResult?.valid === false ? '#d32f2f' : '#ddd'}`,
              borderRadius: '4px',
              fontSize: '14px',
            }}
          />
          {validationResult && (
            <div
              style={{
                fontSize: '12px',
                marginTop: '4px',
                color: validationResult.valid ? '#2e7d32' : '#d32f2f',
              }}
            >
              {validationResult.message}
            </div>
          )}
        </div>
        <div style={{ marginBottom: '12px' }}>
          <label style={{ display: 'block', marginBottom: '4px', fontWeight: '500' }}>
            Endpoint:
          </label>
          <input
            type="text"
            value={form.endpoint}
            readOnly
            style={{
              width: '100%',
              padding: '8px',
              border: '1px solid #ddd',
              borderRadius: '4px',
              fontSize: '12px',
              backgroundColor: '#f5f5f5',
              color: '#666',
            }}
          />
        </div>
        <button
          onClick={() => handleSave(id)}
          disabled={status === 'saving' || !validationResult?.valid}
          style={{
            padding: '8px 16px',
            backgroundColor: status === 'success' ? '#2e7d32' : status === 'error' ? '#d32f2f' : '#1976d2',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: status === 'saving' || !validationResult?.valid ? 'not-allowed' : 'pointer',
            opacity: status === 'saving' || !validationResult?.valid ? 0.6 : 1,
          }}
        >
          {status === 'saving'
            ? 'Salvando...'
            : status === 'success'
            ? '✓ Salvo'
            : status === 'error'
            ? '✗ Erro'
            : isSaved
            ? 'Atualizar'
            : 'Salvar'}
        </button>
        {isSaved && status === 'idle' && (
          <span style={{ marginLeft: '12px', color: '#2e7d32', fontSize: '14px' }}>✓ Configurado</span>
        )}
      </div>
    );
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'system-ui', maxWidth: '800px' }}>
      <h1>Configuração de APIs</h1>
      <p style={{ color: '#666', marginBottom: '24px' }}>
        Configure suas chaves de API para os providers de LLM. As credenciais são armazenadas localmente (migração para Keychain será feita antes da aceitação final).
      </p>

      {renderProviderForm('openai')}
      {renderProviderForm('gemini')}
      {renderProviderForm('anthropic')}
    </div>
  );
};

