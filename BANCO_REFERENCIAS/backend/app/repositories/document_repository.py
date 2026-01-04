"""
Repository para documentos (PostgreSQL).
"""
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.models.document import Document
from app.core.exceptions import DocumentNotFoundError


class DocumentRepository:
    """Repository para operações CRUD de documentos."""
    
    def __init__(self, db: AsyncSession):
        """
        Inicializa repository com sessão do banco.
        
        Args:
            db: Sessão assíncrona do SQLAlchemy
        """
        self.db = db
    
    async def create(
        self,
        google_file_id: str,
        filename: str,
        file_type: Optional[str] = None,
        file_size_bytes: Optional[int] = None,
        metadata: Optional[dict] = None,
        reference_id: Optional[UUID] = None,
        project_id: Optional[UUID] = None,
        user_id: Optional[str] = None
    ) -> Document:
        """
        Cria um novo documento.
        
        Args:
            google_file_id: ID do arquivo no Google File Search
            filename: Nome do arquivo
            file_type: Tipo do arquivo
            file_size_bytes: Tamanho em bytes
            metadata: Metadados adicionais (JSON)
            reference_id: ID da referência relacionada (opcional)
            project_id: ID do projeto relacionado (opcional)
            
        Returns:
            Document criado
        """
        document = Document(
            google_file_id=google_file_id,
            filename=filename,
            file_type=file_type,
            file_size_bytes=file_size_bytes,
            document_metadata=metadata,  # Usa document_metadata (metadata é reservado)
            reference_id=reference_id,
            project_id=project_id,
            user_id=user_id
        )
        
        self.db.add(document)
        await self.db.flush()
        await self.db.refresh(document)
        
        return document
    
    async def get_by_id(self, document_id: UUID, user_id: Optional[str] = None) -> Optional[Document]:
        """
        Busca documento por ID, opcionalmente verificando ownership.
        
        Args:
            document_id: ID do documento
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            Document ou None se não encontrado
        """
        stmt = select(Document).where(Document.id == document_id)
        
        # Verificar ownership se user_id fornecido
        if user_id:
            stmt = stmt.where(Document.user_id == user_id)
        
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_by_google_file_id(self, google_file_id: str) -> Optional[Document]:
        """
        Busca documento por Google File ID.
        
        Args:
            google_file_id: ID do arquivo no Google
            
        Returns:
            Document ou None se não encontrado
        """
        result = await self.db.execute(
            select(Document).where(Document.google_file_id == google_file_id)
        )
        return result.scalar_one_or_none()
    
    async def list_all(
        self,
        skip: int = 0,
        limit: int = 100,
        user_id: Optional[str] = None,
        reference_id: Optional[UUID] = None,
        project_id: Optional[UUID] = None
    ) -> List[Document]:
        """
        Lista documentos, opcionalmente filtrados por user_id, reference_id ou project_id.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros
            user_id: ID do usuário para filtrar (opcional)
            reference_id: ID da referência para filtrar (opcional)
            project_id: ID do projeto para filtrar (opcional)
            
        Returns:
            Lista de documentos
        """
        stmt = select(Document)
        
        # Filtrar por user_id se fornecido
        if user_id:
            stmt = stmt.where(Document.user_id == user_id)
        
        # Filtrar por reference_id se fornecido
        if reference_id:
            stmt = stmt.where(Document.reference_id == reference_id)
        
        # Filtrar por project_id se fornecido
        if project_id:
            stmt = stmt.where(Document.project_id == project_id)
        
        stmt = stmt.order_by(Document.upload_date.desc()).offset(skip).limit(limit)
        result = await self.db.execute(stmt)
        
        return list(result.scalars().all())
    
    async def get_google_file_ids_by_user(self, user_id: str) -> List[str]:
        """
        Obtém lista de google_file_ids dos documentos de um usuário.
        
        Args:
            user_id: ID do usuário
            
        Returns:
            Lista de google_file_ids
        """
        stmt = select(Document.google_file_id).where(Document.user_id == user_id)
        result = await self.db.execute(stmt)
        return [row[0] for row in result.all() if row[0]]
    
    async def get_filenames_by_user(self, user_id: str) -> List[str]:
        """
        Obtém lista de filenames dos documentos de um usuário.
        
        Args:
            user_id: ID do usuário
            
        Returns:
            Lista de filenames
        """
        stmt = select(Document.filename).where(Document.user_id == user_id)
        result = await self.db.execute(stmt)
        return [row[0] for row in result.all() if row[0]]
    
    async def delete(self, document_id: UUID, user_id: Optional[str] = None) -> bool:
        """
        Deleta um documento, opcionalmente verificando ownership.
        
        Args:
            document_id: ID do documento
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            True se deletado
            
        Raises:
            DocumentNotFoundError: Se documento não encontrado
        """
        document = await self.get_by_id(document_id, user_id=user_id)
        if not document:
            raise DocumentNotFoundError(str(document_id))
        
        await self.db.delete(document)
        await self.db.flush()
        
        return True


