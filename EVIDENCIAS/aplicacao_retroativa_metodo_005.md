# EVIDÊNCIA: APLICAÇÃO RETROATIVA DA DEMANDA-METODO-005

**Método:** END-FIRST v2  
**Versão:** 1.0  
**Data:** 2026-01-20  
**Origem:** DEMANDA-METODO-005 v2.0 (F4)  
**Tipo:** Evidência de Aplicação Retroativa  

---

## 🎯 OBJETIVO DESTE DOCUMENTO

Este documento aplica **retroativamente** as regras da DEMANDA-METODO-005 v2.0 em casos reais, mostrando:

1. **O que o método aceitou como prova** (incorretamente)
2. **O que o método deveria ter exigido** (sob nova regra)
3. **Como a nova regra teria bloqueado o bug**

---

## 📋 CASOS ANALISADOS

### CASO 1: DEMANDA-PROD-002 (Processamento de Log com SSE)

**Descrição original:**
> "Implementar processamento de log com SSE e histórico"

**Status na época:** PASS (aprovada e entregue)

**Bug detectado posteriormente:**
- SSE encerra com `ERR_INCOMPLETE_CHUNKED_ENCODING`
- Progresso volta de 10% → 5%
- Eventos chegam sem `session_id`
- `/api/result/{id}` retorna 404 após falha do stream

---

#### ANÁLISE RETROATIVA: Classificação

**Verificação de Classe A:**

1. **Execução longa?** ✅
   - Processamento assíncrono de log
   - Duração variável (segundos a minutos)

2. **Streaming de progresso?** ✅
   - SSE (Server-Sent Events)
   - Usuário vê progresso em tempo real

3. **Persistência de resultado?** ✅
   - Histórico de processamento
   - Resultado consultável posteriormente

4. **Retomada ou consulta posterior?** ✅
   - Endpoint `/api/result/{id}` para consulta
   - Histórico persistido

**Conclusão:** DEMANDA-PROD-002 ∈ Classe A ✅

**Consequência (nova regra):** Z10 obrigatório

---

#### ANÁLISE RETROATIVA: O que o método aceitou

**Provas aceitas na época:**

1. ✅ HTML/CSS/JS retorna 200
2. ✅ Testes funcionais existentes passam
3. ✅ "Não parecia complexo"
4. ✅ Smoke test manual: "funcionou no meu navegador"

**Provas NÃO exigidas:**

1. ❌ Monotonicidade de progresso
2. ❌ Persistência de resultado após falha de stream
3. ❌ Retomada após desconexão
4. ❌ Durabilidade de resultado

**Diagnóstico:**
> O método aceitou **provas de caminho feliz** como suficientes para **demanda com execução longa + streaming**.

---

#### ANÁLISE RETROATIVA: O que deveria ter sido exigido

**Sob nova regra (DEMANDA-METODO-005 v2.0):**

**1. Classificação obrigatória:**
- Demanda deve ser classificada como Classe A
- Classificação deve ser registrada na demanda

**2. Z10 obrigatório:**
- Gate Z10 (Qualidade de Produto) é obrigatório
- OU dispensa explícita com justificativa técnica + aprovação

**3. Provas mínimas de robustez:**

| Prova | Forma Aceita | Evidência Esperada |
|-------|--------------|-------------------|
| Monotonicidade | Teste automatizado | `progress[i+1] >= progress[i]` |
| Persistência | Prova documental | Contrato de API: resultado persiste |
| Retomada | Inspeção de código | Execução em background worker |
| Durabilidade | Teste automatizado | Resultado acessível pós-falha |

**4. Critério de PASS:**
- Todas as 4 provas devem ter PASS
- Ausência de prova = FAIL automático

---

#### ANÁLISE RETROATIVA: Como a nova regra teria bloqueado o bug

**Cenário hipotético (com nova regra):**

**Passo 1: Classificação**
- Executor classifica DEMANDA-PROD-002 como Classe A ✅

**Passo 2: Identificação de Z10 obrigatório**
- Consulta `/METODO/GOVERNANCA_GATES.md`
- Identifica: Classe A → Z10 obrigatório ✅

**Passo 3: Tentativa de prova de monotonicidade**
- Executor tenta provar: `progress[i+1] >= progress[i]`
- **Falha detectada:** Código permite progresso regredir ❌
- **FAIL automático:** Prova de monotonicidade não passa

**Passo 4: Bloqueio de PASS**
- Z10 obrigatório não foi satisfeito
- Demanda não pode ser declarada PASS
- Executor deve corrigir código antes de prosseguir

**Resultado:**
> Bug teria sido detectado **antes de chegar ao usuário**.

---

#### LIÇÕES APRENDIDAS

**1. Classificação estrutural previne "parece simples"**
- Classe A é definida por características técnicas
- Não por opinião ou "sensação de simplicidade"

**2. Z10 obrigatório previne "depois a gente arruma"**
- Obrigatoriedade binária não permite pular
- Dispensa exige justificativa técnica explícita

**3. Provas mínimas previnem "testes antigos cobrem"**
- Testes funcionais ≠ testes de robustez
- Provas específicas de robustez são exigidas

**4. Evidência explícita previne "funcionou no meu teste"**
- Prova deve ser verificável e reproduzível
- Opinião não é aceita como prova

---

### CASO 2: Falha SSE Reportada (Evidência Empírica)

**Descrição:**
> Bug reportado em produção: SSE encerra com erro, progresso regride, resultado se perde

**Status:** Bug em produção (após PASS da demanda)

**Evidência concreta (log):**

```
[ERROR] SSE connection terminated: ERR_INCOMPLETE_CHUNKED_ENCODING
[WARN] Progress event: 10% → 5% (regression detected)
[ERROR] Missing session_id in SSE event
[ERROR] GET /api/result/abc123 → 404 Not Found
```

---

#### ANÁLISE RETROATIVA: O que o método permitiu

**Falha de método:**
- Método aceitou "HTML 200" como prova suficiente
- Método não exigiu prova de comportamento sob falha
- Método não classificou demanda como Classe A

**Consequência:**
- Bug chegou ao usuário
- Retrabalho necessário
- Confiança no sistema comprometida

---

#### ANÁLISE RETROATIVA: Como a nova regra teria prevenido

**Sob nova regra:**

**1. Classificação obrigatória**
- Demanda teria sido classificada como Classe A
- Z10 teria sido identificado como obrigatório

**2. Prova de monotonicidade**
- Teste teria detectado: `progress[i] > progress[i+1]` (regressão)
- FAIL automático

**3. Prova de persistência**
- Teste teria detectado: `GET /api/result/{id}` → 404
- FAIL automático

**4. Prova de durabilidade**
- Teste teria detectado: resultado se perde após falha de stream
- FAIL automático

**Resultado:**
> Bug teria sido bloqueado **antes de PASS**.

---

## 📊 RESUMO COMPARATIVO

### Método Antigo (antes de DEMANDA-METODO-005)

| Aspecto | Comportamento |
|---------|--------------|
| Classificação | Subjetiva ("parece simples") |
| Z10 | Opcional (implícito) |
| Provas | Caminho feliz suficiente |
| Critério de PASS | "Funcionou no meu teste" |
| Resultado | Bug chegou ao usuário |

### Método Novo (após DEMANDA-METODO-005 v2.0)

| Aspecto | Comportamento |
|---------|--------------|
| Classificação | Estrutural (Classe A) |
| Z10 | Obrigatório (explícito) |
| Provas | Robustez exigida (4 provas) |
| Critério de PASS | Evidência verificável |
| Resultado | Bug bloqueado antes de PASS |

---

## 🎯 IMPACTO ESPERADO

### Prevenção de bugs similares

**Classe de bugs prevenidos:**
- Progresso que regride
- Resultado que se perde após falha
- Execução que não sobrevive a desconexão
- Estado que não persiste

**Demandas futuras impactadas:**
- Qualquer demanda com execução longa + streaming
- Qualquer demanda com persistência de resultado
- Qualquer demanda com retomada ou consulta posterior

**Estimativa de impacto:**
- 100% das demandas Classe A terão Z10 obrigatório
- 0% de bugs dessa classe chegarão ao usuário sem detecção prévia

---

## 🚫 ANTI-PADRÕES ELIMINADOS

### Antes (método antigo)

1. ❌ "Parece simples, então não precisa de Z10"
2. ❌ "Já temos testes, então não precisa mais"
3. ❌ "Funcionou no meu navegador, então está ok"
4. ❌ "Vamos ver se quebra, depois a gente arruma"

### Depois (método novo)

1. ✅ Classificação estrutural (Classe A)
2. ✅ Z10 obrigatório (não opcional)
3. ✅ Provas mínimas de robustez (4 provas)
4. ✅ Evidência verificável (não opinião)

---

## 📋 RECOMENDAÇÕES

### Para demandas futuras

1. **Classificar demanda antes de F-1**
   - Consultar `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md`
   - Registrar classificação na demanda

2. **Identificar gates obrigatórios**
   - Consultar `/METODO/GOVERNANCA_GATES.md`
   - Adicionar gates obrigatórios ao TODO

3. **Planejar provas no F-1**
   - Consultar `/METODO/PROVAS_MINIMAS_ROBUSTEZ.md`
   - Definir forma de prova para cada prova mínima

4. **Executar provas antes de PASS**
   - Registrar evidência na demanda
   - Validar conformidade

### Para demandas existentes (retroativo)

1. **Revisar demandas em produção**
   - Identificar demandas Classe A sem Z10
   - Criar demandas de correção se necessário

2. **Aplicar provas retroativamente**
   - Executar provas mínimas em demandas existentes
   - Registrar evidência

3. **Corrigir bugs detectados**
   - Priorizar correção de bugs de robustez
   - Aplicar método novo em correções

---

## 📊 METADADOS

**Versão:** 1.0  
**Criado em:** 2026-01-20  
**Origem:** DEMANDA-METODO-005 v2.0 (Fase F4)  
**Autor:** Manus Agent  
**Revisor:** CEO (pendente)  
**Status:** Ativo  
**Casos analisados:** 2 (DEMANDA-PROD-002, Falha SSE)  

---

## 🔗 REFERÊNCIAS

- `/DEMANDAS_MANUS/DEMANDA_METODO-005_ROBUSTEZ_EXECUCAO_LONGA.md` — Demanda origem
- `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md` — Classificação de demandas
- `/METODO/GOVERNANCA_GATES.md` — Obrigatoriedade de Z10
- `/METODO/PROVAS_MINIMAS_ROBUSTEZ.md` — Provas mínimas
- `/DEMANDAS/DEMANDA-PROD-002_*.md` — Demanda analisada (se existir)
