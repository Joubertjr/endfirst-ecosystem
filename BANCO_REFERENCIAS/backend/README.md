# Backend - Banco de Referências

Sistema de gestão de conhecimento com RAG usando Google Gemini File Search API.
Baseado em @google_Store (Flask).

## 🚀 Setup Inicial

### 1. Criar Ambiente Virtual

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente

Criar arquivo `.env` na raiz do projeto (ou copiar de `.env.example`):

```env
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-2.5-flash
FILE_STORE_ID=fileSearchStores/seu-store-id
```

### 4. Rodar Aplicação

```bash
# Com ambiente virtual ativado
python main.py
```

API estará disponível em: http://localhost:8000

## 🐳 Setup com Docker

```bash
# Na raiz do projeto
docker-compose up --build
```

## 📁 Estrutura

```
backend/
├── main.py                   # API Flask (adaptar do @google_Store)
├── playbook_loader.py        # Sistema de playbooks (reutilizar)
├── requirements.txt          # Dependências
├── Dockerfile
├── .venv/                    # Ambiente virtual (não versionar)
├── rag_database.db           # SQLite (criado automaticamente)
└── .env                      # Variáveis de ambiente (não versionar)
```

## 🔗 Endpoints

### Health Check
- `GET /` - Informações da API
- `GET /health` - Health check

### Documentos (a implementar)
- `POST /documents` - Upload de documento
- `GET /documents` - Listar documentos
- `GET /documents/{id}` - Obter documento
- `DELETE /documents/{id}` - Deletar documento

### Busca (a implementar)
- `POST /search` - Busca semântica RAG

### Referências (a implementar)
- `GET /references` - Listar referências
- `POST /references` - Criar referência

## 📝 Próximos Passos

1. ✅ Ambiente virtual criado
2. ⏭️ Copiar e adaptar `main.py` do @google_Store
3. ⏭️ Adaptar schema SQLite
4. ⏭️ Testar upload e busca

---

**Status:** 🟡 Em desenvolvimento (Fase 1 - Adaptação)
