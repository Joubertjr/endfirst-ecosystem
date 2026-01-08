---
document_id: PROMPT_CURSOR
type: operational
owner: Manus (Agent)
status: approved
approved_by: CEO
approved_at: 2026-01-07
governed_by: /METODO/PILAR_ENDFIRST.md
version: 1.0
created_at: 2026-01-07
---

# PROMPT PARA CURSOR (Modo Plan)

**Versão:** 1.0  
**Data:** 7 de Janeiro de 2026  
**Objetivo:** Implementar Núcleo Operacional ENDFIRST no repositório

---

## 🎯 OBJETIVO (RESULTADO ESPERADO)

Implementar o Núcleo Operacional do Pilar ENDFIRST no repositório como **"fonte única de verdade"**.

**No final, deve ser impossível criar demanda/issue sem uma ENDFIRST_SPEC validada.**

---

## 📦 ARTEFATOS DE ENTRADA (já prontos no ZIP)

- `PILAR_ENDFIRST.md` (fonte soberana de verdade)
- `templates/ENDFIRST_SPEC.md` (template oficial)
- `examples/ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md` (exemplo real)
- `processos/ENDFIRST_PROCESS.md` (processo humano de 30 segundos)
- `README.md` (documentação de entrada)

---

## 📤 RESULTADO DE SAÍDA (o que deve existir no repo)

### Estrutura obrigatória:

```
/METODO/
├── PILAR_ENDFIRST.md              # Texto soberano
├── README.md                       # Documentação de entrada
├── templates/
│   └── ENDFIRST_SPEC.md           # Template oficial
├── examples/
│   └── ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md  # Exemplo real
├── processos/
│   └── ENDFIRST_PROCESS.md        # Processo humano
└── ontologia/
    └── (vazio — criar só quando necessário)
```

### Documentos obrigatórios:

1. **`/METODO/PILAR_ENDFIRST.md`** — Texto soberano
2. **`/METODO/templates/ENDFIRST_SPEC.md`** — Template oficial
3. **`/METODO/examples/ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md`** — Exemplo preenchido real
4. **`/METODO/README.md`** — Documentação de entrada (como iniciar uma demanda)
5. **`/METODO/processos/ENDFIRST_PROCESS.md`** — Processo humano de 30 segundos

---

## 🔒 REGRAS (BLOQUEIOS PRÁTICOS)

### R1 — Um único path canônico por documento
**Proibido:**
- Criar duplicatas (ex: `PILAR_ENDFIRST.md` e `PILAR_ENDFIRST_CANONICO.md`)
- Criar "versões alternativas" do Pilar

**Obrigatório:**
- Cada conceito tem um único path canônico
- Referências internas usam paths exatos

---

### R2 — Referências internas devem bater com arquivos reais
**Proibido:**
- Referenciar `PILAR_ENDFIRST.md` quando o arquivo é `PILAR_ENDFIRST_CANONICO.md`
- Usar paths relativos ambíguos

**Obrigatório:**
- Todas as referências devem apontar para paths canônicos exatos
- Exemplo: `/METODO/PILAR_ENDFIRST.md` (não `PILAR_ENDFIRST.md`)

---

### R3 — Não criar automação ainda
**Proibido:**
- Criar CLI antes do núcleo estar estável
- Criar GitHub Actions antes de adoção humana
- Criar schema JSON antes de validação manual funcionar

**Obrigatório:**
- Foco em documentos e processo humano primeiro
- Automação só depois de adoção real

---

### R4 — Template deve cobrir explicitamente B1–B11
**Proibido:**
- Checklist de validação incompleto
- Bloqueios não mapeados para seções

**Obrigatório:**
- Cada bloqueio (B1-B11) deve ter seção correspondente no template
- Checklist deve listar todos os 11 bloqueios

---

### R5 — Exemplo deve ser real (não fictício)
**Proibido:**
- Exemplo genérico tipo "Sistema de Gestão de Projetos"
- Exemplo sem entrada bruta real

**Obrigatório:**
- Usar caso real: "LLM Orchestrator" (ideia do CEO)
- Entrada bruta capturada exatamente como foi dita

---

## ✅ VALIDAÇÃO (Definition of Done)

### V1 — Links internos funcionam
- [ ] Todas as referências a arquivos apontam para paths corretos
- [ ] Não existem links quebrados
- [ ] Paths canônicos estão consistentes

### V2 — Template cobre B1–B11
- [ ] Cada bloqueio tem seção correspondente
- [ ] Checklist lista todos os 11 bloqueios
- [ ] Modo v0 vs v1 está explícito

### V3 — Exemplo real preenchido
- [ ] Usa caso "LLM Orchestrator"
- [ ] Entrada bruta está capturada
- [ ] Perguntas 1-2 respondidas
- [ ] Status: PASS (Modo v0)

### V4 — README aponta para documentos canônicos
- [ ] README explica "como iniciar uma demanda"
- [ ] README lista os 2 documentos canônicos (Pilar + Template)
- [ ] README explica processo de 30 segundos

### V5 — Estrutura de diretórios correta
- [ ] `/METODO/` existe
- [ ] `/METODO/templates/` existe
- [ ] `/METODO/examples/` existe
- [ ] `/METODO/processos/` existe
- [ ] `/METODO/ontologia/` existe (vazio)

---

## 📋 TAREFA (Passo a Passo)

### Passo 1: Criar estrutura /METODO/
```bash
mkdir -p /METODO/templates
mkdir -p /METODO/examples
mkdir -p /METODO/processos
mkdir -p /METODO/ontologia
```

### Passo 2: Mover/renomear arquivos conforme padrão
- `PILAR_ENDFIRST_CANONICO.md` → `/METODO/PILAR_ENDFIRST.md`
- `ENDFIRST_SPEC_TEMPLATE.md` → `/METODO/templates/ENDFIRST_SPEC.md`
- `ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md` → `/METODO/examples/ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md`
- `ENDFIRST_PROCESS.md` → `/METODO/processos/ENDFIRST_PROCESS.md`
- `README.md` → `/METODO/README.md`

### Passo 3: Revisar textos para remover inconsistências
- Buscar todas as referências a `PILAR_ENDFIRST.md` e garantir que apontam para `/METODO/PILAR_ENDFIRST.md`
- Buscar todas as referências a `ENDFIRST_SPEC.md` e garantir que apontam para `/METODO/templates/ENDFIRST_SPEC.md`
- Garantir que não existem referências a arquivos antigos (ex: `PILAR_ENDFIRST_CANONICO.md`)

### Passo 4: Validar exemplo preenchido
- Verificar que `ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md` está completo
- Verificar que entrada bruta está capturada
- Verificar que Perguntas 1-2 estão respondidas
- Verificar que checklist mínimo está marcado

### Passo 5: Criar README
- Explicar estrutura de arquivos
- Explicar como iniciar uma demanda (4 passos)
- Listar documentos canônicos
- Adicionar proteções anti-paralisia

### Passo 6: Abrir PR com checklist de validação
- Título: "feat: Núcleo operacional ENDFIRST v1.0"
- Descrição: Listar os 5 documentos criados
- Checklist: V1-V5 (links, template, exemplo, README, estrutura)

---

## 🚫 O QUE NÃO FAZER

### ❌ Não criar CLI ainda
Foco em documentos e processo humano primeiro.

### ❌ Não criar GitHub Actions ainda
Automação só depois de adoção humana.

### ❌ Não criar schema JSON ainda
Validação manual primeiro.

### ❌ Não criar ontologia ainda
Só criar quando B7 bloquear repetidamente.

### ❌ Não "melhorar" os textos
Manter fidelidade aos documentos originais.

### ❌ Não criar documentos adicionais
Só os 5 obrigatórios (Pilar, Template, Exemplo, Processo, README).

---

## 📊 MÉTRICAS DE SUCESSO

### M1 — Tempo de implementação
**Objetivo:** < 30 minutos da extração do ZIP até PR aberto.

### M2 — Taxa de validação
**Objetivo:** 100% dos itens do checklist V1-V5 passam na primeira tentativa.

### M3 — Adoção imediata
**Objetivo:** Primeira demanda real criada usando o template em < 24h após merge.

---

## 🎯 REGRA MÃE (Para Colar no Topo do Repo)

```markdown
# REGRA ENDFIRST

"Antes de discutir solução, precisamos escrever a ENDFIRST_SPEC v0.  
Se não existe spec, a demanda não existe."

📖 Documentação: `/METODO/README.md`  
📝 Template: `/METODO/templates/ENDFIRST_SPEC.md`  
🎯 Exemplo: `/METODO/examples/ENDFIRST_SPEC_EF-2026-001_LLM_ORCHESTRATOR.md`
```

---

## 📜 DECLARAÇÃO FINAL

Este prompt é o **contrato de resultado** entre CEO e Cursor.

Se algo não está claro, consulte `/METODO/PILAR_ENDFIRST.md` (fonte soberana).

Se o Pilar não responde, a resposta ainda não existe oficialmente.

---

**Versão:** 1.0  
**Data:** 7 de Janeiro de 2026  
**Path Canônico:** `/METODO/PROMPT_CURSOR.md`  
**Governado por:** `/METODO/PILAR_ENDFIRST.md`
