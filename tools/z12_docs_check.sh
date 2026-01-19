#!/usr/bin/env bash
#
# Z12-B — Auditoria de Documentação (Qualidade)
# Valida Markdown válido, checklists renderizáveis, e ausência de artefatos técnicos
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

echo "============================================"
echo "Z12-B — Auditoria de Documentação (Qualidade)"
echo "============================================"
echo ""

FAIL_COUNT=0
WARNING_COUNT=0

# ============================================
# CHECK 1: Checklists Renderizáveis
# ============================================
echo "CHECK 1: Checklists Renderizáveis (sintaxe correta)"
echo "----------------------------------------------------"

# Busca por checkboxes com backticks (sintaxe errada)
BROKEN_CHECKBOXES=$(find "$REPO_ROOT" -name "*.md" -type f -exec grep -l '\`\[ \]\`\|\`\[x\]\`' {} \; 2>/dev/null || true)

if [ -z "$BROKEN_CHECKBOXES" ]; then
    echo -e "${GREEN}✓ PASS${NC}: Nenhum checkbox com backticks encontrado"
else
    echo -e "${RED}✗ FAIL${NC}: Checkboxes com backticks encontrados (quebram renderização):"
    echo "$BROKEN_CHECKBOXES" | while read -r file; do
        echo "  - $file"
        grep -n '\`\[ \]\`\|\`\[x\]\`' "$file" | head -3
    done
    ((FAIL_COUNT++))
fi

echo ""

# ============================================
# CHECK 2: Markdown Válido (básico)
# ============================================
echo "CHECK 2: Markdown Válido (verificações básicas)"
echo "------------------------------------------------"

# Busca por marcadores de conflito Git
CONFLICT_MARKERS=$(find "$REPO_ROOT" -name "*.md" -type f -exec grep -l '<<<<<<< \|======= \|>>>>>>> ' {} \; 2>/dev/null || true)

if [ -z "$CONFLICT_MARKERS" ]; then
    echo -e "${GREEN}✓ PASS${NC}: Nenhum marcador de conflito Git encontrado"
else
    echo -e "${RED}✗ FAIL${NC}: Marcadores de conflito Git encontrados:"
    echo "$CONFLICT_MARKERS" | while read -r file; do
        echo "  - $file"
    done
    ((FAIL_COUNT++))
fi

echo ""

# ============================================
# CHECK 3: Sem Vazamento de Artefatos Técnicos
# ============================================
echo "CHECK 3: Sem Vazamento de Artefatos Técnicos"
echo "---------------------------------------------"

# Busca por tokens/secrets expostos (padrões comuns)
SECRET_PATTERNS=(
    "ghp_[a-zA-Z0-9]{36}"  # GitHub Personal Access Token
    "github_pat_[a-zA-Z0-9_]{82}"  # GitHub Fine-grained PAT
    "sk-[a-zA-Z0-9]{48}"  # OpenAI API Key
)

SECRETS_FOUND=false

for pattern in "${SECRET_PATTERNS[@]}"; do
    FOUND=$(find "$REPO_ROOT" -name "*.md" -type f -exec grep -l -E "$pattern" {} \; 2>/dev/null || true)
    if [ -n "$FOUND" ]; then
        if [ "$SECRETS_FOUND" = false ]; then
            echo -e "${RED}✗ FAIL${NC}: Possíveis secrets/tokens encontrados:"
            SECRETS_FOUND=true
            ((FAIL_COUNT++))
        fi
        echo "$FOUND" | while read -r file; do
            echo "  - $file (padrão: $pattern)"
        done
    fi
done

if [ "$SECRETS_FOUND" = false ]; then
    echo -e "${GREEN}✓ PASS${NC}: Nenhum secret/token exposto encontrado"
fi

echo ""

# ============================================
# CHECK 4: Arquivos Markdown Renderizáveis
# ============================================
echo "CHECK 4: Arquivos Markdown Renderizáveis"
echo "-----------------------------------------"

# Busca por arquivos .md vazios ou corrompidos
EMPTY_OR_BROKEN=$(find "$REPO_ROOT" -name "*.md" -type f -size 0 2>/dev/null || true)

if [ -z "$EMPTY_OR_BROKEN" ]; then
    echo -e "${GREEN}✓ PASS${NC}: Nenhum arquivo Markdown vazio encontrado"
else
    echo -e "${YELLOW}⚠ WARNING${NC}: Arquivos Markdown vazios encontrados:"
    echo "$EMPTY_OR_BROKEN" | while read -r file; do
        echo "  - $file"
    done
    ((WARNING_COUNT++))
fi

echo ""

# ============================================
# CHECK 5: Sintaxe de Checklist Correta
# ============================================
echo "CHECK 5: Sintaxe de Checklist Correta (- [ ] ou - [x])"
echo "-------------------------------------------------------"

# Busca por checklists com sintaxe correta
CORRECT_CHECKLISTS=$(find "$REPO_ROOT/METODO" -name "*.md" -type f -exec grep -l '^- \[ \]\|^- \[x\]' {} \; 2>/dev/null || true)

if [ -n "$CORRECT_CHECKLISTS" ]; then
    echo -e "${GREEN}✓ PASS${NC}: Checklists com sintaxe correta encontrados:"
    echo "$CORRECT_CHECKLISTS" | while read -r file; do
        COUNT=$(grep -c '^- \[ \]\|^- \[x\]' "$file" || true)
        echo "  - $file ($COUNT itens)"
    done
else
    echo -e "${YELLOW}⚠ WARNING${NC}: Nenhum checklist encontrado em /METODO/"
fi

echo ""

# ============================================
# RESULTADO FINAL
# ============================================
echo "============================================"
echo "RESULTADO FINAL"
echo "============================================"

if [ $FAIL_COUNT -eq 0 ]; then
    echo -e "${GREEN}✓ PASS${NC}: Todas as validações de documentação passaram"
    if [ $WARNING_COUNT -gt 0 ]; then
        echo -e "${YELLOW}⚠${NC} $WARNING_COUNT warning(s) encontrado(s) (não bloqueante)"
    fi
    echo ""
    exit 0
else
    echo -e "${RED}✗ FAIL${NC}: $FAIL_COUNT validação(ões) falharam"
    if [ $WARNING_COUNT -gt 0 ]; then
        echo -e "${YELLOW}⚠${NC} $WARNING_COUNT warning(s) encontrado(s)"
    fi
    echo ""
    echo "Corrija os problemas acima antes de declarar DONE."
    exit 1
fi
