"""
Testes de integração para endpoints da API usando httpx.AsyncClient e database real.
"""
import pytest
from httpx import AsyncClient
from unittest.mock import patch, MagicMock
from uuid import uuid4
import tempfile
import os

from app.main import app
from app.core.database import get_db, Base
from app.models.document import Document


@pytest.mark.asyncio
@pytest.mark.integration
class TestHealthEndpoints:
    """Testes para endpoints de health check."""
    
    async def test_health_check(self, async_client: AsyncClient):
        """Testa endpoint de health check."""
        response = await async_client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}
    
    async def test_root_endpoint(self, async_client: AsyncClient):
        """Testa endpoint raiz."""
        response = await async_client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "version" in data
        assert "status" in data


@pytest.mark.asyncio
@pytest.mark.integration
class TestDocumentEndpoints:
    """Testes de integração para endpoints de documentos."""
    
    async def test_list_documents_empty(self, async_client: AsyncClient):
        """Testa listagem de documentos quando não há documentos."""
        # Como não há autenticação configurada (modo dev), deve retornar 200
        # Mas pode retornar 401 se auth estiver configurada
        response = await async_client.get("/api/v1/documents")
        # Em modo dev sem auth, retorna 200 com lista vazia
        # Com auth configurada, retornaria 401
        assert response.status_code in [200, 401]
        if response.status_code == 200:
            data = response.json()
            assert "documents" in data
            assert "total" in data
            assert isinstance(data["documents"], list)
    
    async def test_get_document_not_found(self, async_client: AsyncClient):
        """Testa obter documento inexistente."""
        fake_id = str(uuid4())
        response = await async_client.get(f"/api/v1/documents/{fake_id}")
        # Pode retornar 401 (auth) ou 404 (not found)
        assert response.status_code in [404, 401]
    
    async def test_delete_document_not_found(self, async_client: AsyncClient):
        """Testa deletar documento inexistente."""
        fake_id = str(uuid4())
        response = await async_client.delete(f"/api/v1/documents/{fake_id}")
        # Pode retornar 401 (auth) ou 404 (not found)
        assert response.status_code in [404, 401]
    
    async def test_upload_document_with_mock_vector_repo(
        self, 
        async_client: AsyncClient,
        test_db_session
    ):
        """Testa upload de documento com mock do VectorRepository."""
        # Cria conteúdo de arquivo de teste
        file_content = b"PDF content test"
        
        with patch('app.services.document_service.VectorRepository') as mock_vec_class:
            # Mock do VectorRepository
            mock_vec_repo = MagicMock()
            mock_vec_repo.upload_document = MagicMock(return_value={
                "file_id": "test_file_id_123",
                "operation_name": "operations/test_operation"
            })
            mock_vec_class.return_value = mock_vec_repo
            
            # Cria arquivo temporário
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(file_content)
                tmp_file_path = tmp_file.name
            
            try:
                # Upload via API
                with open(tmp_file_path, "rb") as f:
                    files = {"file": ("test.pdf", f, "application/pdf")}
                    # Em modo dev, user é mock, então deve funcionar
                    response = await async_client.post(
                        "/api/v1/documents",
                        files=files
                    )
                
                # Pode retornar 201 (sucesso) ou 401 (se auth configurada)
                assert response.status_code in [201, 401]
                
                if response.status_code == 201:
                    data = response.json()
                    assert "id" in data
                    assert data["filename"] == "test.pdf"
                    assert "google_file_id" in data
            
            finally:
                # Limpa arquivo temporário
                if os.path.exists(tmp_file_path):
                    os.unlink(tmp_file_path)
    
    async def test_document_flow_end_to_end(
        self,
        async_client: AsyncClient,
        test_db_session
    ):
        """Testa fluxo completo: criar, listar, obter, deletar documento."""
        # Skip se auth estiver configurada (precisa de token)
        # Este teste funciona apenas em modo desenvolvimento
        
        with patch('app.services.document_service.VectorRepository') as mock_vec_class:
            mock_vec_repo = MagicMock()
            mock_vec_repo.upload_document = MagicMock(return_value={
                "file_id": "e2e_test_file_id",
                "operation_name": "operations/e2e_test"
            })
            mock_vec_repo.delete_file = MagicMock(return_value=True)
            mock_vec_class.return_value = mock_vec_repo
            
            file_content = b"E2E test PDF content"
            document_id = None
            
            try:
                # 1. Upload documento
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    tmp_file.write(file_content)
                    tmp_file_path = tmp_file.name
                
                with open(tmp_file_path, "rb") as f:
                    files = {"file": ("e2e_test.pdf", f, "application/pdf")}
                    response = await async_client.post("/api/v1/documents", files=files)
                
                if response.status_code == 401:
                    pytest.skip("Auth configurada, precisa de token para testes E2E")
                
                assert response.status_code == 201
                upload_data = response.json()
                document_id = upload_data["id"]
                
                # 2. Listar documentos
                response = await async_client.get("/api/v1/documents")
                assert response.status_code == 200
                list_data = response.json()
                assert len(list_data["documents"]) > 0
                
                # 3. Obter documento específico
                response = await async_client.get(f"/api/v1/documents/{document_id}")
                assert response.status_code == 200
                get_data = response.json()
                assert get_data["id"] == document_id
                
                # 4. Deletar documento
                response = await async_client.delete(f"/api/v1/documents/{document_id}")
                assert response.status_code == 204
                
                # 5. Verificar que foi deletado
                response = await async_client.get(f"/api/v1/documents/{document_id}")
                assert response.status_code == 404
            
            finally:
                # Limpa arquivo temporário
                if os.path.exists(tmp_file_path):
                    os.unlink(tmp_file_path)


@pytest.mark.asyncio
@pytest.mark.integration
class TestSearchEndpoints:
    """Testes de integração para endpoints de busca."""
    
    async def test_search_semantic_success(self, async_client: AsyncClient):
        """Testa busca semântica bem-sucedida."""
        with patch('app.services.search_service.VectorRepository') as mock_vec_class:
            mock_vec_repo = MagicMock()
            mock_vec_repo.search_semantic = MagicMock(return_value={
                "answer": "Esta é uma resposta de teste para busca semântica",
                "sources": ["documento1.pdf", "documento2.pdf"],
                "query": "teste"
            })
            mock_vec_class.return_value = mock_vec_repo
            
            response = await async_client.post(
                "/api/v1/search",
                json={
                    "query": "Qual é a arquitetura do sistema?",
                    "max_results": 10
                }
            )
            
            assert response.status_code == 200
            data = response.json()
            assert "answer" in data
            assert "sources" in data
            assert "query" in data
            assert "processing_time_ms" in data
            assert isinstance(data["sources"], list)
    
    async def test_search_empty_query(self, async_client: AsyncClient):
        """Testa busca com query vazia."""
        response = await async_client.post(
            "/api/v1/search",
            json={"query": "", "max_results": 10}
        )
        # Pode retornar 400 (validação) ou 200 (se permitir query vazia)
        assert response.status_code in [200, 400, 422]
    
    async def test_search_invalid_request(self, async_client: AsyncClient):
        """Testa busca com requisição inválida."""
        response = await async_client.post(
            "/api/v1/search",
            json={}  # Falta query
        )
        assert response.status_code == 422  # Validation error
    
    async def test_search_with_custom_max_results(self, async_client: AsyncClient):
        """Testa busca com max_results customizado."""
        with patch('app.services.search_service.VectorRepository') as mock_vec_class:
            mock_vec_repo = MagicMock()
            mock_vec_repo.search_semantic = MagicMock(return_value={
                "answer": "Resposta",
                "sources": [],
                "query": "teste"
            })
            mock_vec_class.return_value = mock_vec_repo
            
            response = await async_client.post(
                "/api/v1/search",
                json={
                    "query": "teste",
                    "max_results": 5
                }
            )
            
            assert response.status_code == 200
            data = response.json()
            assert "answer" in data
