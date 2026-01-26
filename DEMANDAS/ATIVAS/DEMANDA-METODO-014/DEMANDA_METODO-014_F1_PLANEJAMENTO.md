# F-1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-METODO-014 — Personas Operacionais do Método  
**Versão:** 1.0  
**Data:** 23 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Executor:** Manus  
**Chefe de Produto:** CEO (Joubert Jr)

---

## 🔒 END — ESTADO FINAL ESPERADO (EXATO)

> "Existe definição formal de personas: CEO, Chefe de Produto e Executor (IA / humano), com responsabilidade, permissões e papéis no fluxo."

---

## 🔒 Regras estruturais adicionais (obrigatórias)

**Fonte Única de Verdade (Personas):**

> “Persona só é válida se existir em /METODO/PERSONAS//.
> Qualquer definição fora disso é FAIL estrutural.”

**Persona como artefatos (não prompt):**

> "Persona = conjunto de artefatos canônicos (definição, playbook, regras, gates, checklist e evidências-modelo), não um prompt."

**Proibição de persona sem diretório canônico:**

> "Nenhuma persona pode ser ativada sem diretório próprio em /METODO/PERSONAS// contendo definição, playbook, regras, gates e checklist."

### Critérios de Aceitação (Binários)

**PASS:**
- ✅ Documento `/METODO/PERSONAS_OPERACIONAIS.md` criado
- ✅ Personas definidas:
  - **CEO:** Aprova demandas, aprova F-1s, define prioridades
  - **Chefe de Produto:** Cria demandas, cria F-1s, valida execução
  - **Executor:** Executa F-1s, gera evidências, registra outputs
- ✅ Responsabilidades de cada persona definidas
- ✅ Permissões de cada persona definidas
- ✅ Papéis no fluxo de cada persona definidos
- ✅ Critérios de PASS/FAIL para cada persona definidos
- ✅ Referência direta à fonte única de personas: `/METODO/PERSONAS//`
- ✅ Regra explícita: persona = conjunto de artefatos, não prompt
- ✅ Proibição explícita: persona sem diretório canônico é FAIL estrutural

**FAIL:**
- ❌ Documento não existe
- ❌ Personas não estão definidas
- ❌ Responsabilidades não estão definidas
- ❌ Permissões não estão definidas
- ❌ Papéis no fluxo não estão definidos
- ❌ Critérios de PASS/FAIL não estão definidos
- ❌ Persona referenciada fora de `/METODO/PERSONAS//` (dupla fonte de verdade)
- ❌ Persona tratada como prompt (sem artefatos)
- ❌ Persona ativada sem diretório canônico

---

## 📋 FASES DE EXECUÇÃO

### F1 — Definir Persona CEO

**END desta fase:**
> "A persona CEO está definida com responsabilidades, permissões e papéis no fluxo."

**Artefato:**
- Seção "Persona CEO" no documento `/METODO/PERSONAS_OPERACIONAIS.md`

**Critérios de PASS:**
- ✅ Responsabilidades do CEO definidas:
  - Aprovar demandas (status: backlog → approved)
  - Aprovar F-1s (status: pending → approved)
  - Definir prioridades de execução
  - Validar END de demandas
  - Decidir PASS/FAIL final de demandas
- ✅ Permissões do CEO definidas:
  - ✅ Pode: Aprovar demandas
  - ✅ Pode: Aprovar F-1s
  - ✅ Pode: Definir prioridades
  - ✅ Pode: Validar END
  - ✅ Pode: Decidir PASS/FAIL
  - ❌ NÃO pode: Executar F-1s
  - ❌ NÃO pode: Criar artefatos de execução
  - ❌ NÃO pode: Modificar método sem demanda
- ✅ Papéis no fluxo definidos:
  - Recebe demanda do Chefe de Produto
  - Valida END da demanda
  - Aprova ou rejeita demanda
  - Recebe F-1 do Chefe de Produto
  - Aprova ou rejeita F-1
  - Define prioridade de execução
  - Recebe resultado final do Executor
  - Decide PASS/FAIL final
- ✅ Exemplos de ações do CEO fornecidos

**Critérios de FAIL:**
- ❌ Responsabilidades não definidas
- ❌ Permissões não definidas
- ❌ Papéis no fluxo não definidos
- ❌ Exemplos não fornecidos

---

### F2 — Definir Persona Chefe de Produto

**END desta fase:**
> "A persona Chefe de Produto está definida com responsabilidades, permissões e papéis no fluxo."

**Artefato:**
- Seção "Persona Chefe de Produto" no documento

**Critérios de PASS:**
- ✅ Responsabilidades do Chefe de Produto definidas:
  - Criar demandas a partir de problemas observados
  - Definir END (Estado Final Esperado) de demandas
  - Definir critérios de PASS/FAIL de demandas
  - Criar F-1s (Planejamentos Canônicos)
  - Validar execução de fases
  - Validar artefatos gerados
- ✅ Permissões do Chefe de Produto definidas:
  - ✅ Pode: Criar demandas
  - ✅ Pode: Definir END
  - ✅ Pode: Definir critérios de PASS/FAIL
  - ✅ Pode: Criar F-1s
  - ✅ Pode: Validar execução
  - ✅ Pode: Validar artefatos
  - ❌ NÃO pode: Aprovar demandas (só CEO)
  - ❌ NÃO pode: Aprovar F-1s (só CEO)
  - ❌ NÃO pode: Executar F-1s (só Executor)
  - ❌ NÃO pode: Modificar método sem demanda
- ✅ Papéis no fluxo definidos:
  - Observa problema ou oportunidade
  - Cria demanda com END e critérios
  - Submete demanda para aprovação do CEO
  - Cria F-1 após aprovação da demanda
  - Submete F-1 para aprovação do CEO
  - Valida execução de fases pelo Executor
  - Valida artefatos gerados pelo Executor
  - Declara PASS/FAIL de fases
- ✅ Exemplos de ações do Chefe de Produto fornecidos

**Critérios de FAIL:**
- ❌ Responsabilidades não definidas
- ❌ Permissões não definidas
- ❌ Papéis no fluxo não definidos
- ❌ Exemplos não fornecidos

---

### F3 — Definir Persona Executor

**END desta fase:**
> "A persona Executor está definida com responsabilidades, permissões e papéis no fluxo."

**Artefato:**
- Seção "Persona Executor" no documento

**Critérios de PASS:**
- ✅ Responsabilidades do Executor definidas:
  - Executar F-1s aprovados
  - Gerar artefatos conforme especificação
  - Registrar evidências de execução
  - Registrar outputs gerados
  - Seguir templates canônicos
  - Validar integridade de artefatos
- ✅ Permissões do Executor definidas:
  - ✅ Pode: Executar F-1s aprovados
  - ✅ Pode: Gerar artefatos
  - ✅ Pode: Registrar evidências
  - ✅ Pode: Registrar outputs
  - ✅ Pode: Seguir templates
  - ✅ Pode: Validar integridade
  - ❌ NÃO pode: Aprovar demandas
  - ❌ NÃO pode: Aprovar F-1s
  - ❌ NÃO pode: Modificar END de demandas
  - ❌ NÃO pode: Modificar critérios de PASS/FAIL
  - ❌ NÃO pode: Pular fases do F-1
  - ❌ NÃO pode: Executar demandas não aprovadas
- ✅ Papéis no fluxo definidos:
  - Recebe F-1 aprovado
  - Executa fase por fase sequencialmente
  - Gera artefatos conforme especificação
  - Registra evidência de execução
  - Submete artefatos para validação do Chefe de Produto
  - Aguarda validação antes de prosseguir
  - Registra outputs com versionamento cruzado
- ✅ Executor Universal definido:
  - Executor pode ser IA (ex: Manus, Cursor)
  - Executor pode ser humano (ex: Dev, Designer)
  - Método não distingue
  - Método governa ambos igualmente
- ✅ Exemplos de ações do Executor fornecidos

**Critérios de FAIL:**
- ❌ Responsabilidades não definidas
- ❌ Permissões não definidas
- ❌ Papéis no fluxo não definidos
- ❌ Executor Universal não definido
- ❌ Exemplos não fornecidos

---

### F4 — Definir Critérios de PASS/FAIL para Personas

**END desta fase:**
> "Os critérios binários de PASS/FAIL para cada persona estão definidos e auditáveis."

**Artefato:**
- Seção "Critérios de PASS/FAIL para Personas" no documento

**Critérios de PASS:**
- ✅ Critérios de PASS para CEO:
  - ✅ CEO aprova demandas com END validado
  - ✅ CEO aprova F-1s com fases bem definidas
  - ✅ CEO define prioridades de execução
  - ✅ CEO decide PASS/FAIL final com critérios binários
- ✅ Critérios de FAIL para CEO:
  - ❌ CEO aprova demanda sem END
  - ❌ CEO aprova F-1 sem fases
  - ❌ CEO não define prioridades
  - ❌ CEO decide PASS/FAIL sem critérios
- ✅ Critérios de PASS para Chefe de Produto:
  - ✅ Chefe de Produto cria demandas com END claro
  - ✅ Chefe de Produto define critérios binários de PASS/FAIL
  - ✅ Chefe de Produto cria F-1s com fases bem definidas
  - ✅ Chefe de Produto valida artefatos conforme critérios
- ✅ Critérios de FAIL para Chefe de Produto:
  - ❌ Chefe de Produto cria demanda sem END
  - ❌ Chefe de Produto define critérios ambíguos
  - ❌ Chefe de Produto cria F-1 sem fases
  - ❌ Chefe de Produto valida artefatos sem critérios
- ✅ Critérios de PASS para Executor:
  - ✅ Executor executa F-1s aprovados
  - ✅ Executor gera artefatos conforme especificação
  - ✅ Executor registra evidências de execução
  - ✅ Executor segue templates canônicos
- ✅ Critérios de FAIL para Executor:
  - ❌ Executor executa demanda não aprovada
  - ❌ Executor gera artefatos fora da especificação
  - ❌ Executor não registra evidências
  - ❌ Executor não segue templates
- ✅ Critérios são binários (sem ambiguidade)
- ✅ Critérios são auditáveis (verificáveis por script)

**Critérios de FAIL:**
- ❌ Critérios não definidos para alguma persona
- ❌ Critérios são ambíguos
- ❌ Critérios não são auditáveis

---

### F5 — Definir Fluxo de Interação entre Personas

**END desta fase:**
> "O fluxo de interação entre personas está definido com diagrama e descrição textual."

**Artefato:**
- Seção "Fluxo de Interação entre Personas" no documento

**Critérios de PASS:**
- ✅ Fluxo completo definido:
  1. Chefe de Produto cria demanda
  2. CEO aprova ou rejeita demanda
  3. Chefe de Produto cria F-1
  4. CEO aprova ou rejeita F-1
  5. CEO define prioridade de execução
  6. Executor executa fase por fase
  7. Chefe de Produto valida artefatos de cada fase
  8. Executor registra evidências
  9. Chefe de Produto declara PASS/FAIL de fases
  10. CEO decide PASS/FAIL final da demanda
- ✅ Diagrama de fluxo fornecido (Mermaid ou ASCII)
- ✅ Descrição textual de cada etapa
- ✅ Pontos de decisão identificados
- ✅ Bloqueios entre etapas identificados
- ✅ Exemplos de fluxo completo fornecidos

**Critérios de FAIL:**
- ❌ Fluxo não definido
- ❌ Diagrama não fornecido
- ❌ Descrição textual não fornecida
- ❌ Pontos de decisão não identificados
- ❌ Bloqueios não identificados
- ❌ Exemplos não fornecidos

---

### F6 — Criar Documento Completo e Validar

**END desta fase:**
> "O documento `/METODO/PERSONAS_OPERACIONAIS.md` está completo, revisado, validado e commitado."

**Artefato:**
- `/METODO/PERSONAS_OPERACIONAIS.md` (completo)
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

**Personas Operacionais:**
> "Persona sem responsabilidade é papel sem governança. Persona sem permissão é papel sem autoridade."

**Separação de Responsabilidades:**
> "CEO aprova. Chefe de Produto planeja. Executor executa. Mistura de papéis é FAIL estrutural."

**Executor Universal:**
> "Executor pode ser IA ou humano. Método não distingue. Método governa."

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

- Implementação de software para gerenciar personas
- Criação de personas específicas de produtos (isso será feito em demandas de produto)
- Migração de personas existentes

---

## 📌 STATUS

**Status atual:** Aprovado  
**Próximo passo:** Executar F1

---

## 🧭 REGRA FINAL

> "Persona sem responsabilidade é papel sem governança. Persona sem permissão é papel sem autoridade. Personas operacionais são condição de passagem para qualquer execução no método END-FIRST."
