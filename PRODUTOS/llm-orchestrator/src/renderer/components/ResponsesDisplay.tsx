import React, { useState } from 'react';
import { LLMResponse } from '../../shared/types';

interface ResponsesDisplayProps {
  responses: Array<{ success: boolean; response?: LLMResponse; error?: string; providerId: string }>;
}

export const ResponsesDisplay: React.FC<ResponsesDisplayProps> = ({ responses }) => {
  const [selectedResponseId, setSelectedResponseId] = useState<string | null>(null);

  if (responses.length === 0) {
    return (
      <div style={{ padding: '20px', fontFamily: 'system-ui', color: '#666', textAlign: 'center' }}>
        <p>Nenhuma resposta ainda. Envie um prompt para ver as respostas aqui.</p>
      </div>
    );
  }

  // Layout lado a lado fixo: cada resposta ocupa coluna dedicada
  // Com 1 resposta: 100% width
  // Com 2 respostas: 50% cada
  // Com 3 respostas: 33.33% cada
  const columnWidth = `${100 / responses.length}%`;

  const handleSelectResponse = (responseId: string) => {
    // Se já está selecionada, deseleciona. Caso contrário, seleciona e deseleciona outras
    if (selectedResponseId === responseId) {
      setSelectedResponseId(null);
    } else {
      setSelectedResponseId(responseId);
    }
  };

  return (
    <div
      style={{
        padding: '20px',
        fontFamily: 'system-ui',
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
      }}
    >
      <h2 style={{ marginTop: 0, marginBottom: '16px' }}>Respostas Recebidas</h2>
      
      {/* Container lado a lado com scroll independente */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'row',
          gap: '16px',
          height: 'calc(100vh - 200px)', // Altura fixa para garantir visibilidade simultânea
          overflowX: 'auto', // Scroll horizontal se necessário (caso de muitas respostas)
          overflowY: 'hidden',
        }}
      >
        {responses.map((result, index) => {
          const responseId = `${result.providerId}-${index}`;
          const isSelected = selectedResponseId === responseId;
          const hasError = !result.success;

          return (
            <div
              key={responseId}
              onClick={() => !hasError && handleSelectResponse(responseId)}
              style={{
                flex: `0 0 ${columnWidth}`,
                minWidth: '300px', // Largura mínima para legibilidade
                display: 'flex',
                flexDirection: 'column',
                border: isSelected
                  ? `4px solid #1976d2` // Borda mais grossa e azul quando selecionada
                  : `2px solid ${result.success ? '#4caf50' : '#d32f2f'}`,
                borderRadius: '8px',
                backgroundColor: isSelected
                  ? '#e3f2fd' // Background azul claro quando selecionada
                  : result.success
                  ? '#f1f8f4'
                  : '#ffebee',
                overflow: 'hidden', // Container não scrolla, conteúdo interno sim
                cursor: hasError ? 'default' : 'pointer',
                transition: 'all 0.2s ease',
                boxShadow: isSelected ? '0 4px 12px rgba(25, 118, 210, 0.3)' : 'none',
              }}
            >
              {/* Header fixo (não scrolla) */}
              <div
                style={{
                  padding: '16px',
                  borderBottom: isSelected
                    ? `1px solid #1976d2`
                    : `1px solid ${result.success ? '#4caf50' : '#d32f2f'}`,
                  backgroundColor: isSelected
                    ? '#bbdefb' // Background azul mais escuro no header quando selecionada
                    : result.success
                    ? '#e8f5e9'
                    : '#ffcdd2',
                  flexShrink: 0, // Não encolhe
                }}
              >
                <div
                  style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    {isSelected && (
                      <span
                        style={{
                          fontSize: '20px',
                          color: '#1976d2',
                          fontWeight: 'bold',
                        }}
                      >
                        ✓
                      </span>
                    )}
                    <h3
                      style={{
                        margin: 0,
                        fontSize: '16px',
                        fontWeight: '600',
                        color: isSelected ? '#1976d2' : '#333',
                      }}
                    >
                      {result.response?.providerName || result.providerId}
                    </h3>
                    {isSelected && (
                      <span
                        style={{
                          fontSize: '12px',
                          color: '#1976d2',
                          fontWeight: '500',
                          padding: '2px 6px',
                          backgroundColor: '#ffffff',
                          borderRadius: '4px',
                        }}
                      >
                        Melhor
                      </span>
                    )}
                  </div>
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
                    {result.success ? '✓ Sucesso' : '✗ Erro'}
                  </span>
                </div>
              </div>

              {/* Conteúdo com scroll independente */}
              <div
                style={{
                  flex: 1,
                  overflowY: 'auto', // Scroll independente por coluna
                  overflowX: 'hidden',
                  padding: '16px',
                }}
              >
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
                      <div
                        style={{
                          marginTop: '16px',
                          paddingTop: '16px',
                          borderTop: '1px solid #ddd',
                          fontSize: '12px',
                          color: '#666',
                        }}
                      >
                        <strong>Recebido em:</strong>{' '}
                        {new Date(result.response.timestamp).toLocaleString('pt-BR')}
                      </div>
                    )}
                  </div>
                ) : (
                  <div
                    style={{
                      fontSize: '14px',
                      color: '#d32f2f',
                      padding: '12px',
                      backgroundColor: '#ffebee',
                      borderRadius: '4px',
                    }}
                  >
                    <strong>Erro:</strong> {result.error || 'Erro desconhecido'}
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* Indicador de quantidade de respostas e seleção */}
      <div
        style={{
          marginTop: '12px',
          fontSize: '12px',
          color: '#666',
          textAlign: 'center',
        }}
      >
        {responses.length} resposta{responses.length !== 1 ? 's' : ''} exibida{responses.length !== 1 ? 's' : ''} lado a lado
        {selectedResponseId && (
          <span style={{ marginLeft: '12px', color: '#1976d2', fontWeight: '500' }}>
            • Resposta selecionada como melhor
          </span>
        )}
      </div>
    </div>
  );
};
