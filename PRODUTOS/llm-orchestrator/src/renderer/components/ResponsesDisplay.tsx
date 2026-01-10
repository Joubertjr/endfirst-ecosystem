import React from 'react';
import { LLMResponse } from '../../shared/types';

interface ResponsesDisplayProps {
  responses: Array<{ success: boolean; response?: LLMResponse; error?: string; providerId: string }>;
}

export const ResponsesDisplay: React.FC<ResponsesDisplayProps> = ({ responses }) => {
  if (responses.length === 0) {
    return (
      <div style={{ padding: '20px', fontFamily: 'system-ui', color: '#666', textAlign: 'center' }}>
        <p>Nenhuma resposta ainda. Envie um prompt para ver as respostas aqui.</p>
      </div>
    );
  }

  return (
    <div style={{ padding: '20px', fontFamily: 'system-ui' }}>
      <h2 style={{ marginTop: 0 }}>Respostas Recebidas</h2>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '16px' }}>
        {responses.map((result, index) => (
          <div
            key={`${result.providerId}-${index}`}
            style={{
              border: `1px solid ${result.success ? '#4caf50' : '#d32f2f'}`,
              borderRadius: '8px',
              padding: '16px',
              backgroundColor: result.success ? '#f1f8f4' : '#ffebee',
            }}
          >
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                marginBottom: '12px',
              }}
            >
              <h3 style={{ margin: 0, fontSize: '16px', fontWeight: '600' }}>
                {result.response?.providerName || result.providerId}
              </h3>
              <span
                style={{
                  padding: '4px 8px',
                  borderRadius: '4px',
                  fontSize: '12px',
                  fontWeight: '500',
                  backgroundColor: result.success ? '#4caf50' : '#d32f2f',
                  color: 'white',
                }}
              >
                {result.success ? 'Sucesso' : 'Erro'}
              </span>
            </div>

            {result.success && result.response ? (
              <div>
                <div
                  style={{
                    fontSize: '14px',
                    lineHeight: '1.6',
                    color: '#333',
                    whiteSpace: 'pre-wrap',
                    wordBreak: 'break-word',
                  }}
                >
                  {result.response.content}
                </div>
                {result.response.timestamp && (
                  <div style={{ marginTop: '12px', fontSize: '12px', color: '#666' }}>
                    {new Date(result.response.timestamp).toLocaleString('pt-BR')}
                  </div>
                )}
              </div>
            ) : (
              <div style={{ fontSize: '14px', color: '#d32f2f' }}>
                <strong>Erro:</strong> {result.error || 'Erro desconhecido'}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

