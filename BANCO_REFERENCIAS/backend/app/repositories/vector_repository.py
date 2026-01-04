"""
Repository para Google File Search (Vector DB - RAG).
"""
from typing import Optional
from google import genai
from google.genai import types
from app.core.config import settings
from app.core.exceptions import GoogleFileSearchError


class VectorRepository:
    """Repository para interagir com Google File Search Store."""
    
    def __init__(self):
        """Inicializa cliente do Google Gemini."""
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = settings.GEMINI_MODEL
        self.store_id = settings.FILE_STORE_ID or self._get_or_create_store()
    
    def _get_or_create_store(self) -> Optional[str]:
        """
        Obtém ou cria um File Search Store.
        
        Returns:
            ID do store criado ou existente, ou None se não existir
        """
        # Se já tem FILE_STORE_ID configurado, usa ele
        if settings.FILE_STORE_ID:
            return settings.FILE_STORE_ID
        
        # Por enquanto retorna None (será criado no primeiro uso)
        return None
    
    def upload_document(
        self,
        file_path: str,
        display_name: str,
        mime_type: str
    ) -> dict:
        """
        Faz upload de documento para Google File Search Store.
        
        Args:
            file_path: Caminho do arquivo local
            display_name: Nome de exibição
            mime_type: Tipo MIME do arquivo
            
        Returns:
            Dict com informações do upload (file_id, operation_name, etc)
            
        Raises:
            GoogleFileSearchError: Se houver erro no upload
        """
        try:
            if not self.store_id:
                # Cria store se não existir
                self.store_id = self._create_store()
            
            upload_op = self.client.file_search_stores.upload_to_file_search_store(
                file_search_store_name=self.store_id,
                file=file_path,
                config={
                    'display_name': display_name,
                    'mime_type': mime_type
                }
            )
            
            # Aguarda conclusão do upload
            import time
            while not upload_op.done:
                time.sleep(2)
                upload_op = self.client.operations.get(upload_op)
            
            # Extrai file_id
            file_id = None
            if hasattr(upload_op, 'metadata') and upload_op.metadata:
                file_id = upload_op.metadata.get('file_id')
            
            if not file_id:
                file_id = upload_op.name.split('/')[-1]
            
            return {
                "file_id": file_id,
                "operation_name": upload_op.name,
                "store_id": self.store_id
            }
            
        except Exception as e:
            raise GoogleFileSearchError(f"Erro ao fazer upload: {str(e)}")
    
    def search_semantic(
        self,
        query: str,
        max_results: int = 10
    ) -> dict:
        """
        Busca semântica usando RAG no Google File Search.
        
        Args:
            query: Query de busca em linguagem natural
            max_results: Número máximo de resultados
            
        Returns:
            Dict com resposta e fontes
            
        Raises:
            GoogleFileSearchError: Se houver erro na busca
        """
        try:
            if not self.store_id:
                raise GoogleFileSearchError("File Search Store não configurado")
            
            response = self.client.models.generate_content(
                model=self.model,
                contents=query,
                config=types.GenerateContentConfig(
                    tools=[
                        types.Tool(
                            file_search=types.FileSearch(
                                file_search_store_names=[self.store_id]
                            )
                        )
                    ]
                ),
            )
            
            # Extrai resposta e fontes
            answer = response.text if response.text else ""
            
            sources = []
            grounding = response.candidates[0].grounding_metadata if response.candidates else None
            if grounding:
                for chunk in grounding.grounding_chunks:
                    title = getattr(chunk.retrieved_context, "title", None)
                    if title and title not in sources:
                        sources.append(title)
            
            return {
                "answer": answer,
                "sources": sources,
                "query": query
            }
            
        except Exception as e:
            raise GoogleFileSearchError(f"Erro na busca semântica: {str(e)}")
    
    def _create_store(self) -> str:
        """
        Cria um novo File Search Store.
        
        Returns:
            ID do store criado
        """
        try:
            # Cria novo store
            store = self.client.file_search_stores.create(
                display_name="Banco de Referências Store"
            )
            store_id = store.name  # Formato: fileSearchStores/xxx
            
            print(f"✅ File Search Store criado: {store_id}")
            return store_id
            
        except Exception as e:
            raise GoogleFileSearchError(f"Erro ao criar store: {str(e)}")
    
    def delete_file(self, file_id: str) -> bool:
        """
        Deleta arquivo do Google File Search Store.
        
        Args:
            file_id: ID do arquivo no Google File Search
            
        Returns:
            True se deletado com sucesso
            
        Raises:
            GoogleFileSearchError: Se houver erro na deleção
        """
        try:
            # Constrói o nome completo do arquivo
            # Formato: files/{file_id}
            file_name = f"files/{file_id}" if not file_id.startswith("files/") else file_id
            
            # Deleta o arquivo
            self.client.files.delete(file_name)
            
            return True
            
        except Exception as e:
            # Se arquivo não existe, considera sucesso (idempotente)
            if "not found" in str(e).lower() or "404" in str(e):
                return True
            raise GoogleFileSearchError(f"Erro ao deletar arquivo do Google File Search: {str(e)}")

