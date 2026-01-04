# Operational Level Agreement (OLA): Serviço de Validação de Fases via Manus

**Versão do Contrato:** 1.0  
**Status:** Ativo  
**Data:** 4 de Janeiro de 2026

---

## 1. Partes Envolvidas

- **Provedor:** Banco de Referências (Sistema RAG)
- **Cliente:** Qualquer projeto/produto do ecossistema ENDFIRST

---

## 2. Propósito

Este OLA define o contrato formal do serviço de validação de fases via API Manus, permitindo que qualquer projeto ou produto do ecossistema ENDFIRST possa validar entregas de forma padronizada.

---

## 3. Direção da Dependência

- Projetos/Produtos **DEPENDEM** do Banco de Referências para validação
- Banco de Referências **NÃO DEPENDE** dos projetos/produtos

---

## 4. Interface do Serviço

### 4.1. Endpoints

**Base URL:** `http://localhost:8000/api/v1/manus-validation`

#### ⭐ POST /complete (Agent-First - Recomendado)

**Executa todo o fluxo automaticamente - perfeito para agentes de IA!**

**Request:**
```json
{
  "fase": 2,
  "arquivos": ["arquivo1.md"],  // opcional
  "aguardar_conclusao": true,    // padrão: true
  "polling_interval": 10,        // padrão: 10s
  "max_wait_time": 600           // padrão: 600s
}
```

**Response:**
```json
{
  "validacao_id": "abc123",
  "status": "COMPLETED",
  "resultado": {
    "nota_geral": 4.8,
    "decisao": "APROVADO",
    "qualidade": "EXCEPCIONAL",
    "acoes_necessarias": [...]
  },
  "tempo_total": "245.3s",
  "mensagem": "Validação concluída com sucesso! Nota: 4.8/5"
}
```

**Características:**
- ✅ Executa fluxo completo automaticamente
- ✅ Polling automático (não precisa fazer manualmente)
- ✅ Resposta padronizada e clara
- ✅ Perfeito para agentes de IA consumirem
- ✅ Uma única chamada = validação completa

---

#### POST /package
Gera pacote ZIP de validação.

**Request:**
```json
{
  "fase": 2,
  "arquivos": ["arquivo1.md", "arquivo2.md"]  // opcional
}
```

**Response:**
```json
{
  "zip_path": "HOMOLOGACAO/pacotes/PACOTE_VALIDACAO_FASE_2.zip",
  "request_json_path": "HOMOLOGACAO/pacotes/VALIDACAO_REQUEST_FASE_2.json",
  "tamanho_bytes": 42000,
  "arquivos_incluidos": 8
}
```

---

#### POST /submit
Envia pacote para API Manus.

**Request:**
- `pacote`: Arquivo ZIP (multipart/form-data)
- `request_json`: Arquivo JSON (multipart/form-data)

**Response:**
```json
{
  "validacao_id": "abc123",
  "status": "PENDING",
  "estimated_time": "5-10 minutes",
  "polling_url": "/api/v1/manus-validation/abc123/status"
}
```

---

#### GET /{validacao_id}/status
Verifica status da validação.

**Response:**
```json
{
  "validacao_id": "abc123",
  "status": "PROCESSING",
  "progresso": 65,
  "etapa_atual": "Validando arquivo.md",
  "tempo_decorrido": "2m 15s",
  "tempo_estimado_restante": "1m 30s"
}
```

---

#### GET /{validacao_id}/resultado
Obtém resultado completo da validação.

**Response:**
```json
{
  "validacao_id": "abc123",
  "status": "COMPLETED",
  "nota_geral": 4.8,
  "decisao": "APROVADO",
  "qualidade": "EXCEPCIONAL",
  "arquivos_validados": 8,
  "linhas_analisadas": 1543,
  "tempo_validacao": "3m 42s",
  "problemas": {
    "criticos": 0,
    "menores": 1
  },
  "acoes_necessarias": [...],
  "relatorios": [...]
}
```

---

### 4.2. Autenticação

**Método:** Bearer Token

**Fontes:**
- Header `Authorization: Bearer <token>`
- API Key configurada no sistema

---

### 4.3. Códigos de Erro

| Código | Descrição |
|--------|-----------|
| `400` | Dados inválidos (fase inválida, arquivos não encontrados) |
| `401` | Autenticação requerida |
| `500` | Erro interno do servidor |

---

## 5. Garantias do Provedor

### 5.1. Disponibilidade

- API deve estar disponível quando backend estiver rodando
- Health check: `GET /health` deve retornar `200 OK`

### 5.2. Validações

- Fase deve ser >= 0
- Arquivos devem existir no sistema
- ZIP gerado deve ser válido

### 5.3. Processamento

- Geração de pacote: < 30 segundos
- Envio para Manus: < 1 minuto
- Polling: a cada 10 segundos (configurável)

---

## 6. Responsabilidades do Cliente

### 6.1. Autenticação

- Cliente deve fornecer token válido
- Token deve ter permissões adequadas

### 6.2. Polling

- Cliente deve fazer polling do status até conclusão
- Cliente deve respeitar intervalo de polling (10s recomendado)

### 6.3. Tratamento de Erros

- Cliente deve tratar erros de forma apropriada
- Cliente deve retry em caso de erro temporário

---

## 7. Exemplos de Uso

### ⭐ Exemplo 1: Validação Completa (Agent-First - Recomendado)

**Uso por Agente de IA:**
```python
import requests

# Uma única chamada executa tudo!
response = requests.post(
    "http://localhost:8000/api/v1/manus-validation/complete",
    headers={"Authorization": f"Bearer {token}"},
    json={"fase": 2}
)

resultado = response.json()

# Processar resultado
if resultado["status"] == "COMPLETED":
    nota = resultado["resultado"]["nota_geral"]
    print(f"✅ Validação aprovada! Nota: {nota}/5")
    
    # Implementar ações necessárias
    for acao in resultado["resultado"]["acoes_necessarias"]:
        print(f"   Implementando: {acao['descricao']}")
        # ... implementar ação ...
else:
    print(f"⏳ {resultado['mensagem']}")
```

---

### Exemplo 2: Validação Manual (Passo a Passo)

```python
import requests
import time

BASE_URL = "http://localhost:8000/api/v1/manus-validation"
TOKEN = "seu_token"
headers = {"Authorization": f"Bearer {TOKEN}"}

# 1. Gerar pacote
response = requests.post(
    f"{BASE_URL}/package",
    headers=headers,
    json={"fase": 2}
)
package = response.json()

# 2. Enviar
with open(package["zip_path"], "rb") as zip_file, \
     open(package["request_json_path"], "rb") as json_file:
    files = {"pacote": zip_file, "request_json": json_file}
    response = requests.post(f"{BASE_URL}/submit", headers=headers, files=files)
    validation = response.json()

# 3. Aguardar
validacao_id = validation["validacao_id"]
while True:
    response = requests.get(f"{BASE_URL}/{validacao_id}/status", headers=headers)
    status = response.json()
    if status["status"] == "COMPLETED":
        break
    time.sleep(10)

# 4. Obter resultado
response = requests.get(f"{BASE_URL}/{validacao_id}/resultado", headers=headers)
resultado = response.json()
```

---

## 8. Referências

- **API Docs:** http://localhost:8000/api/docs
- **Service:** `app/services/validation_service.py`
- **Schemas:** `app/schemas/validation.py`
- **Endpoints:** `app/api/v1/endpoints/manus_validation.py`

---

**Última atualização:** 4 de Janeiro de 2026

