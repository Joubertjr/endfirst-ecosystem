# ⚡ Clerk - Setup Rápido (5 minutos)

**Para quem quer configurar rápido!**

---

## 🚀 PASSOS RÁPIDOS

### 1. Criar Conta (2 min)

1. Acesse: https://clerk.com
2. Clique em **"Sign Up"**
3. Escolha GitHub, Google ou Email
4. Complete o cadastro

### 2. Criar Aplicação (1 min)

1. No Dashboard, clique em **"Create Application"**
2. Nome: `Banco de Referências`
3. Auth: **Email + Password** (marcar)
4. Clique em **"Create"**

### 3. Copiar Keys (1 min)

1. Menu lateral → **"API Keys"**
2. Copie **Secret Key** (Backend):
   ```
   sk_test_xxxxx
   ```
3. Copie **Publishable Key** (Frontend):
   ```
   pk_test_xxxxx
   ```

### 4. Configurar Backend (1 min)

1. Edite `.env`:
   ```bash
   CLERK_SECRET_KEY=sk_test_xxxxx  # Cole sua Secret Key aqui
   CLERK_PUBLISHABLE_KEY=pk_test_xxxxx  # Cole sua Publishable Key aqui
   ```

2. Salve o arquivo

3. Reinicie o backend:
   ```bash
   docker-compose up --build
   ```

---

## ✅ PRONTO!

Agora seus endpoints estão protegidos!

**Para testar:**
- Acesse: http://localhost:8000/api/docs
- Clique em **"Authorize"**
- Cole um token JWT do Clerk

---

**Guia completo:** Veja `COMO_CONFIGURAR_CLERK.md` para detalhes

