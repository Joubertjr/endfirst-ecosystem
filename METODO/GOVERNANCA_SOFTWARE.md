---
document_id: GOVERNANCA_SOFTWARE
type: canonical
owner: CEO (Joubert Jr)
status: approved
approved_by: CEO
approved_at: 2026-01-24
governed_by: /METODO/END_FIRST_V2.md
version: 1.0
created_at: 2026-01-24
demanda_origem: DEMANDA-METODO-013
---

# GOVERNANÇA DE SOFTWARE — END-FIRST v2.5

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Status:** Canônico (Aprovado)  
**Demanda de Origem:** DEMANDA-METODO-013  
**Path Canônico:** `/METODO/GOVERNANCA_SOFTWARE.md`

---

## 🎯 O QUE É GOVERNANÇA DE SOFTWARE

A **Governança de Software** é o contrato formal que define como um software pode implementar o método END-FIRST sem quebrar o método.

**Princípio fundamental:**
> "Software não redefine método. Software consome método. Software que redefine regras é FAIL estrutural."

---

## 🔒 REGRA ABSOLUTA

**Todo software que implementa END-FIRST DEVE seguir este contrato.**

**Software fora do contrato é FAIL estrutural.**

---

## 📋 REGRAS DE CONSUMO DE /METODO/

### Regra 1: Software DEVE Ler `/METODO/` do Repositório

**Path obrigatório:** `/METODO/`

**Critérios de PASS:**
- ✅ Software lê arquivos de `/METODO/` diretamente do repositório
- ✅ Software não mantém cópia local desatualizada de `/METODO/`
- ✅ Software valida integridade dos arquivos lidos (checksum, hash)
- ✅ Software sincroniza `/METODO/` antes de executar demandas

**Critérios de FAIL:**
- ❌ Software não lê `/METODO/` do repositório
- ❌ Software mantém cópia local desatualizada
- ❌ Software não valida integridade
- ❌ Software não sincroniza antes de executar

**Exemplo de consumo correto:**
```python
# Software lê /METODO/ diretamente do repositório
import git
repo = git.Repo('endfirst-ecosystem')
metodo_path = repo.working_dir + '/METODO/'
template = read_file(metodo_path + 'TEMPLATE_DEMANDA_CANONICA.md')
```

**Exemplo de consumo incorreto:**
```python
# ❌ Software mantém cópia local desatualizada
template = read_file('/local/cache/TEMPLATE_DEMANDA_CANONICA.md')
```

---

### Regra 2: Software NÃO Pode Redefinir Regras do Método

**Critérios de PASS:**
- ✅ Software não altera END de demanda
- ✅ Software não altera critérios de PASS/FAIL
- ✅ Software não pula fases do F-1
- ✅ Software não redefine templates canônicos
- ✅ Software não altera regras canônicas

**Critérios de FAIL:**
- ❌ Software altera END de demanda
- ❌ Software altera critérios de PASS/FAIL
- ❌ Software pula fases do F-1
- ❌ Software redefine templates
- ❌ Software altera regras canônicas

**Exemplo de violação:**
```python
# ❌ Software altera END de demanda
demanda['END'] = "Resultado modificado pelo software"  # FAIL
```

**Exemplo de conformidade:**
```python
# ✅ Software lê END sem modificar
end = demanda['END']  # PASS
```

---

### Regra 3: Software DEVE Consumir Templates Canônicos

**Templates obrigatórios:**
- Template de demanda: `/METODO/TEMPLATE_DEMANDA_CANONICA.md`
- Template de F-1: `/METODO/END_FIRST_V2.md` (seção F-1)
- Template de artefatos: Conforme definido em cada demanda

**Critérios de PASS:**
- ✅ Software lê templates canônicos do repositório
- ✅ Software valida demanda contra template canônico
- ✅ Software valida F-1 contra template canônico
- ✅ Software não cria templates alternativos

**Critérios de FAIL:**
- ❌ Software não lê templates canônicos
- ❌ Software não valida contra templates
- ❌ Software cria templates alternativos

**Exemplo de validação:**
```python
# ✅ Software valida demanda contra template
template = read_template('/METODO/TEMPLATE_DEMANDA_CANONICA.md')
demanda = read_demanda('DEMANDA-XXX.md')
if not validate_against_template(demanda, template):
    raise ValidationError("Demanda não segue template canônico")
```

---

### Critérios de Validação de Consumo

**Checklist de validação:**
- [ ] Software lê `/METODO/` do repositório
- [ ] Software valida integridade dos arquivos
- [ ] Software não redefine regras do método
- [ ] Software consome templates canônicos
- [ ] Software valida demandas contra templates

**Se qualquer item falhar → Software não está conforme.**

---

## 🔒 EXECUÇÃO GOVERNADA

### Regra Explícita

> "Software só executa demandas aprovadas. Software que executa demanda não aprovada é FAIL estrutural."

### Validação Obrigatória Antes de Executar

**Checklist de validação:**
- [ ] Demanda tem F-1 aprovado
- [ ] F-1 tem status `approved`
- [ ] F-1 tem `approved_by: CEO`
- [ ] F-1 tem `approved_at` (data de aprovação)
- [ ] Demanda não está bloqueada

**Formato de aprovação:**
```yaml
status: approved
approved_by: CEO
approved_at: 2026-01-23T19:00:00Z
```

### Comportamento em Caso de Demanda Não Aprovada

**Software DEVE:**
1. Bloquear execução imediatamente
2. Registrar tentativa de execução não autorizada
3. Notificar usuário com mensagem clara:
   > "Esta demanda requer F-1 (Planejamento Canônico). Sem F-1 aprovada, não posso executar."

**Exemplo de bloqueio:**
```python
# ✅ Software bloqueia execução se F-1 não está aprovado
f1 = read_f1('DEMANDA-XXX_F1_PLANEJAMENTO.md')
if f1['status'] != 'approved':
    log_unauthorized_attempt(demanda_id, f1['status'])
    raise ExecutionBlockedError("F-1 não está aprovado")
```

---

## 📝 EVIDÊNCIA OBRIGATÓRIA

### Regra Explícita

> "Software DEVE registrar evidência de execução. Software sem evidência não é auditável."

### Formato de Evidência

```json
{
  "execucao_id": "exec-2026-01-24-001",
  "demanda_id": "DEMANDA-METODO-013",
  "fase": "F1",
  "inicio": "2026-01-24T10:00:00Z",
  "fim": "2026-01-24T10:15:00Z",
  "status": "PASS",
  "artefatos_gerados": ["/METODO/GOVERNANCA_SOFTWARE.md"],
  "executor": "Manus",
  "metodo_version": "END-FIRST v2.5",
  "commit_hash": "abc123def456"
}
```

### Campos Obrigatórios

- `execucao_id`: ID único da execução
- `demanda_id`: ID da demanda executada
- `fase`: Fase executada (F1, F2, ..., F6)
- `inicio`: Timestamp de início (ISO 8601)
- `fim`: Timestamp de fim (ISO 8601)
- `status`: Status da execução (PASS ou FAIL)
- `artefatos_gerados`: Lista de artefatos gerados
- `executor`: Nome do executor (Manus, Cursor, etc.)
- `metodo_version`: Versão do método usado
- `commit_hash`: Hash do commit (se aplicável)

### Local de Armazenamento

**Path obrigatório:** `/EVIDENCIAS/<demanda_id>/<execucao_id>.json`

**Exemplo:**
```
/EVIDENCIAS/DEMANDA-METODO-013/exec-2026-01-24-001.json
```

### Regra de Imutabilidade

**Evidência não pode ser alterada após criação.**

**Critérios de PASS:**
- ✅ Evidência é criada uma vez
- ✅ Evidência não é modificada após criação
- ✅ Evidência é versionada no Git

**Critérios de FAIL:**
- ❌ Evidência é modificada após criação
- ❌ Evidência não é versionada

### Critérios de Validação de Evidência

**Checklist de validação:**
- [ ] Todos os campos obrigatórios presentes
- [ ] Timestamps válidos (ISO 8601)
- [ ] Status é PASS ou FAIL
- [ ] Artefatos gerados existem no repositório
- [ ] Evidência não foi modificada após criação

---

## ✅ CRITÉRIOS DE PASS/FAIL PARA SOFTWARE

### Critérios de PASS

Software está conforme se **TODOS** os critérios abaixo são verdadeiros:

- ✅ Software consome `/METODO/` do repositório
- ✅ Software não redefine regras do método
- ✅ Software só executa demandas aprovadas
- ✅ Software registra evidência de execução
- ✅ Software valida integridade de arquivos
- ✅ Software segue templates canônicos

### Critérios de FAIL

Software está **NÃO conforme** se **QUALQUER** critério abaixo é verdadeiro:

- ❌ Software não consome `/METODO/`
- ❌ Software redefine regras
- ❌ Software executa demanda não aprovada
- ❌ Software não registra evidência
- ❌ Software não valida integridade
- ❌ Software não segue templates

### Critérios são Binários

**Sem ambiguidade:** Software está conforme OU não está conforme.

**Sem "meio-termo":** Não existe "parcialmente conforme".

### Critérios são Auditáveis

**Verificáveis por script:**
- Validação de consumo de `/METODO/`
- Validação de aprovação de F-1
- Validação de evidência
- Validação de templates

---

## 💻 EXEMPLO DE SOFTWARE CONFORME

### Pseudocódigo

```python
# Exemplo de software conforme END-FIRST v2.5

class EndFirstExecutor:
    def __init__(self, repo_path):
        self.repo = git.Repo(repo_path)
        self.metodo_path = repo_path + '/METODO/'
        self.evidencias_path = repo_path + '/EVIDENCIAS/'
    
    def validate_demanda(self, demanda_id):
        """Valida demanda contra template canônico"""
        # 1. Ler template canônico do repositório
        template = self.read_file(self.metodo_path + 'TEMPLATE_DEMANDA_CANONICA.md')
        
        # 2. Ler demanda
        demanda = self.read_file(f'DEMANDAS_MANUS/{demanda_id}.md')
        
        # 3. Validar contra template
        if not self.validate_against_template(demanda, template):
            raise ValidationError("Demanda não segue template canônico")
        
        return True
    
    def validate_f1_approved(self, demanda_id):
        """Valida se F-1 está aprovado"""
        # 1. Ler F-1
        f1 = self.read_file(f'DEMANDAS_MANUS/{demanda_id}_F1_PLANEJAMENTO.md')
        
        # 2. Validar aprovação
        if f1['status'] != 'approved':
            raise ExecutionBlockedError("F-1 não está aprovado")
        
        if f1['approved_by'] != 'CEO':
            raise ExecutionBlockedError("F-1 não foi aprovado pelo CEO")
        
        return True
    
    def execute_phase(self, demanda_id, phase):
        """Executa fase de demanda"""
        # 1. Validar demanda
        self.validate_demanda(demanda_id)
        
        # 2. Validar F-1 aprovado
        self.validate_f1_approved(demanda_id)
        
        # 3. Ler F-1 para obter plano
        f1 = self.read_file(f'DEMANDAS_MANUS/{demanda_id}_F1_PLANEJAMENTO.md')
        phase_plan = f1['phases'][phase]
        
        # 4. Executar fase conforme plano
        inicio = datetime.now()
        artefatos = self.execute_phase_plan(phase_plan)
        fim = datetime.now()
        
        # 5. Registrar evidência
        evidencia = {
            "execucao_id": f"exec-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}",
            "demanda_id": demanda_id,
            "fase": phase,
            "inicio": inicio.isoformat(),
            "fim": fim.isoformat(),
            "status": "PASS",
            "artefatos_gerados": artefatos,
            "executor": "Manus",
            "metodo_version": "END-FIRST v2.5",
            "commit_hash": self.repo.head.commit.hexsha
        }
        
        self.save_evidencia(demanda_id, evidencia)
        
        return evidencia
    
    def read_file(self, path):
        """Lê arquivo do repositório"""
        # Valida integridade (checksum)
        file_content = self.repo.git.show(f'HEAD:{path}')
        return parse_file(file_content)
    
    def save_evidencia(self, demanda_id, evidencia):
        """Salva evidência no repositório"""
        evidencia_dir = f'{self.evidencias_path}/{demanda_id}/'
        os.makedirs(evidencia_dir, exist_ok=True)
        
        evidencia_file = f'{evidencia_dir}/{evidencia["execucao_id"]}.json'
        with open(evidencia_file, 'w') as f:
            json.dump(evidencia, f, indent=2)
        
        # Commit evidência
        self.repo.index.add([evidencia_file])
        self.repo.index.commit(f"feat({demanda_id}): evidência {evidencia['fase']}")
```

### Explicação do Exemplo

**1. Leitura de `/METODO/`:**
- Software lê templates e regras diretamente do repositório
- Valida integridade dos arquivos

**2. Validação de Demanda Aprovada:**
- Software valida se F-1 está aprovado
- Software bloqueia execução se não aprovado

**3. Execução de Fase:**
- Software executa conforme plano do F-1
- Software não altera END ou critérios

**4. Registro de Evidência:**
- Software registra evidência completa
- Evidência é imutável e versionada

---

## 🔗 REFERÊNCIAS CRUZADAS

- `/METODO/GOVERNANCA_PRODUTOS.md` — Versionamento de produtos
- `/METODO/PILAR_ENDFIRST.md` — Princípios fundacionais
- `/METODO/END_FIRST_V2.md` — Método END-FIRST v2
- `/METODO/TEMPLATE_DEMANDA_CANONICA.md` — Template canônico de demanda

---

## 📜 DECLARAÇÃO FINAL

**Este documento define o contrato formal para software que implementa END-FIRST.**

**Software que não segue este contrato não implementa END-FIRST.**

---

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Criado por:** Manus (Agent)  
**Aprovado por:** CEO (Joubert Jr)  
**Status:** Canônico (Aprovado)
