# F-1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-METODO-010 — Governança de Produtos dentro do Método  
**Versão:** 1.0  
**Data:** 23 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Executor:** Manus

---

## 🔒 END — ESTADO FINAL ESPERADO (EXATO)

> "Existe um contrato formal que define como produtos são criados, versionados e governados dentro do repositório endfirst-ecosystem, em `/PRODUTOS/<nome>/`."

### Critérios de Aceitação (Binários)

**PASS:**
- ✅ Documento `/METODO/GOVERNANCA_PRODUTOS.md` criado
- ✅ Estrutura mínima de produto definida:
  ```
  /PRODUTOS/<produto>/
    README.md
    DEMANDAS/
    planejamento/
    EVIDENCIAS/
    CONTEXTO/
    OUTPUTS/
  ```
- ✅ Regra explícita: "produto não nasce fora do método"
- ✅ Critérios de PASS/FAIL para criação de produto definidos
- ✅ Versionamento de produto definido

**FAIL:**
- ❌ Documento não existe
- ❌ Estrutura de produto não está definida
- ❌ Regra de governança não está explícita
- ❌ Critérios de PASS/FAIL não estão definidos

---

## 📋 FASES DE EXECUÇÃO

### F1 — Definir Estrutura Canônica de Produto

**END desta fase:**
> "A estrutura canônica de produto está definida com todas as pastas obrigatórias e seus propósitos."

**Artefato:**
- Seção "Estrutura Canônica de Produto" no documento

**Critérios de PASS:**
- ✅ Estrutura de pastas definida
- ✅ Propósito de cada pasta documentado
- ✅ Arquivos obrigatórios listados

---

### F2 — Definir Regras de Governança

**END desta fase:**
> "As regras de governança de produtos estão explícitas e inequívocas."

**Artefato:**
- Seção "Regras de Governança" no documento

**Critérios de PASS:**
- ✅ Regra "produto vive dentro do método" explícita
- ✅ Regras de criação de produto definidas
- ✅ Regras de versionamento definidas

---

### F3 — Definir Critérios de PASS/FAIL

**END desta fase:**
> "Os critérios binários de PASS/FAIL para criação de produto estão definidos."

**Artefato:**
- Seção "Critérios de PASS/FAIL" no documento

**Critérios de PASS:**
- ✅ Critérios de PASS listados
- ✅ Critérios de FAIL listados
- ✅ Critérios são binários (sem ambiguidade)

---

### F4 — Definir Versionamento de Produto

**END desta fase:**
> "O sistema de versionamento de produto está definido e documentado."

**Artefato:**
- Seção "Versionamento de Produto" no documento

**Critérios de PASS:**
- ✅ Formato de versionamento definido (ex: v1.0, v1.1, v2.0)
- ✅ Regras de incremento de versão definidas
- ✅ Relação entre versão de produto e versão de método definida

---

### F5 — Criar Documento Completo

**END desta fase:**
> "O documento `/METODO/GOVERNANCA_PRODUTOS.md` está completo, revisado e pronto para commit."

**Artefato:**
- `/METODO/GOVERNANCA_PRODUTOS.md` (completo)

**Critérios de PASS:**
- ✅ Documento contém todas as seções (F1-F4)
- ✅ Documento está formatado corretamente
- ✅ Documento está revisado
- ✅ Documento está pronto para commit

---

### F6 — Validar e Commitar

**END desta fase:**
> "O documento está commitado no repositório e a demanda está concluída."

**Artefato:**
- Commit no repositório

**Critérios de PASS:**
- ✅ Documento commitado
- ✅ Commit message segue padrão
- ✅ Documento está no GitHub
- ✅ Demanda marcada como concluída

---

## 🚫 REGRAS CANÔNICAS

**Governança de Produtos:**
> "Produto não nasce fora do método. Produto sem governança é software sem rastreabilidade."

**Estrutura Obrigatória:**
> "Todo produto DEVE seguir a estrutura canônica. Produto fora da estrutura é FAIL estrutural."

---

## 🧱 BLOQUEIOS ESTRUTURAIS

### Bloqueios Técnicos
- Nenhum

### Bloqueios de Método
- Nenhum

### Bloqueios de Governança
- Nenhum

---

## ❌ FORA DE ESCOPO

- Criação de produtos específicos (isso será feito em demandas de produto)
- Implementação de software para gerenciar produtos
- Migração de produtos existentes

---

## 📌 STATUS

**Status atual:** Aprovado  
**Próximo passo:** Executar F1

---

## 🧭 REGRA FINAL

> "Produto sem governança é software sem rastreabilidade. Governança de produtos é condição de passagem para qualquer produto no método END-FIRST."
