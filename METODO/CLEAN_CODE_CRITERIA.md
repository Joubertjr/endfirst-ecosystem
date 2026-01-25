---
document_id: CLEAN_CODE_CRITERIA
type: governance
governed_by: /METODO/END_FIRST_V2.md
version: 1.0
created_at: 2026-01-24
created_by: Manus (Agent)
approved_by: pending
status: active
---

# CRITÉRIOS OBJETIVOS DE CLEAN CODE — END-FIRST v2.5

**Versão:** 1.0  
**Data de Criação:** 24 de Janeiro de 2026  
**Criado por:** Manus (Agent)  
**Status:** Ativo  
**Tipo:** Governança de Método  

---

## 🎯 OBJETIVO DESTE DOCUMENTO

Definir **critérios objetivos, binários e verificáveis** de Clean Code que funcionam como **bloqueio estrutural** no método END-FIRST v2.5.

**Não é:**
- ❌ Opinião sobre "código limpo"
- ❌ Recomendação de boas práticas
- ❌ Guia de estilo de código

**É:**
- ✅ Critérios binários (PASS/FAIL)
- ✅ Verificáveis objetivamente
- ✅ Bloqueantes de PASS de fase

---

## 🔒 REGRA CANÔNICA

> **"Nenhuma fase pode ser declarada PASS se código violar critérios objetivos de Clean Code."**

---

## 📏 CRITÉRIOS OBJETIVOS

### C1: Tamanho de Função

**Critério:** Função com mais de 20 linhas = FAIL

**Justificativa:** Função longa indica múltiplas responsabilidades ou lógica complexa não decomposta.

**Como verificar:**
```bash
# Contar linhas de função
wc -l <arquivo> | awk '{if ($1 > 20) print "FAIL"; else print "PASS"}'
```

**Exemplo PASS:**
```javascript
function calcularTotal(itens) {
  return itens.reduce((acc, item) => acc + item.preco, 0);
}
```

**Exemplo FAIL:**
```javascript
function processarPedido(pedido) {
  // 25+ linhas de lógica misturada
  // validação + cálculo + persistência + notificação
  // = FAIL (múltiplas responsabilidades)
}
```

---

### C2: Responsabilidade Única

**Critério:** Função com mais de 1 responsabilidade = FAIL

**Justificativa:** Função deve fazer uma coisa e fazer bem (Single Responsibility Principle).

**Como verificar:**
- Função faz validação E cálculo? FAIL
- Função faz persistência E notificação? FAIL
- Função faz transformação E apresentação? FAIL

**Exemplo PASS:**
```javascript
// Responsabilidade: validar pedido
function validarPedido(pedido) {
  if (!pedido.itens || pedido.itens.length === 0) {
    throw new Error("Pedido vazio");
  }
  return true;
}

// Responsabilidade: calcular total
function calcularTotal(pedido) {
  return pedido.itens.reduce((acc, item) => acc + item.preco, 0);
}
```

**Exemplo FAIL:**
```javascript
// Responsabilidades: validar + calcular + persistir + notificar
function processarPedido(pedido) {
  // validação
  if (!pedido.itens) throw new Error("Pedido inválido");
  
  // cálculo
  const total = pedido.itens.reduce((acc, item) => acc + item.preco, 0);
  
  // persistência
  db.save(pedido);
  
  // notificação
  email.send(pedido.cliente, "Pedido processado");
  
  return total;
}
// FAIL: 4 responsabilidades em 1 função
```

---

### C3: Complexidade Ciclomática

**Critério:** Complexidade ciclomática > 10 = FAIL

**Justificativa:** Alta complexidade indica lógica difícil de testar e manter.

**Como verificar:**
- Contar caminhos independentes no código
- Ferramenta: `eslint-plugin-complexity` (se disponível)
- Manual: contar `if`, `for`, `while`, `case`, `&&`, `||`

**Exemplo PASS:**
```javascript
function classificarIdade(idade) {
  if (idade < 18) return "Menor";
  if (idade < 60) return "Adulto";
  return "Idoso";
}
// Complexidade: 3 (PASS)
```

**Exemplo FAIL:**
```javascript
function processarStatus(pedido) {
  if (pedido.status === "pendente") {
    if (pedido.pagamento === "aprovado") {
      if (pedido.estoque === "disponível") {
        if (pedido.entrega === "agendada") {
          // ... mais 10 níveis de if aninhados
        }
      }
    }
  }
  // ... mais lógica condicional
}
// Complexidade: 15+ (FAIL)
```

---

### C4: Nomenclatura Descritiva

**Critério:** Nome de variável/função com menos de 3 caracteres (exceto `i`, `j`, `k` em loops) = FAIL

**Justificativa:** Nomes curtos não expressam intenção.

**Como verificar:**
- Variável `x`, `y`, `z`, `a`, `b` = FAIL
- Função `fn`, `do`, `go` = FAIL
- Loop `for (let i = 0; ...)` = PASS (convenção aceita)

**Exemplo PASS:**
```javascript
const totalPedido = calcularTotal(itens);
const clienteAtivo = verificarStatusCliente(cliente);
```

**Exemplo FAIL:**
```javascript
const x = calc(y);
const a = chk(b);
// FAIL: nomes não descritivos
```

---

### C5: Profundidade de Aninhamento

**Critério:** Aninhamento de blocos > 3 níveis = FAIL

**Justificativa:** Aninhamento profundo indica lógica complexa não decomposta.

**Como verificar:**
- Contar níveis de `{` aninhados
- Máximo: 3 níveis

**Exemplo PASS:**
```javascript
function processarPedido(pedido) {
  if (!pedido) return;
  
  if (pedido.status === "pendente") {
    if (pedido.pagamento === "aprovado") {
      aprovarPedido(pedido);
    }
  }
}
// Aninhamento: 3 níveis (PASS)
```

**Exemplo FAIL:**
```javascript
function processarPedido(pedido) {
  if (pedido) {
    if (pedido.status === "pendente") {
      if (pedido.pagamento === "aprovado") {
        if (pedido.estoque === "disponível") {
          if (pedido.entrega === "agendada") {
            // FAIL: 5 níveis de aninhamento
          }
        }
      }
    }
  }
}
```

---

## 🔍 COMO APLICAR ESSES CRITÉRIOS

### Durante F-1 (Planejamento)

- Definir quais critérios se aplicam à demanda
- Documentar no F-1 quais critérios serão validados

### Durante Execução (F2-F5)

- Código deve nascer respeitando critérios
- TDD garante que testes vêm primeiro
- Refatoração garante que critérios são atendidos

### Durante F-6 (Declaração PASS)

- Validar que todos os critérios foram atendidos
- Se qualquer critério falhar = FAIL da fase
- Corrigir e revalidar antes de declarar PASS

---

## 🚫 O QUE NÃO É COBERTO

Esses critérios **não cobrem:**
- ❌ Estilo de código (tabs vs spaces, ponto-e-vírgula, etc.)
- ❌ Formatação (Prettier, etc.)
- ❌ Linting (ESLint, etc.)
- ❌ Frameworks específicos

**Por quê?**
- Estilo é subjetivo e configurável
- Formatação é automatizável
- Linting é específico de linguagem
- Critérios de Clean Code são universais

---

## 📊 RESUMO DOS CRITÉRIOS

| Critério | Limite | PASS | FAIL |
|----------|--------|------|------|
| C1: Tamanho de função | ≤ 20 linhas | ✅ | ❌ |
| C2: Responsabilidade única | 1 responsabilidade | ✅ | ❌ |
| C3: Complexidade ciclomática | ≤ 10 | ✅ | ❌ |
| C4: Nomenclatura descritiva | ≥ 3 caracteres | ✅ | ❌ |
| C5: Profundidade de aninhamento | ≤ 3 níveis | ✅ | ❌ |

---

## 🔐 GOVERNANÇA

**Documento governado por:** `/METODO/END_FIRST_V2.md`  
**Criado por:** DEMANDA-METODO-007 v1.0  
**Versão:** 1.0  
**Status:** Ativo  
**Data de Criação:** 24 de Janeiro de 2026  

---

## 📜 REFERÊNCIAS

- `/DEMANDAS_MANUS/DEMANDA_METODO-007_TDD_CLEAN_CODE_BLOQUEIO_ESTRUTURAL.md`
- `/DEMANDAS_MANUS/DEMANDA_METODO-007_F1_PLANEJAMENTO.md`
- Clean Code (Robert C. Martin) — Princípios adaptados para critérios objetivos

---
