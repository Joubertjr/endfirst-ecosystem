---
document_id: GOVERNANCA_PRODUTOS
type: canonical
owner: CEO (Joubert Jr)
status: in_progress
governed_by: /METODO/END_FIRST_V2.md
version: 1.0
created_at: 2026-01-23
demanda_origem: DEMANDA-METODO-010
---

# GOVERNANÇA DE PRODUTOS — END-FIRST v2

**Versão:** 1.0  
**Data:** 23 de Janeiro de 2026  
**Status:** Em Construção (F1 Concluída)  
**Demanda de Origem:** DEMANDA-METODO-010  
**Path Canônico:** `/METODO/GOVERNANCA_PRODUTOS.md`

---

## 🎯 O QUE É GOVERNANÇA DE PRODUTOS

A **Governança de Produtos** é o contrato formal que define como produtos são criados, versionados e governados dentro do repositório `endfirst-ecosystem`.

**Princípio fundamental:**
> "Produto não nasce fora do método. Produto sem governança é software sem rastreabilidade."

---

## 🔒 REGRA ABSOLUTA

**Todo produto DEVE seguir este contrato.**

**Produtos fora do contrato são FAIL estrutural.**

---

## 📁 ESTRUTURA CANÔNICA DE PRODUTO

### Estrutura Obrigatória

Todo produto DEVE seguir a seguinte estrutura de pastas:

```
/PRODUTOS/<produto>/
  README.md
  DEMANDAS/
  planejamento/
  EVIDENCIAS/
  CONTEXTO/
  OUTPUTS/
```

### Propósito de Cada Pasta

#### 1. `README.md` (Arquivo Obrigatório)

**Propósito:**
- Documentar o produto
- Explicar o que o produto faz
- Definir como usar o produto
- Listar dependências e requisitos

**Conteúdo Obrigatório:**
- Nome do produto
- Descrição do produto
- Versão do produto
- Versão do método END-FIRST usado
- Instruções de uso
- Dependências
- Licença

**Critério de PASS:**
- ✅ README.md existe
- ✅ README.md contém todos os campos obrigatórios
- ✅ README.md está atualizado

**Critério de FAIL:**
- ❌ README.md não existe
- ❌ README.md não contém campos obrigatórios
- ❌ README.md está desatualizado

---

#### 2. `DEMANDAS/` (Pasta Obrigatória)

**Propósito:**
- Armazenar todas as demandas do produto
- Rastrear evolução do produto
- Documentar decisões de produto

**Conteúdo:**
- Demandas de produto (DEMANDA-PROD-XXX)
- F-1s de demandas
- Evidências de execução

**Critério de PASS:**
- ✅ Pasta DEMANDAS/ existe
- ✅ Demandas seguem template canônico
- ✅ Demandas têm F-1s quando obrigatório

**Critério de FAIL:**
- ❌ Pasta DEMANDAS/ não existe
- ❌ Demandas não seguem template
- ❌ Demandas sem F-1s obrigatórios

---

#### 3. `planejamento/` (Pasta Obrigatória)

**Propósito:**
- Armazenar planejamentos de execução
- Documentar fluxos END-FIRST
- Rastrear fases de execução

**Conteúdo:**
- Fluxos END-FIRST
- Planejamentos de execução
- Definições de fases

**Critério de PASS:**
- ✅ Pasta planejamento/ existe
- ✅ Fluxos END-FIRST documentados
- ✅ Fases de execução definidas

**Critério de FAIL:**
- ❌ Pasta planejamento/ não existe
- ❌ Fluxos não documentados
- ❌ Fases não definidas

---

#### 4. `EVIDENCIAS/` (Pasta Obrigatória)

**Propósito:**
- Armazenar evidências de execução
- Provar conformidade
- Permitir auditoria

**Conteúdo:**
- Evidências de execução de demandas
- Logs de execução
- Provas de conformidade

**Critério de PASS:**
- ✅ Pasta EVIDENCIAS/ existe
- ✅ Evidências de execução registradas
- ✅ Evidências são auditáveis

**Critério de FAIL:**
- ❌ Pasta EVIDENCIAS/ não existe
- ❌ Evidências não registradas
- ❌ Evidências não são auditáveis

---

#### 5. `CONTEXTO/` (Pasta Obrigatória)

**Propósito:**
- Armazenar bancos de contexto versionados
- Documentar fontes de conhecimento
- Rastrear legislação, normas, modelos

**Conteúdo:**
- Bancos de contexto versionados
- Leis, normas, regulamentos
- Modelos, templates
- Doutrina, artigos

**Critério de PASS:**
- ✅ Pasta CONTEXTO/ existe
- ✅ Contextos são versionados
- ✅ Contextos têm fonte rastreável

**Critério de FAIL:**
- ❌ Pasta CONTEXTO/ não existe
- ❌ Contextos não são versionados
- ❌ Contextos sem fonte rastreável

---

#### 6. `OUTPUTS/` (Pasta Obrigatória)

**Propósito:**
- Armazenar outputs gerados pelo produto
- Rastrear execuções
- Permitir auditoria de outputs

**Conteúdo:**
- Outputs gerados pelo produto
- Documentos gerados
- Relatórios gerados

**Critério de PASS:**
- ✅ Pasta OUTPUTS/ existe
- ✅ Outputs têm metadata obrigatória
- ✅ Outputs referenciam CONTEXTO usado

**Critério de FAIL:**
- ❌ Pasta OUTPUTS/ não existe
- ❌ Outputs sem metadata
- ❌ Outputs não referenciam CONTEXTO

---

## 📌 STATUS DA CONSTRUÇÃO

**Seções Concluídas:**
- ✅ F1: Estrutura Canônica de Produto

**Próximas Seções:**
- ⏳ F2: Regras de Governança
- ⏳ F3: Critérios de PASS/FAIL
- ⏳ F4: Versionamento de Produto

---

**Documento em construção conforme DEMANDA-METODO-010.**
