# 🗺️ Pilar 0.5: Mapa de Conhecimento (NOVO v10.8)

**Versão:** 1.0  
**Data:** 21 de Dezembro de 2025

---

## 🎯 O Que é o Mapa de Conhecimento?

O **Mapa de Conhecimento** é um novo sub-pilar obrigatório, posicionado entre o Pilar 0 (Estado Final) e o Pilar 1 (Obstáculos). Ele consiste em um documento que serve como o **"escopo do conhecimento"** do projeto, listando **TODO o conhecimento que precisa ser gerado e capturado** durante a execução.

---

## ❓ Por Que Ele é Necessário?

Esta melhoria foi criada para corrigir a **Causa Raiz #5 (Ausência de um Mapa de Conhecimento)**, identificada na análise forense. Sem um mapa, é impossível saber se o pacote final está completo. Ele serve como uma **referência central** para validar a completude da entrega.

---

## 🚀 Como Aplicar

Logo após definir o Estado Final (Pilar 0), crie um documento chamado `00.5_MAPA_CONHECIMENTO.md` e use o template abaixo para listar todos os "artefatos de conhecimento" que você espera criar.

### **Template do Mapa de Conhecimento**

```markdown
# 🗺️ Mapa de Conhecimento: [Nome do Projeto]

## 1. Documentos do Método a Serem Criados

- [ ] 00.0_ESTADO_FINAL.md
- [ ] 00.5_MAPA_CONHECIMENTO.md (este documento)
- [ ] 01_OBSTACULOS.md
- [ ] 02_RECURSOS.md
- [ ] 03_CALIBRACAO.md
- [ ] 03.5_ANALISE_RISCOS.md
- [ ] 04_CAMINHO_REVERSO.md
- [ ] 04.5_ROADMAP.md
- [ ] 05_VALIDACAO_EXTERNA.md
- [ ] 06_EXECUCAO.md
- [ ] 07_APRENDIZADOS.md

## 2. Referências e Fundamentos a Serem Capturados

- [ ] Links de artigos e pesquisas
- [ ] Documentação de tecnologias
- [ ] Livros e frameworks que inspiraram o projeto

## 3. Decisões a Serem Documentadas (ADRs)

- [ ] Decisão de arquitetura principal
- [ ] Escolha do stack tecnológico
- [ ] Decisões de trade-off importantes

## 4. Aprendizados a Serem Registrados

- [ ] O que funcionou bem?
- [ ] O que não funcionou?
- [ ] O que pode ser melhorado no método?

## 5. Artefatos do Projeto a Serem Criados

- [ ] Especificações técnicas
- [ ] Código-fonte
- [ ] Guias de usuário
- [ ] Materiais de marketing
```

---

## 💡 Exemplo Prático: Projeto @google_Store

| ID | Conhecimento a Ser Gerado | Pilar | Formato | Status |
|---|---|---|---|---|
| 1 | Estado Final do @google_Store | Pilar 0 | Documento MD | ✅ Concluído |
| 2 | Obstáculos para o @google_Store | Pilar 1 | Documento MD | ✅ Concluído |
| 3 | Recursos para o @google_Store | Pilar 2 | Documento MD | ✅ Concluído |
| 4 | Calibração do @google_Store | Pilar 3 | Documento MD | ✅ Concluído |
| 5 | Análise de Riscos do @google_Store | Pilar 3.5 | Documento MD | ✅ Concluído |
| 6 | Caminho Reverso do @google_Store | Pilar 4 | Documento MD | ✅ Concluído |
| 7 | Roadmap do @google_Store | Pilar 4.5 | Documento MD | ✅ Concluído |
| 8 | Validação Externa do @google_Store | Pilar 5 | Documento MD | ✅ Concluído |
| 9 | Execução do @google_Store | Pilar 6 | Documento MD | ✅ Concluído |
| 10 | Aprendizados do @google_Store | Pilar 7 | Documento MD | ✅ Concluído |
| 11 | Requisitos do @google_Store | Pilar 2 | Documento MD | ✅ Concluído |
| 12 | Modelo de Dados do @google_Store | Pilar 2 | Documento MD | ✅ Concluído |
| 13 | Custos do @google_Store | Pilar 2 | Documento MD | ✅ Concluído |
| 14 | Testes do @google_Store | Pilar 2 | Documento MD | ✅ Concluído |

---

## ✅ Checkpoints de Validação

- [ ] O Mapa de Conhecimento lista TODOS os documentos a serem criados?
- [ ] Ele está alinhado com o Estado Final (Pilar 0)?
- [ ] Ele foi validado por um terceiro (Pilar 5)?

---

## 🏁 Definition of Done (DoD)

"O Pilar 0.5 está pronto quando: (1) O Mapa de Conhecimento está completo, (2) Ele lista todos os documentos a serem criados, (3) Ele está alinhado com o Estado Final."

---

## 🏆 Critérios de Qualidade

- **Completude:** O mapa cobre 100% do conhecimento a ser gerado?
- **Clareza:** Os nomes dos documentos são claros e autoexplicativos?
- **Consistência:** O mapa está consistente com os outros pilares?

---

## ✅ Checklist de Qualidade

- [ ] O Mapa de Conhecimento foi criado logo após o Pilar 0?
- [ ] Ele lista todos os tipos de conhecimento a serem gerados (teórico, prático, técnico, histórico, contextual)?
- [ ] Ele será usado como base para o "Definition of Done" (Pilar 6) e para o "Inventário de Conhecimento" (Pilar 7)?

---

## 🔗 Relação com Outros Pilares

- **Pilar 0 (Estado Final):** O Mapa de Conhecimento é o primeiro passo para transformar o "Estado Final" em realidade, definindo o que precisa ser conhecido.
- **Pilar 6 (Execução):** O Mapa serve como base para criar o **Definition of Done (DoD)**.
- **Pilar 7 (Aprendizagem):** O Mapa serve como base para o **Inventário de Conhecimento**, garantindo que tudo que foi planejado foi capturado.

---

**Este pilar é a "rede de segurança" que garante que nenhum conhecimento valioso seja perdido no caminho.** 🚀
