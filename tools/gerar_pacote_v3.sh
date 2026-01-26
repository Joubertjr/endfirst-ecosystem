#!/bin/bash

# Script para gerar PACOTE_EXECUCAO_COMPLETA_END_FIRST_v3.zip
# com MANIFEST.json consistente

set -e

REPO_ROOT="/Users/joubertsouza/Documents/@endfirstmethod/endfirst-ecosystem"
cd "$REPO_ROOT"

ZIP_NAME="PACOTE_EXECUCAO_COMPLETA_END_FIRST_v3.zip"
TEMP_DIR=$(mktemp -d)

echo "Gerando pacote ZIP v3..."

# Limpar ZIP anterior se existir
rm -f "$ZIP_NAME"
rm -f "$REPO_ROOT/MANIFEST.json"

# Criar estrutura no diretório temporário
mkdir -p "$TEMP_DIR/DEMANDAS_MANUS"
mkdir -p "$TEMP_DIR/METODO"
mkdir -p "$TEMP_DIR/EVIDENCIAS"
mkdir -p "$TEMP_DIR/PROD"
mkdir -p "$TEMP_DIR/GOV"
mkdir -p "$TEMP_DIR/PRODUTOS"
mkdir -p "$TEMP_DIR/tools"

# Copiar arquivos
echo "Copiando DEMANDAS_MANUS..."
cp -r DEMANDAS_MANUS/*.md "$TEMP_DIR/DEMANDAS_MANUS/" 2>/dev/null || true

echo "Copiando METODO..."
cp -r METODO/*.md "$TEMP_DIR/METODO/" 2>/dev/null || true
if [ -d "METODO/PERSONAS" ]; then
    cp -r METODO/PERSONAS "$TEMP_DIR/METODO/" 2>/dev/null || true
fi

echo "Copiando EVIDENCIAS..."
cp -r EVIDENCIAS/*.md "$TEMP_DIR/EVIDENCIAS/" 2>/dev/null || true

echo "Copiando PROD..."
if [ -d "PROD" ]; then
    cp -r PROD/*.md "$TEMP_DIR/PROD/" 2>/dev/null || true
fi

echo "Copiando GOV..."
if [ -d "GOV" ]; then
    cp -r GOV/*.md "$TEMP_DIR/GOV/" 2>/dev/null || true
fi

echo "Copiando PRODUTOS..."
if [ -d "PRODUTOS" ]; then
    cp -r PRODUTOS "$TEMP_DIR/" 2>/dev/null || true
fi

# Copiar arquivos raiz
echo "Copiando arquivos raiz..."
cp README.md "$TEMP_DIR/" 2>/dev/null || true
cp COMMITS.md "$TEMP_DIR/" 2>/dev/null || true
cp Makefile "$TEMP_DIR/" 2>/dev/null || true

# Copiar relatórios se existirem
if [ -f "RELATORIO_FINAL_EXECUCAO.md" ]; then
    cp RELATORIO_FINAL_EXECUCAO.md "$TEMP_DIR/"
fi
if [ -f "RELATORIO_VALIDACAO_FINAL.md" ]; then
    cp RELATORIO_VALIDACAO_FINAL.md "$TEMP_DIR/"
fi

# Criar ZIP primeiro
echo "Criando ZIP..."
cd "$TEMP_DIR"
zip -r "$REPO_ROOT/$ZIP_NAME" . > /dev/null

# Agora gerar MANIFEST.json calculando hashes do ZIP
echo "Gerando MANIFEST.json..."

cd "$REPO_ROOT"
COMMIT_FINAL=$(git rev-parse HEAD)
COMMIT_SHORT=$(git rev-parse --short HEAD)

python3 <<PYTHON_SCRIPT
import json
import hashlib
import zipfile
from datetime import datetime

manifest = {
    "pacote_version": "v3",
    "commit_final": "$COMMIT_FINAL",
    "commit_short": "$COMMIT_SHORT",
    "data_geracao": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "executor": "Manus (Agent)",
    "metodo_version": "END-FIRST v2.5",
    "arquivos": {}
}

# Calcular SHA256 de cada arquivo no ZIP
with zipfile.ZipFile("$REPO_ROOT/$ZIP_NAME", "r") as z:
    file_list = sorted([f.filename for f in z.infolist() if not f.filename.endswith('/')])
    for filename in file_list:
        content = z.read(filename)
        sha256 = hashlib.sha256(content).hexdigest()
        manifest["arquivos"][filename] = sha256

# Salvar MANIFEST.json
with open("$REPO_ROOT/MANIFEST.json", "w") as f:
    json.dump(manifest, f, indent=2)

print(f"✅ MANIFEST.json gerado com {len(manifest['arquivos'])} arquivos")
PYTHON_SCRIPT

# Limpar diretório temporário
rm -rf "$TEMP_DIR"

echo "✅ Pacote ZIP v3 gerado: $ZIP_NAME"
echo "✅ MANIFEST.json gerado: MANIFEST.json"
echo "✅ Commit final: $COMMIT_FINAL"
