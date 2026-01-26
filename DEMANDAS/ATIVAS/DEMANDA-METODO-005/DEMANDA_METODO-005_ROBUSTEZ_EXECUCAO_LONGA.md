# DEMANDA-METODO-005 — APLICAÇÃO OBRIGATÓRIA DE QUALIDADE EM EXECUÇÃO LONGA E STREAMING

**Tipo:** Método / Governança de Qualidade  
**Método:** END-FIRST v2  
**Status:** F-1 PENDENTE DE APROVAÇÃO  
**Governança:** Método (impacta gates e provas aceitas)  
**Motivação:** Falha real em produção detectada após PASS em gates existentes  

---

## 🔒 END (Resultado Observável)

### Estado Final Esperado

Para qualquer demanda de produto que envolva:
- execução longa
- streaming de progresso (SSE / WebSocket / polling)
- persistência de resultado
- retomada ou consulta posterior

fica **obrigatório e inequívoco** que:

1. **A qualidade NÃO é opcional**, mesmo quando:
   - a lógica parece simples
   - a implementação é incremental
   - existem testes antigos "verdes"

2. **Nenhuma demanda dessa classe pode ser declarada PASS se:**
   - não provar comportamento correto sob falha
   - não provar monotonicidade de progresso
   - não provar durabilidade do resultado

3. **Gates de qualidade (ex.: Z10) não podem ser implicitamente ignorados:**
   - a dispensa precisa ser explícita, justificada e registrada
   - ausência de decisão explícita = FAIL automático

4. **Um revisor consegue olhar a demanda e responder binariamente:**
   - "qualidade foi exigida e provada"
   - ou "qualidade foi conscientemente dispensada"

**Sem interpretação subjetiva.**

### Resumo do END

> **"Se o sistema promete execução longa + histórico, ele prova que não perde estado nem resultado quando a conexão falha."**

---

## 🧭 FRASES CANÔNICAS (BLOQUEANTES)

- **Qualidade:** "Qualidade não é complexidade; é sobrevivência sob falha."
- **Gate:** "Gate não citado no END não está implicitamente dispensado."
- **Streaming:** "Se o progresso pode regredir, o sistema não é confiável."
- **Resultado:** "Resultado que se perde após falha não é resultado."
- **Método:** "Se o método permite pular qualidade sem declarar, o método falhou."
- **Governança:** "Qualidade que não é exigida explicitamente será violada silenciosamente."

**Violação de qualquer frase = FAIL automático da demanda avaliada.**

---

## 🎯 PROBLEMA REAL (EVIDÊNCIA)

### Evidência concreta (log)

- SSE encerra com `ERR_INCOMPLETE_CHUNKED_ENCODING`
- progresso volta de 10% → 5%
- eventos chegam sem `session_id`
- `/api/result/{id}` retorna 404 após falha do stream

### Diagnóstico objetivo

- estado não é garantido fora da conexão
- contrato de progresso não é monotônico
- persistência não é prova de durabilidade

---

## ❌ O QUE O MÉTODO PERMITIU ERRADO

O método aceitou como prova:
- ✅ HTML/CSS/JS 200
- ✅ testes existentes
- ✅ "não parecia complexo"

Mas não exigiu prova da classe real de risco:
- falha de conexão
- execução longa
- contrato de streaming
- persistência pós-falha

👉 **O erro não é de implementação — é de critério de validação.**

---

## ✅ CRITÉRIOS DE ACEITAÇÃO (BINÁRIOS)

### PASS

- ✅ Existe definição canônica de quando Z10 é obrigatório
- ✅ Demandas com execução longa + streaming são explicitamente classificadas
- ✅ Existe regra binária: **Z10 obrigatório OU dispensa explicitamente registrada**
- ✅ O método define "o que provar" (robustez, monotonicidade, persistência, retomada)
- ✅ O método define "quando exigir" (obrigatoriedade de Z10 por classe de demanda)
- ✅ Provas mínimas de robustez são exigidas (não automação, mas critérios)
- ✅ Nenhuma demanda dessa classe pode "passar por acidente"
- ✅ A prova não depende de opinião ("parece robusto")
- ✅ A prova pode ser documental, teste ou contrato, mas é explícita
- ✅ Gates existentes (Z10/Z11/Z12) não são enfraquecidos, apenas qualificados
- ✅ Evidência documental criada aplicando a regra em casos reais:
  - DEMANDA-PROD-002
  - falha SSE reportada

### FAIL (AUTOMÁTICO)

- ❌ Gate Z10 ignorado por "parecia simples"
- ❌ Confundir "teste existente" com "prova de robustez"
- ❌ Confundir "teste funcional" com "teste de robustez"
- ❌ PASS declarado sem prova de comportamento sob falha
- ❌ Decisão implícita sobre qualidade
- ❌ Demandas com streaming PASSAM sem prova de monotonicidade
- ❌ Persistência é validada apenas "no caminho feliz"
- ❌ Gate Z10 continua opcional por "sensação de simplicidade"
- ❌ Robustez é tratada como "edge case"
- ❌ Transferir responsabilidade para "bug futuro"
- ❌ Resolver com automação em vez de governança
- ❌ O método continua permitindo que bugs dessa classe cheguem ao usuário

---

## 🚫 DO / DON'T

### DO

- ✅ Tratar qualidade como contrato, não opinião
- ✅ Exigir decisão explícita sobre Z10
- ✅ Diferenciar:
  - teste funcional (caminho feliz)
  - teste de robustez (falha, reconexão, persistência)
- ✅ Documentar critérios mínimos de streaming correto
- ✅ Manter independência de ferramenta

### DON'T

- ❌ "Não é complexo, então não precisa"
- ❌ "Os testes antigos cobrem"
- ❌ "Depois a gente arruma"
- ❌ Resolver bug sem corrigir método
- ❌ Criar exceção tácita

---

## 🧱 BLOQUEIOS ESTRUTURAIS

- 🔒 F-1 obrigatório (demanda de método)
- 🔒 Sem execução sem aprovação explícita
- 🔒 Nenhuma correção de produto
- 🔒 Nenhuma automação nova
- 🔒 Nenhum gate novo criado
- 🔒 Revisão apenas do uso correto dos gates existentes
- 🔒 Não criar bugfix de produto aqui
- 🔒 Não criar automação por reflexo
- 🔒 Não alterar UI
- 🔒 Não "culpar implementação"
- 🔒 Governar critérios de prova, não código

---

## 📋 TODO CANÔNICO (F0–F6)

### F0 — Aprovação do Planejamento

**Bloqueante. Nenhuma execução.**

**END:** F-1 aprovado pelo CEO

---

### F1 — Classificar Demandas por Tipo de Execução

**END:** Definição canônica de "demanda com execução longa + streaming"

**PASS quando:**
- Documento define critérios objetivos:
  - streaming ativo (SSE, WebSocket, polling progressivo)
  - progresso incremental
  - resultado pós-processamento
  - persistência de estado
  - recuperação pós-falha

**Artefato:** Documento de classificação de tipos de demanda

---

### F2 — Definir Obrigatoriedade de Z10 por Classe

**END:** Regra binária:
- esta classe → Z10 obrigatório
- exceção → justificativa explícita registrada

**PASS quando:**
- Regra está documentada
- Critérios de dispensa estão explícitos
- Ausência de decisão = FAIL automático

**Artefato:** Atualização de gate Z10 ou documento de governança de gates

---

### F3 — Definir Provas Mínimas de Robustez (Conceitual)

**END:** Critérios documentais mínimos de prova

**PASS quando:**
- Lista explícita de provas aceitas:
  - ✅ "Resultado disponível após desconectar stream"
  - ✅ "Progresso monotônico por contrato"
  - ✅ "Reconexão não perde estado"
  - ✅ "Resultado persiste após falha"
- Lista explícita de provas NÃO aceitas:
  - ❌ "Funcionou no meu teste manual"
  - ❌ "HTML 200"
  - ❌ "Testes antigos passam"

**Artefato:** Documento de critérios de prova para execução longa/streaming

*Sem exigir teste automático — apenas prova conceitual clara*

---

### F4 — Aplicar Regra Retroativamente (Evidência)

**END:** Análise documentada de casos reais

**PASS quando:**
- DEMANDA-PROD-002 reavaliada sob novo critério
- Falha SSE observada analisada
- Documento mostra exatamente onde o método deixou passar

**Artefato:** Evidência documental de aplicação retroativa

---

### F5 — Integrar ao Método

**END:** Documento integrado ao método END-FIRST v2

**PASS quando:**
- Referência canônica adicionada a:
  - END-FIRST v2
  - definição de gates
  - template de demanda
- Integração por referência canônica, não path

**Artefato:** Commits de atualização dos documentos do método

---

### F6 — Declarar PASS

**END:** Regra ativa, documentada e verificável

**PASS quando:**
- Método atualizado
- Evidência criada
- Sem tocar no produto
- Gates não enfraquecidos

---

## 🧭 REGRA FINAL (CANÔNICA)

> **"Qualidade não é ausência de erro visível.  
> Qualidade é ausência de classes inteiras de falha não provadas."**

> **"Qualidade que não é exigida explicitamente será violada silenciosamente."**

> **"Quando dois documentos governam o mesmo END, o método perdeu autoridade."**

---

## 📊 HISTÓRICO DE VERSÕES

### v1.0 (2026-01-19)
- Criação inicial
- Status: BACKLOG
- Foco: identificação do problema e classe de falha

### v2.0 (2026-01-20)
- Incorporação de elementos de obrigatoriedade de Z10
- Consolidação "o que provar" + "quando exigir"
- Status: F-1 PENDENTE DE APROVAÇÃO
- Razão: Evitar duplicação com proposta DEMANDA-METODO-006
- Decisão: "Quando dois documentos governam o mesmo END, o método perdeu autoridade"

---

## 📊 METADADOS

**Criado em:** 2026-01-19  
**Atualizado em:** 2026-01-20  
**Versão:** 2.0  
**Autor:** CEO  
**Status:** F-1 PENDENTE DE APROVAÇÃO  
**Issue:** #14  
**Próxima ação:** Criar F-1 (Planejamento Canônico) para aprovação do CEO  
