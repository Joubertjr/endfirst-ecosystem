# Banco de Referências - Frontend Next.js 15

Frontend moderno construído com Next.js 15, TypeScript, Tailwind CSS e Clerk.

## 🚀 Tecnologias

- **Next.js 15** - Framework React
- **TypeScript** - Tipagem estática
- **Tailwind CSS** - Estilização
- **Clerk** - Autenticação
- **Radix UI** - Componentes acessíveis
- **Axios** - Cliente HTTP

## 📦 Instalação

```bash
# Instalar dependências
npm install

# Copiar variáveis de ambiente
cp .env.local.example .env.local

# Editar .env.local com suas configurações
```

## 🔧 Configuração

Edite `.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
```

## 🏃 Desenvolvimento

```bash
# Rodar em desenvolvimento
npm run dev

# Build para produção
npm run build

# Rodar produção
npm start

# Type check
npm run type-check

# Lint
npm run lint
```

## 📁 Estrutura

```
frontend-nextjs/
├── app/                    # App Router (Next.js 15)
│   ├── dashboard/          # Páginas do dashboard
│   ├── sign-in/            # Página de login
│   ├── sign-up/            # Página de cadastro
│   ├── layout.tsx          # Layout raiz
│   └── page.tsx            # Página inicial
├── components/             # Componentes reutilizáveis
├── lib/                    # Utilitários
│   └── api.ts             # Cliente API
├── middleware.ts           # Middleware (Clerk)
└── package.json
```

## 🎯 Páginas

- `/` - Redireciona para dashboard ou sign-in
- `/dashboard` - Dashboard principal
- `/dashboard/documents` - Gerenciar documentos
- `/dashboard/search` - Busca semântica
- `/dashboard/references` - Gerenciar referências
- `/dashboard/projects` - Gerenciar projetos
- `/dashboard/playbooks` - Gerenciar playbooks
- `/dashboard/analyses` - Gerenciar análises
- `/sign-in` - Login
- `/sign-up` - Cadastro

## 📝 Notas

Este é um frontend básico criado com Next.js 15. As páginas específicas de cada funcionalidade devem ser implementadas conforme necessário.

---

**Última atualização:** 22 de Dezembro de 2025

