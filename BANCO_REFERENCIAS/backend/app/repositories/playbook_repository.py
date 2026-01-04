"""
Repository para playbooks (PostgreSQL).
"""
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.models.playbook import Playbook
from app.core.exceptions import PlaybookNotFoundError


class PlaybookRepository:
    """Repository para operações CRUD de playbooks."""
    
    def __init__(self, db: AsyncSession):
        """
        Inicializa repository com sessão do banco.
        
        Args:
            db: Sessão assíncrona do SQLAlchemy
        """
        self.db = db
    
    async def create(
        self,
        name: str,
        description: Optional[str] = None,
        template: str = "",
        category: Optional[str] = None,
        is_active: bool = True,
        user_id: Optional[str] = None
    ) -> Playbook:
        """
        Cria um novo playbook.
        
        Args:
            name: Nome do playbook
            description: Descrição
            template: Template Markdown
            category: Categoria
            is_active: Se está ativo
            user_id: ID do usuário
            
        Returns:
            Playbook criado
        """
        playbook = Playbook(
            name=name,
            description=description,
            template=template,
            category=category,
            is_active=is_active,
            user_id=user_id
        )
        
        self.db.add(playbook)
        await self.db.flush()
        await self.db.refresh(playbook)
        
        return playbook
    
    async def get_by_id(self, playbook_id: UUID, user_id: Optional[str] = None) -> Optional[Playbook]:
        """
        Busca playbook por ID.
        
        Args:
            playbook_id: ID do playbook
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            Playbook ou None se não encontrado
        """
        stmt = select(Playbook).where(Playbook.id == playbook_id)
        
        if user_id:
            stmt = stmt.where(Playbook.user_id == user_id)
        
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def list_all(
        self,
        skip: int = 0,
        limit: int = 100,
        category: Optional[str] = None,
        is_active: Optional[bool] = None,
        user_id: Optional[str] = None
    ) -> List[Playbook]:
        """
        Lista playbooks, opcionalmente filtrados.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros
            category: Categoria para filtrar (opcional)
            is_active: Filtrar por status ativo (opcional)
            user_id: ID do usuário para filtrar (opcional)
            
        Returns:
            Lista de playbooks
        """
        stmt = select(Playbook)
        
        if user_id:
            stmt = stmt.where(Playbook.user_id == user_id)
        
        if category:
            stmt = stmt.where(Playbook.category == category)
        
        if is_active is not None:
            stmt = stmt.where(Playbook.is_active == is_active)
        
        stmt = stmt.order_by(Playbook.created_at.desc()).offset(skip).limit(limit)
        result = await self.db.execute(stmt)
        
        return list(result.scalars().all())
    
    async def update(
        self,
        playbook_id: UUID,
        name: Optional[str] = None,
        description: Optional[str] = None,
        template: Optional[str] = None,
        category: Optional[str] = None,
        is_active: Optional[bool] = None,
        user_id: Optional[str] = None
    ) -> Playbook:
        """
        Atualiza um playbook.
        
        Args:
            playbook_id: ID do playbook
            name: Nome (opcional)
            description: Descrição (opcional)
            template: Template (opcional)
            category: Categoria (opcional)
            is_active: Status ativo (opcional)
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            Playbook atualizado
            
        Raises:
            PlaybookNotFoundError: Se playbook não encontrado
        """
        playbook = await self.get_by_id(playbook_id, user_id=user_id)
        if not playbook:
            raise PlaybookNotFoundError(str(playbook_id))
        
        if name is not None:
            playbook.name = name
        if description is not None:
            playbook.description = description
        if template is not None:
            playbook.template = template
        if category is not None:
            playbook.category = category
        if is_active is not None:
            playbook.is_active = is_active
        
        await self.db.flush()
        await self.db.refresh(playbook)
        
        return playbook
    
    async def delete(self, playbook_id: UUID, user_id: Optional[str] = None) -> bool:
        """
        Deleta um playbook.
        
        Args:
            playbook_id: ID do playbook
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            True se deletado
            
        Raises:
            PlaybookNotFoundError: Se playbook não encontrado
        """
        playbook = await self.get_by_id(playbook_id, user_id=user_id)
        if not playbook:
            raise PlaybookNotFoundError(str(playbook_id))
        
        await self.db.delete(playbook)
        await self.db.flush()
        
        return True

