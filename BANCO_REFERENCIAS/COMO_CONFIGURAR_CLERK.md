# 🔐 Guia Completo: Como Configurar Clerk

**Data:** 22 de Dezembro de 2025  
**Status:** Guia passo a passo completo

---

## 📋 ÍNDICE

1. [Criar Conta no Clerk](#1-criar-conta-no-clerk)
2. [Criar Aplicação](#2-criar-aplicação)
3. [Obter API Keys](#3-obter-api-keys)
4. [Configurar Backend](#4-configurar-backend)
5. [Testar Autenticação](#5-testar-autenticação)
6. [Troubleshooting](#6-troubleshooting)

---

## 1. CRIAR CONTA NO CLERK

### Passo 1.1: Acessar Clerk

1. Abra o navegador e acesse: **https://clerk.com**
2. Clique em **"Sign Up"** (canto superior direito)
3. Escolha uma das opções:
   - **GitHub** (recomendado)
   - **Google**
   - **Email** (criar conta com email)

### Passo 1.2: Completar Cadastro

1. Preencha os dados solicitados
2. Verifique seu email (se usar cadastro por email)
3. Complete o processo de criação de conta

**✅ Free Tier Disponível:**
- Clerk oferece um plano gratuito generoso
- Perfeito para desenvolvimento e testes
- Inclui até 10.000 usuários mensais gratuitos

---

## 2. CRIAR APLICAÇÃO

### Passo 2.1: Dashboard do Clerk

1. Após fazer login, você verá o **Dashboard do Clerk**
2. Se for a primeira vez, clique em **"Create Application"**
3. Se já tiver aplicações, clique no botão **"+ Create"** (canto superior direito)

### Passo 2.2: Configurar Aplicação

Preencha o formulário:

**Application Name:**
```
Banco de Referências
```
ou
```
Banco Referencias
```

**Authentication Methods:**
- ✅ **Email** (marcar)
- ✅ **Password** (marcar)
- ⬜ **Social logins** (opcional - Google, GitHub, etc)

**Continue** ou **Create Application**

### Passo 2.3: Selecionar Instance

Escolha:
- **Development** (para desenvolvimento)
- **Production** (para produção - só depois)

Clique em **"Create"**

---

## 3. OBTER API KEYS

### Passo 3.1: Acessar API Keys

Após criar a aplicação, você será redirecionado para o dashboard:

1. No menu lateral esquerdo, clique em **"API Keys"**
2. Você verá duas keys principais:

### Passo 3.2: Copiar Keys

#### 🔑 Secret Key (Backend)

**Localização:** Seção **"Backend API Keys"**

```
sk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**⚠️ IMPORTANTE:**
- Esta é a **SECRET KEY** - NUNCA exponha publicamente
- Use apenas no backend (.env)
- Nunca commite no Git

**Como copiar:**
1. Clique no ícone de **"copiar"** ao lado da key
2. Ou clique em **"Show"** para revelar e copiar

#### 🔑 Publishable Key (Frontend)

**Localização:** Seção **"Publishable Keys"**

```
pk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Como copiar:**
1. Esta key já está visível
2. Clique no ícone de **"copiar"**

### Passo 3.3: Frontend API (Opcional)

No mesmo painel, você também verá:

**Frontend API:**
```
https://your-app-name.clerk.accounts.dev
```

**Nota:** Esta URL é útil para o frontend, mas não é obrigatória para o backend.

---

## 4. CONFIGURAR BACKEND

### Passo 4.1: Localizar Arquivo .env

No diretório do projeto:

```bash
cd /Users/joubert/Documents/GitHub/@endfirst/BANCO_REFERENCIAS
```

**Arquivo:** `.env`

Se não existir, crie copiando do exemplo:

```bash
cp .env.example .env
```

### Passo 4.2: Editar .env

Abra o arquivo `.env` no editor de sua preferência e adicione:

```bash
# Clerk Authentication
CLERK_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CLERK_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CLERK_FRONTEND_API=https://your-app-name.clerk.accounts.dev
```

**Substitua:**
- `sk_test_xxxxx` → Sua Secret Key copiada
- `pk_test_xxxxx` → Sua Publishable Key copiada
- `https://your-app-name.clerk.accounts.dev` → Sua Frontend API URL

**Exemplo real:**
```bash
# Clerk Authentication
CLERK_SECRET_KEY=sk_test_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
CLERK_PUBLISHABLE_KEY=pk_test_z9y8x7w6v5u4t3s2r1q0p9o8n7m6
CLERK_FRONTEND_API=https://banco-referencias.clerk.accounts.dev
```

### Passo 4.3: Salvar Arquivo

Salve o arquivo `.env`

**⚠️ IMPORTANTE:**
- Verifique que `.env` está no `.gitignore`
- Nunca commite o arquivo `.env` com as keys

---

## 5. TESTAR AUTENTICAÇÃO

### Passo 5.1: Reiniciar Backend

Se o backend estiver rodando, pare e reinicie:

```bash
# Parar (Ctrl+C)

# Iniciar novamente
docker-compose up --build
```

ou

```bash
cd backend
uvicorn app.main:app --reload
```

### Passo 5.2: Verificar Logs

Ao iniciar, verifique os logs:

**✅ Se configurado corretamente:**
- Backend inicia normalmente
- Sem erros relacionados ao Clerk

**❌ Se houver erro:**
- Verifique se as keys foram copiadas corretamente
- Verifique se não há espaços extras nas keys
- Verifique se o arquivo `.env` foi salvo

### Passo 5.3: Testar Endpoint Protegido

#### Opção A: Usando Swagger UI

1. Acesse: **http://localhost:8000/api/docs**
2. Clique em qualquer endpoint de documentos
3. Clique em **"Authorize"** (topo da página)
4. Cole um token JWT do Clerk no campo:
   ```
   Bearer YOUR_TOKEN_HERE
   ```
5. Clique em **"Authorize"**
6. Teste os endpoints

#### Opção B: Usando cURL

**Nota:** Para obter um token JWT, você precisa criar um usuário no Clerk primeiro.

1. Crie um usuário de teste no Clerk Dashboard
2. Obtenha o token JWT (via frontend ou Clerk API)
3. Teste:

```bash
curl -X GET http://localhost:8000/api/v1/documents \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

**Sem token (deve retornar 401):**
```bash
curl -X GET http://localhost:8000/api/v1/documents
# Retorna: {"detail":"Token de autenticação requerido"}
```

---

## 6. TROUBLESHOOTING

### Problema 1: "CLERK_SECRET_KEY not found"

**Sintoma:**
```
AttributeError: CLERK_SECRET_KEY
```

**Solução:**
1. Verifique se o arquivo `.env` existe
2. Verifique se as keys estão corretas no `.env`
3. Reinicie o backend
4. Verifique se não há espaços extras nas keys

### Problema 2: "Invalid token"

**Sintoma:**
```
AuthenticationError: Token inválido ou expirado
```

**Solução:**
1. Verifique se está usando um token válido
2. Tokens JWT expiram - gere um novo
3. Verifique se a Secret Key está correta

### Problema 3: Backend não inicia

**Sintoma:**
```
ImportError: No module named 'clerk_sdk_python'
```

**Solução:**
```bash
cd backend
pip install -r requirements.txt
```

### Problema 4: Modo Desenvolvimento vs Produção

**Sintoma:**
- Sistema funciona sem autenticação (modo dev)

**Explicação:**
- Se `CLERK_SECRET_KEY` não estiver configurado, o sistema funciona em modo desenvolvimento
- Retorna usuário mock (`dev_user_123`)
- Útil para desenvolvimento local

**Para ativar autenticação real:**
- Configure `CLERK_SECRET_KEY` no `.env`

---

## 📝 CHECKLIST RÁPIDO

Use este checklist para garantir que tudo está configurado:

- [ ] Conta Clerk criada
- [ ] Aplicação criada no Clerk
- [ ] Secret Key copiada
- [ ] Publishable Key copiada
- [ ] Keys adicionadas ao `.env`
- [ ] Arquivo `.env` salvo
- [ ] Backend reiniciado
- [ ] Logs verificados (sem erros)
- [ ] Endpoint protegido testado

---

## 🎯 PRÓXIMOS PASSOS

Após configurar o Clerk:

1. **Criar usuários de teste** no Clerk Dashboard
2. **Integrar frontend** (quando implementar)
3. **Configurar produção** (quando for fazer deploy)

---

## 📚 REFERÊNCIAS

- **Clerk Dashboard:** https://dashboard.clerk.com
- **Clerk Docs:** https://clerk.com/docs
- **Clerk Python SDK:** https://clerk.com/docs/reference/python

---

## 🆘 PRECISA DE AJUDA?

Se encontrar problemas:

1. Verifique a seção [Troubleshooting](#6-troubleshooting)
2. Consulte a documentação do Clerk
3. Verifique os logs do backend

---

**Última atualização:** 22 de Dezembro de 2025

