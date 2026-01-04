# Metodologia de Pesquisa e Contribuição

**Versão:** 1.0  
**Data:** 24 de novembro de 2025

---

## 1. Filosofia

Este repositório opera sob uma filosofia de **completude radical e rastreabilidade total**. O objetivo não é apenas apresentar uma síntese, mas preservar todo o processo de pesquisa, análise e descoberta. Cada peça de informação deve ser atômica, conectada e rastreável até sua fonte original.

## 2. Estrutura de Diretórios

A estrutura de diretórios é a espinha dorsal do sistema. Cada pasta tem um propósito específico:

- **`00-META/`**: Governança do repositório (metodologia, rastreabilidade, gaps).
- **`01-FRANKL-CORE/`**: Conhecimento atômico sobre Viktor Frankl.
- **`02-AUTORES-RELACIONADOS/`**: Perfis de autores que fazem a ponte entre Frankl e IA.
- **`03-IA-AGENTES/`**: Conceitos de IA relevantes para a pesquisa.
- **`04-INTERSECOES/`**: O coração da pesquisa, onde os conceitos se encontram.
- **`05-FONTES/`**: Arquivos brutos de fontes primárias (artigos, livros, perfis).
- **`06-SINTESES/`**: Produtos finais da pesquisa (análises, mapas, materiais pedagógicos).

## 3. Sistema de IDs Únicos

Todo o conteúdo é rastreado por um sistema de IDs únicos para evitar ambiguidade.

| Prefixo | Descrição | Exemplo |
| :--- | :--- | :--- |
| `FK-C` | Conceito de Frankl | `FK-C-001: Vontade de Sentido` |
| `FK-O` | Obra de Frankl | `FK-O-001: Em Busca de Sentido` |
| `AR-E` | Autor Relacionado (Existencialista) | `AR-E-001: Sartre` |
| `AR-IA` | Autor Relacionado (Pesquisador de IA) | `AR-IA-001: Quynh Nguyen` |
| `IA-C` | Conceito de IA | `IA-C-001: Agentes Autônomos` |
| `INT` | Interseção | `INT-001: Sentido em Agentes` |
| `SRC` | Fonte | `SRC-001: Nguyen et al. (2022)` |
| `SYN` | Síntese | `SYN-001: Análise de Nguyen et al.` |

## 4. Workflow de Entrada de Novos Conteúdos

Siga este processo de 6 passos para adicionar novos conteúdos ao repositório:

### Passo 1: Captura (Adicionar Fonte)

1.  **Encontrou uma nova fonte?** (artigo, livro, post de blog)
2.  **Salve o arquivo bruto** (PDF, Markdown, etc.) na pasta `05-FONTES/` apropriada (ex: `academicas/`).
3.  **Crie um ID de fonte:** `SRC-XXX`.
4.  **Renomeie o arquivo** com o ID: `SRC-005_Autor_Ano_Titulo.pdf`.

### Passo 2: Extração (Criar Notas Atômicas)

1.  **Leia a fonte** e identifique conceitos-chave (de Frankl, de IA, ou novos autores).
2.  **Para cada conceito**, crie um novo arquivo `.md` na pasta apropriada (ex: `01-FRANKL-CORE/conceitos/`).
3.  **Use o template de arquivo** (ver `_TEMPLATE.md`) para estruturar a nota.
4.  **Atribua um ID único** ao novo conceito (ex: `FK-C-005`).

### Passo 3: Linkagem (Conectar o Conhecimento)

1.  **No arquivo do conceito**, preencha o frontmatter YAML:
    - `id`: O ID que você acabou de criar.
    - `relacionado_com`: Adicione os IDs de outros conceitos relacionados.
    - `fontes`: Adicione o ID da fonte (`SRC-XXX`).
2.  **Use links no estilo Obsidian** (`[[ID]]`) no corpo do texto para conectar ideias.

### Passo 4: Mapeamento (Atualizar Rastreabilidade)

1.  **Abra o arquivo `00-META/_RASTREABILIDADE.md`**.
2.  **Adicione a nova cadeia conceitual** que você descobriu. Exemplo:
    `FK-C-005 → INT-008 → IA-C-012 → SRC-005`
3.  **Atualize a tabela de status de cobertura** com o novo conceito e o status da pesquisa.

### Passo 5: Identificação de Gaps

1.  **Durante a pesquisa, você encontrou uma conexão que *deveria* existir, mas não encontrou fontes?**
2.  **Abra o arquivo `00-META/_GAPS.md`**.
3.  **Adicione uma nova entrada** descrevendo a lacuna, as buscas que você já fez e as palavras-chave que usou.

### Passo 6: Síntese (Criar Conhecimento Original)

1.  **Depois de analisar várias fontes**, você está pronto para criar uma síntese original (uma análise, um mapa conceitual, um plano de aula).
2.  **Crie um novo arquivo** na pasta `06-SINTESES/` apropriada.
3.  **Atribua um ID de síntese** (`SYN-XXX`).
4.  **Use o template de síntese** para estruturar seu trabalho, referenciando os IDs dos conceitos e fontes que você usou.

## 5. Template de Arquivo

Consulte o arquivo **`00-META/_TEMPLATE.md`** para o template completo a ser usado em todas as novas notas.

## 6. Mitigação de Fragmentação

Para evitar que o conteúdo se torne excessivamente fragmentado, esta metodologia inclui um passo crucial:

- **Síntese Periódica:** A cada 5-10 notas atômicas criadas, é obrigatório criar uma **nota de síntese** (`SYN-XXX`) que conecte essas ideias em um argumento coeso. Isso garante que o conhecimento não apenas se expanda, mas também se aprofunde.
- **Índices de Diretório:** Cada diretório principal contém um arquivo `_INDEX.md` que resume o conteúdo daquela seção, funcionando como um "mapa local".

Ao seguir esta metodologia, garantimos que o repositório cresça de forma estruturada, rastreável e, o mais importante, **significativa**.
