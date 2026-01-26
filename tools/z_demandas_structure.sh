#!/bin/bash

# Gate Z-DEMANDAS-STRUCTURE
# Valida estrutura canônica de demandas
# FAIL se estrutura não está conforme

set -e

REPO_ROOT="/Users/joubertsouza/Documents/@endfirstmethod/endfirst-ecosystem"
cd "$REPO_ROOT"

FAIL_COUNT=0
PASS_COUNT=0

echo "🔍 Executando Z-DEMANDAS-STRUCTURE..."
echo ""

# 1. Verificar pastas proibidas na raiz
echo "1. Verificando pastas proibidas na raiz..."

if [ -d "DEMANDAS_MANUS" ]; then
    echo "  ❌ FAIL: DEMANDAS_MANUS/ existe na raiz"
    FAIL_COUNT=$((FAIL_COUNT + 1))
else
    echo "  ✅ PASS: DEMANDAS_MANUS/ não existe"
    PASS_COUNT=$((PASS_COUNT + 1))
fi

if [ -d "EVIDENCIAS" ]; then
    echo "  ❌ FAIL: EVIDENCIAS/ existe na raiz"
    FAIL_COUNT=$((FAIL_COUNT + 1))
else
    echo "  ✅ PASS: EVIDENCIAS/ não existe na raiz"
    PASS_COUNT=$((PASS_COUNT + 1))
fi

if [ -d "OUTPUTS" ]; then
    echo "  ❌ FAIL: OUTPUTS/ existe na raiz"
    FAIL_COUNT=$((FAIL_COUNT + 1))
else
    echo "  ✅ PASS: OUTPUTS/ não existe na raiz"
    PASS_COUNT=$((PASS_COUNT + 1))
fi

echo ""

# 2. Verificar que todas as demandas estão em ATIVAS ou FINALIZADAS
echo "2. Verificando localização de demandas..."

demandas_fora=$(find DEMANDAS -maxdepth 1 -type f -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
if [ "$demandas_fora" -gt 0 ]; then
    echo "  ❌ FAIL: $demandas_fora demanda(s) fora de ATIVAS/FINALIZADAS"
    find DEMANDAS -maxdepth 1 -type f -name "*.md"
    FAIL_COUNT=$((FAIL_COUNT + 1))
else
    echo "  ✅ PASS: Nenhuma demanda fora de ATIVAS/FINALIZADAS"
    PASS_COUNT=$((PASS_COUNT + 1))
fi

echo ""

# 3. Verificar estrutura de cada demanda
echo "3. Verificando estrutura de pastas de demanda..."

demandas_sem_evidencias=0
demandas_sem_outputs=0
demandas_sem_arquivo=0

for demanda_dir in DEMANDAS/ATIVAS/* DEMANDAS/FINALIZADAS/*; do
    if [ ! -d "$demanda_dir" ]; then
        continue
    fi
    
    demanda_id=$(basename "$demanda_dir")
    
    # Verificar EVIDENCIAS/
    if [ ! -d "$demanda_dir/EVIDENCIAS" ]; then
        echo "  ❌ FAIL: $demanda_id sem pasta EVIDENCIAS/"
        demandas_sem_evidencias=$((demandas_sem_evidencias + 1))
    fi
    
    # Verificar OUTPUTS/
    if [ ! -d "$demanda_dir/OUTPUTS" ]; then
        echo "  ❌ FAIL: $demanda_id sem pasta OUTPUTS/"
        demandas_sem_outputs=$((demandas_sem_outputs + 1))
    fi
    
    # Verificar arquivo da demanda (pode ter vários nomes)
    # Exceção: pastas que são apenas para evidências de atualização do método
    if [ "$demanda_id" = "DEMANDA-METODO-017" ]; then
        # Esta pasta é apenas para evidência de atualização do método
        continue
    fi
    
    arquivos_demanda=$(find "$demanda_dir" -maxdepth 1 -type f \( -name "DEMANDA-*.md" -o -name "DEMANDA_*.md" \) 2>/dev/null | wc -l | tr -d ' ')
    if [ "$arquivos_demanda" -eq 0 ]; then
        echo "  ❌ FAIL: $demanda_id sem arquivo de demanda principal"
        demandas_sem_arquivo=$((demandas_sem_arquivo + 1))
    fi
done

if [ "$demandas_sem_evidencias" -eq 0 ] && [ "$demandas_sem_outputs" -eq 0 ] && [ "$demandas_sem_arquivo" -eq 0 ]; then
    echo "  ✅ PASS: Todas as demandas têm estrutura completa"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    if [ "$demandas_sem_evidencias" -gt 0 ]; then
        FAIL_COUNT=$((FAIL_COUNT + demandas_sem_evidencias))
    fi
    if [ "$demandas_sem_outputs" -gt 0 ]; then
        FAIL_COUNT=$((FAIL_COUNT + demandas_sem_outputs))
    fi
    if [ "$demandas_sem_arquivo" -gt 0 ]; then
        FAIL_COUNT=$((FAIL_COUNT + demandas_sem_arquivo))
    fi
fi

echo ""

# 4. Verificar evidências e outputs estão nos locais corretos
echo "4. Verificando localização de evidências e outputs..."

# Evidências específicas devem estar dentro de pastas de demanda
evidencias_fora=0
for evidencia in $(find DEMANDAS/ATIVAS DEMANDAS/FINALIZADAS -name "execucao_*.md" -o -name "*.zip" 2>/dev/null | grep -v "/EVIDENCIAS/" | grep -v "/OUTPUTS/"); do
    if [ -f "$evidencia" ]; then
        echo "  ❌ FAIL: Evidência/output fora de EVIDENCIAS/ ou OUTPUTS/: $evidencia"
        evidencias_fora=$((evidencias_fora + 1))
    fi
done

if [ "$evidencias_fora" -eq 0 ]; then
    echo "  ✅ PASS: Todas as evidências e outputs estão nos locais corretos"
    PASS_COUNT=$((PASS_COUNT + 1))
else
    FAIL_COUNT=$((FAIL_COUNT + evidencias_fora))
fi

echo ""

# Resultado final
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 RESULTADO DO GATE Z-DEMANDAS-STRUCTURE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ PASS: $PASS_COUNT"
echo "❌ FAIL: $FAIL_COUNT"
echo ""

if [ "$FAIL_COUNT" -eq 0 ]; then
    echo "🎯 STATUS: ✅ PASS"
    echo ""
    echo "Estrutura está conforme a estrutura canônica definida em:"
    echo "/METODO/ESTRUTURA_CANONICA_DEMANDAS.md"
    exit 0
else
    echo "🎯 STATUS: ❌ FAIL"
    echo ""
    echo "Estrutura não está conforme. Corrija os problemas acima antes de prosseguir."
    echo ""
    echo "Referência: /METODO/ESTRUTURA_CANONICA_DEMANDAS.md"
    exit 1
fi
