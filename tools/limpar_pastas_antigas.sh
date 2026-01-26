#!/bin/bash

# Script para limpar pastas antigas após reorganização
# Remove duplicatas e mantém apenas a nova estrutura

set -e

REPO_ROOT="/Users/joubertsouza/Documents/@endfirstmethod/endfirst-ecosystem"
cd "$REPO_ROOT"

echo "🧹 Limpando pastas antigas..."

# 1. Remover DEMANDAS_MANUS (já foram copiados para DEMANDAS/ATIVAS e FINALIZADAS)
echo "📦 Removendo DEMANDAS_MANUS/ (arquivos já estão em DEMANDAS/)..."
if [ -d "DEMANDAS_MANUS" ]; then
    rm -rf DEMANDAS_MANUS
    echo "  ✅ DEMANDAS_MANUS/ removida"
fi

# 2. Remover arquivos duplicados de EVIDENCIAS que já estão nas pastas de demanda
echo "📋 Verificando evidências duplicadas em EVIDENCIAS/..."

# Lista de evidências que já foram movidas para as pastas de demanda
evidencias_movidas=(
    "execucao_demanda_metodo_005_f1.md"
    "execucao_demanda_metodo_005_f2.md"
    "execucao_demanda_metodo_005_f3.md"
    "execucao_demanda_metodo_005_f4.md"
    "execucao_demanda_metodo_005_f5.md"
    "execucao_demanda_metodo_005_f6.md"
    "execucao_demanda_metodo_010_f1.md"
    "execucao_demanda_metodo_010_f2.md"
    "execucao_demanda_metodo_010_f3.md"
    "execucao_demanda_metodo_010_f4.md"
    "execucao_demanda_metodo_010_f5.md"
    "execucao_demanda_metodo_010_f6.md"
    "execucao_demanda_metodo_013_completa.md"
    "execucao_demanda_metodo_016.md"
    "execucao_demanda_soft_005_completa.md"
    "execucao_demanda_soft_006_completa.md"
    "execucao_gov_001_consolidada.md"
    "execucao_metodo_006_consolidada.md"
    "execucao_metodo_007_consolidada.md"
    "execucao_metodo_011_consolidada.md"
    "execucao_metodo_012_consolidada.md"
    "execucao_metodo_013_consolidada.md"
    "execucao_metodo_015_consolidada.md"
    "execucao_prod_001_consolidada.md"
    "execucao_prod_002_consolidada.md"
    "execucao_prod_003_consolidada.md"
    "execucao_prod_004_consolidada.md"
    "execucao_soft_002_consolidada.md"
    "execucao_soft_003_consolidada.md"
    "execucao_soft_004_consolidada.md"
    "execucao_soft_005_consolidada.md"
    "execucao_soft_006_consolidada.md"
)

for evidencia in "${evidencias_movidas[@]}"; do
    if [ -f "EVIDENCIAS/$evidencia" ]; then
        rm "EVIDENCIAS/$evidencia"
        echo "  ✅ Removida duplicata: $evidencia"
    fi
done

# 3. Remover pacotes ZIP duplicados (já estão nas pastas de demanda)
echo "📦 Verificando pacotes ZIP duplicados..."
if [ -f "EVIDENCIAS/pacote_demanda_metodo_010.zip" ]; then
    rm "EVIDENCIAS/pacote_demanda_metodo_010.zip"
    echo "  ✅ Removido duplicata: pacote_demanda_metodo_010.zip"
fi

# 4. Verificar se há arquivos restantes em DEMANDAS/ (fora de ATIVAS e FINALIZADAS)
echo "📁 Verificando arquivos restantes em DEMANDAS/..."
arquivos_restantes=$(find DEMANDAS -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' ')
if [ "$arquivos_restantes" -gt 0 ]; then
    echo "  ⚠️  Ainda há $arquivos_restantes arquivo(s) em DEMANDAS/ (fora de ATIVAS/FINALIZADAS)"
    find DEMANDAS -maxdepth 1 -type f
else
    echo "  ✅ DEMANDAS/ está limpo (apenas ATIVAS e FINALIZADAS)"
fi

echo ""
echo "✅ Limpeza concluída!"
echo ""
echo "📊 Estrutura final:"
echo "   - DEMANDAS/ATIVAS/ - $(find DEMANDAS/ATIVAS -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ') demandas"
echo "   - DEMANDAS/FINALIZADAS/ - $(find DEMANDAS/FINALIZADAS -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ') demandas"
echo "   - EVIDENCIAS/ - $(find EVIDENCIAS -type f -name "*.md" 2>/dev/null | wc -l | tr -d ' ') arquivos (apenas evidências gerais)"
echo "   - OUTPUTS/ - $(find OUTPUTS -type f 2>/dev/null | wc -l | tr -d ' ') arquivos (pacotes gerais)"
