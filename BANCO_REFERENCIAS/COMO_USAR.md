# 📖 Como Usar - Banco de Referências

**Data:** 2025-12-16

---

## 🚀 Início Rápido

### 1. Acesse o Frontend

Abra no navegador: **http://localhost:5173**

---

## 📤 Upload de Documentos

1. Na seção **"📤 Upload de Documento"**, clique em **"Escolher arquivo"**
2. Selecione um arquivo (PDF, DOCX, TXT, MD, etc)
3. O upload começará automaticamente
4. Aguarde a mensagem de sucesso
5. O documento aparecerá na lista abaixo

**Formatos suportados:**
- PDF (.pdf)
- Word (.docx, .doc)
- Texto (.txt)
- Markdown (.md)
- JSON (.json)
- Excel (.xlsx)
- PowerPoint (.pptx)
- Imagens (.png, .jpg, .jpeg, .gif, .webp)

---

## 📄 Ver Documentos

A lista de documentos aparece automaticamente na seção **"📄 Documentos"**.

**Informações exibidas:**
- Nome do arquivo
- Tipo do arquivo
- Tamanho (em KB)
- Data de upload

**Atualizar lista:**
- Clique no botão **"Atualizar"** para recarregar a lista

---

## 🔍 Busca Semântica

1. Na seção **"🔍 Busca Semântica"**, digite sua pergunta
2. Clique em **"Buscar"** ou pressione **Enter**
3. Aguarde o resultado (pode levar alguns segundos)
4. Veja a resposta gerada pelo RAG
5. Fontes citadas aparecem abaixo da resposta

**Exemplos de buscas:**
- "Qual é o conteúdo principal deste documento?"
- "Resuma os pontos principais"
- "Quais são as datas mencionadas?"
- "Explique o conceito X"

**Nota:** Você precisa ter documentos enviados para fazer buscas.

---

## 🗑️ Deletar Documentos

1. Na lista de documentos, encontre o documento que deseja deletar
2. Clique no botão **"Deletar"** (vermelho)
3. Confirme a exclusão no popup
4. O documento será removido

**Atenção:** A exclusão é permanente!

---

## ⚙️ Configuração

### Adicionar API Key do Google Gemini

Para usar upload e busca, você precisa da `GEMINI_API_KEY`:

1. Abra o arquivo `.env` na raiz do projeto
2. Substitua `your_gemini_api_key_here` pela sua chave real
3. Reinicie o backend:
   ```bash
   docker-compose restart backend
   ```

**Onde obter a chave:**
- Acesse: https://ai.google.dev/
- Crie um projeto ou use um existente
- Gere uma API key
- Cole no arquivo `.env`

---

## 🔧 Comandos Úteis

### Ver logs
```bash
# Todos os serviços
docker-compose logs -f

# Apenas backend
docker-compose logs -f backend

# Apenas frontend
docker-compose logs -f frontend
```

### Parar serviços
```bash
docker-compose down
```

### Iniciar serviços
```bash
docker-compose up -d
```

### Reiniciar um serviço
```bash
docker-compose restart backend
docker-compose restart frontend
```

### Rebuild (após mudanças no código)
```bash
docker-compose up --build -d
```

---

## 🌐 URLs Importantes

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000
- **Swagger Docs:** http://localhost:8000/api/docs
- **Health Check:** http://localhost:8000/health

---

## ❓ Troubleshooting

### Frontend não carrega

```bash
docker-compose logs frontend
docker-compose restart frontend
```

### Backend não responde

```bash
docker-compose logs backend
docker-compose restart backend
```

### Erro ao fazer upload

- Verifique se a `GEMINI_API_KEY` está configurada no `.env`
- Verifique os logs: `docker-compose logs backend`
- Confirme que o arquivo não está corrompido

### Busca não funciona

- Certifique-se de ter documentos enviados
- Verifique se a `GEMINI_API_KEY` está válida
- Veja os logs para detalhes do erro

---

## ✅ Pronto!

Agora você pode usar o sistema completo. Acesse **http://localhost:5173** e comece!

---

**Última atualização:** 2025-12-16

