---
document_id: REGRAS_VALIDACAO_AUTOMATICA
type: canonical
owner: CEO (Joubert Jr)
status: approved
approved_by: CEO
approved_at: 2026-01-26
governed_by: /METODO/END_FIRST_V2.md
version: 1.0
created_at: 2026-01-26
demanda_origem: Atualização do método END-FIRST v2.5
---

# REGRAS DE VALIDAÇÃO AUTOMÁTICA — END-FIRST v2.5

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Status:** Canônico (Obrigatório)  
**Path Canônico:** `/METODO/REGRAS_VALIDACAO_AUTOMATICA.md`

---

## 🎯 O QUE SÃO REGRAS DE VALIDAÇÃO AUTOMÁTICA

As **Regras de Validação Automática** definem critérios binários que devem ser validados automaticamente antes de aceitar qualquer artefato no método END-FIRST.

**Princípio fundamental:**
> "Validação automática elimina dependência de disciplina humana. Gates bloqueiam estruturalmente violações."

---

## 🔒 REGRAS OBRIGATÓRIAS

### Regra 1: Demanda sem END = FAIL

**Critério:**
- Demanda DEVE ter seção `## 🔒 END (Resultado Observável)`
- END DEVE conter pelo menos 3 resultados observáveis
- END DEVE ter frase única de resumo

**Validação:**
```bash
# Verificar seção END existe
grep -q "## 🔒 END" DEMANDA-*.md || echo "FAIL: Sem seção END"

# Verificar resultados observáveis
grep -c "✅" DEMANDA-*.md | awk '$1 < 3 {print "FAIL: Menos de 3 resultados observáveis"}'
```

**Critérios de PASS:**
- ✅ Seção END existe
- ✅ Pelo menos 3 resultados observáveis
- ✅ Frase única de resumo existe

**Critérios de FAIL:**
- ❌ Seção END não existe
- ❌ Menos de 3 resultados observáveis
- ❌ Frase única de resumo não existe

---

### Regra 2: Demanda sem ### PASS / ### FAIL = FAIL

**Critério:**
- Demanda DEVE ter seção `### PASS`
- Demanda DEVE ter seção `### FAIL`
- Cada seção DEVE ter pelo menos 3 critérios

**Validação:**
```bash
# Verificar seções PASS e FAIL
grep -q "### PASS" DEMANDA-*.md || echo "FAIL: Sem seção PASS"
grep -q "### FAIL" DEMANDA-*.md || echo "FAIL: Sem seção FAIL"

# Verificar critérios
grep -A 10 "### PASS" DEMANDA-*.md | grep -c "✅" | awk '$1 < 3 {print "FAIL: Menos de 3 critérios PASS"}'
grep -A 10 "### FAIL" DEMANDA-*.md | grep -c "❌" | awk '$1 < 3 {print "FAIL: Menos de 3 critérios FAIL"}'
```

**Critérios de PASS:**
- ✅ Seção PASS existe
- ✅ Seção FAIL existe
- ✅ Pelo menos 3 critérios em cada seção

**Critérios de FAIL:**
- ❌ Seção PASS não existe
- ❌ Seção FAIL não existe
- ❌ Menos de 3 critérios em cada seção

---

### Regra 3: F-1 sem status explícito = FAIL

**Critério:**
- F-1 DEVE ter seção `## 📌 STATUS`
- Status DEVE ser explícito: `APROVADO`, `PENDENTE` ou `REJEITADO`
- Se aprovado, DEVE ter declaração "F-1 aprovada"

**Validação:**
```bash
# Verificar seção STATUS
grep -q "## 📌 STATUS" F1-*.md || echo "FAIL: Sem seção STATUS"

# Verificar status explícito
grep -E "(APROVADO|PENDENTE|REJEITADO)" F1-*.md || echo "FAIL: Status não explícito"
```

**Critérios de PASS:**
- ✅ Seção STATUS existe
- ✅ Status é explícito (APROVADO/PENDENTE/REJEITADO)
- ✅ Se APROVADO, declaração "F-1 aprovada" existe

**Critérios de FAIL:**
- ❌ Seção STATUS não existe
- ❌ Status não é explícito
- ❌ Se APROVADO, declaração "F-1 aprovada" não existe

---

### Regra 4: Artefato com TODO/TBD/PLACEHOLDER = FAIL

**Critério:**
- END de demanda NÃO pode conter TODO, TBD ou PLACEHOLDER
- END de F-1 NÃO pode conter TODO, TBD ou PLACEHOLDER
- Critérios de fase podem ter `[A definir durante execução]` (permitido)

**Validação:**
```bash
# Verificar END da demanda
grep -A 20 "## 🔒 END" DEMANDA-*.md | grep -iE "(TODO|TBD|PLACEHOLDER|\[A definir|\[Extraído)" && echo "FAIL: END com placeholder"

# Verificar END do F-1
grep -A 20 "## 🔒 END" F1-*.md | grep -iE "(TODO|TBD|PLACEHOLDER|\[A definir|\[Extraído)" && echo "FAIL: F-1 END com placeholder"
```

**Critérios de PASS:**
- ✅ END da demanda não contém TODO/TBD/PLACEHOLDER
- ✅ END do F-1 não contém TODO/TBD/PLACEHOLDER
- ✅ Placeholders em critérios de fase são permitidos (se resolvidos durante execução)

**Critérios de FAIL:**
- ❌ END da demanda contém TODO/TBD/PLACEHOLDER
- ❌ END do F-1 contém TODO/TBD/PLACEHOLDER
- ❌ Placeholder em END (não em critérios de fase)

---

### Regra 5: Evidência fora da pasta da demanda = FAIL

**Critério:**
- Evidência específica DEVE estar em `DEMANDAS/<STATUS>/<DEMANDA-ID>/EVIDENCIAS/`
- Evidência NÃO pode estar em `EVIDENCIAS/` na raiz
- Evidência NÃO pode estar fora da pasta da demanda

**Validação:**
```bash
# Verificar evidências na raiz (não devem existir)
test -d EVIDENCIAS && echo "FAIL: EVIDENCIAS/ existe na raiz" || echo "PASS"

# Verificar evidências específicas estão nas pastas corretas
for evidencia in $(find DEMANDAS -name "execucao_demanda_*.md"); do
  if ! echo "$evidencia" | grep -q "/EVIDENCIAS/"; then
    echo "FAIL: Evidência fora de EVIDENCIAS/: $evidencia"
  fi
done
```

**Critérios de PASS:**
- ✅ Evidência específica está em `DEMANDAS/<STATUS>/<DEMANDA-ID>/EVIDENCIAS/`
- ✅ `EVIDENCIAS/` não existe na raiz
- ✅ Nenhuma evidência fora da pasta da demanda

**Critérios de FAIL:**
- ❌ Evidência específica está fora da pasta da demanda
- ❌ `EVIDENCIAS/` existe na raiz
- ❌ Evidência está em local incorreto

---

## 🔒 GATE Z-VALIDACAO-AUTOMATICA

### Definição

**Z-VALIDACAO-AUTOMATICA** é o gate que valida todas as regras de validação automática.

**Obrigatoriedade:** Universal (todas as demandas)

**Quando executar:**
- Antes de aceitar qualquer demanda
- Antes de aceitar qualquer F-1
- Antes de registrar qualquer evidência
- Em qualquer commit que altere demandas ou F-1s

---

### Critérios de PASS

**Z-VALIDACAO-AUTOMATICA passa se TODAS as regras abaixo passam:**

1. ✅ **Regra 1:** Demanda tem END válido
2. ✅ **Regra 2:** Demanda tem PASS/FAIL válidos
3. ✅ **Regra 3:** F-1 tem status explícito (se existe)
4. ✅ **Regra 4:** Nenhum artefato tem TODO/TBD/PLACEHOLDER em END
5. ✅ **Regra 5:** Evidências estão nos locais corretos

---

### Critérios de FAIL

**Z-VALIDACAO-AUTOMATICA falha se QUALQUER regra falha:**

1. ❌ **Regra 1:** Demanda sem END válido
2. ❌ **Regra 2:** Demanda sem PASS/FAIL válidos
3. ❌ **Regra 3:** F-1 sem status explícito
4. ❌ **Regra 4:** Artefato com TODO/TBD/PLACEHOLDER em END
5. ❌ **Regra 5:** Evidência fora da pasta da demanda

---

### Consequências de FAIL

**Se Z-VALIDACAO-AUTOMATICA falha:**

1. ❌ **Bloqueio de aceitação:**
   - Demanda não pode ser aceita
   - F-1 não pode ser aceito
   - Evidência não pode ser registrada
   - Commit não pode ser aceito

2. ❌ **Correção obrigatória:**
   - Problemas devem ser corrigidos antes de prosseguir
   - Gate deve passar antes de qualquer execução

3. ❌ **Auditoria:**
   - FAIL é registrado
   - Causa raiz deve ser identificada
   - Prevenção deve ser implementada

---

## 📋 INTEGRAÇÃO COM OUTROS GATES

### Z-VALIDACAO-AUTOMATICA + Z-DEMANDAS-STRUCTURE

**Z-DEMANDAS-STRUCTURE** valida estrutura física.

**Z-VALIDACAO-AUTOMATICA** valida conteúdo e conformidade.

**Ordem:**
1. Z-DEMANDAS-STRUCTURE (estrutura)
2. Z-VALIDACAO-AUTOMATICA (conteúdo)

---

### Z-VALIDACAO-AUTOMATICA + Z-F1-INTEGRITY

**Z-VALIDACAO-AUTOMATICA** valida regras gerais.

**Z-F1-INTEGRITY** valida integridade específica do F-1.

**Ordem:**
1. Z-VALIDACAO-AUTOMATICA (regras gerais)
2. Z-F1-INTEGRITY (integridade F-1)

---

## 📊 METADADOS

**Versão:** 1.0  
**Criado em:** 2026-01-26  
**Origem:** Atualização do método END-FIRST v2.5  
**Autor:** Auto (Agent)  
**Aprovado por:** CEO (Joubert Jr)  
**Status:** Canônico (Obrigatório)

---

## 🔗 REFERÊNCIAS

- `/METODO/END_FIRST_V2.md` — Fluxo END-FIRST v2
- `/METODO/ESTRUTURA_CANONICA_DEMANDAS.md` — Estrutura canônica
- `/METODO/GOVERNANCA_GATES.md` — Governança de gates
- `/METODO/TEMPLATE_DEMANDA_CANONICA.md` — Template de demanda
