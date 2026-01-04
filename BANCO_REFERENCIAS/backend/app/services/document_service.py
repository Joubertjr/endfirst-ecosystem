"""
Service para gestão de documentos.
Business logic para operações de documentos.
"""
from typing import Optional
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
import tempfile
import os

from app.repositories.document_repository import DocumentRepository
from app.repositories.vector_repository import VectorRepository
from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentResponse
from app.core.exceptions import DocumentNotFoundError, GoogleFileSearchError
from app.core.validators import validate_file_size, validate_file_type
import logging

logger = logging.getLogger(__name__)


class DocumentService:
    """Service para operações de documentos."""
    
    def __init__(self, db: AsyncSession):
        """
        Inicializa service com sessão do banco.
        
        Args:
            db: Sessão assíncrona do SQLAlchemy
        """
        self.db = db
        self.document_repo = DocumentRepository(db)
        self.vector_repo = VectorRepository()
    
    async def upload_document(
        self,
        file_content: bytes,
        filename: str,
        user_id: str,
        mime_type: Optional[str] = None,
        reference_id: Optional[UUID] = None,
        project_id: Optional[UUID] = None,
        metadata: Optional[dict] = None
    ) -> DocumentResponse:
        """
        Faz upload de documento para Google File Search e salva metadata no PostgreSQL.
        
        Args:
            file_content: Conteúdo binário do arquivo
            filename: Nome do arquivo
            mime_type: Tipo MIME do arquivo
            reference_id: ID da referência relacionada (opcional)
            project_id: ID do projeto relacionado (opcional)
            metadata: Metadados adicionais (opcional)
            
        Returns:
            DocumentResponse com informações do documento criado
            
        Raises:
            GoogleFileSearchError: Se houver erro no upload para Google
            FileTooLargeError: Se arquivo exceder tamanho máximo
            InvalidFileTypeError: Se tipo de arquivo não for permitido
        """
        # Validações
        validate_file_size(len(file_content))
        validate_file_type(mime_type, filename)
        
        # Detecta mime_type se não fornecido
        if not mime_type:
            mime_type = self._detect_mime_type(filename)
        
        logger.info(f"Upload iniciado: {filename} ({len(file_content)} bytes, {mime_type})")
        
        # Salva arquivo temporariamente para upload
        with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{filename}") as tmp_file:
            tmp_file.write(file_content)
            tmp_file_path = tmp_file.name
        
        try:
            # Upload para Google File Search (sync)
            upload_result = self.vector_repo.upload_document(
                file_path=tmp_file_path,
                display_name=filename,
                mime_type=mime_type
            )
            
            # Salva metadata no PostgreSQL
            document_metadata = metadata or {"operation_name": upload_result["operation_name"]}
            document = await self.document_repo.create(
                google_file_id=upload_result["file_id"],
                filename=filename,
                file_type=mime_type,
                file_size_bytes=len(file_content),
                metadata=document_metadata,  # Repository converte para document_metadata internamente
                reference_id=reference_id,
                project_id=project_id,
                user_id=user_id
            )
            
            await self.db.commit()
            
            logger.info(f"Upload concluído: {filename} (ID: {document.id})")
            return DocumentResponse.model_validate(document)
            
        except (GoogleFileSearchError, DocumentNotFoundError) as e:
            await self.db.rollback()
            logger.error(f"Erro ao fazer upload de {filename}: {str(e)}")
            raise
        except Exception as e:
            await self.db.rollback()
            logger.error(f"Erro inesperado ao fazer upload de {filename}: {str(e)}", exc_info=True)
            raise GoogleFileSearchError(f"Erro ao fazer upload: {str(e)}")
        
        finally:
            # Remove arquivo temporário
            if os.path.exists(tmp_file_path):
                os.unlink(tmp_file_path)
    
    async def get_document(self, document_id: UUID, user_id: Optional[str] = None) -> DocumentResponse:
        """
        Busca documento por ID, opcionalmente verificando ownership.
        
        Args:
            document_id: ID do documento
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            DocumentResponse
            
        Raises:
            DocumentNotFoundError: Se documento não encontrado
        """
        document = await self.document_repo.get_by_id(document_id, user_id=user_id)
        if not document:
            raise DocumentNotFoundError(str(document_id))
        
        return DocumentResponse.model_validate(document)
    
    async def list_documents(
        self,
        skip: int = 0,
        limit: int = 100,
        user_id: Optional[str] = None,
        reference_id: Optional[UUID] = None,
        project_id: Optional[UUID] = None
    ) -> list[DocumentResponse]:
        """
        Lista documentos, opcionalmente filtrados por user_id, reference_id ou project_id.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros
            user_id: ID do usuário para filtrar (opcional)
            reference_id: ID da referência para filtrar (opcional)
            project_id: ID do projeto para filtrar (opcional)
            
        Returns:
            Lista de DocumentResponse
        """
        documents = await self.document_repo.list_all(
            skip=skip,
            limit=limit,
            user_id=user_id,
            reference_id=reference_id,
            project_id=project_id
        )
        return [DocumentResponse.model_validate(doc) for doc in documents]
    
    async def delete_document(self, document_id: UUID, user_id: Optional[str] = None) -> bool:
        """
        Deleta documento do PostgreSQL e do Google File Search, verificando ownership.
        
        Args:
            document_id: ID do documento
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            True se deletado com sucesso
            
        Raises:
            DocumentNotFoundError: Se documento não encontrado ou sem permissão
        """
        # Busca documento para obter google_file_id (verifica ownership)
        document = await self.document_repo.get_by_id(document_id, user_id=user_id)
        if not document:
            raise DocumentNotFoundError(str(document_id))
        
        try:
            # Deleta do Google File Search primeiro
            self.vector_repo.delete_file(document.google_file_id)
            
            # Deleta do PostgreSQL
            deleted = await self.document_repo.delete(document_id, user_id=user_id)
            await self.db.commit()
            
            return deleted
            
        except Exception as e:
            await self.db.rollback()
            # Log do erro mas não falha se Google File Search falhar
            # (arquivo pode já ter sido deletado ou não existir)
            print(f"⚠️ Aviso ao deletar do Google File Search: {str(e)}")
            # Tenta deletar do PostgreSQL mesmo assim
            try:
                deleted = await self.document_repo.delete(document_id, user_id=user_id)
                await self.db.commit()
                return deleted
            except Exception:
                raise GoogleFileSearchError(f"Erro ao deletar documento: {str(e)}")
    
    def _detect_mime_type(self, filename: str) -> str:
        """
        Detecta MIME type baseado na extensão do arquivo.
        
        Args:
            filename: Nome do arquivo
            
        Returns:
            MIME type detectado
        """
        extension = filename.lower().split('.')[-1] if '.' in filename else ''
        
        mime_types = {
            'pdf': 'application/pdf',
            'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'doc': 'application/msword',
            'txt': 'text/plain',
            'md': 'text/markdown',
            'json': 'application/json',
            'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            'png': 'image/png',
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'gif': 'image/gif',
            'webp': 'image/webp',
        }
        
        return mime_types.get(extension, 'application/octet-stream')

