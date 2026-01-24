# F-1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-METODO-011 — Governança de Bancos de Contexto  
**Versão:** 1.0  
**Data:** 23 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Executor:** Manus  
**Chefe de Produto:** CEO (Joubert Jr)

---

## 🔒 END — ESTADO FINAL ESPERADO (EXATO)

> "Existe um contrato que define como bancos de contexto são criados, versionados e usados por produtos."

### Critérios de Aceitação (Binários)

**PASS:**
- ✅ Documento `/METODO/GOVERNANCA_CONTEXTO.md` criado
- ✅ Estrutura de CONTEXTO definida:
  - CONTEXTO é versionado
  - CONTEXTO tem fonte rastreável
  - CONTEXTO é referenciado nos outputs
- ✅ Regra explícita: "CONTEXTO ≠ prompt solto"
- ✅ Critérios de PASS/FAIL para criação de contexto definidos
- ✅ Formato de versionamento de contexto definido

**FAIL:**
- ❌ Documento não existe
- ❌ Estrutura de CONTEXTO não está definida
- ❌ Regra de versionamento não está explícita
- ❌ Fonte não é obrigatória
- ❌ Referência em outputs não é obrigatória

---

## 📋 FASES DE EXECUÇÃO

### F1 — Definir Estrutura Canônica de CONTEXTO

**END desta fase:**
> "A estrutura canônica de CONTEXTO está definida com todas as pastas obrigatórias, formato de arquivo e metadados obrigatórios."

**Artefato:**
- Seção "Estrutura Canônica de CONTEXTO" no documento `/METODO/GOVERNANCA_CONTEXTO.md`

**Critérios de PASS:**
- ✅ Estrutura de pastas definida:
  ```
  /PRODUTOS/<produto>/CONTEXTO/
    <tipo>_<nome>_v<versao>.md
    metadata.json
  ```
- ✅ Formato de arquivo definido (Markdown + metadata JSON)
- ✅ Campos obrigatórios de metadata definidos:
  - `contexto_id`
  - `tipo` (lei, norma, modelo, doutrina, acórdão)
  - `nome`
  - `versao`
  - `fonte_url`
  - `fonte_tipo`
  - `data_obtencao`
  - `hash_conteudo`
- ✅ Propósito de cada campo documentado

**Critérios de FAIL:**
- ❌ Estrutura de pastas não definida
- ❌ Formato de arquivo não definido
- ❌ Campos obrigatórios não listados
- ❌ Propósito dos campos não documentado

---

### F2 — Definir Regras de Fonte Rastreável

**END desta fase:**
> "As regras de fonte rastreável estão explícitas e inequívocas, com critérios binários de validação."

**Artefato:**
- Seção "Regras de Fonte Rastreável" no documento

**Critérios de PASS:**
- ✅ Regra explícita: "Todo CONTEXTO DEVE ter fonte rastreável"
- ✅ Tipos de fonte válidos definidos:
  - URL pública (lei, norma, acórdão)
  - Documento oficial (com hash)
  - Modelo canônico (com versão)
  - Doutrina (com referência bibliográfica)
- ✅ Formato de referência de fonte definido
- ✅ Critérios de validação de fonte definidos:
  - URL deve ser acessível ou arquivada
  - Documento deve ter hash verificável
  - Modelo deve ter versão rastreável
  - Doutrina deve ter referência completa
- ✅ Exemplos de fontes válidas e inválidas

**Critérios de FAIL:**
- ❌ Regra de fonte não está explícita
- ❌ Tipos de fonte não definidos
- ❌ Formato de referência não definido
- ❌ Critérios de validação não definidos
- ❌ Exemplos não fornecidos

---

### F3 — Definir Versionamento de CONTEXTO

**END desta fase:**
> "O sistema de versionamento de CONTEXTO está definido com regras claras de incremento e rastreabilidade."

**Artefato:**
- Seção "Versionamento de CONTEXTO" no documento

**Critérios de PASS:**
- ✅ Formato de versionamento definido: `v<major>.<minor>`
  - `major`: mudança de conteúdo (nova lei, alteração substancial)
  - `minor`: correção, atualização de fonte, ajuste de formato
- ✅ Regras de incremento de versão definidas:
  - Quando incrementar `major`
  - Quando incrementar `minor`
- ✅ Regra de imutabilidade: versão publicada não muda
- ✅ Regra de deprecação: versão antiga é marcada como `deprecated`
- ✅ Formato de nome de arquivo com versão: `<tipo>_<nome>_v<versao>.md`
- ✅ Exemplos de versionamento

**Critérios de FAIL:**
- ❌ Formato de versionamento não definido
- ❌ Regras de incremento não definidas
- ❌ Regra de imutabilidade não explícita
- ❌ Regra de deprecação não definida
- ❌ Formato de nome não definido
- ❌ Exemplos não fornecidos

---

### F4 — Definir Formato de Referência em Outputs

**END desta fase:**
> "O formato de referência de CONTEXTO em outputs está definido com metadata obrigatória e rastreabilidade garantida."

**Artefato:**
- Seção "Referência de CONTEXTO em Outputs" no documento

**Critérios de PASS:**
- ✅ Formato de referência definido:
  ```json
  {
    "contexto_usado": [
      {
        "contexto_id": "lei_14133_v2.0",
        "tipo": "lei",
        "nome": "Lei 14.133/2021",
        "versao": "v2.0",
        "path": "/PRODUTOS/contratacao-ti/CONTEXTO/lei_14133_v2.0.md",
        "hash": "sha256:abc123..."
      }
    ]
  }
  ```
- ✅ Campos obrigatórios de referência definidos
- ✅ Regra explícita: "Todo OUTPUT DEVE conter metadata de CONTEXTO usado"
- ✅ Critérios de validação de referência:
  - `contexto_id` deve existir
  - `versao` deve ser válida
  - `path` deve ser acessível
  - `hash` deve bater com o conteúdo
- ✅ Exemplos de referência válida e inválida

**Critérios de FAIL:**
- ❌ Formato de referência não definido
- ❌ Campos obrigatórios não listados
- ❌ Regra de obrigatoriedade não explícita
- ❌ Critérios de validação não definidos
- ❌ Exemplos não fornecidos

---

### F5 — Definir Critérios de PASS/FAIL para Criação de CONTEXTO

**END desta fase:**
> "Os critérios binários de PASS/FAIL para criação de CONTEXTO estão definidos e auditáveis."

**Artefato:**
- Seção "Critérios de PASS/FAIL para Criação de CONTEXTO" no documento

**Critérios de PASS:**
- ✅ Critérios de PASS listados:
  - ✅ CONTEXTO tem fonte rastreável
  - ✅ CONTEXTO está versionado
  - ✅ CONTEXTO tem metadata completa
  - ✅ CONTEXTO está no path canônico
  - ✅ CONTEXTO tem hash verificável
- ✅ Critérios de FAIL listados:
  - ❌ CONTEXTO sem fonte
  - ❌ CONTEXTO sem versão
  - ❌ CONTEXTO sem metadata
  - ❌ CONTEXTO fora do path canônico
  - ❌ CONTEXTO sem hash
- ✅ Critérios são binários (sem ambiguidade)
- ✅ Critérios são auditáveis (verificáveis por script)

**Critérios de FAIL:**
- ❌ Critérios de PASS não listados
- ❌ Critérios de FAIL não listados
- ❌ Critérios são ambíguos
- ❌ Critérios não são auditáveis

---

### F6 — Criar Documento Completo e Validar

**END desta fase:**
> "O documento `/METODO/GOVERNANCA_CONTEXTO.md` está completo, revisado, validado e commitado."

**Artefato:**
- `/METODO/GOVERNANCA_CONTEXTO.md` (completo)
- Commit no repositório

**Critérios de PASS:**
- ✅ Documento contém todas as seções (F1-F5)
- ✅ Documento está formatado corretamente
- ✅ Documento está revisado (sem placeholders, TODOs)
- ✅ Documento está commitado no repositório
- ✅ Commit message segue padrão
- ✅ Documento está no GitHub
- ✅ Demanda marcada como concluída

**Critérios de FAIL:**
- ❌ Documento incompleto
- ❌ Documento mal formatado
- ❌ Documento não revisado
- ❌ Documento não commitado
- ❌ Commit message fora do padrão
- ❌ Documento não está no GitHub
- ❌ Demanda não marcada como concluída

---

## 🚫 REGRAS CANÔNICAS

**Governança de Contexto:**
> "CONTEXTO não é prompt solto. CONTEXTO é artefato versionado com fonte rastreável."

**Rastreabilidade de Fonte:**
> "Todo CONTEXTO DEVE ter fonte (lei, norma, modelo, doutrina). Contexto sem fonte é FAIL estrutural."

**Referência Obrigatória:**
> "Todo OUTPUT gerado DEVE referenciar o CONTEXTO usado. Output sem referência é FAIL estrutural."

---

## 🧱 BLOQUEIOS ESTRUTURAIS

### Bloqueios Técnicos
- Nenhum

### Bloqueios de Método
- Nenhum

### Bloqueios de Governança
- Nenhum

---

## ❌ FORA DE ESCOPO

- Criação de bancos de contexto específicos (isso será feito em demandas de produto)
- Implementação de software para gerenciar contextos
- Migração de contextos existentes

---

## 📌 STATUS

**Status atual:** Aprovado  
**Próximo passo:** Executar F1

---

## 🧭 REGRA FINAL

> "CONTEXTO sem fonte é prompt solto. CONTEXTO sem versionamento é perda de rastreabilidade. Governança de contexto é condição de passagem para qualquer produto no método END-FIRST."
