import React, { useState } from 'react';
import { APIConfig } from './components/APIConfig';
import { PromptInput } from './components/PromptInput';
import { ResponsesDisplay } from './components/ResponsesDisplay';
import { LLMResponse } from '../shared/types';

const App: React.FC = () => {
  const [currentView, setCurrentView] = useState<'home' | 'config'>('home');
  const [responses, setResponses] = useState<Array<{ success: boolean; response?: LLMResponse; error?: string; providerId: string }>>([]);

  return (
    <div style={{ fontFamily: 'system-ui', height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <nav style={{ padding: '12px 20px', borderBottom: '1px solid #ddd', backgroundColor: '#f5f5f5' }}>
        <div style={{ display: 'flex', gap: '16px', alignItems: 'center' }}>
          <h2 style={{ margin: 0, fontSize: '18px' }}>LLM Orchestrator</h2>
          <button
            onClick={() => setCurrentView('home')}
            style={{
              padding: '6px 12px',
              border: 'none',
              backgroundColor: currentView === 'home' ? '#1976d2' : 'transparent',
              color: currentView === 'home' ? 'white' : '#666',
              cursor: 'pointer',
              borderRadius: '4px',
            }}
          >
            Início
          </button>
          <button
            onClick={() => setCurrentView('config')}
            style={{
              padding: '6px 12px',
              border: 'none',
              backgroundColor: currentView === 'config' ? '#1976d2' : 'transparent',
              color: currentView === 'config' ? 'white' : '#666',
              cursor: 'pointer',
              borderRadius: '4px',
            }}
          >
            Configuração
          </button>
        </div>
      </nav>

      <div style={{ flex: 1, overflow: 'hidden', display: 'flex', flexDirection: 'column' }}>
        {currentView === 'home' && (
          <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
            <div style={{ flexShrink: 0, borderBottom: '1px solid #ddd' }}>
              <PromptInput onResponsesReceived={setResponses} />
            </div>
            <div style={{ flex: 1, overflow: 'hidden' }}>
              <ResponsesDisplay responses={responses} />
            </div>
          </div>
        )}

        {currentView === 'config' && (
          <div style={{ flex: 1, overflow: 'auto' }}>
            <APIConfig />
          </div>
        )}
      </div>
    </div>
  );
};

export default App;

