# F-1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-METODO-012 — Versionamento Cruzado (Método x Produto x Execução)  
**Versão:** 1.0  
**Data:** 23 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Executor:** Manus  
**Chefe de Produto:** CEO (Joubert Jr)

---

## 🔒 END — ESTADO FINAL ESPERADO (EXATO)

> "Todo output gerado por um produto registra: versão do método, versão do produto, versão do contexto e id da execução."

### Critérios de Aceitação (Binários)

**PASS:**
- ✅ Documento `/METODO/VERSIONAMENTO_CRUZADO.md` criado
- ✅ Campos obrigatórios definidos:
  - `metodo_version` (ex: `END-FIRST v2.5`)
  - `produto_version` (ex: `contratacao-ti v1.2`)
  - `contexto_version` (ex: `lei-14133 v2.0`)
  - `execucao_id` (ex: `exec-2026-01-23-001`)
- ✅ Formato de versionamento definido
- ✅ Critérios de PASS/FAIL para versionamento definidos
- ✅ Exemplo de output com versionamento cruzado fornecido

**FAIL:**
- ❌ Documento não existe
- ❌ Campos obrigatórios não estão definidos
- ❌ Formato de versionamento não está explícito
- ❌ Critérios de PASS/FAIL não estão definidos
- ❌ Exemplo não está fornecido

---

## 📋 FASES DE EXECUÇÃO

### F1 — Definir Campos Obrigatórios de Versionamento

**END desta fase:**
> "Os 4 campos obrigatórios de versionamento cruzado estão definidos com formato, propósito e exemplos."

**Artefato:**
- Seção "Campos Obrigatórios de Versionamento" no documento `/METODO/VERSIONAMENTO_CRUZADO.md`

**Critérios de PASS:**
- ✅ Campo `metodo_version` definido:
  - Formato: `END-FIRST v<major>.<minor>`
  - Propósito: Rastrear versão do método usado
  - Exemplo: `END-FIRST v2.5`
- ✅ Campo `produto_version` definido:
  - Formato: `<produto-id> v<major>.<minor>`
  - Propósito: Rastrear versão do produto usado
  - Exemplo: `contratacao-ti v1.2`
- ✅ Campo `contexto_version` definido:
  - Formato: `<contexto-id> v<major>.<minor>`
  - Propósito: Rastrear versão do contexto usado
  - Exemplo: `lei-14133 v2.0`
- ✅ Campo `execucao_id` definido:
  - Formato: `exec-<YYYY-MM-DD>-<seq>`
  - Propósito: Rastrear execução específica
  - Exemplo: `exec-2026-01-23-001`
- ✅ Propósito de cada campo documentado
- ✅ Exemplos fornecidos para cada campo

**Critérios de FAIL:**
- ❌ Algum campo não definido
- ❌ Formato não especificado
- ❌ Propósito não documentado
- ❌ Exemplos não fornecidos

---

### F2 — Definir Formato de Metadata de Versionamento

**END desta fase:**
> "O formato de metadata de versionamento está definido como JSON Schema com validação automática."

**Artefato:**
- Seção "Formato de Metadata de Versionamento" no documento
- JSON Schema de validação

**Critérios de PASS:**
- ✅ Formato JSON definido:
  ```json
  {
    "versionamento": {
      "metodo_version": "END-FIRST v2.5",
      "produto_version": "contratacao-ti v1.2",
      "contexto_version": "lei-14133 v2.0",
      "execucao_id": "exec-2026-01-23-001",
      "timestamp": "2026-01-23T19:42:00Z",
      "executor": "Manus"
    }
  }
  ```
- ✅ JSON Schema de validação definido:
  - Campos obrigatórios marcados como `required`
  - Formato de cada campo validado por regex
  - Tipos de dados especificados
- ✅ Exemplo de metadata válida fornecido
- ✅ Exemplo de metadata inválida fornecido
- ✅ Regra explícita: "Metadata DEVE ser validada antes de gerar output"

**Critérios de FAIL:**
- ❌ Formato JSON não definido
- ❌ JSON Schema não definido
- ❌ Exemplos não fornecidos
- ❌ Regra de validação não explícita

---

### F3 — Definir Formato de Versionamento por Tipo

**END desta fase:**
> "Os formatos de versionamento para Método, Produto e Contexto estão definidos com regras de incremento."

**Artefato:**
- Seção "Formato de Versionamento por Tipo" no documento

**Critérios de PASS:**
- ✅ Versionamento de Método definido:
  - Formato: `v<major>.<minor>`
  - `major`: mudança de estrutura (breaking change)
  - `minor`: adição de funcionalidade (não-breaking)
  - Exemplo: `v2.5` → `v2.6` (nova demanda) → `v3.0` (reestruturação)
- ✅ Versionamento de Produto definido:
  - Formato: `v<major>.<minor>`
  - `major`: mudança de fluxo ou contexto principal
  - `minor`: ajuste de template ou correção
  - Exemplo: `v1.2` → `v1.3` (ajuste) → `v2.0` (novo fluxo)
- ✅ Versionamento de Contexto definido:
  - Formato: `v<major>.<minor>`
  - `major`: mudança de conteúdo (nova lei, alteração substancial)
  - `minor`: correção, atualização de fonte
  - Exemplo: `v2.0` → `v2.1` (correção) → `v3.0` (nova lei)
- ✅ Regras de incremento documentadas
- ✅ Exemplos de incremento fornecidos

**Critérios de FAIL:**
- ❌ Formato não definido para algum tipo
- ❌ Regras de incremento não documentadas
- ❌ Exemplos não fornecidos

---

### F4 — Definir Formato de ID de Execução

**END desta fase:**
> "O formato de ID de execução está definido com geração automática e unicidade garantida."

**Artefato:**
- Seção "Formato de ID de Execução" no documento

**Critérios de PASS:**
- ✅ Formato definido: `exec-<YYYY-MM-DD>-<seq>`
  - `YYYY-MM-DD`: data da execução
  - `seq`: sequencial do dia (001, 002, ...)
- ✅ Regra de geração automática:
  - ID é gerado no início da execução
  - Sequencial é incrementado a cada execução do dia
  - ID é único por execução
- ✅ Regra de unicidade:
  - Mesmo produto + mesmo dia → IDs diferentes
  - ID é imutável após geração
- ✅ Exemplo de geração de IDs:
  - Execução 1 do dia: `exec-2026-01-23-001`
  - Execução 2 do dia: `exec-2026-01-23-002`
  - Execução 1 do dia seguinte: `exec-2026-01-24-001`
- ✅ Regra de rastreabilidade:
  - ID permite rastrear execução específica
  - ID permite correlacionar outputs da mesma execução

**Critérios de FAIL:**
- ❌ Formato não definido
- ❌ Regra de geração não especificada
- ❌ Unicidade não garantida
- ❌ Exemplos não fornecidos
- ❌ Rastreabilidade não documentada

---

### F5 — Definir Critérios de PASS/FAIL para Versionamento

**END desta fase:**
> "Os critérios binários de PASS/FAIL para versionamento de outputs estão definidos e auditáveis."

**Artefato:**
- Seção "Critérios de PASS/FAIL para Versionamento" no documento

**Critérios de PASS:**
- ✅ Critérios de PASS listados:
  - ✅ Output contém metadata de versionamento
  - ✅ Metadata tem todos os 4 campos obrigatórios
  - ✅ Formato de cada campo é válido (valida por regex)
  - ✅ Versões referenciadas existem
  - ✅ ID de execução é único
- ✅ Critérios de FAIL listados:
  - ❌ Output sem metadata de versionamento
  - ❌ Metadata sem algum campo obrigatório
  - ❌ Formato de campo inválido
  - ❌ Versão referenciada não existe
  - ❌ ID de execução duplicado
- ✅ Critérios são binários (sem ambiguidade)
- ✅ Critérios são auditáveis (verificáveis por script)
- ✅ Script de validação fornecido (pseudocódigo ou exemplo)

**Critérios de FAIL:**
- ❌ Critérios de PASS não listados
- ❌ Critérios de FAIL não listados
- ❌ Critérios são ambíguos
- ❌ Critérios não são auditáveis
- ❌ Script de validação não fornecido

---

### F6 — Criar Documento Completo e Validar

**END desta fase:**
> "O documento `/METODO/VERSIONAMENTO_CRUZADO.md` está completo, revisado, validado e commitado."

**Artefato:**
- `/METODO/VERSIONAMENTO_CRUZADO.md` (completo)
- Commit no repositório

**Critérios de PASS:**
- ✅ Documento contém todas as seções (F1-F5)
- ✅ Documento inclui exemplo completo de output com versionamento cruzado
- ✅ Documento está formatado corretamente
- ✅ Documento está revisado (sem placeholders, TODOs)
- ✅ Documento está commitado no repositório
- ✅ Commit message segue padrão
- ✅ Documento está no GitHub
- ✅ Demanda marcada como concluída

**Critérios de FAIL:**
- ❌ Documento incompleto
- ❌ Exemplo completo não fornecido
- ❌ Documento mal formatado
- ❌ Documento não revisado
- ❌ Documento não commitado
- ❌ Commit message fora do padrão
- ❌ Documento não está no GitHub
- ❌ Demanda não marcada como concluída

---

## 🚫 REGRAS CANÔNICAS

**Versionamento Cruzado:**
> "Output sem versionamento cruzado é output sem rastreabilidade. Rastreabilidade é condição de passagem."

**Campos Obrigatórios:**
> "Todo OUTPUT DEVE conter: versão do método, versão do produto, versão do contexto e id da execução. Output sem esses campos é FAIL estrutural."

---

## 🧱 BLOQUEIOS ESTRUTURAIS

### Bloqueios Técnicos
- Nenhum

### Bloqueios de Método
- **Depende de:** DEMANDA-METODO-010 (Governança de Produtos)
- **Depende de:** DEMANDA-METODO-011 (Governança de Contexto)

### Bloqueios de Governança
- Nenhum

---

## ❌ FORA DE ESCOPO

- Implementação de software para gerenciar versionamento
- Migração de outputs existentes
- Criação de outputs específicos

---

## 📌 STATUS

**Status atual:** Aprovado  
**Próximo passo:** Executar F1

---

## 🧭 REGRA FINAL

> "Output sem versionamento cruzado é output sem rastreabilidade. Versionamento cruzado é condição de passagem para qualquer output no método END-FIRST."
