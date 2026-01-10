# Evidências de Execução - DEMANDA-001

Este diretório contém evidências técnicas e visuais da execução dos critérios de aceitação da DEMANDA-001.

## Estrutura

```
EVIDENCIAS/
├── README.md                    # Este arquivo
├── CRITERIO_01.md              # Evidências do Critério 1 (Envio simultâneo)
├── screenshots/                 # Screenshots e GIFs (criar quando necessário)
│   ├── criterio_01_1llm.png
│   ├── criterio_01_2llms.png
│   └── criterio_01_3llms.png
└── [outros critérios...]
```

## Critérios Documentados

- [x] **Critério 1** - Envio simultâneo para 1-3 LLMs → `CRITERIO_01.md`
- [ ] **Critério 2** - Respostas lado a lado (pendente - Incremento 4)
- [ ] **Critério 3** - Seleção de melhor resposta (pendente)
- [ ] **Critério 4** - Validação cruzada automática (pendente)
- [ ] **Critério 5** - Ordem baseada na LLM inicial (pendente)
- [ ] **Critério 6** - Contexto preservado (pendente)
- [ ] **Critério 7** - Sistema roda localmente no macOS (pendente - validação final)

## Como Adicionar Evidências

Para cada critério:

1. Criar arquivo `CRITERIO_XX.md` com:
   - Checklist executado
   - Evidências técnicas (código, commits)
   - Evidências visuais (screenshots/gifs)

2. Adicionar screenshots em `screenshots/`:
   - Nomear: `criterio_XX_descricao.png` ou `.gif`
   - Referenciar no arquivo do critério

3. Documentar decisões técnicas temporárias quando aplicável

4. Commitar no Git junto com o código que implementa o critério

---

**Objetivo:** Provar objetivamente que cada critério foi atendido, não apenas "implementado"  
**Regra:** Sem evidência no Git = não passou

