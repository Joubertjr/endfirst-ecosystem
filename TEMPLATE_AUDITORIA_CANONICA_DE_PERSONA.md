INSTRUÇÃO FORMAL — AUDITORIA CANÔNICA DE PERSONA (VERSÃO ROBUSTA)

Você DEVE auditar a pasta METODO/PERSONAS/ usando exclusivamente este template.
É proibido interpretar livremente, resumir, pular blocos ou corrigir arquivos.

Regras gerais:
	•	Trabalhar SOMENTE sobre a pasta METODO/PERSONAS/ (fonte auditada local; sem ZIP).
	•	Auditoria do ZERO: é proibido reaproveitar qualquer relatório, checksum, achado, evidência, ou saída de auditorias anteriores (incluindo `auditoria_canonica/`).
	•	Gerar SHA256 de TODOS os arquivos.
	•	Incluir cópia integral do pacote auditado.
	•	Tudo é PASS/FAIL binário.
	•	Qualquer BLOQUEIO ⇒ FAIL final.
	•	Não elogiar. Não explicar método. Apenas auditar.

⸻

CABECALHO (obrigatório)

Preencher:
	•	Data:
	•	Auditor:
	•	Método:
	•	Fonte (diretório local auditado): METODO/PERSONAS/
	•	Commit/Repo (se existir):

⸻

BLOCO 0 — PROVAS DE REPRODUÇÃO (BLOQUEANTE)

Registrar:
	•	Comando de captura/cópia da fonte auditada (para _ORIGINAL/)
	•	Árvore completa: tree -a
	•	Gerar 01_CHECKSUMS_VERIFICAVEIS.txt (SHA256 de todos os arquivos)
	•	Incluir cópia integral da fonte auditada em:
_ORIGINAL/

Resultado do bloco 0: PASS / FAIL

⸻

BLOCO 1 — ESTRUTURA (BINÁRIO)

Verificar presença obrigatória:
	•	DEFINICOES/
	•	PLAYBOOKS/
	•	REGRAS/
	•	GATES/
	•	CHECKLISTS/
	•	EVIDENCIAS_MODELO/
	•	README.md

Tabela:

Item obrigatório	Presente? (PASS/FAIL)	Evidência (caminho)


Resultado do bloco 1: PASS / FAIL

⸻

BLOCO 2 — INVENTÁRIO DE ARQUIVOS

Listar TODOS os arquivos com SHA256.

Para cada pasta:
	•	Existe pelo menos 1 arquivo válido? PASS/FAIL

Tabela obrigatória:

Pasta	Arquivos encontrados	PASS/FAIL


Resultado do bloco 2: PASS / FAIL

⸻

BLOCO 3 — CONTEÚDO POR ARQUIVO (LINHA A LINHA)

Para CADA arquivo individualmente:

Preencher tabela:

<caminho_do_arquivo>

Requisito obrigatório	PASS/FAIL	Evidência (linha/trecho)
Objetivo		
Autoridade		
Responsabilidades		
Limites		
Perguntas canônicas		
Critérios de PASS		
Decisões permitidas		
Decisões proibidas		
Rastreabilidade		
Versionamento		

Regra:
	•	Falta de qualquer item ⇒ FAIL do arquivo.

Resultado por arquivo: PASS / FAIL
Resultado do bloco 3: PASS / FAIL

⸻

BLOCO 4 — VARREDURA DE FALHAS

Registrar achados no formato obrigatório:

ACHADO-XXX
Severidade: BLOQUEIO | ALTA | MEDIA | BAIXA
Tag: PLACEHOLDER | AMBIGUIDADE | CONTRADICAO | NAO_BINARIO | SEM_RASTREABILIDADE | REFERENCIA_AUSENTE | INCONSISTENCIA_CRUZADA
Arquivo:linha
Trecho
Regra violada
Correção mínima

Categorias obrigatórias:
	•	Placeholders/TODO/TBD
	•	Ambiguidade (termo sem teste objetivo)
	•	Contradições
	•	Não-binariedade (não dá SIM/NÃO)
	•	Falta de rastreabilidade
	•	Referências ausentes
	•	Inconsistência cruzada

Se existir qualquer BLOQUEIO ⇒ FAIL.

Resultado do bloco 4: PASS / FAIL

⸻

BLOCO 5 — CONSISTÊNCIA CRUZADA

Validar:
	•	Playbook ↔ Gates
	•	Checklist ↔ Gates
	•	Definição ↔ Regras
	•	Termos críticos definidos (clareza, viabilidade, evidência, risco, etc.)
	•	Templates citados existem fisicamente

Tabela:

Cruzamento	PASS/FAIL	Evidência


Resultado do bloco 5: PASS / FAIL

⸻

BLOCO 6 — VEREDITO FINAL

FAIL se:
	•	Bloco 0, 1, 2, 3 ou 5 = FAIL
OU
	•	Existir qualquer ACHADO com severidade BLOQUEIO

Reportar:
	•	Quantidade de BLOQUEIOS:
	•	Quantidade de ALTAS:
	•	Quantidade de MÉDIAS:
	•	Quantidade de BAIXAS:

Status final: PASS / FAIL

⸻

BLOCO 7 — TEMPLATEABILIDADE

Responder apenas:

Pode virar template para outras personas? SIM / NÃO

Se NÃO:
Listar condições faltantes objetivas:
	•	(lista)

⸻

BLOCO 8 — AÇÕES

Listar somente ações objetivas, sem explicação:
	1.	
	2.	
	3.	

⸻

ENTREGÁVEIS OBRIGATÓRIOS

Gerar exatamente estes arquivos:
	•	00_MANIFESTO.md
	•	01_CHECKSUMS_VERIFICAVEIS.txt
	•	02_ESTRUTURA_COMPLETA.txt
	•	03_RELATORIO_EXECUTIVO.md
	•	04_ANALISE_DETALHADA_POR_ARQUIVO.md
	•	05_FALHAS_IDENTIFICADAS.md
	•	06_CONSISTENCIA_CRUZADA.md
	•	07_RECOMENDACOES_ACAO.md
	•	_ORIGINAL/ (cópia integral da fonte auditada)

⸻

PROIBIDO
	•	Interpretar
	•	Resumir
	•	Corrigir arquivos
	•	Reaproveitar qualquer conteúdo/artefato de auditorias anteriores (incluindo `auditoria_canonica/`)
	•	Explicar método
	•	Suavizar falhas
	•	Ignorar bloco

⸻

PERMITIDO APENAS

AUDITAR → CLASSIFICAR → BLOQUEAR OU APROVAR.
