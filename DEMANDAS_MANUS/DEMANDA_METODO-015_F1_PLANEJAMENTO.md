# F-1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-METODO-015 — Mecanismo Dinâmico de Ativação de Papéis  
**Versão:** 1.0  
**Data:** 23 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Executor:** Manus  
**Chefe de Produto:** CEO (Joubert Jr)

---

## 🔒 END — ESTADO FINAL ESPERADO (EXATO)

> "Dado um contexto (produto + tipo de demanda + classe + fase), o método determina automaticamente qual papel está ativo, quais decisões são permitidas, quais perguntas são obrigatórias e quais evidências bloqueiam PASS — de forma auditável e sem depender de explicação humana."

### Critérios de Aceitação (Binários)

**PASS:**
- ✅ Existe um artefato canônico no método com:
  - Papéis (CEO, Produto, Executor, Auditor)
  - Autoridade de cada papel
  - Proibições de cada papel
  - Checklist obrigatório por papel
  - Evidências obrigatórias por papel
- ✅ Existe um artefato canônico com regras de ativação dinâmica:
  - Matriz de contexto → perfil ativo
  - INPUTS: Classe (A/B/C/D), Tipo (Método/Produto/Software), Fase (F-1, F1-F6), Produto alvo, Risco
  - OUTPUT: Papel ativo, Checklist obrigatório, Bloqueios ativados
- ✅ Para 3 cenários reais, o método produz o mesmo "perfil ativo" sempre (determinístico):
  - Cenário 1: Classe A + Produto + F4
  - Cenário 2: Classe C + UX + F1
  - Cenário 3: Método + F-1
- ✅ "Executor" não consegue justificar decisão fora do papel sem gerar FAIL (regra explícita)

**FAIL:**
- ❌ Artefato de papéis não existe
- ❌ Artefato de ativação dinâmica não existe
- ❌ Método não é determinístico (mesmo contexto produz papéis diferentes)
- ❌ Executor pode decidir fora do papel sem FAIL
- ❌ Papel sem limite explícito

---

## 📋 FASES DE EXECUÇÃO

### F1 — Definir Matriz de Papéis Canônicos

**END desta fase:**
> "A matriz de papéis canônicos está definida com autoridade, proibições, checklist e evidências obrigatórias para cada papel."

**Artefato:**
- `/METODO/PAPEIS_CANONICOS.md`

**Critérios de PASS:**
- ✅ Papel CEO definido:
  - Autoridade: Validar END, decidir PASS/FAIL, priorizar, definir regra canônica
  - Proibições: Implementar, escrever código, executar fases
  - Checklist: END está claro? Critérios são binários? Prioridade está definida?
  - Evidências: Aprovação registrada, prioridade documentada, decisão PASS/FAIL com justificativa
- ✅ Papel Produto (Chefe de Produto) definido:
  - Autoridade: Converter problema em demanda, definir aceitação binária, recortar escopo
  - Proibições: Reescrever método, implementar, decidir PASS/FAIL final
  - Checklist: END está mensurável? Critérios são binários? Escopo está claro?
  - Evidências: Demanda criada, F-1 criado, validação de artefatos registrada
- ✅ Papel Executor definido:
  - Autoridade: Executar F-1 aprovado, gerar evidência, implementar
  - Proibições: Decidir escopo, mudar END, aprovar demanda
  - Checklist: F-1 está aprovado? Artefato está conforme? Evidência está registrada?
  - Evidências: Artefatos gerados, evidência de execução, outputs com versionamento
- ✅ Papel Auditor definido:
  - Autoridade: Procurar falhas escondidas, validar binariamente, tentar quebrar
  - Proibições: Aprovar por simpatia, implementar, decidir escopo
  - Checklist: Critérios são binários? Evidências existem? Rastreabilidade está garantida?
  - Evidências: Relatório de auditoria, falhas identificadas, validação binária registrada
- ✅ Documento está formatado e commitado

**Critérios de FAIL:**
- ❌ Algum papel não definido
- ❌ Autoridade não especificada
- ❌ Proibições não especificadas
- ❌ Checklist não especificado
- ❌ Evidências não especificadas
- ❌ Documento não commitado

---

### F2 — Definir INPUTS do Mecanismo de Ativação

**END desta fase:**
> "Os INPUTS do mecanismo de ativação dinâmica estão definidos com formato, valores válidos e exemplos."

**Artefato:**
- Seção "INPUTS do Mecanismo" no documento `/METODO/ATIVACAO_DINAMICA_PAPEIS.md`

**Critérios de PASS:**
- ✅ INPUT 1: Classe da demanda
  - Formato: A, B, C, D
  - Valores válidos: A (crítico), B (importante), C (desejável), D (opcional)
  - Exemplo: `classe: A`
- ✅ INPUT 2: Tipo da demanda
  - Formato: Método, Produto, Software
  - Valores válidos: Método (altera método), Produto (cria produto), Software (implementa software)
  - Exemplo: `tipo: Método`
- ✅ INPUT 3: Fase
  - Formato: F-1, F1, F2, F3, F4, F5, F6
  - Valores válidos: F-1 (planejamento), F1-F6 (execução)
  - Exemplo: `fase: F1`
- ✅ INPUT 4: Produto alvo
  - Formato: String (id do produto)
  - Valores válidos: Qualquer produto em `/PRODUTOS/`
  - Exemplo: `produto: contratacao-ti`
- ✅ INPUT 5: Risco
  - Formato: Array de strings
  - Valores válidos: execucao_longa, persistencia, auditabilidade, integracao_externa
  - Exemplo: `risco: [execucao_longa, auditabilidade]`
- ✅ Exemplos de INPUTS completos fornecidos

**Critérios de FAIL:**
- ❌ Algum INPUT não definido
- ❌ Formato não especificado
- ❌ Valores válidos não listados
- ❌ Exemplos não fornecidos

---

### F3 — Definir OUTPUTS do Mecanismo de Ativação

**END desta fase:**
> "Os OUTPUTS do mecanismo de ativação dinâmica estão definidos com formato, campos obrigatórios e exemplos."

**Artefato:**
- Seção "OUTPUTS do Mecanismo" no documento

**Critérios de PASS:**
- ✅ OUTPUT 1: Papel ativo
  - Formato: String (CEO, Produto, Executor, Auditor)
  - Propósito: Determinar qual papel está ativo no contexto
  - Exemplo: `papel_ativo: Executor`
- ✅ OUTPUT 2: Checklist obrigatório
  - Formato: Array de strings (perguntas obrigatórias)
  - Propósito: Determinar quais perguntas devem ser respondidas
  - Exemplo: `checklist: ["F-1 está aprovado?", "Artefato está conforme?"]`
- ✅ OUTPUT 3: Bloqueios ativados
  - Formato: Array de strings (evidências obrigatórias)
  - Propósito: Determinar quais evidências bloqueiam PASS
  - Exemplo: `bloqueios: ["evidencia_execucao", "artefato_gerado"]`
- ✅ Formato JSON do OUTPUT completo definido:
  ```json
  {
    "papel_ativo": "Executor",
    "checklist": ["F-1 está aprovado?", "Artefato está conforme?"],
    "bloqueios": ["evidencia_execucao", "artefato_gerado"]
  }
  ```
- ✅ Exemplos de OUTPUTS completos fornecidos

**Critérios de FAIL:**
- ❌ Algum OUTPUT não definido
- ❌ Formato não especificado
- ❌ Propósito não documentado
- ❌ Formato JSON não definido
- ❌ Exemplos não fornecidos

---

### F4 — Definir Matriz de Ativação Dinâmica

**END desta fase:**
> "A matriz de ativação dinâmica está definida com regras de mapeamento de contexto para perfil ativo."

**Artefato:**
- Seção "Matriz de Ativação Dinâmica" no documento

**Critérios de PASS:**
- ✅ Regras de ativação definidas:
  - **F-1 (Planejamento):** Papel ativo = Produto
    - Checklist: END está claro? Critérios são binários? Fases estão bem definidas?
    - Bloqueios: demanda_aprovada, end_validado, criterios_binarios
  - **F1-F6 (Execução):** Papel ativo = Executor
    - Checklist: F-1 está aprovado? Artefato está conforme? Evidência está registrada?
    - Bloqueios: f1_aprovado, artefato_conforme, evidencia_registrada
  - **Validação de Fase:** Papel ativo = Produto
    - Checklist: Artefato está conforme? Critérios de PASS foram atendidos?
    - Bloqueios: artefato_validado, criterios_pass_atendidos
  - **Aprovação de Demanda:** Papel ativo = CEO
    - Checklist: END está validado? Prioridade está definida?
    - Bloqueios: end_validado, prioridade_definida
  - **Auditoria:** Papel ativo = Auditor
    - Checklist: Critérios são binários? Evidências existem? Rastreabilidade está garantida?
    - Bloqueios: criterios_binarios, evidencias_existem, rastreabilidade_garantida
- ✅ Matriz está em formato de tabela ou JSON
- ✅ Exemplos de ativação fornecidos para cada regra

**Critérios de FAIL:**
- ❌ Regras de ativação não definidas
- ❌ Matriz não está em formato estruturado
- ❌ Exemplos não fornecidos

---

### F5 — Validar Determinismo com 3 Cenários

**END desta fase:**
> "O determinismo do mecanismo está validado: 3 cenários reais produzem o mesmo perfil ativo sempre."

**Artefato:**
- Seção "Validação de Determinismo" no documento

**Critérios de PASS:**
- ✅ Cenário 1 definido e validado:
  - Contexto: Classe A + Produto + F4
  - Papel ativo esperado: Executor
  - Checklist esperado: ["F-1 está aprovado?", "Artefato está conforme?", "Evidência está registrada?"]
  - Bloqueios esperados: ["f1_aprovado", "artefato_conforme", "evidencia_registrada"]
  - Validação: Executado 3 vezes, resultado idêntico
- ✅ Cenário 2 definido e validado:
  - Contexto: Classe C + UX + F1
  - Papel ativo esperado: Executor
  - Checklist esperado: ["F-1 está aprovado?", "Artefato está conforme?", "Evidência está registrada?"]
  - Bloqueios esperados: ["f1_aprovado", "artefato_conforme", "evidencia_registrada"]
  - Validação: Executado 3 vezes, resultado idêntico
- ✅ Cenário 3 definido e validado:
  - Contexto: Método + F-1
  - Papel ativo esperado: Produto
  - Checklist esperado: ["END está claro?", "Critérios são binários?", "Fases estão bem definidas?"]
  - Bloqueios esperados: ["demanda_aprovada", "end_validado", "criterios_binarios"]
  - Validação: Executado 3 vezes, resultado idêntico
- ✅ Prova de determinismo documentada
- ✅ Regra explícita: "Mesmo contexto DEVE produzir mesmo papel ativo"

**Critérios de FAIL:**
- ❌ Algum cenário não definido
- ❌ Algum cenário não validado
- ❌ Resultado não é idêntico nas 3 execuções
- ❌ Prova de determinismo não documentada
- ❌ Regra não explícita

---

### F6 — Criar Regra Anti-Alucinação e Validar

**END desta fase:**
> "A regra anti-alucinação está definida: papel fora de limite é FAIL estrutural."

**Artefato:**
- Seção "Regra Anti-Alucinação" no documento
- Documento completo commitado

**Critérios de PASS:**
- ✅ Regra anti-alucinação explícita:
  - "Executor não decide escopo. CEO não implementa. Auditor não aprova por simpatia. Papel fora de limite é FAIL estrutural."
- ✅ Exemplos de alucinação de papel fornecidos:
  - Executor tenta aprovar demanda → FAIL
  - CEO tenta executar F-1 → FAIL
  - Auditor aprova por simpatia → FAIL
  - Produto tenta reescrever método → FAIL
- ✅ Critérios de detecção de alucinação definidos:
  - Papel tenta executar ação fora de sua autoridade
  - Papel não segue checklist obrigatório
  - Papel não gera evidências obrigatórias
- ✅ Consequência de alucinação definida: FAIL estrutural
- ✅ Documento completo revisado e commitado
- ✅ Documento está no GitHub
- ✅ Demanda marcada como concluída

**Critérios de FAIL:**
- ❌ Regra anti-alucinação não explícita
- ❌ Exemplos não fornecidos
- ❌ Critérios de detecção não definidos
- ❌ Consequência não definida
- ❌ Documento não commitado
- ❌ Documento não está no GitHub
- ❌ Demanda não marcada como concluída

---

## 🚫 REGRAS CANÔNICAS

**Papel Dinâmico:**
> "Papel muda conforme contexto. Contexto determina papel. Papel sem contexto é improviso."

**Determinismo Obrigatório:**
> "Mesmo contexto DEVE produzir mesmo papel ativo. Não-determinismo é alucinação."

**Anti-Alucinação por Papel:**
> "Executor não decide escopo. CEO não implementa. Auditor não aprova por simpatia. Papel fora de limite é FAIL estrutural."

---

## 🧱 BLOQUEIOS ESTRUTURAIS

### Bloqueios Técnicos
- Nenhum

### Bloqueios de Método
- **Depende de:** DEMANDA-METODO-014 (Personas Operacionais)

### Bloqueios de Governança
- Nenhum

---

## ❌ FORA DE ESCOPO

- Definição de personas de produto (isso é DEMANDA-METODO-014)
- Implementação de software para gerenciar papéis
- Migração de papéis existentes

---

## 📌 STATUS

**Status atual:** Aprovado  
**Próximo passo:** Executar F1

---

## 🧭 REGRA FINAL

> "Papel sem contexto é improviso. Contexto sem papel é alucinação. Mecanismo dinâmico de ativação de papéis é condição de passagem para governança de execução no método END-FIRST."
