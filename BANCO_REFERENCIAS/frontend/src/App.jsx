import { useState, useEffect } from 'react'
import axios from 'axios'

// Tenta usar proxy, se não funcionar usa URL direta
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:8000/api/v1'
  : '/api/v1'

function App() {
  const [documents, setDocuments] = useState([])
  const [loading, setLoading] = useState(false)
  const [uploading, setUploading] = useState(false)
  const [error, setError] = useState(null)
  const [success, setSuccess] = useState(null)
  const [searchQuery, setSearchQuery] = useState('')
  const [searchResults, setSearchResults] = useState(null)
  const [searching, setSearching] = useState(false)

  useEffect(() => {
    loadDocuments()
  }, [])

  const loadDocuments = async () => {
    try {
      setLoading(true)
      setError(null)
      const response = await axios.get(`${API_BASE}/documents`)
      setDocuments(response.data.documents || [])
    } catch (err) {
      setError('Erro ao carregar documentos: ' + (err.response?.data?.detail || err.message))
    } finally {
      setLoading(false)
    }
  }

  const handleUpload = async (event) => {
    const file = event.target.files[0]
    if (!file) return

    try {
      setUploading(true)
      setError(null)
      setSuccess(null)

      const formData = new FormData()
      formData.append('file', file)

      await axios.post(`${API_BASE}/documents`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })

      setSuccess('Documento enviado com sucesso!')
      await loadDocuments()
      event.target.value = '' // Reset input
    } catch (err) {
      setError('Erro ao enviar documento: ' + (err.response?.data?.detail || err.message))
    } finally {
      setUploading(false)
    }
  }

  const handleDelete = async (documentId) => {
    if (!confirm('Tem certeza que deseja deletar este documento?')) return

    try {
      setError(null)
      await axios.delete(`${API_BASE}/documents/${documentId}`)
      setSuccess('Documento deletado com sucesso!')
      await loadDocuments()
    } catch (err) {
      setError('Erro ao deletar documento: ' + (err.response?.data?.detail || err.message))
    }
  }

  const handleSearch = async () => {
    if (!searchQuery.trim()) {
      setError('Digite uma query de busca')
      return
    }

    try {
      setSearching(true)
      setError(null)
      const response = await axios.post(`${API_BASE}/search`, {
        query: searchQuery,
        max_results: 10
      })
      setSearchResults(response.data)
    } catch (err) {
      setError('Erro na busca: ' + (err.response?.data?.detail || err.message))
    } finally {
      setSearching(false)
    }
  }

  return (
    <div className="container">
      <div className="header">
        <h1>🗂️ Banco de Referências</h1>
        <p>Sistema de gestão de conhecimento com RAG usando Google Gemini File Search</p>
      </div>

      {error && <div className="error">{error}</div>}
      {success && <div className="success">{success}</div>}

      {/* Upload */}
      <div className="card">
        <h2>📤 Upload de Documento</h2>
        <div className="input-file">
          <input
            type="file"
            onChange={handleUpload}
            disabled={uploading}
          />
          {uploading && <span>Enviando...</span>}
        </div>
      </div>

      {/* Busca */}
      <div className="card">
        <h2>🔍 Busca Semântica</h2>
        <div style={{ display: 'flex', gap: '10px', marginTop: '15px' }}>
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Digite sua pergunta..."
            style={{
              flex: 1,
              padding: '10px',
              borderRadius: '4px',
              border: '1px solid #ddd',
              fontSize: '14px'
            }}
            onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
          />
          <button
            className="btn"
            onClick={handleSearch}
            disabled={searching}
          >
            {searching ? 'Buscando...' : 'Buscar'}
          </button>
        </div>

        {searchResults && (
          <div style={{ marginTop: '20px' }}>
            <h3>Resultado:</h3>
            <div style={{
              background: '#f8f9fa',
              padding: '15px',
              borderRadius: '4px',
              marginTop: '10px',
              whiteSpace: 'pre-wrap'
            }}>
              {searchResults.answer}
            </div>
            {searchResults.sources && searchResults.sources.length > 0 && (
              <div style={{ marginTop: '15px' }}>
                <h4>Fontes:</h4>
                <ul style={{ marginLeft: '20px', marginTop: '10px' }}>
                  {searchResults.sources.map((source, idx) => (
                    <li key={idx}>{source}</li>
                  ))}
                </ul>
              </div>
            )}
            {searchResults.processing_time_ms && (
              <p style={{ marginTop: '10px', color: '#666', fontSize: '12px' }}>
                Tempo de processamento: {searchResults.processing_time_ms}ms
              </p>
            )}
          </div>
        )}
      </div>

      {/* Lista de Documentos */}
      <div className="card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
          <h2>📄 Documentos ({documents.length})</h2>
          <button className="btn" onClick={loadDocuments} disabled={loading}>
            {loading ? 'Carregando...' : 'Atualizar'}
          </button>
        </div>

        {loading && documents.length === 0 ? (
          <div className="loading">Carregando documentos...</div>
        ) : documents.length === 0 ? (
          <div className="loading">Nenhum documento encontrado. Faça upload de um documento acima.</div>
        ) : (
          <ul className="document-list">
            {documents.map((doc) => (
              <li key={doc.id} className="document-item">
                <div className="document-info">
                  <h3>{doc.filename}</h3>
                  <p>
                    Tipo: {doc.file_type || 'N/A'} | 
                    Tamanho: {doc.file_size_bytes ? (doc.file_size_bytes / 1024).toFixed(2) + ' KB' : 'N/A'} |
                    Data: {new Date(doc.upload_date).toLocaleString('pt-BR')}
                  </p>
                </div>
                <button
                  className="btn btn-danger"
                  onClick={() => handleDelete(doc.id)}
                >
                  Deletar
                </button>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  )
}

export default App

