"""
Service para gestão de projetos.
Business logic para operações de projetos.
"""
from typing import List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.core.exceptions import ProjectNotFoundError
import logging

logger = logging.getLogger(__name__)


class ProjectService:
    """Service para operações de projetos."""
    
    def __init__(self, db: AsyncSession):
        """
        Inicializa service com sessão do banco.
        
        Args:
            db: Sessão assíncrona do SQLAlchemy
        """
        self.db = db
        self.project_repo = ProjectRepository(db)
    
    async def create_project(self, data: ProjectCreate) -> ProjectResponse:
        """
        Cria um novo projeto.
        
        Args:
            data: Dados do projeto
            
        Returns:
            ProjectResponse do projeto criado
        """
        project = await self.project_repo.create(
            name=data.name,
            description=data.description,
            documentation_path=data.documentation_path
        )
        
        await self.db.commit()
        logger.info(f"Projeto criado: {project.id} - {project.name}")
        
        return ProjectResponse.model_validate(project)
    
    async def get_project(self, project_id: UUID) -> ProjectResponse:
        """
        Busca projeto por ID.
        
        Args:
            project_id: ID do projeto
            
        Returns:
            ProjectResponse
            
        Raises:
            ProjectNotFoundError: Se projeto não encontrado
        """
        project = await self.project_repo.get_by_id(project_id)
        if not project:
            raise ProjectNotFoundError(str(project_id))
        
        return ProjectResponse.model_validate(project)
    
    async def list_projects(self, skip: int = 0, limit: int = 100) -> List[ProjectResponse]:
        """
        Lista projetos.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros
            
        Returns:
            Lista de ProjectResponse
        """
        projects = await self.project_repo.list_all(skip=skip, limit=limit)
        return [ProjectResponse.model_validate(proj) for proj in projects]
    
    async def update_project(
        self,
        project_id: UUID,
        data: ProjectUpdate
    ) -> ProjectResponse:
        """
        Atualiza um projeto.
        
        Args:
            project_id: ID do projeto
            data: Dados para atualização
            
        Returns:
            ProjectResponse atualizado
            
        Raises:
            ProjectNotFoundError: Se projeto não encontrado
        """
        project = await self.project_repo.update(
            project_id=project_id,
            name=data.name,
            description=data.description,
            documentation_path=data.documentation_path
        )
        
        await self.db.commit()
        logger.info(f"Projeto atualizado: {project.id} - {project.name}")
        
        return ProjectResponse.model_validate(project)
    
    async def delete_project(self, project_id: UUID) -> bool:
        """
        Deleta um projeto.
        
        Args:
            project_id: ID do projeto
            
        Returns:
            True se deletado com sucesso
            
        Raises:
            ProjectNotFoundError: Se projeto não encontrado
        """
        deleted = await self.project_repo.delete(project_id)
        await self.db.commit()
        
        logger.info(f"Projeto deletado: {project_id}")
        return deleted

