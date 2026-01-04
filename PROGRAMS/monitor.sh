#!/bin/bash
# Script de Monitoramento Contínuo - ENDFIRST V2.1
# Atualiza métricas e status do projeto automaticamente

set -e

PROJECT_ROOT="/home/ubuntu/projeto_usuario/@endfirst"
PROGRAMS_DIR="$PROJECT_ROOT/PROGRAMS"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔍 Monitoramento ENDFIRST V2.1${NC}"
echo -e "${BLUE}Timestamp: $TIMESTAMP${NC}"
echo ""

# 1. Contar itens no backlog
echo -e "${YELLOW}📋 Analisando Backlog...${NC}"
TOTAL_ITEMS=$(grep -c "^### ITEM-" "$PROGRAMS_DIR/BACKLOG.md" 2>/dev/null || echo "0")
echo "   Total de itens: $TOTAL_ITEMS"

# 2. Contar bloqueios
echo -e "${YELLOW}🔴 Verificando Bloqueios...${NC}"
BLOQUEIOS=$(grep -c "^| BLOCK-" "$PROGRAMS_DIR/STATUS_ATUAL.md" 2>/dev/null || echo "0")
echo "   Bloqueios ativos: $BLOQUEIOS"

# 3. Verificar RAG
echo -e "${YELLOW}🔍 Verificando RAG...${NC}"
cd "$PROJECT_ROOT/BANCO_REFERENCIAS"
if docker-compose ps | grep -q "Up"; then
    echo -e "   ${GREEN}✅ RAG está rodando${NC}"
    RAG_STATUS="🟢 ATIVO"
else
    echo -e "   ${RED}❌ RAG não está rodando${NC}"
    RAG_STATUS="🔴 INATIVO"
fi

# 4. Contar arquivos por tipo
echo -e "${YELLOW}📊 Contando Arquivos...${NC}"
MD_FILES=$(find "$PROJECT_ROOT/METODO" -name "*.md" 2>/dev/null | wc -l)
PY_FILES=$(find "$PROJECT_ROOT/BANCO_REFERENCIAS" -name "*.py" 2>/dev/null | wc -l)
echo "   Arquivos Markdown (METODO): $MD_FILES"
echo "   Arquivos Python (RAG): $PY_FILES"

# 5. Verificar pilares
echo -e "${YELLOW}🏛️ Verificando Pilares...${NC}"
PILARES=$(ls -1 "$PROJECT_ROOT/METODO/pilares/" 2>/dev/null | wc -l)
echo "   Pilares existentes: $PILARES/13"

# 6. Verificar material copiado
echo -e "${YELLOW}📁 Verificando Material...${NC}"
if [ -f "$PROJECT_ROOT/_TRANSCISAO/TRANSCRICAO_15_MODELOS_MENTAIS.md" ]; then
    echo -e "   ${GREEN}✅ Material 15 Modelos Mentais disponível${NC}"
else
    echo -e "   ${RED}❌ Material 15 Modelos Mentais não encontrado${NC}"
fi

if [ -d "$PROJECT_ROOT/_TRANSCISAO/ladeira" ]; then
    echo -e "   ${GREEN}✅ Material Ladeira disponível${NC}"
else
    echo -e "   ${RED}❌ Material Ladeira não encontrado${NC}"
fi

# 7. Gerar resumo
echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}📊 RESUMO DO MONITORAMENTO${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "   📋 Backlog: $TOTAL_ITEMS itens"
echo "   🔴 Bloqueios: $BLOQUEIOS ativos"
echo "   🏛️ Pilares: $PILARES/13"
echo "   🔍 RAG: $RAG_STATUS"
echo "   📝 Documentação: $MD_FILES arquivos"
echo "   🐍 Código Python: $PY_FILES arquivos"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# 8. Atualizar timestamp no STATUS_ATUAL.md
sed -i "s/Última Atualização:.*/Última Atualização: $TIMESTAMP/" "$PROGRAMS_DIR/STATUS_ATUAL.md" 2>/dev/null || true

echo ""
echo -e "${BLUE}✅ Monitoramento concluído!${NC}"
