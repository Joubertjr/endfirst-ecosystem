# O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos _ por Civil Learning _ Coding Nexus _ Nov, 2025 _ Medium

**Arquivo original:** `O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos _ por Civil Learning _ Coding Nexus _ Nov, 2025 _ Medium.pdf`

**Total de páginas:** 13

---

# Página 1

Coding Nexus · Seguindo
História exclusiva para membros
O Google acaba de tornar o RAG ridiculamente
fácil com a nova ferramenta de busca de
arquivos.
3 minutos de leitura · 9 de novembro de 2025
Aprendizado Cívico
Seguindo
Ouvir
Compartilhar
Mais
Se você já tentou construir sua própria configuração RAG, provavelmente entende o
desafio: gerenciar embeddings, bancos de dados vetoriais, dividir o texto em partes
(short-frames) corretamente e garantir que tudo interaja com seu modelo sem
gastar uma fortuna.
Bom, o Google acabou de fazer toda essa confusão desaparecer.
Eles introduziram discretamente uma nova ferramenta de busca de arquivos dentro da
API Gemini, que cuida de todo o trabalho pesado do RAG para você . Você adiciona seus
arquivos, faz sua pergunta e ela descobre o resto.
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
1/13



---

# Página 2

Imagem por — Google
O que é isso?
Em sua essência, a Busca de Arquivos permite que o Gemini "entenda" seus dados.
Você pode enviar PDFs, arquivos DOCX, textos, JSON ou até mesmo arquivos de
código. Quando você faz uma pergunta ao Gemini, ele não apenas tenta adivinhar —
ele examina os arquivos enviados, encontra as partes relevantes e as utiliza para
responder.
É como conectar seu cérebro pessoal diretamente ao Gemini. Sem banco de dados
vetorial separado, sem pipeline de recuperação, nada para gerenciar.
Simplesmente entram os arquivos e saem as respostas.
É barato. Tipo, muito barato mesmo.
Essa é a parte que me surpreendeu. Você não paga por consultas ou
armazenamento; você paga apenas uma vez — quando indexa seus arquivos.
A criação de um componente incorporado custa US$ 0,15 por 1 milhão de tokens ,
usando esse gemini-embedding-001 modelo. Isso é insignificante comparado à criação
de seu próprio pipeline com ferramentas como Pinecone ou Weaviate.
Depois disso, você poderá consultar esses arquivos livremente, quantas vezes quiser.
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
2/13



---

# Página 3

Como funciona na prática
A Busca de Arquivos simplifica o RAG ao dividir arquivos automaticamente em
partes, gerar incorporações, armazená-las e recuperá-las, além de inserir contexto
em seus prompts do Gemini.
Tudo é gerenciado dentro da mesma generateContent chamada de API que você já
utiliza.
Ao fazer uma consulta, o sistema realiza uma busca vetorial nos bastidores usando
o modelo Gemini Embedding mais recente. Dessa forma, ele entende o significado ,
e não apenas as palavras-chave.
Melhor ainda: as respostas do Gemini incluem citações — ele indica explicitamente
de qual arquivo e seção a fonte foi retirada. Você pode clicar e verificar. Chega de
ficar adivinhando se o seu modelo teve uma alucinação.
Caso de uso: Geração de jogos extremamente rápida do Beam
Um dos primeiros testadores, o Phaser Studio , está usando a Busca de Arquivos em
sua plataforma de jogos com inteligência artificial, o Beam.
Eles possuem uma biblioteca com mais de 3.000 arquivos — incluindo modelos,
trechos de código, documentos de design e outros dados internos. A Busca de
Arquivos permite que eles consultem tudo isso em menos de 2 segundos.
Anteriormente, levava horas para encontrar manualmente as mesmas informações.
Richard Davey, o diretor de tecnologia (CTO) da empresa, resumiu tudo
perfeitamente:
“Ideias que antes levavam dias para serem prototipadas agora se tornam jogáveis ​
em minutos.”
Isso é muito louco.
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
3/13



---

# Página 4

Um exemplo rápido em Python
Você não precisa de muito código para começar. Aqui está um exemplo simples:
from google import genai 
from google.genai import types 
import time 
client = genai.Client() 
store = client.file_search_stores.create() 
upload_op = client.file_search_stores.upload_to_file_search_store( 
    file_search_store_name=store.name, 
    file= 'path/to/your/document.pdf'
 ) 
while  not upload_op.done: 
    time.sleep( 5 ) 
    upload_op = client.operations.get(upload_op) 
response = client.models.generate_content( 
    model= 'gemini-2.5-flash' , 
    contents= 'Resuma a pesquisa sobre IA sustentável.' , 
    config=types.GenerateContentConfig( 
        tools=[types.Tool( 
            file_search=types.FileSearch( 
                file_search_store_names=[store.name] 
            ) 
        )] 
    ) 
) 
print (response.text) 
grounding = response.candidates[ 0 ].grounding_metadata 
sources = {c.retrieved_context.title for c in grounding.grounding_chunks} 
print ( 'Fontes:' , *sources)
É isso aí. Envie arquivos, faça uma pergunta e receba uma resposta com fontes.
Pronto.
Por que isso é importante?
Todo desenvolvedor de IA se depara com o mesmo problema: os modelos parecem
impressionantes, mas não têm acesso aos dados internos da sua empresa.
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
4/13



---

# Página 5

A Busca de Arquivos muda isso, permitindo que o Gemini analise seu conteúdo sem
uma configuração de recuperação complexa.
Se você estiver criando algo que exija informações atuais ou específicas do domínio
— como bots de suporte, ferramentas internas ou perguntas e respostas sobre
documentos — isso vai mudar tudo.
Experimente você mesmo
Você pode experimentar a Pesquisa de Arquivos agora mesmo emGoogle AI
StudioExiste uma demonstração chamada“Consulte o manual”— Carregue alguns
arquivos, faça perguntas e veja o quão bem isso fundamenta as respostas.
Depois de pegar o jeito, você pode remixar a demonstração ou integrá-la
diretamente ao seu aplicativo.
Seguindo
Publicado no Coding Nexus
9 mil seguidores · Última publicação  há 2 horas
A Coding Nexus é uma comunidade de desenvolvedores, entusiastas de tecnologia e aspirantes a
programadores. Seja você um iniciante explorando as profundezas do Python, um aprofundando-se em
ciência de dados, um mestre em desenvolvimento web ou um entusiasta das últimas tendências em IA, a
Coding Nexus tem algo para você.
Seguindo
Escrito por Civil Learning
3,7 mil seguidores · 6 seguintes
Plataforma Google Cloud
Trapos
IA
Agente de IA
Ferramentas de IA
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
5/13



---

# Página 6

Compartilhamos o que você precisa saber. Compartilhado apenas para fins informativos.
Respostas ( 6 )
Joubert Júnior
Rama Rao Desai
12 de novembro
Você deixou passar alguns pontos importantes. Se você enviar arquivos, eles se tornarão públicos. Além 
disso, essa ferramenta ainda não está disponível na versão chat do Gemini, mas sim em ecossistemas de 
desenvolvedores para criar aplicativos robustos. No Claude, ela está disponível na interface de chat, na 
seção de projetos.
2 respostas
Responder
Daniel Twum
9 de novembro
Muito obrigado pelo artigo. Este NotebookLM é uma versão reempacotada ou revisada?
1 resposta
Responder
Rinfo
13 de novembro
Este artigo explica muito bem como a nova ferramenta de busca de arquivos do Google simplifica a geração 
aumentada por recuperação (RAG). A ferramenta parece ser revolucionária para aprimorar os fluxos de 
trabalho de IA, facilitando muito a obtenção rápida de dados relevantes. É… mais
Responder
O que você acha?
17
7
1
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
6/13



---

# Página 7

Ver todas as respostas
Mais conteúdo de Civil Learning e Coding Nexus
Em
por
Como fiz meus agentes de IA para programação conversarem,
planejarem e programarem juntos como uma equipe de desenvolvimen…
Já faz um tempo que uso agentes de codificação — Codex, Claude Code, Cursor, e tudo mais.
Eles são ótimos para gerar código, mas coordenar…
5 de novembro
Coding Nexus
Aprendizado Cívico
264
8
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
7/13



---

# Página 8

Em
por
Agent Lightning da Microsoft: a estrutura de código aberto que treina e
otimiza agentes de IA…
A Microsoft lançou discretamente uma nova estrutura de código aberto chamada Agent
Lightning, e é um daqueles casos em que nos perguntamos "por que não tínhamos isso…
1 de novembro
Em
por
OpenStock — O aplicativo de mercado de ações gratuito e de código
aberto, criado para todos.
Coding Nexus
Golpe de Código
150
4
Coding Nexus
Tattva Tarang
Abrir no aplicativo
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
8/13



---

# Página 9

Veja tudo da área de Aprendizagem Civil
Veja tudo da Coding Nexus
Recomendado pelo Medium
Há algum tempo, percebi que estava gastando mais tempo alternando entre aplicativos
financeiros do que realmente aprendendo com eles. Tudo que vale a pena…
18 de outubro
Em
por
RTX 3090 vs 4090 vs 5090 vs PRO 6000 — Qual GPU faz mais sentido
para LLMs?
Se você estiver experimentando com modelos de linguagem grandes (LLMs) ou tentando
executá-los localmente, a GPU escolhida determinará a fluidez (ou a qualidade) do processo.
7 de novembro
207
3
Coding Nexus
Aprendizado Cívico
323
7
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
9/13



---

# Página 10

Em
por
Como executar o n8n gratuitamente para sempre no Google Cloud
Economize US$ 240 por ano hospedando o n8n por conta própria no plano gratuito do Google
Cloud. Este guia mostra como configurar automação ilimitada gratuitamente.
2 de novembro
Em
por
Stanford acaba de encerrar o Prompt Engineering com uma única frase…
Um novo método de pesquisa restaura silenciosamente a criatividade que pensávamos ter
perdido para sempre nos modelos de IA… sem retreinamento, plugins ou recursos…
Mente de IA
Shakir Majeed Mir
376
6
Inteligência Artificial em Linguagem Simples
Kiran Maan
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
10/13



---

# Página 11

11 de novembro
Em
por
Este novo modelo de incorporação reduz os custos de bancos de dados
vetoriais em cerca de 200 vezes!
Além disso, supera os modelos da OpenAI e da Cohere.
4 de novembro
547
12
Em direção à IA
Avi Chawla
490
5
Ichigo
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
11/13



---

# Página 12

Acidentalmente, deixei Claude 45% mais inteligente. Veja como.
Às 2 da manhã, descobri acidentalmente truques de estímulo psicológico que parecem
loucura, mas são comprovados por pesquisas reais. Testei-os em mais de 40 pessoas…
21 de novembro
Em
por
Testei a nova API RAG Gemini do Google para busca de arquivos (que
você nem sabia que existia…)
O Google lançou discretamente essa nova API Gemini de busca de arquivos com um poderoso
sistema RAG, e ela não está recebendo a atenção que merece.
10 de novembro
543
10
Engenheiro de Software de IA
Joe Njenga
191
6
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
12/13



---

# Página 13

Veja mais recomendações
Em
por
Será que o Google acabou de dizimar um setor inteiro (e criar um novo)?
6 dias atrás
Códice
Coelho de IA
485
12
30/11/2025, 12:37
O Google acaba de tornar o RAG ridiculamente fácil com a nova ferramenta de busca de arquivos | por Civil Learning | Coding Nexus | Nov…
https://medium.com/coding-nexus/google-just-made-rag-ridiculously-easy-with-the-new-file-search-tool-a95a29cde211
13/13

