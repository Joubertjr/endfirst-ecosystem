# Operational Level Agreement (OLA): Serviço de Upload de Documentos

**Versão do Contrato:** 1.0  
**Status:** Ativo  
**Data:** 4 de Janeiro de 2026

---

## 1. Partes Envolvidas

- **Provedor:** Banco de Referências (Sistema RAG)
- **Cliente:** Qualquer projeto/produto do ecossistema ENDFIRST

---

## 2. Propósito

Este OLA define o contrato formal do serviço de upload de documentos, permitindo que qualquer projeto ou produto do ecossistema ENDFIRST possa fazer upload de arquivos para o Banco de Referências de forma padronizada e genérica.

---

## 3. Direção da Dependência

- Projetos/Produtos **DEPENDEM** do Banco de Referências para upload
- Banco de Referências **NÃO DEPENDE** dos projetos/produtos

---

## 4. Interface do Serviço

### 4.1. Endpoints

**Upload Individual:**
- **URL:** `POST /api/v1/documents`
- **Descrição:** Upload de um único arquivo

**Upload em Lote:**
- **URL:** `POST /api/v1/documents/bulk`
- **Descrição:** Upload de múltiplos arquivos em uma única requisição
- **Recomendado para:** Automações e uploads em massa

**Base URL:** Configurável via `ENDFIRST_API_BASE` (padrão: `http://localhost:8000`)

### 4.2. Autenticação

**Método:** Bearer Token

**Fontes:**
- `ENDFIRST_API_TOKEN` (variável de ambiente)
- `CLERK_API_TOKEN` (variável de ambiente, fallback)
- `--api-token` (argumento CLI)

**Formato:**
```
Authorization: Bearer <token>
```

### 4.3. Parâmetros de Entrada

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `file` | File | ✅ Sim | Arquivo a ser enviado |
| `description` | String | ❌ Não | Descrição do arquivo |
| `reference_id` | UUID | ❌ Não | ID da referência relacionada |
| `project_id` | UUID | ❌ Não | ID do projeto relacionado |
| `metadata` | JSON | ❌ Não | Metadados adicionais (JSON string) |

### 4.4. Resposta de Sucesso

**Status:** `201 Created`

**Body:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "google_file_id": "files/abc123",
  "filename": "documento.md",
  "file_type": "text/markdown",
  "file_size_bytes": 10240,
  "upload_date": "2026-01-04T10:00:00Z",
  "status": "active",
  "document_metadata": {},
  "reference_id": null,
  "project_id": null
}
```

### 4.5. Códigos de Erro

| Código | Descrição |
|--------|-----------|
| `400` | Dados inválidos (UUID inválido, arquivo muito grande, tipo não permitido) |
| `401` | Autenticação requerida |
| `404` | Recurso não encontrado (reference_id ou project_id não existe) |
| `500` | Erro interno do servidor |

---

## 5. Implementação do Cliente

### 5.1. cURL

**Upload Individual:**
```bash
curl -X POST "http://localhost:8000/api/v1/documents" \
  -H "Authorization: Bearer $ENDFIRST_API_TOKEN" \
  -F "file=@arquivo.md" \
  -F "description=Descrição"
```

**Upload em Lote:**
```bash
curl -X POST "http://localhost:8000/api/v1/documents/bulk" \
  -H "Authorization: Bearer $ENDFIRST_API_TOKEN" \
  -F "files=@arquivo1.md" \
  -F "files=@arquivo2.md" \
  -F "project_id=<project_uuid>"
```

### 5.2. Python (requests)

**Upload Individual:**
```python
import requests

url = "http://localhost:8000/api/v1/documents"
headers = {"Authorization": f"Bearer {token}"}
files = {"file": open("arquivo.md", "rb")}
data = {"description": "Descrição"}

response = requests.post(url, headers=headers, files=files, data=data)
print(response.json())
```

**Upload em Lote:**
```python
import requests

url = "http://localhost:8000/api/v1/documents/bulk"
headers = {"Authorization": f"Bearer {token}"}
files = [
    ("files", open("arquivo1.md", "rb")),
    ("files", open("arquivo2.md", "rb")),
]
data = {"project_id": "uuid-do-projeto"}

response = requests.post(url, headers=headers, files=files, data=data)
print(response.json())
```

---

## 6. Garantias do Provedor

### 6.1. Disponibilidade

- API deve estar disponível quando backend estiver rodando
- Health check: `GET /health` deve retornar `200 OK`

### 6.2. Validações

- Tamanho máximo: 10 MB (configurável)
- Tipos permitidos: Markdown, PDF, Text, JSON, YAML, etc.
- UUIDs validados antes de uso

### 6.3. Processamento

- Upload para Google File Search
- Indexação para busca semântica
- Metadados salvos no PostgreSQL

---

## 7. Responsabilidades do Cliente

### 7.1. Autenticação

- Cliente deve fornecer token válido
- Token deve ter permissões adequadas

### 7.2. Validação

- Cliente deve validar arquivo antes de enviar
- Cliente deve validar UUIDs antes de enviar

### 7.3. Tratamento de Erros

- Cliente deve tratar erros de forma apropriada
- Cliente deve retry em caso de erro temporário

---

## 8. Versionamento

**Versão Atual:** 1.0

**Mudanças Futuras:**
- Versões serão documentadas neste OLA
- Breaking changes serão comunicados com antecedência
- Versões antigas serão mantidas por período de transição

---

## 9. Exemplos de Uso

### Exemplo 1: Upload Individual (cURL)

```bash
curl -X POST "http://localhost:8000/api/v1/documents" \
  -H "Authorization: Bearer $ENDFIRST_API_TOKEN" \
  -F "file=@METODO/pilares/PILAR_1_5_MODELOS_MENTAIS.md" \
  -F "description=Pilar 1.5: Modelos Mentais"
```

### Exemplo 2: Upload em Lote (cURL)

```bash
curl -X POST "http://localhost:8000/api/v1/documents/bulk" \
  -H "Authorization: Bearer $ENDFIRST_API_TOKEN" \
  -F "files=@arquivo1.md" \
  -F "files=@arquivo2.md" \
  -F "files=@arquivo3.md" \
  -F "project_id=<project_uuid>"
```

### Exemplo 3: Upload em Lote (Python)

```python
import requests

url = "http://localhost:8000/api/v1/documents/bulk"
headers = {"Authorization": f"Bearer {token}"}

files = [
    ("files", ("arquivo1.md", open("arquivo1.md", "rb"), "text/markdown")),
    ("files", ("arquivo2.md", open("arquivo2.md", "rb"), "text/markdown")),
    ("files", ("arquivo3.md", open("arquivo3.md", "rb"), "text/markdown")),
]

data = {"project_id": "uuid-do-projeto"}

response = requests.post(url, headers=headers, files=files, data=data)
result = response.json()

print(f"Total: {result['total']}")
print(f"Sucesso: {result['successful']}")
print(f"Falhas: {result['failed']}")

for item in result['results']:
    if item['success']:
        print(f"✅ {item['filename']}: {item['document_id']}")
    else:
        print(f"❌ {item['filename']}: {item['error']}")
```

---

## 10. Troubleshooting

### Erro: "Autenticação requerida"
**Solução:** Configurar `ENDFIRST_API_TOKEN` ou `CLERK_API_TOKEN`

### Erro: "Arquivo muito grande"
**Solução:** Verificar tamanho máximo (10 MB padrão)

### Erro: "Tipo de arquivo não permitido"
**Solução:** Verificar tipos permitidos na documentação

### Erro: "API não responde"
**Solução:** Verificar se backend está rodando (`docker-compose ps`)

---

## 11. Referências

- **API Docs:** http://localhost:8000/api/docs
- **Health Check:** http://localhost:8000/health
- **Código do Serviço:** `scripts/endfirst_upload_service.py`
- **Documentação Completa:** `BANCO_REFERENCIAS/docs/EXEMPLOS_API.md`

---

**Última atualização:** 4 de Janeiro de 2026

