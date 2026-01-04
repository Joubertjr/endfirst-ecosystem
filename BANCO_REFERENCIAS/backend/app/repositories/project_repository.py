"""
Repository para projetos (PostgreSQL).
"""
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.models.project import Project
from app.core.exceptions import ProjectNotFoundError


class ProjectRepository:
    """Repository para operações CRUD de projetos."""
    
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
        documentation_path: Optional[str] = None
    ) -> Project:
        """
        Cria um novo projeto.
        
        Args:
            name: Nome do projeto
            description: Descrição
            documentation_path: Caminho da documentação
            
        Returns:
            Project criado
        """
        project = Project(
            name=name,
            description=description,
            documentation_path=documentation_path
        )
        
        self.db.add(project)
        await self.db.flush()
        await self.db.refresh(project)
        
        return project
    
    async def get_by_id(self, project_id: UUID) -> Optional[Project]:
        """
        Busca projeto por ID.
        
        Args:
            project_id: ID do projeto
            
        Returns:
            Project ou None se não encontrado
        """
        result = await self.db.execute(
            select(Project).where(Project.id == project_id)
        )
        return result.scalar_one_or_none()
    
    async def list_all(self, skip: int = 0, limit: int = 100) -> List[Project]:
        """
        Lista projetos.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros
            
        Returns:
            Lista de projetos
        """
        stmt = select(Project)
        stmt = stmt.order_by(Project.created_at.desc()).offset(skip).limit(limit)
        result = await self.db.execute(stmt)
        
        return list(result.scalars().all())
    
    async def update(
        self,
        project_id: UUID,
        name: Optional[str] = None,
        description: Optional[str] = None,
        documentation_path: Optional[str] = None
    ) -> Project:
        """
        Atualiza um projeto.
        
        Args:
            project_id: ID do projeto
            name: Nome (opcional)
            description: Descrição (opcional)
            documentation_path: Caminho da documentação (opcional)
            
        Returns:
            Project atualizado
            
        Raises:
            ProjectNotFoundError: Se projeto não encontrado
        """
        project = await self.get_by_id(project_id)
        if not project:
            raise ProjectNotFoundError(str(project_id))
        
        if name is not None:
            project.name = name
        if description is not None:
            project.description = description
        if documentation_path is not None:
            project.documentation_path = documentation_path
        
        await self.db.flush()
        await self.db.refresh(project)
        
        return project
    
    async def delete(self, project_id: UUID) -> bool:
        """
        Deleta um projeto.
        
        Args:
            project_id: ID do projeto
            
        Returns:
            True se deletado
            
        Raises:
            ProjectNotFoundError: Se projeto não encontrado
        """
        project = await self.get_by_id(project_id)
        if not project:
            raise ProjectNotFoundError(str(project_id))
        
        await self.db.delete(project)
        await self.db.flush()
        
        return True

