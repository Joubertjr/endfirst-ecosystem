#!/bin/bash

# Script para reorganizar estrutura de demandas
# Cria estrutura hierárquica: DEMANDAS/ATIVAS/<demanda_id>/ e DEMANDAS/FINALIZADAS/<demanda_id>/

set -e

REPO_ROOT="/Users/joubertsouza/Documents/@endfirstmethod/endfirst-ecosystem"
cd "$REPO_ROOT"

echo "🔄 Iniciando reorganização de demandas..."

# Criar estrutura base
mkdir -p "DEMANDAS/ATIVAS"
mkdir -p "DEMANDAS/FINALIZADAS"

# Função para extrair ID da demanda do nome do arquivo
extract_demanda_id() {
    local filename="$1"
    # Extrai padrões como DEMANDA-METODO-010, DEMANDA-SOFT-005, etc.
    echo "$filename" | sed -E 's/.*(DEMANDA-[A-Z]+-[0-9]+).*/\1/' | head -1
}

# Função para verificar se demanda está finalizada
is_finalizada() {
    local file="$1"
    # Verifica se status é done, DONE, aprovado, etc.
    if grep -qiE "status:\s*(done|aprovado|finalizada)" "$file" 2>/dev/null; then
        return 0
    fi
    # Verifica se tem F-6 de conclusão
    if echo "$file" | grep -qi "F6.*CONCLUSAO\|F6.*CONCLUSAO"; then
        return 0
    fi
    return 1
}

# Processar arquivos de DEMANDAS_MANUS
echo "📦 Processando DEMANDAS_MANUS..."
for file in DEMANDAS_MANUS/*.md; do
    if [ ! -f "$file" ]; then
        continue
    fi
    
    filename=$(basename "$file")
    demanda_id=$(extract_demanda_id "$filename")
    
    if [ -z "$demanda_id" ] || [ "$demanda_id" = "$filename" ]; then
        # Não conseguiu extrair ID, usa nome base sem extensão
        demanda_id=$(basename "$file" .md | sed 's/^DEMANDA_//' | sed 's/-/_/g')
    fi
    
    # Determinar se é finalizada
    if is_finalizada "$file"; then
        target_dir="DEMANDAS/FINALIZADAS/$demanda_id"
    else
        target_dir="DEMANDAS/ATIVAS/$demanda_id"
    fi
    
    mkdir -p "$target_dir"
    cp "$file" "$target_dir/$filename"
    echo "  ✅ $filename → $target_dir/"
done

# Processar arquivos de DEMANDAS (se existir e tiver arquivos)
if [ -d "DEMANDAS" ] && [ "$(ls -A DEMANDAS/*.md 2>/dev/null | wc -l)" -gt 0 ]; then
    echo "📦 Processando DEMANDAS..."
    for file in DEMANDAS/*.md; do
        if [ ! -f "$file" ]; then
            continue
        fi
        
        filename=$(basename "$file")
        demanda_id=$(extract_demanda_id "$filename")
        
        if [ -z "$demanda_id" ] || [ "$demanda_id" = "$filename" ]; then
            demanda_id=$(basename "$file" .md)
        fi
        
        if is_finalizada "$file"; then
            target_dir="DEMANDAS/FINALIZADAS/$demanda_id"
        else
            target_dir="DEMANDAS/ATIVAS/$demanda_id"
        fi
        
        mkdir -p "$target_dir"
        cp "$file" "$target_dir/$filename"
        echo "  ✅ $filename → $target_dir/"
    done
fi

# Mover evidências para dentro das pastas de demanda
echo "📋 Organizando evidências..."
for evidencia in EVIDENCIAS/execucao_demanda_*.md EVIDENCIAS/execucao_*.md; do
    if [ ! -f "$evidencia" ]; then
        continue
    fi
    
    filename=$(basename "$evidencia")
    # Extrai ID da demanda do nome da evidência
    demanda_id=$(echo "$filename" | sed -E 's/execucao_(demanda_)?([a-z]+[-_])?([0-9]+).*/\2\3/' | sed 's/_/-/g' | sed 's/-$//')
    
    # Tenta padrões mais específicos
    if echo "$filename" | grep -q "metodo_"; then
        num=$(echo "$filename" | sed -E 's/.*metodo_([0-9]+).*/METODO-\1/')
        demanda_id="DEMANDA-$num"
    elif echo "$filename" | grep -q "soft_"; then
        num=$(echo "$filename" | sed -E 's/.*soft_([0-9]+).*/SOFT-\1/')
        demanda_id="DEMANDA-$num"
    elif echo "$filename" | grep -q "prod_"; then
        num=$(echo "$filename" | sed -E 's/.*prod_([0-9]+).*/PROD-\1/')
        demanda_id="DEMANDA-$num"
    elif echo "$filename" | grep -q "gov_"; then
        num=$(echo "$filename" | sed -E 's/.*gov_([0-9]+).*/GOV-\1/')
        demanda_id="DEMANDA-$num"
    fi
    
    # Procura pasta da demanda
    found_dir=""
    if [ -d "DEMANDAS/ATIVAS/$demanda_id" ]; then
        found_dir="DEMANDAS/ATIVAS/$demanda_id"
    elif [ -d "DEMANDAS/FINALIZADAS/$demanda_id" ]; then
        found_dir="DEMANDAS/FINALIZADAS/$demanda_id"
    else
        # Tenta encontrar por padrão parcial
        for dir in DEMANDAS/ATIVAS/* DEMANDAS/FINALIZADAS/*; do
            if [ -d "$dir" ] && echo "$dir" | grep -qi "$(echo "$demanda_id" | cut -d'-' -f2-3)"; then
                found_dir="$dir"
                break
            fi
        done
    fi
    
    if [ -n "$found_dir" ]; then
        mkdir -p "$found_dir/EVIDENCIAS"
        cp "$evidencia" "$found_dir/EVIDENCIAS/$filename"
        echo "  ✅ $filename → $found_dir/EVIDENCIAS/"
    else
        echo "  ⚠️  Não encontrou pasta para: $filename (demanda_id: $demanda_id)"
    fi
done

# Mover pacotes ZIP de demandas específicas
echo "📦 Organizando pacotes ZIP..."
for zip in EVIDENCIAS/pacote_demanda_*.zip; do
    if [ ! -f "$zip" ]; then
        continue
    fi
    
    filename=$(basename "$zip")
    demanda_id=$(echo "$filename" | sed -E 's/pacote_demanda_([a-z]+_)?([0-9]+).*/DEMANDA-\1\2/' | sed 's/_/-/g')
    
    # Ajusta formato
    if echo "$demanda_id" | grep -q "metodo"; then
        num=$(echo "$demanda_id" | sed 's/.*\([0-9]\+\).*/METODO-\1/')
        demanda_id="DEMANDA-$num"
    fi
    
    found_dir=""
    if [ -d "DEMANDAS/ATIVAS/$demanda_id" ]; then
        found_dir="DEMANDAS/ATIVAS/$demanda_id"
    elif [ -d "DEMANDAS/FINALIZADAS/$demanda_id" ]; then
        found_dir="DEMANDAS/FINALIZADAS/$demanda_id"
    fi
    
    if [ -n "$found_dir" ]; then
        mkdir -p "$found_dir/EVIDENCIAS"
        cp "$zip" "$found_dir/EVIDENCIAS/$filename"
        echo "  ✅ $filename → $found_dir/EVIDENCIAS/"
    fi
done

echo ""
echo "✅ Reorganização concluída!"
echo ""
echo "📊 Estrutura criada:"
echo "   DEMANDAS/ATIVAS/ - $(find DEMANDAS/ATIVAS -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ') demandas ativas"
echo "   DEMANDAS/FINALIZADAS/ - $(find DEMANDAS/FINALIZADAS -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ') demandas finalizadas"
echo ""
echo "⚠️  IMPORTANTE:"
echo "   1. Revisar estrutura criada"
echo "   2. Validar que todas as evidências foram movidas corretamente"
echo "   3. Após validação, remover DEMANDAS_MANUS/ (backup feito)"
echo "   4. Atualizar scripts e referências aos caminhos antigos"
