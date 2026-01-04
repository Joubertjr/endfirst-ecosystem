# File Search  |  Gemini API  |  Google AI for Developers

**URL:** https://ai.google.dev/gemini-api/docs/file-search

---

Skip to main content
/
Get API key
Cookbook
Community
Docs
API reference
Get started
Overview
Quickstart
API keys
Libraries
Interactions API
Models
Gemini
Gemini 3
Nano banana (image generation)
Veo (video generation)
Lyria (music generation)
Imagen (image generation)
Embeddings
Robotics
Pricing
Rate limits
Core capabilities
Text
Image
Video
Documents
Speech and audio
Thinking and thought signatures
Structured outputs
Function calling
Long context
Tools and agents
Overview
Deep Research
Google Search
Google Maps
Code execution
URL context
Computer Use
File Search
Live API
Get started
Capabilities
Tool use
Session management
Ephemeral tokens
Guides
Batch API
Files API
Context caching
OpenAI compatibility
Media resolution
Token counting
Prompt engineering
Logs and datasets
Safety
Open-Source frameworks
Resources
Migrate to Gen AI SDK
Release notes
Deprecations
API troubleshooting
Billing info
Partner and library integrations
Google AI Studio
Google Cloud Platform
Policies
Terms of service
Available regions
Additional usage polices
On this page
Directly upload to File Search store
Importing files
Chunking configuration
How it works
File Search stores
File metadata
Citations
Supported models
Supported file types
Application file types
Text file types
Rate limits
Pricing
What's next
Gemini 3 Flash is here. Try it for free in Google AI Studio.
Home
Gemini API
Docs
File Search
content_copy

The Gemini API enables Retrieval Augmented Generation ("RAG") through the File Search tool. File Search imports, chunks, and indexes your data to enable fast retrieval of relevant information based on a provided prompt. This information is then used as context to the model, allowing the model to provide more accurate and relevant answers.

To make File Search simple and affordable for developers, we're making file storage and embedding generation at query time free of charge. You only pay for creating embeddings when you first index your files (at the applicable embedding model cost) and the normal Gemini model input / output tokens cost. This new billing paradigm makes the File Search Tool both easier and more cost-effective to build and scale with.

Directly upload to File Search store

This examples shows how to directly upload a file to the file search store:

Python
JavaScript
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
file_search_store = client.file_search_stores.create(config={'display_name': 'your-fileSearchStore-name'})

operation = client.file_search_stores.upload_to_file_search_store(
  file='sample.txt',
  file_search_store_name=file_search_store.name,
  config={
      'display_name' : 'display-file-name',
  }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="""Can you tell me about [insert question]""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)


Check the API reference for uploadToFileSearchStore for more information.

Importing files

Alternatively, you can upload an existing file and import it to your file search store:

Python
JavaScript
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
sample_file = client.files.upload(file='sample.txt', config={'name': 'display_file_name'})

file_search_store = client.file_search_stores.create(config={'display_name': 'your-fileSearchStore-name'})

operation = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="""Can you tell me about [insert question]""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)


Check the API reference for importFile for more information.

Chunking configuration

When you import a file into a File Search store, it's automatically broken down into chunks, embedded, indexed, and uploaded to your File Search store. If you need more control over the chunking strategy, you can specify a chunking_config setting to set a maximum number of tokens per chunk and maximum number of overlapping tokens.

Python
JavaScript
operation = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    config={
        'chunking_config': {
          'white_space_config': {
            'max_tokens_per_chunk': 200,
            'max_overlap_tokens': 20
          }
        }
    }
)


To use your File Search store, pass it as a tool to the generateContent method, as shown in the Upload and Import examples.

How it works

File Search uses a technique called semantic search to find information relevant to the user prompt. Unlike standard keyword-based search, semantic search understands the meaning and context of your query.

When you import a file, it's converted into numerical representations called embeddings, which capture the semantic meaning of the text. These embeddings are stored in a specialized File Search database. When you make a query, it's also converted into an embedding. Then the system performs a File Search to find the most similar and relevant document chunks from the File Search store.

Here's a breakdown of the process for using the File Search uploadToFileSearchStore API:

Create a File Search store: A File Search store contains the processed data from your files. It's the persistent container for the embeddings that the semantic search will operate on.

Upload a file and import into a File Search store: Simultaneously upload a file and import the results into your File Search store. This creates a temporary File object, which is a reference to your raw document. That data is then chunked, converted into File Search embeddings, and indexed. The File object gets deleted after 48 hours, while the data imported into the File Search store will be stored indefinitely until you choose to delete it.

Query with File Search: Finally, you use the FileSearch tool in a generateContent call. In the tool configuration, you specify a FileSearchRetrievalResource, which points to the FileSearchStore you want to search. This tells the model to perform a semantic search on that specific File Search store to find relevant information to ground its response.

The indexing and querying process of File Search

In this diagram, the dotted line from from Documents to Embedding model (using gemini-embedding-001) represents the uploadToFileSearchStore API (bypassing File storage). Otherwise, using the Files API to separately create and then import files moves the indexing process from Documents to File storage and then to Embedding model.

File Search stores

A File Search store is a container for your document embeddings. While raw files uploaded through the File API are deleted after 48 hours, the data imported into a File Search store is stored indefinitely until you manually delete it. You can create multiple File Search stores to organize your documents. The FileSearchStore API lets you create, list, get, and delete to manage your file search stores. File Search store names are globally scoped.

Here are some examples of how to manage your File Search stores:

Python
JavaScript
REST
file_search_store = client.file_search_stores.create(config={'display_name': 'my-file_search-store-123'})

for file_search_store in client.file_search_stores.list():
    print(file_search_store)

my_file_search_store = client.file_search_stores.get(name='fileSearchStores/my-file_search-store-123')

client.file_search_stores.delete(name='fileSearchStores/my-file_search-store-123', config={'force': True})


The File Search Documents API reference for methods and fields related to managing documents in your file stores.

File metadata

You can add custom metadata to your files to help filter them or provide additional context. Metadata is a set of key-value pairs.

Python
JavaScript
op = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    custom_metadata=[
        {"key": "author", "string_value": "Robert Graves"},
        {"key": "year", "numeric_value": 1934}
    ]
)


This is useful when you have multiple documents in a File Search store and want to search only a subset of them.

Python
JavaScript
REST
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me about the book 'I, Claudius'",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name],
                    metadata_filter="author=Robert Graves",
                )
            )
        ]
    )
)

print(response.text)


Guidance on implementing list filter syntax for metadata_filter can be found at google.aip.dev/160

Citations

When you use File Search, the model's response may include citations that specify which parts of your uploaded documents were used to generate the answer. This helps with fact-checking and verification.

You can access citation information through the grounding_metadata attribute of the response.

Python
JavaScript
print(response.candidates[0].grounding_metadata)

Supported models

The following models support File Search:

gemini-3-pro-preview
gemini-2.5-pro
gemini-2.5-flash and its preview versions
gemini-2.5-flash-lite and its preview versions
Supported file types

File Search supports a wide range of file formats, listed in the following sections.

Application file types
Text file types
Rate limits

The File Search API has the following limits to enforce service stability:

Maximum file size / per document limit: 100 MB
Total size of project File Search stores (based on user tier):
Free: 1 GB
Tier 1: 10 GB
Tier 2: 100 GB
Tier 3: 1 TB
Recommendation: Limit the size of each File Search store to under 20 GB to ensure optimal retrieval latencies.
Note: The limit on File Search store size is computed on the backend, based on the size of your input plus the embeddings generated and stored with it. This is typically approximately 3 times the size of your input data.
Pricing
Developers are charged for embeddings at indexing time based on existing embeddings pricing ($0.15 per 1M tokens).
Storage is free of charge.
Query time embeddings are free of charge.
Retrieved document tokens are charged as regular context tokens.
What's next
Visit the API reference for File Search Stores and File Search Documents.
Send feedback

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.

Terms
Privacy