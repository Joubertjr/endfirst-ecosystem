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

## 🔒 REGRAS DE GOVERNANÇA

### Regra 1: Criação de Produto

**Regra canônica:**
> "Produto novo DEVE ser criado via DEMANDA-PROD. Produto sem demanda é FAIL estrutural."

**Processo obrigatório:**

1. ✅ Criar DEMANDA-PROD com END explícito
2. ✅ CEO aprova DEMANDA-PROD
3. ✅ Produto cria F-1 da demanda
4. ✅ CEO aprova F-1
5. ✅ Executor cria estrutura canônica em `/PRODUTOS/<produto>/`
6. ✅ Executor executa fases do F-1
7. ✅ Auditor Técnico valida conformidade
8. ✅ CEO valida END atingido

**Papel responsável pela criação:**
- **Produto** (cria demanda e F-1)
- **CEO** (aprova demanda e F-1)
- **Executor** (implementa produto)
- **Auditor Técnico** (valida conformidade)

**Bloqueios:**
- ❌ Produto criado fora de `/PRODUTOS/`
- ❌ Produto sem DEMANDA-PROD correspondente
- ❌ Produto sem estrutura canônica
- ❌ Produto sem README.md

---

### Regra 2: Alteração de Produto

**Regra canônica:**
> "Alteração de produto DEVE ser rastreada via DEMANDA-PROD. Alteração sem demanda é FAIL estrutural."

**Processo obrigatório:**

1. ✅ Criar DEMANDA-PROD para alteração
2. ✅ CEO aprova DEMANDA-PROD
3. ✅ Produto cria F-1 da demanda
4. ✅ CEO aprova F-1
5. ✅ Executor executa alterações
6. ✅ Executor atualiza README.md com nova versão
7. ✅ Executor gera evidência de execução
8. ✅ Auditor Técnico valida conformidade
9. ✅ CEO valida END atingido

**Papel responsável pela alteração:**
- **Produto** (define alteração e cria F-1)
- **CEO** (aprova alteração)
- **Executor** (implementa alteração)
- **Auditor Técnico** (valida conformidade)

**Bloqueios:**
- ❌ Alteração sem DEMANDA-PROD
- ❌ Alteração sem F-1 aprovado
- ❌ README.md não atualizado com nova versão
- ❌ Evidência de execução ausente

---

### Regra 3: Aprovação de Produto

**Regra canônica:**
> "Produto DEVE ser aprovado pelo CEO. Produto sem aprovação do CEO é FAIL estrutural."

**Processo obrigatório:**

1. ✅ Executor declara produto completo
2. ✅ Executor gera evidência de conformidade
3. ✅ Auditor Técnico valida estrutura canônica
4. ✅ Auditor Técnico valida rastreabilidade
5. ✅ Auditor Técnico aplica gates obrigatórios
6. ✅ CEO valida END da DEMANDA-PROD
7. ✅ CEO declara PASS ou FAIL

**Papel responsável pela aprovação:**
- **CEO** (único papel com autoridade para aprovar produto)

**Bloqueios:**
- ❌ Produto sem evidência de conformidade
- ❌ Produto sem validação do Auditor Técnico
- ❌ Produto sem aprovação do CEO
- ❌ END da DEMANDA-PROD não atingido

---

### Regra 4: Auditoria de Produto

**Regra canônica:**
> "Produto DEVE ser auditado pelo Auditor Técnico. Produto sem auditoria é FAIL estrutural."

**Quando auditar:**

1. ✅ Antes da aprovação do CEO (obrigatório)
2. ✅ Após alteração de produto (obrigatório)
3. ✅ Quando gate obrigatório é ativado (obrigatório)
4. ✅ Quando CEO solicita auditoria (opcional)

**Papel responsável pela auditoria:**
- **Auditor Técnico** (único papel com autoridade para auditar)

**O que o Auditor Técnico valida:**

1. ✅ Estrutura canônica presente
2. ✅ README.md existe e está completo
3. ✅ Todas as pastas obrigatórias existem
4. ✅ DEMANDA-PROD existe e está rastreada
5. ✅ F-1 existe e foi aprovado
6. ✅ Evidências de execução existem
7. ✅ Gates obrigatórios foram aplicados
8. ✅ Nenhum placeholder em artefatos
9. ✅ Rastreabilidade total garantida

**Bloqueios:**
- ❌ Estrutura canônica ausente
- ❌ README.md ausente ou incompleto
- ❌ Pastas obrigatórias ausentes
- ❌ DEMANDA-PROD ausente
- ❌ F-1 não aprovado
- ❌ Evidências ausentes
- ❌ Gates não aplicados
- ❌ Placeholders em artefatos
- ❌ Rastreabilidade quebrada

---

### Regra 5: Bloqueio de Produto

**Regra canônica:**
> "Produto que viola regras de governança DEVE ser bloqueado. Bloqueio é FAIL estrutural."

**Condições de bloqueio:**

1. ❌ Produto criado fora do método
2. ❌ Produto sem DEMANDA-PROD
3. ❌ Produto sem estrutura canônica
4. ❌ Produto sem README.md
5. ❌ Produto sem aprovação do CEO
6. ❌ Produto sem auditoria do Auditor Técnico
7. ❌ Produto com placeholders em artefatos
8. ❌ Produto com rastreabilidade quebrada
9. ❌ Produto que falha em gate obrigatório

**Papel responsável pelo bloqueio:**
- **Auditor Técnico** (bloqueia por violação técnica)
- **CEO** (bloqueia por violação de governança)

**Consequência do bloqueio:**
- ❌ Produto não pode ser usado
- ❌ Produto não pode ser publicado
- ❌ Produto não pode ser versionado
- ❌ Produto DEVE ser corrigido antes de PASS

---

## ✅ CRITÉRIOS DE PASS/FAIL PARA CRIAÇÃO DE PRODUTO

### Critérios Binários de PASS

Um produto PASSA se e somente se:

#### 1. Estrutura Canônica Completa

**Critério:**
- ✅ Produto está em `/PRODUTOS/<produto>/`
- ✅ README.md existe e contém todos os campos obrigatórios
- ✅ Pasta `DEMANDAS/` existe
- ✅ Pasta `planejamento/` existe
- ✅ Pasta `EVIDENCIAS/` existe
- ✅ Pasta `CONTEXTO/` existe
- ✅ Pasta `OUTPUTS/` existe

**Relação com:**
- **Estrutura canônica:** Definida na seção "Estrutura Canônica de Produto"
- **Regra de governança:** Regra 1 (Criação de Produto)
- **Papel responsável:** Executor (cria estrutura)

**Bloqueio automático se:**
- ❌ Produto fora de `/PRODUTOS/`
- ❌ README.md ausente
- ❌ Qualquer pasta obrigatória ausente

---

#### 2. Rastreabilidade Total

**Critério:**
- ✅ DEMANDA-PROD existe em `/PRODUTOS/<produto>/DEMANDAS/`
- ✅ DEMANDA-PROD tem END explícito
- ✅ DEMANDA-PROD foi aprovada pelo CEO
- ✅ F-1 da DEMANDA-PROD existe
- ✅ F-1 foi aprovado pelo CEO
- ✅ Evidências de execução existem em `/PRODUTOS/<produto>/EVIDENCIAS/`

**Relação com:**
- **Estrutura canônica:** Pasta `DEMANDAS/` e `EVIDENCIAS/`
- **Regra de governança:** Regra 1 (Criação de Produto) e Regra 4 (Auditoria)
- **Papel responsável:** Produto (cria demanda), CEO (aprova), Executor (gera evidências)

**Bloqueio automático se:**
- ❌ DEMANDA-PROD ausente
- ❌ DEMANDA-PROD sem END
- ❌ DEMANDA-PROD não aprovada
- ❌ F-1 ausente ou não aprovado
- ❌ Evidências ausentes

---

#### 3. Aprovação Formal

**Critério:**
- ✅ Auditor Técnico validou estrutura canônica
- ✅ Auditor Técnico validou rastreabilidade
- ✅ Auditor Técnico aplicou gates obrigatórios
- ✅ CEO validou END da DEMANDA-PROD
- ✅ CEO declarou PASS

**Relação com:**
- **Regra de governança:** Regra 3 (Aprovação de Produto) e Regra 4 (Auditoria)
- **Papel responsável:** Auditor Técnico (valida), CEO (aprova)
- **Ontologia de personas:** `/METODO/PERSONAS/DEFINICOES/CEO.md` e `/METODO/PERSONAS/DEFINICOES/AUDITOR_TECNICO.md`

**Bloqueio automático se:**
- ❌ Auditor Técnico não validou
- ❌ Gates obrigatórios não aplicados
- ❌ CEO não aprovou
- ❌ END não atingido

---

#### 4. Conformidade Técnica

**Critério:**
- ✅ README.md contém: Nome, Descrição, Versão, Instruções, Dependências, Licença
- ✅ README.md referencia versão do método END-FIRST usado
- ✅ Nenhum placeholder (TODO/TBD/PLACEHOLDER) em artefatos
- ✅ Todos os arquivos obrigatórios existem
- ✅ Metadata obrigatória presente em outputs

**Relação com:**
- **Estrutura canônica:** README.md e OUTPUTS/
- **Regra de governança:** Regra 4 (Auditoria) e Regra 5 (Bloqueio)
- **Papel responsável:** Executor (implementa), Auditor Técnico (valida)

**Bloqueio automático se:**
- ❌ README.md incompleto
- ❌ Placeholders em artefatos
- ❌ Arquivos obrigatórios ausentes
- ❌ Metadata ausente em outputs

---

### Critérios Binários de FAIL

Um produto FALHA se:

#### 1. Violação Estrutural

**Critério de FAIL:**
- ❌ Produto criado fora de `/PRODUTOS/`
- ❌ Estrutura canônica ausente ou incompleta
- ❌ README.md ausente
- ❌ Qualquer pasta obrigatória ausente

**Consequência:**
- ❌ Produto é bloqueado imediatamente
- ❌ Produto não pode ser usado
- ❌ Produto DEVE ser corrigido antes de PASS

**Papel que bloqueia:** Auditor Técnico

---

#### 2. Violação de Rastreabilidade

**Critério de FAIL:**
- ❌ Produto sem DEMANDA-PROD
- ❌ DEMANDA-PROD sem END
- ❌ DEMANDA-PROD não aprovada pelo CEO
- ❌ F-1 ausente ou não aprovado
- ❌ Evidências de execução ausentes

**Consequência:**
- ❌ Produto é bloqueado imediatamente
- ❌ Rastreabilidade quebrada
- ❌ Produto DEVE ser corrigido antes de PASS

**Papel que bloqueia:** Auditor Técnico

---

#### 3. Violação de Governança

**Critério de FAIL:**
- ❌ Produto criado fora do método
- ❌ Produto sem aprovação do CEO
- ❌ Produto sem auditoria do Auditor Técnico
- ❌ Produto que falha em gate obrigatório

**Consequência:**
- ❌ Produto é bloqueado imediatamente
- ❌ Governança violada
- ❌ Produto DEVE ser corrigido antes de PASS

**Papel que bloqueia:** CEO

---

#### 4. Violação Técnica

**Critério de FAIL:**
- ❌ README.md incompleto ou desatualizado
- ❌ Placeholders em artefatos
- ❌ Arquivos obrigatórios ausentes
- ❌ Metadata ausente em outputs
- ❌ Outputs não referenciam CONTEXTO usado

**Consequência:**
- ❌ Produto é bloqueado imediatamente
- ❌ Conformidade técnica violada
- ❌ Produto DEVE ser corrigido antes de PASS

**Papel que bloqueia:** Auditor Técnico

---

### Critérios de Bloqueio Automático

**Bloqueio automático ocorre quando:**

1. ❌ Produto viola estrutura canônica
2. ❌ Produto viola rastreabilidade
3. ❌ Produto viola governança
4. ❌ Produto viola conformidade técnica
5. ❌ Produto falha em gate obrigatório
6. ❌ Auditor Técnico declara FAIL
7. ❌ CEO declara FAIL

**Quando bloqueio é ativado:**
- ❌ Produto não pode ser usado
- ❌ Produto não pode ser publicado
- ❌ Produto não pode ser versionado
- ❌ Produto DEVE ser corrigido
- ❌ Nova auditoria é obrigatória após correção

---

### Relação com Ontologia de Personas

**Papéis envolvidos na criação de produto:**

| Papel | Arquivo de Definição | Responsabilidade na Criação |
|---|---|---|
| **Produto** | `/METODO/PERSONAS/DEFINICOES/PRODUTO.md` | Cria DEMANDA-PROD, define END, cria F-1 |
| **CEO** | `/METODO/PERSONAS/DEFINICOES/CEO.md` | Aprova DEMANDA-PROD, aprova F-1, valida END, declara PASS/FAIL |
| **Executor** | `/METODO/PERSONAS/DEFINICOES/EXECUTOR.md` | Cria estrutura canônica, executa fases, gera evidências |
| **Auditor Técnico** | `/METODO/PERSONAS/DEFINICOES/AUDITOR_TECNICO.md` | Valida estrutura, valida rastreabilidade, aplica gates, bloqueia se FAIL |

**Vínculos:**
- `/METODO/PERSONAS/VINCULOS_PROCESSO/PAPEL_TIPO_PRODUTO.md` (define papel principal por tipo de produto)
- `/METODO/PERSONAS/VINCULOS_PROCESSO/PAPEL_TIPO_DEMANDA.md` (define papel principal por tipo de demanda)

---

## 📌 STATUS DA CONSTRUÇÃO

**Seções Concluídas:**
- ✅ F1: Estrutura Canônica de Produto
- ✅ F2: Regras de Governança
- ✅ F3: Critérios de PASS/FAIL

**Próximas Seções:**
- ⏳ F4: Versionamento de Produto

---

**Documento em construção conforme DEMANDA-METODO-010.**
