# 📖 Exemplos de Uso da API

**Versão:** 1.0.0  
**Base URL:** `http://localhost:8000/api/v1`

---

## 🔐 Autenticação

Todas as rotas (exceto `/search`) requerem autenticação via Clerk.

**Header:**
```http
Authorization: Bearer <clerk_jwt_token>
```

---

## 📄 Documentos

### Upload de Documento

```bash
curl -X POST "http://localhost:8000/api/v1/documents" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@documento.pdf" \
  -F "reference_id=optional-uuid" \
  -F "project_id=optional-uuid"
```

**Resposta:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "google_file_id": "files/abc123",
  "filename": "documento.pdf",
  "file_type": "application/pdf",
  "file_size_bytes": 102400,
  "upload_date": "2025-12-22T10:00:00Z",
  "status": "active",
  "document_metadata": {"operation_name": "operations/123"},
  "reference_id": null,
  "project_id": null
}
```

### Listar Documentos

```bash
curl -X GET "http://localhost:8000/api/v1/documents?skip=0&limit=10&reference_id=uuid&project_id=uuid" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Resposta:**
```json
{
  "total": 1,
  "documents": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "filename": "documento.pdf",
      ...
    }
  ]
}
```

### Obter Documento

```bash
curl -X GET "http://localhost:8000/api/v1/documents/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Deletar Documento

```bash
curl -X DELETE "http://localhost:8000/api/v1/documents/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## 🔍 Busca Semântica

### Buscar (Autenticação Opcional)

```bash
curl -X POST "http://localhost:8000/api/v1/search" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "query": "Qual é a arquitetura do sistema?",
    "max_results": 10
  }'
```

**Resposta:**
```json
{
  "query": "Qual é a arquitetura do sistema?",
  "answer": "O sistema utiliza uma arquitetura em camadas...",
  "sources": ["documento1.pdf", "documento2.pdf"],
  "processing_time_ms": 1234
}
```

---

## 📚 Referências

### Criar Referência

```bash
curl -X POST "http://localhost:8000/api/v1/references" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Referência de Exemplo",
    "category": "Tecnologia",
    "subject": "Arquitetura de Software",
    "description": "Descrição da referência",
    "sources": "[\"fonte1\", \"fonte2\"]",
    "concepts": "[\"conceito1\", \"conceito2\"]"
  }'
```

### Listar Referências

```bash
curl -X GET "http://localhost:8000/api/v1/references?skip=0&limit=10&category=Tecnologia" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Obter Referência

```bash
curl -X GET "http://localhost:8000/api/v1/references/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Atualizar Referência

```bash
curl -X PUT "http://localhost:8000/api/v1/references/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Título Atualizado",
    "description": "Nova descrição"
  }'
```

### Deletar Referência

```bash
curl -X DELETE "http://localhost:8000/api/v1/references/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## 🗂️ Projetos

### Criar Projeto

```bash
curl -X POST "http://localhost:8000/api/v1/projects" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Projeto Exemplo",
    "description": "Descrição do projeto",
    "documentation_path": "/docs/projeto"
  }'
```

### Listar Projetos

```bash
curl -X GET "http://localhost:8000/api/v1/projects?skip=0&limit=10" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Obter Projeto

```bash
curl -X GET "http://localhost:8000/api/v1/projects/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Atualizar Projeto

```bash
curl -X PUT "http://localhost:8000/api/v1/projects/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Nome Atualizado",
    "description": "Nova descrição"
  }'
```

### Deletar Projeto

```bash
curl -X DELETE "http://localhost:8000/api/v1/projects/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## 📊 Códigos de Status HTTP

- **200 OK** - Sucesso
- **201 Created** - Criado com sucesso
- **204 No Content** - Deletado com sucesso
- **400 Bad Request** - Requisição inválida
- **401 Unauthorized** - Não autenticado
- **404 Not Found** - Recurso não encontrado
- **422 Unprocessable Entity** - Erro de validação
- **500 Internal Server Error** - Erro do servidor

---

## ⚠️ Tratamento de Erros

**Exemplo de erro:**
```json
{
  "detail": "Documento '550e8400-e29b-41d4-a716-446655440000' não encontrado"
}
```

**Validação:**
```json
{
  "detail": [
    {
      "loc": ["body", "query"],
      "msg": "ensure this value has at least 3 characters",
      "type": "value_error.any_str.min_length"
    }
  ]
}
```

---

## 🐍 Python SDK (Exemplo)

```python
import httpx

BASE_URL = "http://localhost:8000/api/v1"
TOKEN = "your_clerk_token"

headers = {"Authorization": f"Bearer {TOKEN}"}

# Upload documento
with open("documento.pdf", "rb") as f:
    files = {"file": ("documento.pdf", f, "application/pdf")}
    response = httpx.post(
        f"{BASE_URL}/documents",
        headers=headers,
        files=files
    )
    document = response.json()

# Busca
response = httpx.post(
    f"{BASE_URL}/search",
    headers={**headers, "Content-Type": "application/json"},
    json={"query": "Qual é a arquitetura?", "max_results": 10}
)
result = response.json()
print(result["answer"])
```

---

## 📚 Documentação Interativa

Acesse a documentação Swagger UI:
- **URL:** `http://localhost:8000/api/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

**Última atualização:** 22 de Dezembro de 2025

