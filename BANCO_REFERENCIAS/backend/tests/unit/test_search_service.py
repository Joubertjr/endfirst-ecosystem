"""
Testes unitários para SearchService.
"""
import pytest
from unittest.mock import MagicMock, patch
import time

from app.services.search_service import SearchService
from app.core.exceptions import GoogleFileSearchError
from app.schemas.search import SearchRequest, SearchResponse


@pytest.mark.asyncio
@pytest.mark.unit
class TestSearchService:
    """Testes para SearchService."""
    
    @pytest.fixture
    def service(self, mock_db_session):
        """Cria instância de SearchService para testes."""
        with patch('app.services.search_service.VectorRepository') as mock_vector_repo_class:
            mock_vector_repo = mock_vector_repo_class.return_value
            
            service = SearchService(mock_db_session)
            service.vector_repo = mock_vector_repo
            return service
    
    async def test_search_semantic_success(self, service):
        """Testa busca semântica bem-sucedida."""
        # Arrange
        query = "Qual é a arquitetura do sistema?"
        expected_answer = "A arquitetura usa FastAPI, PostgreSQL e Google File Search"
        expected_sources = ["doc1.pdf", "doc2.pdf"]
        
        service.vector_repo.search_semantic = MagicMock(return_value={
            "answer": expected_answer,
            "sources": expected_sources
        })
        
        request = SearchRequest(query=query, max_results=10)
        
        # Act
        result = await service.search_semantic(request)
        
        # Assert
        assert isinstance(result, SearchResponse)
        assert result.query == query
        assert result.answer == expected_answer
        assert result.sources == expected_sources
        assert result.processing_time_ms > 0
        service.vector_repo.search_semantic.assert_called_once_with(
            query=query,
            max_results=10
        )
    
    async def test_search_semantic_with_custom_max_results(self, service):
        """Testa busca semântica com max_results customizado."""
        # Arrange
        query = "Teste"
        service.vector_repo.search_semantic = MagicMock(return_value={
            "answer": "Resposta",
            "sources": []
        })
        
        request = SearchRequest(query=query, max_results=5)
        
        # Act
        result = await service.search_semantic(request)
        
        # Assert
        service.vector_repo.search_semantic.assert_called_once_with(
            query=query,
            max_results=5
        )
    
    async def test_search_semantic_with_default_max_results(self, service):
        """Testa busca semântica com max_results padrão (None)."""
        # Arrange
        query = "Teste"
        service.vector_repo.search_semantic = MagicMock(return_value={
            "answer": "Resposta",
            "sources": []
        })
        
        request = SearchRequest(query=query, max_results=None)
        
        # Act
        result = await service.search_semantic(request)
        
        # Assert
        service.vector_repo.search_semantic.assert_called_once_with(
            query=query,
            max_results=10  # Valor padrão
        )
    
    async def test_search_semantic_google_error(self, service):
        """Testa busca semântica quando Google File Search retorna erro."""
        # Arrange
        query = "Teste"
        service.vector_repo.search_semantic = MagicMock(
            side_effect=Exception("Google API Error")
        )
        
        request = SearchRequest(query=query, max_results=10)
        
        # Act & Assert
        with pytest.raises(GoogleFileSearchError) as exc_info:
            await service.search_semantic(request)
        
        assert "Erro na busca semântica" in str(exc_info.value)
    
    async def test_search_semantic_processing_time(self, service):
        """Testa que processing_time_ms é calculado corretamente."""
        # Arrange
        query = "Teste"
        service.vector_repo.search_semantic = MagicMock(return_value={
            "answer": "Resposta",
            "sources": []
        })
        
        request = SearchRequest(query=query, max_results=10)
        
        # Act
        start_time = time.time()
        result = await service.search_semantic(request)
        end_time = time.time()
        
        # Assert
        expected_time_range = (end_time - start_time) * 1000
        # Permite margem de erro de 100ms
        assert abs(result.processing_time_ms - expected_time_range) < 100
    
    async def test_search_semantic_empty_sources(self, service):
        """Testa busca semântica quando não há fontes."""
        # Arrange
        query = "Teste"
        service.vector_repo.search_semantic = MagicMock(return_value={
            "answer": "Resposta sem fontes",
            "sources": []
        })
        
        request = SearchRequest(query=query, max_results=10)
        
        # Act
        result = await service.search_semantic(request)
        
        # Assert
        assert result.sources == []
        assert result.answer == "Resposta sem fontes"

