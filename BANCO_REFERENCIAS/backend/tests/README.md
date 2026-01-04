# 🧪 Testes - Banco de Referências

**Status:** ✅ Estrutura Completa Criada  
**Cobertura Alvo:** 70% mínimo

---

## 📋 Estrutura

```
tests/
├── __init__.py
├── conftest.py           # Fixtures compartilhadas
├── unit/                 # Testes unitários
│   ├── test_document_service.py
│   └── test_search_service.py
└── integration/          # Testes de integração
    └── (a implementar)
```

---

## 🚀 Como Rodar

### Instalar Dependências

```bash
cd backend
pip install -r requirements.txt
```

### Rodar Todos os Testes

```bash
pytest
```

### Rodar com Coverage

```bash
pytest --cov=app --cov-report=html
```

### Rodar Testes Específicos

```bash
# Apenas testes unitários
pytest tests/unit/

# Apenas um arquivo
pytest tests/unit/test_document_service.py

# Apenas um teste
pytest tests/unit/test_document_service.py::TestDocumentService::test_upload_document_success

# Apenas testes marcados como unit
pytest -m unit
```

### Rodar com Verbose

```bash
pytest -v
```

---

## 📊 Cobertura

### Meta
- **Mínimo:** 70% de cobertura
- **Ideal:** 80%+ de cobertura

### Verificar Cobertura

```bash
# Terminal
pytest --cov=app --cov-report=term-missing

# HTML (abre no navegador)
pytest --cov=app --cov-report=html
open htmlcov/index.html
```

---

## 🎯 Testes Implementados

### DocumentService (10+ testes)
- ✅ Upload de documento bem-sucedido
- ✅ Upload com reference_id
- ✅ Obter documento por ID
- ✅ Obter documento inexistente
- ✅ Listar documentos
- ✅ Listar documentos com paginação
- ✅ Deletar documento
- ✅ Deletar documento inexistente
- ✅ Upload com erro do Google File Search
- ✅ Detecção de MIME type

### SearchService (6+ testes)
- ✅ Busca semântica bem-sucedida
- ✅ Busca com max_results customizado
- ✅ Busca com max_results padrão
- ✅ Busca com erro do Google File Search
- ✅ Cálculo de processing_time_ms
- ✅ Busca sem fontes

---

## 🔧 Fixtures Disponíveis

### conftest.py

- `mock_db_session` - Mock de sessão do banco
- `mock_document_repository` - Mock do DocumentRepository
- `mock_vector_repository` - Mock do VectorRepository
- `sample_document` - Documento de exemplo
- `sample_file_content` - Conteúdo de arquivo de exemplo
- `sample_file_content_pdf` - Conteúdo PDF válido
- `mock_uuid` - Mock de UUID
- `mock_tempfile` - Mock de tempfile

---

## 📝 Próximos Passos

### Testes de Integração (Próximo)
- [ ] Testes de endpoints (FastAPI TestClient)
- [ ] Testes com database real (SQLite in-memory)
- [ ] Testes end-to-end

### CI/CD (Futuro)
- [ ] GitHub Actions workflow
- [ ] Pipeline automatizado
- [ ] Coverage reports no PR

---

## 🐛 Troubleshooting

### Erro: "Module not found"
```bash
# Certifique-se de estar no diretório backend
cd backend
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
pytest
```

### Erro: "asyncio"
```bash
# Certifique-se de ter pytest-asyncio instalado
pip install pytest-asyncio
```

### Erro: "Database"
Os testes usam mocks, não precisam de database real. Se houver erros relacionados ao DB, verifique os mocks em `conftest.py`.

---

**Última atualização:** 22 de Dezembro de 2025

