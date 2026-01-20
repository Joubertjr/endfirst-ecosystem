# F-1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-METODO-005 v2.0 — Aplicação Obrigatória de Qualidade em Execução Longa e Streaming  
**Status:** PENDENTE DE APROVAÇÃO  
**Método:** END-FIRST v2  
**Tipo:** Planejamento Canônico (F-1)  
**Data:** 2026-01-20  

---

## 🔒 OBJETIVO DESTE DOCUMENTO

Este é o **F-1 (Planejamento Canônico)** da DEMANDA-METODO-005 v2.0.

Conforme END-FIRST v2 e OD-012 ("Planning is a first-class artifact. Executor only executes."):

- **Este documento define COMO executar a demanda**
- **Nenhuma execução pode começar sem aprovação deste F-1**
- **Executor (Cursor ou Manus) só executa após aprovação do CEO**

---

## 📋 REFERÊNCIA À DEMANDA

**Arquivo:** `/DEMANDAS_MANUS/DEMANDA_METODO-005_ROBUSTEZ_EXECUCAO_LONGA.md`  
**Versão:** 2.0  
**Issue:** #14  
**Commit:** `af817fd`  

**END da demanda:**
> "Se o sistema promete execução longa + histórico, ele prova que não perde estado nem resultado quando a conexão falha."

**Escopo:** Governança de qualidade (método), não correção de produto

---

## 🎯 RESULTADO ESPERADO (END DO F-1)

**Ao final da execução deste planejamento:**

O método END-FIRST v2 terá:

1. **Classificação canônica** de demandas por tipo de execução (execução longa + streaming)
2. **Regra binária obrigatória** sobre Z10: obrigatório OU dispensa explícita registrada
3. **Critérios documentais** de provas mínimas de robustez (monotonicidade, persistência, retomada)
4. **Evidência retroativa** aplicando a regra em casos reais (DEMANDA-PROD-002, falha SSE)
5. **Integração ao método** via referências canônicas nos documentos oficiais

**Sem:**
- ❌ Criar bugfix de produto
- ❌ Criar automação nova
- ❌ Criar gate novo
- ❌ Alterar código de produto

---

## 🧱 BLOQUEIOS ESTRUTURAIS

**Este planejamento NÃO autoriza:**

- 🔒 Nenhuma correção de produto
- 🔒 Nenhuma automação nova
- 🔒 Nenhum gate novo criado
- 🔒 Nenhuma alteração de UI
- 🔒 Nenhuma mudança de código

**Este planejamento AUTORIZA apenas:**

- ✅ Criação/atualização de documentos de método
- ✅ Criação de evidências documentais
- ✅ Atualização de referências canônicas
- ✅ Governança de critérios de prova

---

## 📋 FASES DE EXECUÇÃO (F1–F6)

### F1 — Classificar Demandas por Tipo de Execução

**END:**
> Definição canônica de "demanda com execução longa + streaming" existe e é objetiva.

**Critérios de PASS:**
- ✅ Documento criado: `/METODO/CLASSIFICACAO_TIPOS_DEMANDA.md` (ou seção em documento existente)
- ✅ Critérios objetivos definidos:
  - Streaming ativo (SSE, WebSocket, polling progressivo)
  - Progresso incremental
  - Resultado pós-processamento
  - Persistência de estado
  - Recuperação pós-falha
- ✅ Critérios são verificáveis por leitura binária (não opinião)

**Artefato esperado:**
- Documento de classificação ou seção em documento existente
- Commit com mensagem descritiva

**Tempo estimado:** 1-2 horas

---

### F2 — Definir Obrigatoriedade de Z10 por Classe

**END:**
> Regra binária: "esta classe → Z10 obrigatório OU exceção → justificativa explícita registrada"

**Critérios de PASS:**
- ✅ Regra documentada em local canônico (ex: atualização de `/METODO/PILAR_ENDFIRST.md` ou documento de gates)
- ✅ Regra é binária e inequívoca
- ✅ Critérios de dispensa estão explícitos
- ✅ Ausência de decisão = FAIL automático (documentado)

**Artefato esperado:**
- Atualização de documento de método (PILAR_ENDFIRST.md, gate Z10, ou documento de governança)
- Commit com mensagem descritiva

**Tempo estimado:** 1-2 horas

---

### F3 — Definir Provas Mínimas de Robustez (Conceitual)

**END:**
> Critérios documentais mínimos de prova existem e são explícitos.

**Critérios de PASS:**
- ✅ Documento criado ou seção adicionada
- ✅ Lista explícita de provas **aceitas**:
  - "Resultado disponível após desconectar stream"
  - "Progresso monotônico por contrato"
  - "Reconexão não perde estado"
  - "Resultado persiste após falha"
- ✅ Lista explícita de provas **NÃO aceitas**:
  - "Funcionou no meu teste manual"
  - "HTML 200"
  - "Testes antigos passam"
- ✅ Distinção clara: teste funcional (caminho feliz) vs teste de robustez (falha, reconexão, persistência)

**Artefato esperado:**
- Documento de critérios de prova para execução longa/streaming
- Commit com mensagem descritiva

**Tempo estimado:** 2-3 horas

**Nota:** Sem exigir teste automático — apenas prova conceitual clara

---

### F4 — Aplicar Regra Retroativamente (Evidência)

**END:**
> Análise documentada de casos reais mostra exatamente onde o método deixou passar.

**Critérios de PASS:**
- ✅ Documento de evidência criado: `/EVIDENCIAS/aplicacao_retroativa_metodo_005.md` (ou similar)
- ✅ DEMANDA-PROD-002 reavaliada sob novo critério
- ✅ Falha SSE observada analisada
- ✅ Documento mostra:
  - O que o método aceitou como prova (incorretamente)
  - O que o método deveria ter exigido
  - Como a nova regra teria bloqueado o bug

**Artefato esperado:**
- Evidência documental de aplicação retroativa
- Commit com mensagem descritiva

**Tempo estimado:** 1-2 horas

---

### F5 — Integrar ao Método

**END:**
> Documentos do método END-FIRST v2 referenciam canonicamente as novas regras.

**Critérios de PASS:**
- ✅ Referências canônicas adicionadas a:
  - `/METODO/END_FIRST_V2.md` (ou `/METODO/PILAR_ENDFIRST.md`)
  - Definição de gates (se aplicável)
  - Template de demanda (se aplicável)
- ✅ Integração por referência canônica (não path absoluto)
- ✅ Versionamento atualizado nos documentos modificados

**Artefato esperado:**
- Commits de atualização dos documentos do método
- Mensagens descritivas

**Tempo estimado:** 1-2 horas

---

### F6 — Declarar PASS

**END:**
> Regra ativa, documentada, verificável e integrada ao método.

**Critérios de PASS:**
- ✅ Todas as fases anteriores (F1-F5) concluídas com PASS
- ✅ Método atualizado
- ✅ Evidência criada
- ✅ Sem tocar no produto
- ✅ Gates não enfraquecidos
- ✅ Commits pushed ao repositório remoto
- ✅ Issue #14 atualizada

**Artefato esperado:**
- Documento de conclusão ou atualização de status da DEMANDA-METODO-005
- Commit final

**Tempo estimado:** 30 minutos

---

## 📊 ESTIMATIVA TOTAL

**Tempo total estimado:** 7-12 horas de trabalho efetivo

**Distribuição:**
- F1: 1-2h
- F2: 1-2h
- F3: 2-3h
- F4: 1-2h
- F5: 1-2h
- F6: 0.5h

---

## 🧭 DEPENDÊNCIAS E RISCOS

### Dependências

1. **DEMANDA-METODO-005 v2.0** já está aprovada e versionada ✅
2. **Estrutura de diretórios** `/METODO/` e `/EVIDENCIAS/` existem ✅
3. **Acesso ao repositório** para commits e push ✅

### Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Conflito com outros documentos de método | Baixa | Médio | Revisar documentos existentes antes de modificar |
| Sobreposição com outras demandas de método | Baixa | Baixo | Verificar DEMANDAS_MANUS ativas |
| Escopo creep (tentar corrigir produto) | Média | Alto | Bloqueios estruturais explícitos no F-1 |

---

## ✅ CRITÉRIOS DE APROVAÇÃO DESTE F-1

**Este F-1 está pronto para aprovação se:**

1. ✅ **Escopo está claro:** método (não produto)
2. ✅ **Fases estão bem definidas:** ENDs, critérios de PASS, artefatos
3. ✅ **Bloqueios estão explícitos:** nenhuma correção de produto, automação, gate novo
4. ✅ **Estimativas são realistas:** 7-12 horas total
5. ✅ **Dependências estão satisfeitas:** DEMANDA-METODO-005 v2.0 aprovada
6. ✅ **Riscos estão mapeados:** mitigações definidas

---

## 🔒 APROVAÇÃO NECESSÁRIA

**Este F-1 aguarda aprovação do CEO antes de qualquer execução.**

**Após aprovação:**
- Status muda: F-1 PENDENTE → F-1 APROVADO
- Execução pode começar (F1-F6)
- Executor segue este planejamento rigorosamente

**Sem aprovação:**
- Nenhuma execução autorizada
- Nenhum commit de implementação
- Planejamento pode ser revisado se necessário

---

## 📊 METADADOS

**Criado em:** 2026-01-20  
**Versão:** 1.0  
**Autor:** Manus Agent  
**Revisor:** CEO (pendente)  
**Status:** PENDENTE DE APROVAÇÃO  
**Demanda relacionada:** DEMANDA-METODO-005 v2.0  
**Issue:** #14  
