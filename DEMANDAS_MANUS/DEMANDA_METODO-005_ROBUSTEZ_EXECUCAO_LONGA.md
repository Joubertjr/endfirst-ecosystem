# DEMANDA-METODO-005 — ROBUSTEZ DE EXECUÇÃO LONGA, STREAMING E RESULTADO DURÁVEL

**Tipo:** Método / Qualidade de Produto  
**Método:** END-FIRST v2  
**Status:** BACKLOG (NÃO EXECUTAR)  
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

o método garante que:
- ❌ Nenhuma demanda PASSA sem prova explícita de que:
  - o progresso é monotônico (não regride)
  - a execução sobrevive à queda de conexão do cliente
  - o resultado não se perde mesmo se o stream quebrar
- ✅ Um revisor consegue dizer PASS/FAIL sem "achar que está ok"
- ✅ Um bug como o do log não chega ao usuário validado como "qualidade suficiente"

### Resumo do END

> **"Se o sistema promete execução longa + histórico, ele prova que não perde estado nem resultado quando a conexão falha."**

---

## 🧭 FRASES CANÔNICAS (BLOQUEANTES)

- **Robustez:** "Execução longa sem prova de retomada é promessa falsa."
- **Streaming:** "Progresso que regride é bug, não detalhe."
- **Persistência:** "Resultado que depende do stream para existir não é persistido."
- **Qualidade:** "Smoke verde não prova robustez."
- **Gate:** "Se a classe de falha não é coberta por prova, o gate é insuficiente."

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

- ✅ O método define quando Z10 é obrigatório, independentemente de "complexidade percebida"
- ✅ Existe uma classe explícita de demandas: "execução longa / streaming / histórico"
- ✅ Para essa classe, o método exige prova explícita de:
  - progresso monotônico
  - persistência independente do stream
  - resultado acessível após falha
- ✅ A prova não depende de opinião ("parece robusto")
- ✅ A prova pode ser documental, teste ou contrato, mas é explícita
- ✅ Gates existentes (Z10/Z11/Z12) não são enfraquecidos, apenas qualificados

### FAIL (AUTOMÁTICO)

- ❌ Demandas com streaming PASSAM sem prova de monotonicidade
- ❌ Persistência é validada apenas "no caminho feliz"
- ❌ Gate Z10 continua opcional por "sensação de simplicidade"
- ❌ Robustez é tratada como "edge case"
- ❌ O método continua permitindo que bugs dessa classe cheguem ao usuário

---

## 🧱 BLOQUEIOS ESTRUTURAIS

- 🔒 F-1 obrigatório (demanda de método)
- 🔒 Não criar bugfix de produto aqui
- 🔒 Não criar automação por reflexo
- 🔒 Não alterar UI
- 🔒 Não "culpar implementação"
- 🔒 Governar critérios de prova, não código

---

## 📋 TODO CANÔNICO (F0–F6)

### F0 — Aprovação do Planejamento

**Bloqueante. Nenhuma execução.**

---

### F1 — Classificar Tipos de Demanda por Classe de Risco

**END:** O método diferencia "CRUD simples" de "execução longa + estado".

---

### F2 — Definir Classe "Execução Longa / Streaming"

**END:** Classe canônica criada com critérios objetivos (tempo, estado, stream).

---

### F3 — Revisar Gate Z10 para Essa Classe

**END:** Z10 torna-se obrigatório para essa classe, mesmo sem lógica complexa.

---

### F4 — Definir Provas Mínimas de Robustez

**END:** Provas aceitas e não aceitas são listadas explicitamente.

**Exemplo:**
- ❌ "Funcionou no meu teste manual"
- ❌ "HTML 200"
- ✅ "Resultado disponível após desconectar stream"
- ✅ "Progresso monotônico por contrato"

---

### F5 — Aplicar Retroativamente (Evidência)

**END:** DEMANDA-PROD-002 é reavaliada conceitualmente e classificada como FAIL sob o novo critério (evidência documental).

---

### F6 — Declarar PASS

**Método atualizado, evidência criada, sem tocar no produto.**

---

## 🧭 REGRA FINAL (CANÔNICA)

> **"Qualidade não é ausência de erro visível.  
> Qualidade é ausência de classes inteiras de falha não provadas."**

---

## 📊 METADADOS

**Criado em:** 2026-01-19  
**Versão:** 1.0  
**Autor:** CEO  
**Status:** BACKLOG  
**Próxima ação:** Aguardar decisão do CEO para promover a F-1  
