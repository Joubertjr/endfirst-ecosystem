"""
Service para gestão de referências.
Business logic para operações de referências.
"""
from typing import Optional, List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.reference_repository import ReferenceRepository
from app.schemas.reference import ReferenceCreate, ReferenceUpdate, ReferenceResponse
from app.core.exceptions import ReferenceNotFoundError
import logging

logger = logging.getLogger(__name__)


class ReferenceService:
    """Service para operações de referências."""
    
    def __init__(self, db: AsyncSession):
        """
        Inicializa service com sessão do banco.
        
        Args:
            db: Sessão assíncrona do SQLAlchemy
        """
        self.db = db
        self.reference_repo = ReferenceRepository(db)
    
    async def create_reference(self, data: ReferenceCreate) -> ReferenceResponse:
        """
        Cria uma nova referência.
        
        Args:
            data: Dados da referência
            
        Returns:
            ReferenceResponse da referência criada
        """
        reference = await self.reference_repo.create(
            title=data.title,
            category=data.category,
            subject=data.subject,
            sources=data.sources,
            concepts=data.concepts,
            description=data.description
        )
        
        await self.db.commit()
        logger.info(f"Referência criada: {reference.id} - {reference.title}")
        
        return ReferenceResponse.model_validate(reference)
    
    async def get_reference(self, reference_id: UUID) -> ReferenceResponse:
        """
        Busca referência por ID.
        
        Args:
            reference_id: ID da referência
            
        Returns:
            ReferenceResponse
            
        Raises:
            ReferenceNotFoundError: Se referência não encontrada
        """
        reference = await self.reference_repo.get_by_id(reference_id)
        if not reference:
            raise ReferenceNotFoundError(str(reference_id))
        
        return ReferenceResponse.model_validate(reference)
    
    async def list_references(
        self,
        skip: int = 0,
        limit: int = 100,
        category: Optional[str] = None
    ) -> List[ReferenceResponse]:
        """
        Lista referências, opcionalmente filtradas por categoria.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros
            category: Categoria para filtrar (opcional)
            
        Returns:
            Lista de ReferenceResponse
        """
        references = await self.reference_repo.list_all(
            skip=skip,
            limit=limit,
            category=category
        )
        return [ReferenceResponse.model_validate(ref) for ref in references]
    
    async def update_reference(
        self,
        reference_id: UUID,
        data: ReferenceUpdate
    ) -> ReferenceResponse:
        """
        Atualiza uma referência.
        
        Args:
            reference_id: ID da referência
            data: Dados para atualização
            
        Returns:
            ReferenceResponse atualizada
            
        Raises:
            ReferenceNotFoundError: Se referência não encontrada
        """
        reference = await self.reference_repo.update(
            reference_id=reference_id,
            title=data.title,
            category=data.category,
            subject=data.subject,
            sources=data.sources,
            concepts=data.concepts,
            description=data.description
        )
        
        await self.db.commit()
        logger.info(f"Referência atualizada: {reference.id} - {reference.title}")
        
        return ReferenceResponse.model_validate(reference)
    
    async def delete_reference(self, reference_id: UUID) -> bool:
        """
        Deleta uma referência.
        
        Args:
            reference_id: ID da referência
            
        Returns:
            True se deletada com sucesso
            
        Raises:
            ReferenceNotFoundError: Se referência não encontrada
        """
        deleted = await self.reference_repo.delete(reference_id)
        await self.db.commit()
        
        logger.info(f"Referência deletada: {reference_id}")
        return deleted

