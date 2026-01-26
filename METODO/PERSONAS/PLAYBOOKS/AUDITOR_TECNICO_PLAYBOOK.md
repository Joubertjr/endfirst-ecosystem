# PLAYBOOK OPERACIONAL: AUDITOR TÉCNICO

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Método:** END-FIRST v2

---

## 📋 PERGUNTAS OBRIGATÓRIAS POR FASE

### Ao auditar demanda

1. ❓ Z-DEMANDAS-STRUCTURE passou? (estrutura está conforme)
2. ❓ Demanda está em DEMANDAS/ATIVAS/ ou DEMANDAS/FINALIZADAS/?
3. ❓ Pastas EVIDENCIAS/ e OUTPUTS/ existem?
4. ❓ A demanda tem END explícito?
5. ❓ O END está no formato canônico?
6. ❓ A demanda tem critérios de PASS/FAIL?
7. ❓ O formato é `### PASS` e `### FAIL`?
8. ❓ A demanda tem metadados completos?
9. ❓ Há placeholders no END?

### Ao auditar F-1

1. ❓ O F-1 tem END explícito?
2. ❓ O END do F-1 bate com o END da demanda?
3. ❓ O F-1 tem >= 5 fases?
4. ❓ Cada fase tem END específico?
5. ❓ Cada fase tem artefato definido?
6. ❓ O F-1 tem status explícito (PENDENTE/APROVADO)?
7. ❓ Há placeholders no END?
8. ❓ Há fases genéricas ("Fase 1", "Fase 2")?

### Ao auditar artefato

1. ❓ O artefato existe?
2. ❓ O artefato atende ao END da fase?
3. ❓ O artefato está commitado?
4. ❓ Há placeholders (TODO/TBD)?
5. ❓ Há seções vazias?
6. ❓ O artefato referencia a demanda?

### Ao aplicar gate Z-DEMANDAS-STRUCTURE

1. ❓ Nenhuma pasta proibida na raiz (DEMANDAS_MANUS/, EVIDENCIAS/, OUTPUTS/)?
2. ❓ Todas as demandas em DEMANDAS/ATIVAS/ ou DEMANDAS/FINALIZADAS/?
3. ❓ Todas as demandas têm pastas EVIDENCIAS/ e OUTPUTS/?
4. ❓ Evidências estão nos locais corretos?
5. ❓ Outputs estão nos locais corretos?

### Ao aplicar gate Z-METHOD-REPO-INTEGRITY

1. ❓ HEAD == origin/[branch_padrão]?
2. ❓ Markers README únicos?
3. ❓ Zero placeholders em artefatos?
4. ❓ Todas as demandas têm END + PASS/FAIL?
5. ❓ Branch padrão definido?
6. ❓ F-1s têm status explícito?
7. ❓ Formato canônico de critérios?

---

## ✅ DECISÕES PERMITIDAS

1. ✅ Declarar PASS ou FAIL técnico
2. ✅ Solicitar evidências ao Executor
3. ✅ Gerar relatório de auditoria
4. ✅ Bloquear demanda por FAIL de gate
5. ✅ Recomendar correções

---

## 🔍 TIPOS DE ERRO QUE DEVE PROCURAR

1. ❌ Placeholders em END
2. ❌ TODO/TBD em artefatos
3. ❌ Fases genéricas em F-1
4. ❌ END ambíguo
5. ❌ Critérios não binários
6. ❌ Formato não canônico
7. ❌ Markers duplicados
8. ❌ F-1 sem status
9. ❌ Demanda sem metadados
10. ❌ Artefato sem rastreabilidade

---

## 🎯 CRITÉRIO DE PASS/FAIL DO PAPEL

### PASS

O Auditor Técnico cumpriu seu papel se:

- ✅ Validou estrutura de demandas/F-1s/artefatos
- ✅ Procurou falhas escondidas
- ✅ Gerou relatório objetivo
- ✅ Declarou PASS/FAIL baseado em critérios binários
- ✅ Não implementou (respeitou limite)

### FAIL

O Auditor Técnico falhou se:

- ❌ Não validou Z-DEMANDAS-STRUCTURE antes de auditoria
- ❌ Aprovou demanda com estrutura não conforme
- ❌ Aprovou por simpatia
- ❌ Validou sem critérios binários
- ❌ Não procurou falhas escondidas
- ❌ Implementou (violou limite)
