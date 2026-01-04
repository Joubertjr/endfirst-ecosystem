# 🔄 Processo 32: Governança de Serviços e APIs

**Código:** PROCESSO_32  
**Versão:** 1.0  
**Data:** 4 de Janeiro de 2026  
**Frequência:** Contínua (ao criar/modificar serviços) + Trimestral (revisão)  
**Duração:** 15-30 minutos (por serviço) + 2-4 horas (revisão trimestral)

---

## 🎯 OBJETIVO

Este processo define como criar, manter e governar serviços e APIs em **TODO o ecossistema ENDFIRST**, garantindo que:
- Não perdemos o controle do inventário
- Scripts são transformados em APIs quando apropriado
- Serviços seguem padrões estabelecidos (Agent-First)
- Documentação está sempre atualizada
- Cada projeto mantém seu próprio inventário
- Inventário geral está sempre atualizado

---

## 📋 INTEGRAÇÃO COM PILARES

### Pilares que Usam Este Processo

- **Pilar 2 (Recursos):** Ao identificar necessidade de serviço/API
- **Pilar 3.5 (Riscos):** Ao avaliar riscos de criar script vs API
- **Pilar 4 (Planejamento):** Ao planejar arquitetura de software
- **Pilar 5 (Validação):** Ao validar serviços/APIs
- **Pilar 6 (Execução):** Ao criar/modificar serviços durante execução
- **Pilar 7 (Aprendizagem):** Ao consolidar aprendizados sobre serviços

### Triggers

- **Automático:** Ao criar novo serviço/API
- **Automático:** Ao transformar script em API
- **Automático:** Ao adicionar novo projeto com software
- **Temporal:** Trimestral (revisão completa)
- **Manual:** Quando necessário

---

## 🔄 QUANDO EXECUTAR

### Executar Este Processo Quando:

1. **Criar novo serviço/API**
   - Antes de criar, verificar se já existe
   - Seguir processo de criação
   - Atualizar inventários

2. **Transformar script em API**
   - Identificar script a transformar
   - Criar API seguindo processo
   - Remover script
   - Atualizar inventários

3. **Adicionar novo projeto com software**
   - Criar estrutura de governança
   - Criar inventário local
   - Atualizar inventário geral

4. **Revisão trimestral**
   - Revisar todos os inventários
   - Verificar scripts legados
   - Revisar OLAs
   - Atualizar estatísticas

---

## 📋 CHECKLIST DE EXECUÇÃO

### Ao Criar Novo Serviço/API

- [ ] Identificar necessidade (funcionalidade de negócio?)
- [ ] Verificar se já existe serviço similar
- [ ] **Identificar vinculação (Projeto/Subprojeto/Produto)**
- [ ] Criar schema (Pydantic)
- [ ] Criar service layer
- [ ] Criar endpoint de API
- [ ] Adicionar ao router
- [ ] Criar OLA (se serviço público)
- [ ] Atualizar inventário local (`<PROJETO>/INTEGRACOES/INVENTARIO_SERVICOS.md`)
- [ ] **Documentar vinculação no inventário local**
- [ ] Atualizar inventário geral (`GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`)
- [ ] **Documentar vinculação no inventário geral**
- [ ] Documentar exemplos de uso por agentes
- [ ] Testar API

### Ao Transformar Script em API

- [ ] Identificar script a transformar
- [ ] Avaliar se deve ser transformado (funcionalidade de negócio?)
- [ ] Criar API seguindo processo acima
- [ ] Remover script
- [ ] Atualizar inventário local (mover para "Transformados")
- [ ] Atualizar inventário geral
- [ ] Validar funcionalidade

### Ao Adicionar Novo Projeto com Software

- [ ] Criar diretório `INTEGRACOES/` no projeto
- [ ] Criar `INTEGRACOES/INVENTARIO_SERVICOS.md` (usar template)
- [ ] Atualizar inventário geral (`GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`)
- [ ] Adicionar projeto na tabela "Projetos com Software"
- [ ] Linkar para inventário local

### Revisão Trimestral

- [ ] Revisar inventário geral
- [ ] Revisar inventários locais de cada projeto
- [ ] Verificar scripts legados (avaliar se devem ser transformados)
- [ ] Revisar OLAs (atualizar se necessário)
- [ ] Atualizar estatísticas
- [ ] Documentar aprendizados

---

## 🎯 PRINCÍPIOS FUNDAMENTAIS

### 1. Agent-First
- ✅ Todos os serviços devem ser consumíveis por agentes de IA
- ✅ Endpoints "complete" para fluxos inteiros
- ✅ Respostas padronizadas e claras

### 2. APIs, NÃO Scripts
- ❌ NUNCA criar scripts Python/Bash para funcionalidades de negócio
- ✅ SEMPRE criar endpoints de API no backend
- ✅ Scripts apenas para manutenção/CI/CD

### 3. Contrato Formal (OLA)
- ✅ Cada serviço público deve ter um OLA
- ✅ OLA define interface, garantias e responsabilidades
- ✅ Versionamento documentado

### 4. Inventário Hierárquico
- ✅ Inventário geral na raiz (`GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`)
- ✅ Inventário específico em cada projeto (`<PROJETO>/INTEGRACOES/INVENTARIO_SERVICOS.md`)
- ✅ Ambos devem ser atualizados sempre

---

## 📚 DOCUMENTAÇÃO RELACIONADA

### Documentos Principais

- **Processo Completo:** `GOVERNANCA/PROCESSO_GOVERNANCA_SERVICOS.md`
- **Inventário Geral:** `GOVERNANCA/INVENTARIO_SERVICOS_ENDFIRST.md`
- **Banco de Referências - Inventário:** `BANCO_REFERENCIAS/INTEGRACOES/INVENTARIO_SERVICOS.md`
- **Banco de Referências - Processo:** `BANCO_REFERENCIAS/INTEGRACOES/PROCESSO_GOVERNANCA_SERVICOS.md`

### OLAs

- `BANCO_REFERENCIAS/INTEGRACOES/OLA_*.md`

---

## 🔗 RASTREABILIDADE

### Processos Relacionados

- **PROCESSO_10:** Reorganização de Diretórios (pode identificar scripts a transformar)
- **PROCESSO_30:** Revisão de Modelo de Dados (pode identificar necessidade de serviços)
- **PROCESSO_31:** Geração de Pacote de Validação (usa serviço de validação)

### Atividades que Usam Este Processo

- **Pilar 2 (Recursos):** Identificar necessidade de serviço
- **Pilar 3.5 (Riscos):** Avaliar riscos de criar script vs API
- **Pilar 4 (Planejamento):** Planejar arquitetura de software
- **Pilar 5 (Validação):** Validar serviços/APIs
- **Pilar 6 (Execução):** Criar/modificar serviços
- **Pilar 7 (Aprendizagem):** Consolidar aprendizados sobre serviços

---

## 📊 MÉTRICAS

### Métricas a Acompanhar

- Total de projetos com software
- Total de serviços ativos (por projeto e geral)
- Total de APIs disponíveis (por projeto e geral)
- Total de OLAs (por projeto e geral)
- Scripts transformados em API (por projeto e geral)
- Scripts legados (manutenção)

### Frequência de Revisão

- **Semanal:** Verificar se há scripts novos a transformar
- **Mensal:** Revisar inventários completos (local e geral)
- **Trimestral:** Revisão completa (este processo)

---

## ✅ VALIDAÇÃO

### Critérios de Sucesso

- [ ] Todos os serviços estão documentados
- [ ] Todos os serviços têm OLA (se públicos)
- [ ] Inventários estão atualizados
- [ ] Scripts de negócio foram transformados em APIs
- [ ] Documentação está completa e acessível

---

**Última atualização:** 4 de Janeiro de 2026

