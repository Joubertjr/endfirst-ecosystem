"""
Testes unitários para DocumentService.
"""
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

from app.services.document_service import DocumentService
from app.core.exceptions import DocumentNotFoundError, GoogleFileSearchError
from app.schemas.document import DocumentResponse


@pytest.mark.asyncio
@pytest.mark.unit
class TestDocumentService:
    """Testes para DocumentService."""
    
    @pytest.fixture
    def service(self, mock_db_session):
        """Cria instância de DocumentService para testes."""
        with patch('app.services.document_service.VectorRepository') as mock_vector_repo_class:
            mock_vector_repo = mock_vector_repo_class.return_value
            mock_vector_repo.upload_document = MagicMock(return_value={
                "file_id": "test_file_id_123",
                "operation_name": "operations/test_operation"
            })
            
            service = DocumentService(mock_db_session)
            service.vector_repo = mock_vector_repo
            return service
    
    async def test_upload_document_success(
        self, 
        service, 
        sample_file_content_pdf,
        mock_tempfile
    ):
        """Testa upload de documento bem-sucedido."""
        # Arrange
        filename = "test_document.pdf"
        expected_file_id = "test_file_id_123"
        
        # Mock do repository
        mock_doc = MagicMock()
        mock_doc.id = uuid4()
        mock_doc.google_file_id = expected_file_id
        mock_doc.filename = filename
        mock_doc.file_type = "application/pdf"
        mock_doc.file_size_bytes = len(sample_file_content_pdf)
        mock_doc.status = "active"
        mock_doc.upload_date = None
        mock_doc.document_metadata = None
        
        service.document_repo.create = AsyncMock(return_value=mock_doc)
        service.db.commit = AsyncMock()
        
        # Act
        with patch('os.remove'):  # Mock remove do arquivo temporário
            result = await service.upload_document(
                file_content=sample_file_content_pdf,
                filename=filename
            )
        
        # Assert
        assert isinstance(result, DocumentResponse)
        assert result.filename == filename
        assert result.google_file_id == expected_file_id
        service.vector_repo.upload_document.assert_called_once()
        service.document_repo.create.assert_called_once()
        service.db.commit.assert_called_once()
    
    async def test_upload_document_with_reference_id(
        self,
        service,
        sample_file_content_pdf,
        mock_tempfile
    ):
        """Testa upload de documento com reference_id."""
        # Arrange
        filename = "test_document.pdf"
        reference_id = uuid4()
        
        mock_doc = MagicMock()
        mock_doc.id = uuid4()
        mock_doc.google_file_id = "test_file_id"
        mock_doc.filename = filename
        service.document_repo.create = AsyncMock(return_value=mock_doc)
        service.db.commit = AsyncMock()
        
        # Act
        with patch('os.remove'):
            result = await service.upload_document(
                file_content=sample_file_content_pdf,
                filename=filename,
                reference_id=reference_id
            )
        
        # Assert
        assert isinstance(result, DocumentResponse)
        # Verifica que reference_id foi passado para create
        call_kwargs = service.document_repo.create.call_args[1]
        assert call_kwargs.get('reference_id') == reference_id
    
    async def test_get_document_success(self, service):
        """Testa obter documento por ID com sucesso."""
        # Arrange
        document_id = uuid4()
        mock_doc = MagicMock()
        mock_doc.id = document_id
        mock_doc.google_file_id = "test_file_id"
        mock_doc.filename = "test.pdf"
        mock_doc.file_type = "application/pdf"
        mock_doc.file_size_bytes = 1024
        mock_doc.status = "active"
        mock_doc.upload_date = None
        mock_doc.document_metadata = None
        
        service.document_repo.get_by_id = AsyncMock(return_value=mock_doc)
        
        # Act
        result = await service.get_document(document_id)
        
        # Assert
        assert isinstance(result, DocumentResponse)
        assert result.id == document_id
        service.document_repo.get_by_id.assert_called_once_with(document_id)
    
    async def test_get_document_not_found(self, service):
        """Testa obter documento inexistente."""
        # Arrange
        document_id = uuid4()
        service.document_repo.get_by_id = AsyncMock(return_value=None)
        
        # Act & Assert
        with pytest.raises(DocumentNotFoundError):
            await service.get_document(document_id)
    
    async def test_list_documents(self, service):
        """Testa listar documentos."""
        # Arrange
        mock_doc1 = MagicMock()
        mock_doc1.id = uuid4()
        mock_doc1.google_file_id = "file1"
        mock_doc1.filename = "doc1.pdf"
        mock_doc1.file_type = "application/pdf"
        mock_doc1.file_size_bytes = 1024
        mock_doc1.status = "active"
        mock_doc1.upload_date = None
        mock_doc1.document_metadata = None
        
        mock_doc2 = MagicMock()
        mock_doc2.id = uuid4()
        mock_doc2.google_file_id = "file2"
        mock_doc2.filename = "doc2.pdf"
        mock_doc2.file_type = "application/pdf"
        mock_doc2.file_size_bytes = 2048
        mock_doc2.status = "active"
        mock_doc2.upload_date = None
        mock_doc2.document_metadata = None
        
        service.document_repo.list_all = AsyncMock(return_value=[mock_doc1, mock_doc2])
        
        # Act
        result = await service.list_documents(skip=0, limit=10)
        
        # Assert
        assert len(result) == 2
        assert all(isinstance(doc, DocumentResponse) for doc in result)
        service.document_repo.list_all.assert_called_once_with(skip=0, limit=10)
    
    async def test_list_documents_with_pagination(self, service):
        """Testa listar documentos com paginação."""
        # Arrange
        service.document_repo.list_all = AsyncMock(return_value=[])
        
        # Act
        result = await service.list_documents(skip=10, limit=5)
        
        # Assert
        assert result == []
        service.document_repo.list_all.assert_called_once_with(skip=10, limit=5)
    
    async def test_delete_document_success(self, service):
        """Testa deletar documento com sucesso."""
        # Arrange
        document_id = uuid4()
        service.document_repo.delete = AsyncMock(return_value=True)
        service.db.commit = AsyncMock()
        
        # Act
        result = await service.delete_document(document_id)
        
        # Assert
        assert result is True
        service.document_repo.delete.assert_called_once_with(document_id)
        service.db.commit.assert_called_once()
    
    async def test_delete_document_not_found(self, service):
        """Testa deletar documento inexistente."""
        # Arrange
        document_id = uuid4()
        # O repository raise DocumentNotFoundError quando não encontra
        service.document_repo.delete = AsyncMock(
            side_effect=DocumentNotFoundError(str(document_id))
        )
        service.db.commit = AsyncMock()
        
        # Act & Assert
        with pytest.raises(DocumentNotFoundError):
            await service.delete_document(document_id)
        
        service.db.commit.assert_not_called()
    
    async def test_upload_document_google_error(
        self,
        service,
        sample_file_content_pdf,
        mock_tempfile
    ):
        """Testa upload quando Google File Search retorna erro."""
        # Arrange
        service.vector_repo.upload_document = MagicMock(
            side_effect=Exception("Google API Error")
        )
        
        # Act & Assert
        with patch('os.remove'):
            with pytest.raises(GoogleFileSearchError):
                await service.upload_document(
                    file_content=sample_file_content_pdf,
                    filename="test.pdf"
                )
        
        # Verifica que rollback foi chamado
        service.db.rollback.assert_called_once()

