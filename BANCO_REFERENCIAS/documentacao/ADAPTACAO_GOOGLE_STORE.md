# 🔄 Adaptação do @google_Store para Banco de Referências

**Data:** 2025-12-16  
**Objetivo:** Documentar as mudanças e adaptações do código base

---

## 📋 Resumo

Este documento registra as adaptações feitas no código do `@google_Store` para criar o sistema de Banco de Referências.

---

## 🎯 O Que Mantemos

### Stack Tecnológico
- ✅ **Flask 3.1.0** - Framework web que já funciona
- ✅ **SQLite** - Database simples e suficiente
- ✅ **Google File Search** - RAG nativo (obrigatório)
- ✅ **React + Vite** - Frontend que já funciona
- ✅ **Docker** - Containerização (obrigatório)

### Padrões de Código
- ✅ Type hints obrigatórios
- ✅ Docstrings completas
- ✅ Tratamento de erros estruturado
- ✅ `.cursorrules` adaptado

### Funcionalidades Core
- ✅ Upload de documentos para Google File Search
- ✅ Busca semântica RAG
- ✅ Sistema de playbooks (adaptado para genérico)
- ✅ Processamento em background (threading)
- ✅ Persistência em SQLite

---

## 🔄 O Que Adaptamos

### 1. Schema do Database

**@google_Store:**
```sql
procuracao_analyses (
    file_id, filename, status,
    analise_falecido, analise_judicial, ...
)
```

**Banco de Referências:**
```sql
references (
    id, title, category, subject, sources, concepts, ...
)

projects (
    id, name, description, documentation_path, ...
)

documents (
    id, google_file_id, filename, reference_id, project_id, ...
)

analyses (
    id, document_id, playbook_id, status, results, ...
)
```

### 2. Endpoints da API

**Removidos (específicos):**
- ❌ `/analyze-procuracoes` - Análise específica jurídica
- ❌ `/analyses` - Análise de procurações

**Adaptados:**
- ✅ `/documents` - Mantido, adaptado para referências/projetos
- ✅ `/search` - Mantido, busca genérica

**Adicionados:**
- ✅ `/references` - CRUD de referências externas
- ✅ `/projects` - CRUD de projetos documentados
- ✅ `/analysis` - Análise genérica com playbooks

### 3. Lógica de Negócio

**Removido:**
- ❌ Validação de procurações judiciais
- ❌ Métricas de risco (BAIXO/MÉDIO/ALTO)
- ❌ Playbooks específicos (falecido, judicial)
- ❌ Pré-check de processos judiciais

**Adaptado:**
- ✅ Sistema de playbooks (genérico, configurável)
- ✅ Análise (genérica, resultado em JSON)
- ✅ Upload (genérico, qualquer documento)

**Adicionado:**
- ✅ Gestão de referências (2.400+ fontes)
- ✅ Gestão de projetos documentados
- ✅ Categorização e organização
- ✅ Vinculação documentos ↔ referências/projetos

---

## 📁 Arquivos Adaptados

### Backend

| Arquivo Original | Arquivo Adaptado | Mudanças |
|------------------|------------------|----------|
| `main.py` | `main.py` | Removido código jurídico, adaptado endpoints |
| `playbook_loader.py` | `playbook_loader.py` | Mantido (genérico) |
| `requirements.txt` | `requirements.txt` | Mantido (Flask) |

### Frontend

| Arquivo Original | Arquivo Adaptado | Mudanças |
|------------------|------------------|----------|
| `App.tsx` | `App.tsx` | Removido UI jurídica, adaptado para referências/projetos |
| `package.json` | `package.json` | Mantido (React + Vite) |

---

## 🔍 Diferenças Principais

### 1. Escopo

**@google_Store:**
- Sistema específico para análise de procurações judiciais
- 2 playbooks fixos (falecido, judicial)
- Métricas específicas (M1-M5, scores)

**Banco de Referências:**
- Sistema genérico de gestão de conhecimento
- Playbooks configuráveis (qualquer tipo)
- Resultados em JSON genérico

### 2. Models

**@google_Store:**
- `procuracao_analyses` (análises específicas)

**Banco de Referências:**
- `references` (referências externas)
- `projects` (projetos documentados)
- `documents` (documentos indexados)
- `analyses` (análises genéricas)

### 3. UI

**@google_Store:**
- Interface focada em análise jurídica
- Badges de risco (BAIXO/MÉDIO/ALTO)
- Métricas específicas (M1-M5)

**Banco de Referências:**
- Interface genérica de conhecimento
- Gestão de referências e projetos
- Busca e organização

---

## ✅ Checklist de Adaptação

### Backend
- [x] Copiar `main.py` base
- [ ] Remover código jurídico específico
- [ ] Adaptar schema SQLite
- [ ] Adaptar endpoints
- [ ] Manter Google File Search integration
- [ ] Testar upload e busca

### Frontend
- [ ] Copiar `App.tsx` base
- [ ] Remover UI jurídica específica
- [ ] Adaptar para referências/projetos
- [ ] Testar interface

### Documentação
- [x] Documentar adaptações (este arquivo)
- [ ] Atualizar README
- [ ] Criar guia de uso

---

## 📝 Notas de Implementação

### Decisões Tomadas

1. **Manter Flask**: Já funciona bem, não precisamos mudar
2. **Manter SQLite**: Simples, suficiente para MVP
3. **Manter estrutura simples**: Não complicar desnecessariamente
4. **Remover específico**: Limpar código jurídico específico
5. **Adicionar genérico**: Criar estrutura para referências/projetos

### Próximos Passos

1. Copiar código base do @google_Store
2. Fazer adaptações documentadas
3. Testar funcionamento
4. Iterar conforme necessidade

---

**Última atualização:** 2025-12-16


