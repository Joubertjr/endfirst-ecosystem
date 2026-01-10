import React, { useState } from 'react';
import { APIConfig } from './components/APIConfig';

const App: React.FC = () => {
  const [currentView, setCurrentView] = useState<'home' | 'config'>('config');

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

      <div style={{ flex: 1, overflow: 'auto' }}>
        {currentView === 'home' && (
          <div style={{ padding: '20px' }}>
            <h1>LLM Orchestrator</h1>
            <p>DEMANDA-001 - ENDFIRST_SPEC_EF-2026-001</p>
            <p>Status: Em desenvolvimento - Incremento 2</p>
            <p>Stack: Electron + React + TypeScript</p>
            <p style={{ marginTop: '20px', color: '#666' }}>
              Configure suas APIs na aba "Configuração" para começar a usar o orquestrador.
            </p>
          </div>
        )}

        {currentView === 'config' && <APIConfig />}
      </div>
    </div>
  );
};

export default App;

