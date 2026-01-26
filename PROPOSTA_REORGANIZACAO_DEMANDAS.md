# PROPOSTA DE REORGANIZAÇÃO ESTRUTURAL — DEMANDAS

**Data:** 2026-01-26  
**Proponente:** Manus (Agent)  
**Status:** Proposta

---

## 🎯 PROBLEMA IDENTIFICADO

A estrutura atual apresenta problemas de rastreabilidade:

1. **Duas pastas de demandas** (`DEMANDAS` e `DEMANDAS_MANUS`) sem critério claro de separação
2. **Evidências desconectadas** — todas em `EVIDENCIAS/` sem organização por demanda
3. **Outputs desconectados** — todos em `OUTPUTS/` sem rastreabilidade à demanda origem
4. **Sem separação** entre demandas ativas e finalizadas
5. **Falta de hierarquia** — não há estrutura que agrupe tudo relacionado a uma demanda

---

## ✅ PROPOSTA DE ESTRUTURA

### Estrutura Proposta

```
DEMANDAS/
├── ATIVAS/
│   ├── DEMANDA-METODO-010/
│   │   ├── DEMANDA-METODO-010_GOVERNANCA_PRODUTOS.md
│   │   ├── DEMANDA-METODO-010_F1_PLANEJAMENTO.md
│   │   ├── EVIDENCIAS/
│   │   │   ├── execucao_demanda_metodo_010_f1.md
│   │   │   ├── execucao_demanda_metodo_010_f2.md
│   │   │   ├── execucao_demanda_metodo_010_f3.md
│   │   │   ├── execucao_demanda_metodo_010_f4.md
│   │   │   ├── execucao_demanda_metodo_010_f5.md
│   │   │   ├── execucao_demanda_metodo_010_f6.md
│   │   │   └── pacote_demanda_metodo_010.zip
│   │   └── OUTPUTS/
│   │       └── (outputs específicos desta demanda, se houver)
│   ├── DEMANDA-SOFT-005/
│   │   ├── DEMANDA-SOFT-005_INTEGRACAO_NOTEBOOKLM.md
│   │   ├── DEMANDA-SOFT-005_F1_PLANEJAMENTO.md
│   │   ├── EVIDENCIAS/
│   │   │   └── execucao_demanda_soft_005_completa.md
│   │   └── OUTPUTS/
│   └── ...
│
└── FINALIZADAS/
    ├── DEMANDA-METODO-005/
    │   ├── DEMANDA-METODO-005_ROBUSTEZ_EXECUCAO_LONGA.md
    │   ├── DEMANDA-METODO-005_F1_PLANEJAMENTO.md
    │   ├── DEMANDA-METODO-005_F6_CONCLUSAO.md
    │   ├── EVIDENCIAS/
    │   │   ├── execucao_demanda_metodo_005_f1.md
    │   │   ├── execucao_demanda_metodo_005_f2.md
    │   │   ├── execucao_demanda_metodo_005_f3.md
    │   │   ├── execucao_demanda_metodo_005_f4.md
    │   │   ├── execucao_demanda_metodo_005_f5.md
    │   │   └── execucao_demanda_metodo_005_f6.md
    │   └── OUTPUTS/
    └── ...
```

---

## 📋 REGRAS DE ORGANIZAÇÃO

### 1. Unificação de Pastas

- **`DEMANDAS/`** — única pasta para todas as demandas
- **`DEMANDAS/ATIVAS/`** — demandas em execução (status: backlog, doing, in_progress)
- **`DEMANDAS/FINALIZADAS/`** — demandas concluídas (status: done, aprovado)

### 2. Estrutura por Demanda

Cada demanda tem sua própria pasta com:
- **Arquivos da demanda** (demanda principal, F-1, F-6, etc.)
- **`EVIDENCIAS/`** — todas as evidências de execução desta demanda
- **`OUTPUTS/`** — todos os outputs gerados por esta demanda

### 3. Critério de Finalização

Demanda vai para `FINALIZADAS/` quando:
- Status = `done` ou `aprovado`
- F-6 concluída (quando aplicável)
- Validação do CEO concluída

### 4. Rastreabilidade

**Tudo relacionado a uma demanda está na mesma pasta:**
- ✅ Demanda original
- ✅ F-1 (planejamento)
- ✅ F-6 (conclusão, se houver)
- ✅ Todas as evidências
- ✅ Todos os outputs
- ✅ Pacotes ZIP relacionados

---

## 🔄 PROCESSO DE MIGRAÇÃO

### Fase 1: Criar Nova Estrutura
1. Criar `DEMANDAS/ATIVAS/` e `DEMANDAS/FINALIZADAS/`
2. Criar pastas individuais para cada demanda identificada

### Fase 2: Mover Arquivos
1. Mover demandas de `DEMANDAS_MANUS/` para `DEMANDAS/ATIVAS/` ou `DEMANDAS/FINALIZADAS/`
2. Mover demandas de `DEMANDAS/` (se houver) para estrutura unificada
3. Mover evidências de `EVIDENCIAS/` para dentro das pastas de cada demanda
4. Mover outputs específicos de `OUTPUTS/` para dentro das pastas de cada demanda

### Fase 3: Limpeza
1. Remover `DEMANDAS_MANUS/` (após migração completa)
2. Manter `EVIDENCIAS/` apenas para evidências gerais (não específicas de demanda)
3. Manter `OUTPUTS/` apenas para outputs gerais (pacotes completos, etc.)

---

## ✅ BENEFÍCIOS

1. **Rastreabilidade completa** — tudo de uma demanda em um lugar
2. **Organização clara** — separação entre ativas e finalizadas
3. **Estrutura única** — uma única pasta DEMANDAS
4. **Facilita auditoria** — fácil encontrar tudo relacionado a uma demanda
5. **Facilita navegação** — estrutura hierárquica intuitiva

---

## ⚠️ CONSIDERAÇÕES

### Evidências Gerais
Algumas evidências não são específicas de uma demanda (ex: `auditoria_repositorio_completa_2026-01-23.md`). Estas permanecem em `EVIDENCIAS/` na raiz.

### Outputs Gerais
Pacotes completos de execução (ex: `PACOTE_EXECUCAO_COMPLETA_END_FIRST_v3.zip`) permanecem em `OUTPUTS/` na raiz, pois não são específicos de uma demanda.

### Scripts e Referências
Scripts que referenciam caminhos antigos precisarão ser atualizados:
- `tools/gerar_pacote_v3.sh`
- Referências em documentos do método
- Referências em evidências

---

## 📝 PRÓXIMOS PASSOS

1. ✅ Aprovar proposta
2. ⏳ Executar migração (script automatizado)
3. ⏳ Atualizar referências
4. ⏳ Validar estrutura final
5. ⏳ Documentar nova estrutura no método

---

**Status:** Aguardando aprovação do CEO
