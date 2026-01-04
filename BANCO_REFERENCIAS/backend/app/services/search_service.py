"""
Service para busca semântica com RAG.
Business logic para operações de busca.
"""
from sqlalchemy.ext.asyncio import AsyncSession
import time
import logging

from app.repositories.vector_repository import VectorRepository
from app.repositories.document_repository import DocumentRepository
from app.schemas.search import SearchRequest, SearchResponse
from app.core.exceptions import GoogleFileSearchError
from app.core.validators import validate_search_query
from typing import Optional

logger = logging.getLogger(__name__)


class SearchService:
    """Service para busca semântica RAG."""
    
    def __init__(self, db: AsyncSession):
        """
        Inicializa service com sessão do banco.
        
        Args:
            db: Sessão assíncrona do SQLAlchemy
        """
        self.db = db
        self.vector_repo = VectorRepository()
        self.document_repo = DocumentRepository(db)
    
    async def search_semantic(self, request: SearchRequest, user_id: Optional[str] = None) -> SearchResponse:
        """
        Busca semântica usando RAG no Google File Search.
        
        Args:
            request: SearchRequest com query e parâmetros
            user_id: ID do usuário para filtrar documentos (opcional)
            
        Returns:
            SearchResponse com resposta e fontes (filtradas por user_id se fornecido)
            
        Raises:
            GoogleFileSearchError: Se houver erro na busca
            InvalidQueryError: Se query for inválida
        """
        # Valida query
        validate_search_query(request.query)
        
        logger.info(f"Busca iniciada: query='{request.query[:50]}...' (max_results={request.max_results}, user_id={user_id})")
        
        # Verifica cache
        cache_key = self._cache_key(request.query, user_id)
        cached_result = await cache_repo.get(cache_key)
        if cached_result:
            logger.info(f"Busca encontrada no cache: {cache_key}")
            return SearchResponse(**cached_result)
        
        start_time = time.time()
        
        try:
            # Busca no Google File Search (sync)
            result = self.vector_repo.search_semantic(
                query=request.query,
                max_results=request.max_results or 10
            )
            
            # Filtrar fontes por user_id se fornecido
            filtered_sources = result["sources"]
            if user_id:
                # Obtém filenames dos documentos do usuário
                user_filenames = await self.document_repo.get_filenames_by_user(user_id)
                user_filenames_set = set(user_filenames)
                
                # Filtra fontes para incluir apenas documentos do usuário
                filtered_sources = [
                    source for source in result["sources"]
                    if any(filename in source for filename in user_filenames_set)
                ]
                
                logger.info(f"Fontes filtradas: {len(filtered_sources)} de {len(result['sources'])} para user_id={user_id}")
            
            processing_time_ms = int((time.time() - start_time) * 1000)
            
            logger.info(f"Busca concluída: {processing_time_ms}ms, {len(filtered_sources)} fontes encontradas")
            
            response = SearchResponse(
                query=request.query,
                answer=result["answer"],
                sources=filtered_sources,
                processing_time_ms=processing_time_ms
            )
            
            # Armazena no cache (TTL: 15 minutos = 900 segundos)
            await cache_repo.set(
                cache_key,
                response.model_dump(),
                ttl=900
            )
            
            return response
            
        except GoogleFileSearchError as e:
            logger.error(f"Erro na busca semântica: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Erro inesperado na busca semântica: {str(e)}", exc_info=True)
            raise GoogleFileSearchError(f"Erro na busca semântica: {str(e)}")

