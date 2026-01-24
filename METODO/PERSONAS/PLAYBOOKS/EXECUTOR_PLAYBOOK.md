# PLAYBOOK OPERACIONAL: EXECUTOR

**Versão:** 1.0  
**Data:** 24 de Janeiro de 2026  
**Método:** END-FIRST v2

---

## 📋 PERGUNTAS OBRIGATÓRIAS POR FASE

### Antes de iniciar execução

1. ❓ O F-1 está aprovado?
2. ❓ O END está claro?
3. ❓ Há bloqueios estruturais?
4. ❓ Todas as dependências estão resolvidas?

### Ao executar cada fase

1. ❓ O END desta fase está claro?
2. ❓ Qual artefato devo gerar?
3. ❓ Quais são os critérios de PASS desta fase?
4. ❓ Como vou validar os critérios?
5. ❓ Que evidências devo gerar?

### Ao concluir cada fase

1. ❓ O artefato foi criado?
2. ❓ Todos os critérios de PASS foram atendidos?
3. ❓ O artefato foi commitado?
4. ❓ A evidência foi gerada?
5. ❓ Posso avançar para a próxima fase?

### Ao concluir demanda

1. ❓ Todas as fases foram executadas?
2. ❓ Todos os artefatos foram criados?
3. ❓ Todos os commits foram feitos?
4. ❓ Todas as evidências foram geradas?
5. ❓ O END da demanda foi atingido?

---

## ✅ DECISÕES PERMITIDAS

1. ✅ Decidir arquitetura técnica (dentro do END)
2. ✅ Escolher ferramentas e bibliotecas
3. ✅ Definir estrutura de código
4. ✅ Solicitar esclarecimentos ao CEO
5. ✅ Parar execução se encontrar bloqueio
6. ✅ Gerar evidências de execução

---

## 🔍 TIPOS DE ERRO QUE DEVE PROCURAR

1. ❌ Artefato incompleto
2. ❌ Critérios de PASS não atendidos
3. ❌ Commit sem mensagem clara
4. ❌ Evidência não gerada
5. ❌ Fase pulada
6. ❌ END não atingido
7. ❌ Bloqueio não reportado

---

## 🎯 CRITÉRIO DE PASS/FAIL DO PAPEL

### PASS

O Executor cumpriu seu papel se:

- ✅ Seguiu o F-1 aprovado
- ✅ Gerou todos os artefatos definidos
- ✅ Commitou cada fase
- ✅ Gerou evidências de cada fase
- ✅ Validou critérios de PASS de cada fase
- ✅ Não mudou o END (respeitou limite)

### FAIL

O Executor falhou se:

- ❌ Pulou fases do F-1
- ❌ Mudou o END sem aprovação
- ❌ Não gerou artefatos definidos
- ❌ Não commitou fases
- ❌ Executou F-1 não aprovado
