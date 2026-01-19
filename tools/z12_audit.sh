#!/usr/bin/env bash
#
# Z12-A — Auditoria de Método (Estrutural)
# Valida conformidade com Template Canônico, F-1, e ordem de gates
#
# Exit codes:
#   0 = PASS (todas as validações passaram)
#   1 = FAIL (pelo menos uma validação falhou)
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================="
echo "Z12-A — Auditoria de Método (Estrutural)"
echo "========================================="
echo ""

FAIL_COUNT=0

# ============================================
# CHECK 1: Template Canônico (11 seções)
# ============================================
echo "CHECK 1: Template Canônico (11 seções obrigatórias)"
echo "---------------------------------------------------"

TEMPLATE_FILE="$REPO_ROOT/METODO/TEMPLATE_DEMANDA_CANONICA.md"

if [ ! -f "$TEMPLATE_FILE" ]; then
    echo -e "${RED}✗ FAIL${NC}: Template Canônico não encontrado em $TEMPLATE_FILE"
    ((FAIL_COUNT++))
else
    echo -e "${GREEN}✓ PASS${NC}: Template Canônico existe"
    
    # Verifica se template menciona 11 seções
    if grep -q "11 seções" "$TEMPLATE_FILE"; then
        echo -e "${GREEN}✓ PASS${NC}: Template documenta 11 seções obrigatórias"
    else
        echo -e "${YELLOW}⚠ WARNING${NC}: Template não menciona explicitamente '11 seções'"
    fi
fi

echo ""

# ============================================
# CHECK 2: F-1 (Planejamento Canônico)
# ============================================
echo "CHECK 2: F-1 (Planejamento Canônico)"
echo "------------------------------------"

END_FIRST_V2="$REPO_ROOT/METODO/END_FIRST_V2.md"

if [ ! -f "$END_FIRST_V2" ]; then
    echo -e "${RED}✗ FAIL${NC}: END_FIRST_V2.md não encontrado"
    ((FAIL_COUNT++))
else
    echo -e "${GREEN}✓ PASS${NC}: END_FIRST_V2.md existe"
    
    # Verifica se F-1 está documentado
    if grep -q "F-1" "$END_FIRST_V2"; then
        echo -e "${GREEN}✓ PASS${NC}: F-1 (Planejamento Canônico) está documentado"
    else
        echo -e "${RED}✗ FAIL${NC}: F-1 não encontrado em END_FIRST_V2.md"
        ((FAIL_COUNT++))
    fi
fi

echo ""

# ============================================
# CHECK 3: Ordem Canônica dos Gates
# ============================================
echo "CHECK 3: Ordem Canônica dos Gates (Z0 → Z11 → Z12 → DONE)"
echo "----------------------------------------------------------"

CURSOR_INSTRUCTIONS="$REPO_ROOT/METODO/CURSOR_INSTRUCTIONS.md"

if [ ! -f "$CURSOR_INSTRUCTIONS" ]; then
    echo -e "${RED}✗ FAIL${NC}: CURSOR_INSTRUCTIONS.md não encontrado"
    ((FAIL_COUNT++))
else
    echo -e "${GREEN}✓ PASS${NC}: CURSOR_INSTRUCTIONS.md existe"
    
    # Verifica se ordem canônica está documentada
    if grep -q "Z0.*Z11.*Z12.*DONE" "$CURSOR_INSTRUCTIONS"; then
        echo -e "${GREEN}✓ PASS${NC}: Ordem canônica Z0 → Z11 → Z12 → DONE está documentada"
    else
        echo -e "${RED}✗ FAIL${NC}: Ordem canônica dos gates não encontrada em CURSOR_INSTRUCTIONS.md"
        ((FAIL_COUNT++))
    fi
    
    # Verifica se Z12 é declarado como último gate
    if grep -q "último gate antes de DONE" "$CURSOR_INSTRUCTIONS"; then
        echo -e "${GREEN}✓ PASS${NC}: Z12 declarado como último gate antes de DONE"
    else
        echo -e "${YELLOW}⚠ WARNING${NC}: Z12 não está explicitamente declarado como último gate"
    fi
fi

echo ""

# ============================================
# CHECK 4: Gate Z12 Documentado
# ============================================
echo "CHECK 4: Gate Z12 Documentado"
echo "------------------------------"

if [ ! -f "$END_FIRST_V2" ]; then
    echo -e "${RED}✗ FAIL${NC}: END_FIRST_V2.md não encontrado (já reportado)"
    ((FAIL_COUNT++))
else
    # Verifica se Gate Z12 está documentado
    if grep -q "Gate Z12" "$END_FIRST_V2"; then
        echo -e "${GREEN}✓ PASS${NC}: Gate Z12 está documentado em END_FIRST_V2.md"
    else
        echo -e "${RED}✗ FAIL${NC}: Gate Z12 não encontrado em END_FIRST_V2.md"
        ((FAIL_COUNT++))
    fi
    
    # Verifica se Z12-A, Z12-B, Z12-C estão documentados
    if grep -q "Z12-A\|Z12-B\|Z12-C" "$CURSOR_INSTRUCTIONS"; then
        echo -e "${GREEN}✓ PASS${NC}: Sub-gates Z12-A, Z12-B, Z12-C documentados"
    else
        echo -e "${RED}✗ FAIL${NC}: Sub-gates Z12-A, Z12-B, Z12-C não encontrados"
        ((FAIL_COUNT++))
    fi
fi

echo ""

# ============================================
# RESULTADO FINAL
# ============================================
echo "========================================="
echo "RESULTADO FINAL"
echo "========================================="

if [ $FAIL_COUNT -eq 0 ]; then
    echo -e "${GREEN}✓ PASS${NC}: Todas as validações de método passaram"
    echo ""
    exit 0
else
    echo -e "${RED}✗ FAIL${NC}: $FAIL_COUNT validação(ões) falharam"
    echo ""
    echo "Corrija os problemas acima antes de declarar DONE."
    exit 1
fi
