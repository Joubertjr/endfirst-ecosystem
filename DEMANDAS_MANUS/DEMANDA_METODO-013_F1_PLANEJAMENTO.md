# F-1 — PLANEJAMENTO CANÔNICO

**Demanda:** DEMANDA-METODO-013 — Governança de Software que implementa o Método  
**Versão:** 1.0  
**Data:** 23 de Janeiro de 2026  
**Método:** END-FIRST v2  
**Executor:** Manus  
**Chefe de Produto:** CEO (Joubert Jr)

---

## 🔒 END — ESTADO FINAL ESPERADO (EXATO)

> "Existe um contrato que define como um software pode implementar END-FIRST sem quebrar o método."

### Critérios de Aceitação (Binários)

**PASS:**
- ✅ Documento `/METODO/GOVERNANCA_SOFTWARE.md` criado
- ✅ Regras de consumo de `/METODO/` definidas:
  - Software consome `/METODO/`
  - Software não redefine regras
  - Software só executa demandas aprovadas
  - Software registra evidência
- ✅ Critérios de PASS/FAIL para software definidos
- ✅ Exemplo de software conforme fornecido

**FAIL:**
- ❌ Documento não existe
- ❌ Regras de consumo não estão definidas
- ❌ Critérios de PASS/FAIL não estão definidos
- ❌ Exemplo não está fornecido

---

## 📋 FASES DE EXECUÇÃO

### F1 — Definir Regras de Consumo de /METODO/

**END desta fase:**
> "As regras de consumo de `/METODO/` estão definidas com critérios binários de validação."

**Artefato:**
- Seção "Regras de Consumo de /METODO/" no documento `/METODO/GOVERNANCA_SOFTWARE.md`

**Critérios de PASS:**
- ✅ Regra 1: Software DEVE ler `/METODO/` do repositório
  - Path obrigatório: `/METODO/`
  - Software não pode ter cópia local desatualizada
  - Software deve validar integridade dos arquivos
- ✅ Regra 2: Software NÃO pode redefinir regras do método
  - Software não pode alterar END de demanda
  - Software não pode alterar critérios de PASS/FAIL
  - Software não pode pular fases do F-1
- ✅ Regra 3: Software DEVE consumir templates canônicos
  - Templates de demanda
  - Templates de F-1
  - Templates de artefatos
- ✅ Critérios de validação de consumo definidos
- ✅ Exemplos de consumo correto e incorreto

**Critérios de FAIL:**
- ❌ Regras não definidas
- ❌ Critérios de validação não definidos
- ❌ Exemplos não fornecidos

---

### F2 — Definir Regra de Execução Governada

**END desta fase:**
> "A regra de execução governada está definida: software só executa demandas aprovadas."

**Artefato:**
- Seção "Execução Governada" no documento

**Critérios de PASS:**
- ✅ Regra explícita: "Software só executa demandas com status 'approved'"
- ✅ Validação obrigatória antes de executar:
  - Demanda tem F-1 aprovado
  - F-1 tem status 'approved'
  - Demanda não está bloqueada
- ✅ Comportamento em caso de demanda não aprovada:
  - Software DEVE bloquear execução
  - Software DEVE registrar tentativa de execução não autorizada
  - Software DEVE notificar usuário
- ✅ Formato de aprovação definido:
  ```yaml
  status: approved
  approved_by: CEO
  approved_at: 2026-01-23T19:00:00Z
  ```
- ✅ Exemplos de validação fornecidos

**Critérios de FAIL:**
- ❌ Regra não explícita
- ❌ Validação não obrigatória
- ❌ Comportamento de bloqueio não definido
- ❌ Formato de aprovação não definido
- ❌ Exemplos não fornecidos

---

### F3 — Definir Obrigatoriedade de Evidência

**END desta fase:**
> "A obrigatoriedade de evidência está definida: software DEVE registrar evidência de execução."

**Artefato:**
- Seção "Evidência Obrigatória" no documento

**Critérios de PASS:**
- ✅ Regra explícita: "Software DEVE registrar evidência de execução"
- ✅ Formato de evidência definido:
  ```json
  {
    "execucao_id": "exec-2026-01-23-001",
    "demanda_id": "DEMANDA-METODO-013",
    "fase": "F1",
    "inicio": "2026-01-23T19:00:00Z",
    "fim": "2026-01-23T19:15:00Z",
    "status": "PASS",
    "artefatos_gerados": ["/METODO/GOVERNANCA_SOFTWARE.md"],
    "executor": "Manus",
    "metodo_version": "END-FIRST v2.5"
  }
  ```
- ✅ Campos obrigatórios de evidência definidos
- ✅ Local de armazenamento de evidência definido: `/EVIDENCIAS/<demanda_id>/<execucao_id>.json`
- ✅ Regra de imutabilidade: evidência não pode ser alterada após criação
- ✅ Critérios de validação de evidência definidos
- ✅ Exemplos de evidência válida e inválida

**Critérios de FAIL:**
- ❌ Regra não explícita
- ❌ Formato não definido
- ❌ Campos obrigatórios não listados
- ❌ Local de armazenamento não definido
- ❌ Imutabilidade não garantida
- ❌ Exemplos não fornecidos

---

### F4 — Definir Critérios de PASS/FAIL para Software

**END desta fase:**
> "Os critérios binários de PASS/FAIL para software que implementa o método estão definidos."

**Artefato:**
- Seção "Critérios de PASS/FAIL para Software" no documento

**Critérios de PASS:**
- ✅ Critérios de PASS listados:
  - ✅ Software consome `/METODO/` do repositório
  - ✅ Software não redefine regras do método
  - ✅ Software só executa demandas aprovadas
  - ✅ Software registra evidência de execução
  - ✅ Software valida integridade de arquivos
  - ✅ Software segue templates canônicos
- ✅ Critérios de FAIL listados:
  - ❌ Software não consome `/METODO/`
  - ❌ Software redefine regras
  - ❌ Software executa demanda não aprovada
  - ❌ Software não registra evidência
  - ❌ Software não valida integridade
  - ❌ Software não segue templates
- ✅ Critérios são binários (sem ambiguidade)
- ✅ Critérios são auditáveis (verificáveis por script)

**Critérios de FAIL:**
- ❌ Critérios de PASS não listados
- ❌ Critérios de FAIL não listados
- ❌ Critérios são ambíguos
- ❌ Critérios não são auditáveis

---

### F5 — Criar Exemplo de Software Conforme

**END desta fase:**
> "Um exemplo de software conforme está documentado com código e explicação."

**Artefato:**
- Seção "Exemplo de Software Conforme" no documento

**Critérios de PASS:**
- ✅ Exemplo de código fornecido (pseudocódigo ou Python)
- ✅ Exemplo mostra:
  - Leitura de `/METODO/`
  - Validação de demanda aprovada
  - Execução de fase
  - Registro de evidência
- ✅ Exemplo está comentado e explicado
- ✅ Exemplo segue todas as regras definidas
- ✅ Exemplo é executável (ou quase executável)

**Critérios de FAIL:**
- ❌ Exemplo não fornecido
- ❌ Exemplo não mostra todos os passos
- ❌ Exemplo não está comentado
- ❌ Exemplo não segue regras
- ❌ Exemplo não é executável

---

### F6 — Criar Documento Completo e Validar

**END desta fase:**
> "O documento `/METODO/GOVERNANCA_SOFTWARE.md` está completo, revisado, validado e commitado."

**Artefato:**
- `/METODO/GOVERNANCA_SOFTWARE.md` (completo)
- Commit no repositório

**Critérios de PASS:**
- ✅ Documento contém todas as seções (F1-F5)
- ✅ Documento está formatado corretamente
- ✅ Documento está revisado (sem placeholders, TODOs)
- ✅ Documento está commitado no repositório
- ✅ Commit message segue padrão
- ✅ Documento está no GitHub
- ✅ Demanda marcada como concluída

**Critérios de FAIL:**
- ❌ Documento incompleto
- ❌ Documento mal formatado
- ❌ Documento não revisado
- ❌ Documento não commitado
- ❌ Commit message fora do padrão
- ❌ Documento não está no GitHub
- ❌ Demanda não marcada como concluída

---

## 🚫 REGRAS CANÔNICAS

**Governança de Software:**
> "Software não redefine método. Software consome método. Software que redefine regras é FAIL estrutural."

**Consumo de Método:**
> "Software DEVE consumir `/METODO/` do repositório. Software que não consome método não implementa END-FIRST."

**Execução Governada:**
> "Software só executa demandas aprovadas. Software que executa demanda não aprovada é FAIL estrutural."

**Evidência Obrigatória:**
> "Software DEVE registrar evidência de execução. Software sem evidência não é auditável."

---

## 🧱 BLOQUEIOS ESTRUTURAIS

### Bloqueios Técnicos
- Nenhum

### Bloqueios de Método
- **Depende de:** DEMANDA-METODO-010 (Governança de Produtos)

### Bloqueios de Governança
- Nenhum

---

## ❌ FORA DE ESCOPO

- Criação de software específico (isso será feito em demandas de software)
- Implementação de software para gerenciar método
- Migração de software existente

---

## 📌 STATUS

**Status atual:** Aprovado  
**Próximo passo:** Executar F1

---

## 🧭 REGRA FINAL

> "Software que redefine método não implementa END-FIRST. Software que não consome método não é governado. Governança de software é condição de passagem para qualquer software no método END-FIRST."
