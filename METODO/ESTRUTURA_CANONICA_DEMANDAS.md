---
document_id: ESTRUTURA_CANONICA_DEMANDAS
type: canonical
owner: CEO (Joubert Jr)
status: approved
approved_by: CEO
approved_at: 2026-01-26
governed_by: /METODO/END_FIRST_V2.md
version: 1.0
created_at: 2026-01-26
demanda_origem: Reorganização estrutural 2026-01-26
---

# ESTRUTURA CANÔNICA DE DEMANDAS — END-FIRST v2.5

**Versão:** 1.0  
**Data:** 26 de Janeiro de 2026  
**Status:** Canônico (Obrigatório)  
**Path Canônico:** `/METODO/ESTRUTURA_CANONICA_DEMANDAS.md`

---

## 🎯 O QUE É ESTRUTURA CANÔNICA DE DEMANDAS

A **Estrutura Canônica de Demandas** define a organização obrigatória de todas as demandas, evidências e outputs no repositório `endfirst-ecosystem`.

**Princípio fundamental:**
> "Nenhuma demanda pode existir fora de DEMANDAS/ATIVAS/ ou DEMANDAS/FINALIZADAS/. Tudo relacionado a uma demanda está na mesma pasta."

---

## 🔒 REGRA ABSOLUTA

**Toda demanda DEVE seguir esta estrutura.**

**Demandas fora desta estrutura são FAIL estrutural.**

---

## 📁 ESTRUTURA OBRIGATÓRIA

### Árvore Oficial

```
DEMANDAS/
├── ATIVAS/              # Demandas em execução
│   └── DEMANDA-<TIPO>-<NUMERO>/
│       ├── DEMANDA-<TIPO>-<NUMERO>_<TITULO>.md
│       ├── DEMANDA-<TIPO>-<NUMERO>_F1_PLANEJAMENTO.md
│       ├── DEMANDA-<TIPO>-<NUMERO>_F6_CONCLUSAO.md (se houver)
│       ├── EVIDENCIAS/
│       │   ├── execucao_demanda_<tipo>_<numero>_f1.md
│       │   ├── execucao_demanda_<tipo>_<numero>_f2.md
│       │   ├── ... (evidências de todas as fases)
│       │   └── pacote_demanda_<tipo>_<numero>.zip (se houver)
│       └── OUTPUTS/
│           └── (outputs específicos desta demanda, se houver)
│
├── FINALIZADAS/         # Demandas concluídas
│   └── DEMANDA-<TIPO>-<NUMERO>/
│       ├── (mesma estrutura de ATIVAS/)
│       ├── EVIDENCIAS/
│       └── OUTPUTS/
│
└── SEM_VINCULO/          # Arquivos sem vínculo específico
    ├── EVIDENCIAS/       # Evidências gerais (auditorias, gates, etc.)
    └── OUTPUTS/          # Pacotes gerais (execução completa, etc.)
```

---

## 📋 REGRAS CANÔNICAS

### Regra 1: Localização de Demandas

**Regra canônica:**
> "Nenhuma demanda pode existir fora de DEMANDAS/ATIVAS/ ou DEMANDAS/FINALIZADAS/."

**Critérios de PASS:**
- ✅ Demanda está em `DEMANDAS/ATIVAS/<DEMANDA-ID>/` ou `DEMANDAS/FINALIZADAS/<DEMANDA-ID>/`
- ✅ Nome da pasta segue padrão `DEMANDA-<TIPO>-<NUMERO>`

**Critérios de FAIL:**
- ❌ Demanda existe em `DEMANDAS_MANUS/` (pasta removida)
- ❌ Demanda existe na raiz de `DEMANDAS/` (fora de ATIVAS/FINALIZADAS)
- ❌ Demanda existe em qualquer outro local

---

### Regra 2: Estrutura de Pasta da Demanda

**Regra canônica:**
> "Cada demanda DEVE ter sua própria pasta com subpastas EVIDENCIAS/ e OUTPUTS/."

**Estrutura obrigatória:**
```
DEMANDAS/ATIVAS/DEMANDA-<TIPO>-<NUMERO>/
├── DEMANDA-<TIPO>-<NUMERO>_<TITULO>.md        # Obrigatório
├── DEMANDA-<TIPO>-<NUMERO>_F1_PLANEJAMENTO.md # Obrigatório (se exige_f1: sim)
├── EVIDENCIAS/                                 # Obrigatório
└── OUTPUTS/                                    # Obrigatório
```

**Critérios de PASS:**
- ✅ Pasta da demanda existe
- ✅ Pasta `EVIDENCIAS/` existe (mesmo que vazia)
- ✅ Pasta `OUTPUTS/` existe (mesmo que vazia)
- ✅ Arquivo da demanda principal existe

**Critérios de FAIL:**
- ❌ Pasta da demanda não existe
- ❌ Pasta `EVIDENCIAS/` não existe
- ❌ Pasta `OUTPUTS/` não existe
- ❌ Arquivo da demanda principal não existe

---

### Regra 3: Evidências

**Regra canônica:**
> "Toda evidência DEVE estar dentro da pasta EVIDENCIAS/ da demanda correspondente."

**Critérios de PASS:**
- ✅ Evidências estão em `DEMANDAS/ATIVAS/<DEMANDA-ID>/EVIDENCIAS/` ou `DEMANDAS/FINALIZADAS/<DEMANDA-ID>/EVIDENCIAS/`
- ✅ Evidências gerais (sem vínculo) estão em `DEMANDAS/SEM_VINCULO/EVIDENCIAS/`

**Critérios de FAIL:**
- ❌ Evidência existe em `EVIDENCIAS/` na raiz (pasta removida)
- ❌ Evidência existe fora da pasta da demanda
- ❌ Evidência específica de demanda está em `SEM_VINCULO/`

---

### Regra 4: Outputs

**Regra canônica:**
> "Todo output DEVE estar dentro da pasta OUTPUTS/ da demanda correspondente ou em SEM_VINCULO/ se for geral."

**Critérios de PASS:**
- ✅ Outputs específicos estão em `DEMANDAS/ATIVAS/<DEMANDA-ID>/OUTPUTS/` ou `DEMANDAS/FINALIZADAS/<DEMANDA-ID>/OUTPUTS/`
- ✅ Outputs gerais (pacotes completos) estão em `DEMANDAS/SEM_VINCULO/OUTPUTS/`

**Critérios de FAIL:**
- ❌ Output existe em `OUTPUTS/` na raiz (pasta removida)
- ❌ Output específico de demanda está fora da pasta da demanda
- ❌ Output geral está dentro de pasta de demanda específica

---

### Regra 5: Pastas Proibidas na Raiz

**Regra canônica:**
> "As pastas DEMANDAS_MANUS/, EVIDENCIAS/ e OUTPUTS/ NÃO podem existir na raiz do repositório."

**Critérios de PASS:**
- ✅ `DEMANDAS_MANUS/` não existe na raiz
- ✅ `EVIDENCIAS/` não existe na raiz
- ✅ `OUTPUTS/` não existe na raiz

**Critérios de FAIL:**
- ❌ `DEMANDAS_MANUS/` existe na raiz
- ❌ `EVIDENCIAS/` existe na raiz
- ❌ `OUTPUTS/` existe na raiz

---

## 🔒 GATE ESTRUTURAL: Z-DEMANDAS-STRUCTURE

### Definição

**Z-DEMANDAS-STRUCTURE** é o gate obrigatório que valida a conformidade com a estrutura canônica de demandas.

**Obrigatoriedade:** Universal (todas as demandas)

**Quando executar:**
- Antes de criar qualquer demanda
- Antes de executar qualquer fase
- Antes de mover demanda para FINALIZADAS
- Em qualquer commit que altere estrutura de pastas

---

### Critérios de PASS

**Z-DEMANDAS-STRUCTURE passa se TODOS os critérios abaixo são verdadeiros:**

1. ✅ **Nenhuma pasta proibida na raiz:**
   - `DEMANDAS_MANUS/` não existe
   - `EVIDENCIAS/` não existe
   - `OUTPUTS/` não existe

2. ✅ **Todas as demandas estão em local correto:**
   - Todas em `DEMANDAS/ATIVAS/` ou `DEMANDAS/FINALIZADAS/`
   - Nenhuma demanda na raiz de `DEMANDAS/`

3. ✅ **Estrutura de pasta da demanda está completa:**
   - Pasta `EVIDENCIAS/` existe dentro da pasta da demanda
   - Pasta `OUTPUTS/` existe dentro da pasta da demanda
   - Arquivo da demanda principal existe

4. ✅ **Evidências estão no local correto:**
   - Evidências específicas estão em `DEMANDAS/<STATUS>/<DEMANDA-ID>/EVIDENCIAS/`
   - Evidências gerais estão em `DEMANDAS/SEM_VINCULO/EVIDENCIAS/`
   - Nenhuma evidência em `EVIDENCIAS/` na raiz

5. ✅ **Outputs estão no local correto:**
   - Outputs específicos estão em `DEMANDAS/<STATUS>/<DEMANDA-ID>/OUTPUTS/`
   - Outputs gerais estão em `DEMANDAS/SEM_VINCULO/OUTPUTS/`
   - Nenhum output em `OUTPUTS/` na raiz

---

### Critérios de FAIL

**Z-DEMANDAS-STRUCTURE falha se QUALQUER critério abaixo é verdadeiro:**

1. ❌ **Pasta proibida existe na raiz:**
   - `DEMANDAS_MANUS/` existe
   - `EVIDENCIAS/` existe
   - `OUTPUTS/` existe

2. ❌ **Demanda fora do local correto:**
   - Demanda existe fora de `DEMANDAS/ATIVAS/` ou `DEMANDAS/FINALIZADAS/`
   - Demanda existe na raiz de `DEMANDAS/`

3. ❌ **Estrutura de pasta da demanda incompleta:**
   - Pasta `EVIDENCIAS/` não existe dentro da pasta da demanda
   - Pasta `OUTPUTS/` não existe dentro da pasta da demanda
   - Arquivo da demanda principal não existe

4. ❌ **Evidência fora do local correto:**
   - Evidência específica está fora da pasta da demanda
   - Evidência específica está em `SEM_VINCULO/`
   - Evidência existe em `EVIDENCIAS/` na raiz

5. ❌ **Output fora do local correto:**
   - Output específico está fora da pasta da demanda
   - Output específico está em `SEM_VINCULO/`
   - Output existe em `OUTPUTS/` na raiz

---

### Consequências de FAIL

**Se Z-DEMANDAS-STRUCTURE falha:**

1. ❌ **Bloqueio de execução:**
   - Executor não pode executar fases
   - Demanda não pode ser movida para FINALIZADAS
   - Commit não pode ser aceito

2. ❌ **Correção obrigatória:**
   - Estrutura deve ser corrigida antes de prosseguir
   - Gate deve passar antes de qualquer execução

3. ❌ **Auditoria:**
   - FAIL é registrado em evidência
   - Causa raiz deve ser identificada
   - Prevenção deve ser implementada

---

## 📋 EXEMPLOS PRÁTICOS

### Exemplo 1: Estrutura Correta ✅

```
DEMANDAS/ATIVAS/DEMANDA-METODO-010/
├── DEMANDA-METODO-010_GOVERNANCA_PRODUTOS.md
├── DEMANDA-METODO-010_F1_PLANEJAMENTO.md
├── EVIDENCIAS/
│   ├── execucao_demanda_metodo_010_f1.md
│   ├── execucao_demanda_metodo_010_f2.md
│   └── pacote_demanda_metodo_010.zip
└── OUTPUTS/
```

**Status:** ✅ PASS (Z-DEMANDAS-STRUCTURE)

---

### Exemplo 2: Estrutura Incorreta ❌

```
DEMANDAS/
├── DEMANDA-METODO-010.md  # ❌ Fora de ATIVAS/
└── ATIVAS/
    └── DEMANDA-METODO-010/
        └── (sem EVIDENCIAS/)  # ❌ Falta pasta obrigatória
```

**Status:** ❌ FAIL (Z-DEMANDAS-STRUCTURE)

**Problemas:**
1. Demanda na raiz de DEMANDAS/ (deveria estar em ATIVAS/)
2. Falta pasta EVIDENCIAS/ dentro da demanda

---

### Exemplo 3: Pasta Proibida ❌

```
endfirst-ecosystem/
├── DEMANDAS/
│   └── ATIVAS/
└── EVIDENCIAS/  # ❌ Pasta proibida na raiz
```

**Status:** ❌ FAIL (Z-DEMANDAS-STRUCTURE)

**Problema:**
- `EVIDENCIAS/` existe na raiz (deveria estar dentro de DEMANDAS/)

---

## 🔄 FLUXO OBRIGATÓRIO

### Fluxo de Criação de Demanda

```
1. Criar pasta: DEMANDAS/ATIVAS/DEMANDA-<TIPO>-<NUMERO>/
   ↓
2. Criar subpastas: EVIDENCIAS/ e OUTPUTS/
   ↓
3. Criar arquivo: DEMANDA-<TIPO>-<NUMERO>_<TITULO>.md
   ↓
4. Executar Z-DEMANDAS-STRUCTURE
   ↓
5. Se PASS → Prosseguir
   Se FAIL → Corrigir estrutura
```

### Fluxo de Execução

```
1. Validar Z-DEMANDAS-STRUCTURE
   ↓
2. Criar F-1 (se necessário)
   ↓
3. Executar fases (F1-F6)
   ↓
4. Registrar evidências em DEMANDAS/ATIVAS/<DEMANDA-ID>/EVIDENCIAS/
   ↓
5. Gerar outputs em DEMANDAS/ATIVAS/<DEMANDA-ID>/OUTPUTS/
   ↓
6. Validar Z-DEMANDAS-STRUCTURE novamente
   ↓
7. Se todas as fases PASS → Mover para FINALIZADAS/
```

### Fluxo de Finalização

```
1. Validar Z-DEMANDAS-STRUCTURE
   ↓
2. Validar completude (todas as fases PASS)
   ↓
3. Mover pasta de ATIVAS/ para FINALIZADAS/
   ↓
4. Validar Z-DEMANDAS-STRUCTURE após movimentação
   ↓
5. Se PASS → Demanda finalizada
```

---

## 🚫 ANTI-PADRÕES (PROIBIDOS)

### ❌ Criar demanda fora de DEMANDAS/

**Proibido:**
- Criar demanda em `DEMANDAS_MANUS/`
- Criar demanda na raiz de `DEMANDAS/`
- Criar demanda em qualquer outro local

**Correto:**
- Criar em `DEMANDAS/ATIVAS/<DEMANDA-ID>/`

---

### ❌ Criar evidência fora da pasta da demanda

**Proibido:**
- Criar evidência em `EVIDENCIAS/` na raiz
- Criar evidência fora da pasta da demanda
- Criar evidência específica em `SEM_VINCULO/`

**Correto:**
- Criar em `DEMANDAS/ATIVAS/<DEMANDA-ID>/EVIDENCIAS/`

---

### ❌ Criar output fora da pasta da demanda

**Proibido:**
- Criar output em `OUTPUTS/` na raiz
- Criar output fora da pasta da demanda
- Criar output específico em `SEM_VINCULO/`

**Correto:**
- Criar em `DEMANDAS/ATIVAS/<DEMANDA-ID>/OUTPUTS/`

---

## ✅ VALIDAÇÃO AUTOMÁTICA

### Script de Validação

O gate Z-DEMANDAS-STRUCTURE pode ser validado automaticamente:

```bash
# Verificar pastas proibidas
test -d DEMANDAS_MANUS && echo "FAIL: DEMANDAS_MANUS existe" || echo "PASS"
test -d EVIDENCIAS && echo "FAIL: EVIDENCIAS existe na raiz" || echo "PASS"
test -d OUTPUTS && echo "FAIL: OUTPUTS existe na raiz" || echo "PASS"

# Verificar estrutura de demandas
for demanda in DEMANDAS/ATIVAS/* DEMANDAS/FINALIZADAS/*; do
  test -d "$demanda/EVIDENCIAS" || echo "FAIL: $demanda sem EVIDENCIAS/"
  test -d "$demanda/OUTPUTS" || echo "FAIL: $demanda sem OUTPUTS/"
done
```

---

## 🔗 RELAÇÃO COM OUTROS GATES

### Z-DEMANDAS-STRUCTURE + Z-F1-INTEGRITY

**Z-DEMANDAS-STRUCTURE** valida estrutura física.

**Z-F1-INTEGRITY** valida conteúdo do F-1.

**Ordem:**
1. Z-DEMANDAS-STRUCTURE (estrutura)
2. Z-F1-INTEGRITY (conteúdo)

---

### Z-DEMANDAS-STRUCTURE + Z-DEMANDA-COMPLETUDE

**Z-DEMANDAS-STRUCTURE** valida estrutura física.

**Z-DEMANDA-COMPLETUDE** valida completude de execução.

**Ordem:**
1. Z-DEMANDAS-STRUCTURE (estrutura)
2. Z-DEMANDA-COMPLETUDE (completude)

---

## 📊 METADADOS

**Versão:** 1.0  
**Criado em:** 2026-01-26  
**Origem:** Reorganização estrutural 2026-01-26  
**Autor:** Auto (Agent)  
**Aprovado por:** CEO (Joubert Jr)  
**Status:** Canônico (Obrigatório)

---

## 🔗 REFERÊNCIAS

- `/METODO/END_FIRST_V2.md` — Fluxo END-FIRST v2
- `/METODO/GOVERNANCA_GATES.md` — Governança de gates
- `/METODO/TEMPLATE_DEMANDA_CANONICA.md` — Template de demanda
- `/RELATORIO_REORGANIZACAO_DEMANDAS.md` — Relatório de reorganização
