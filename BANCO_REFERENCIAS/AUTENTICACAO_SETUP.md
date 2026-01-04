# 🔐 Setup de Autenticação - Clerk

**Status:** 🟡 Em Implementação  
**Data:** 22 de Dezembro de 2025

---

## 📋 O QUE FOI IMPLEMENTADO

### ✅ Estrutura Base

1. **SDK do Clerk adicionado** (`requirements.txt`)
   - `clerk-sdk-python==0.1.0`

2. **Configurações** (`app/core/config.py`)
   - `CLERK_SECRET_KEY` - Secret key do Clerk
   - `CLERK_PUBLISHABLE_KEY` - Publishable key (para frontend)
   - `CLERK_FRONTEND_API` - Frontend API URL (opcional)

3. **Módulo de Autenticação** (`app/core/auth.py`)
   - Classe `ClerkAuth` para gerenciar autenticação
   - `get_current_user()` - Dependency para rotas protegidas
   - `get_optional_user()` - Dependency para rotas públicas/privadas
   - Modo desenvolvimento (sem auth se não configurado)

4. **Exceptions** (`app/core/exceptions.py`)
   - `AuthenticationError` - Exceção customizada

---

## 🚀 PRÓXIMOS PASSOS

### 1. Configurar Conta Clerk

1. **Criar conta em:** https://clerk.com
2. **Criar aplicação** (ou usar existente)
3. **Obter keys:**
   - Secret Key (Backend)
   - Publishable Key (Frontend)

### 2. Adicionar ao .env

```bash
# Clerk Authentication
CLERK_SECRET_KEY=sk_test_xxxxx
CLERK_PUBLISHABLE_KEY=pk_test_xxxxx
CLERK_FRONTEND_API=https://your-app.clerk.accounts.dev  # Opcional
```

### 3. Proteger Endpoints

Atualizar endpoints para usar autenticação:

```python
from app.api.v1.deps import get_current_user_dep

@router.post("")
async def upload_document(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)  # Adicionar aqui
):
    user_id = user["user_id"]
    # Usar user_id nas operações
    ...
```

### 4. Testar Autenticação

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar aplicação
uvicorn app.main:app --reload

# Testar endpoint protegido
curl -X POST http://localhost:8000/api/v1/documents \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@document.pdf"
```

---

## 📝 NOTAS

### Modo Desenvolvimento

Se `CLERK_SECRET_KEY` não estiver configurado:
- Sistema funciona sem autenticação
- Retorna usuário mock (`dev_user_123`)
- Útil para desenvolvimento local

### Produção

Em produção, **sempre** configure:
- `CLERK_SECRET_KEY`
- `CLERK_PUBLISHABLE_KEY`

---

## ✅ CHECKLIST

- [x] SDK do Clerk adicionado
- [x] Configurações criadas
- [x] Módulo de autenticação implementado
- [x] Dependencies criadas
- [ ] Conta Clerk criada
- [ ] Keys adicionadas ao .env
- [ ] Endpoints protegidos
- [ ] Testes de autenticação
- [ ] Documentação atualizada

---

**Próxima ação:** Configurar conta Clerk e proteger endpoints

