"""
Repository para referências (PostgreSQL).
"""
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.models.reference import Reference
from app.core.exceptions import ReferenceNotFoundError


class ReferenceRepository:
    """Repository para operações CRUD de referências."""
    
    def __init__(self, db: AsyncSession):
        """
        Inicializa repository com sessão do banco.
        
        Args:
            db: Sessão assíncrona do SQLAlchemy
        """
        self.db = db
    
    async def create(
        self,
        title: str,
        category: Optional[str] = None,
        subject: Optional[str] = None,
        sources: Optional[str] = None,
        concepts: Optional[str] = None,
        description: Optional[str] = None
    ) -> Reference:
        """
        Cria uma nova referência.
        
        Args:
            title: Título da referência
            category: Categoria
            subject: Assunto
            sources: Fontes (JSON array como string)
            concepts: Conceitos (JSON array como string)
            description: Descrição
            
        Returns:
            Reference criada
        """
        reference = Reference(
            title=title,
            category=category,
            subject=subject,
            sources=sources,
            concepts=concepts,
            description=description
        )
        
        self.db.add(reference)
        await self.db.flush()
        await self.db.refresh(reference)
        
        return reference
    
    async def get_by_id(self, reference_id: UUID) -> Optional[Reference]:
        """
        Busca referência por ID.
        
        Args:
            reference_id: ID da referência
            
        Returns:
            Reference ou None se não encontrada
        """
        result = await self.db.execute(
            select(Reference).where(Reference.id == reference_id)
        )
        return result.scalar_one_or_none()
    
    async def list_all(
        self,
        skip: int = 0,
        limit: int = 100,
        category: Optional[str] = None
    ) -> List[Reference]:
        """
        Lista referências, opcionalmente filtradas por categoria.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros
            category: Categoria para filtrar (opcional)
            
        Returns:
            Lista de referências
        """
        stmt = select(Reference)
        
        if category:
            stmt = stmt.where(Reference.category == category)
        
        stmt = stmt.order_by(Reference.created_at.desc()).offset(skip).limit(limit)
        result = await self.db.execute(stmt)
        
        return list(result.scalars().all())
    
    async def update(
        self,
        reference_id: UUID,
        title: Optional[str] = None,
        category: Optional[str] = None,
        subject: Optional[str] = None,
        sources: Optional[str] = None,
        concepts: Optional[str] = None,
        description: Optional[str] = None
    ) -> Reference:
        """
        Atualiza uma referência.
        
        Args:
            reference_id: ID da referência
            title: Título (opcional)
            category: Categoria (opcional)
            subject: Assunto (opcional)
            sources: Fontes (opcional)
            concepts: Conceitos (opcional)
            description: Descrição (opcional)
            
        Returns:
            Reference atualizada
            
        Raises:
            ReferenceNotFoundError: Se referência não encontrada
        """
        reference = await self.get_by_id(reference_id)
        if not reference:
            raise ReferenceNotFoundError(str(reference_id))
        
        if title is not None:
            reference.title = title
        if category is not None:
            reference.category = category
        if subject is not None:
            reference.subject = subject
        if sources is not None:
            reference.sources = sources
        if concepts is not None:
            reference.concepts = concepts
        if description is not None:
            reference.description = description
        
        await self.db.flush()
        await self.db.refresh(reference)
        
        return reference
    
    async def delete(self, reference_id: UUID) -> bool:
        """
        Deleta uma referência.
        
        Args:
            reference_id: ID da referência
            
        Returns:
            True se deletada
            
        Raises:
            ReferenceNotFoundError: Se referência não encontrada
        """
        reference = await self.get_by_id(reference_id)
        if not reference:
            raise ReferenceNotFoundError(str(reference_id))
        
        await self.db.delete(reference)
        await self.db.flush()
        
        return True

