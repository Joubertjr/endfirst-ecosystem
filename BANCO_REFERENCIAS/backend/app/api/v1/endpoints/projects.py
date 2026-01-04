"""
Endpoints para gestão de projetos.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.api.v1.deps import get_db_session, get_current_user_dep
from app.services.project_service import ProjectService
from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse,
    ProjectListResponse
)
from app.core.exceptions import ProjectNotFoundError

router = APIRouter()


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(
    data: ProjectCreate,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Cria um novo projeto.
    Requer autenticação.
    
    - **name**: Nome do projeto
    - **description**: Descrição (opcional)
    - **documentation_path**: Caminho da documentação (opcional)
    """
    try:
        service = ProjectService(db)
        project = await service.create_project(data)
        return project
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar projeto: {str(e)}"
        )


@router.get("", response_model=ProjectListResponse)
async def list_projects(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Lista projetos.
    Requer autenticação.
    
    - **skip**: Número de registros para pular (paginação)
    - **limit**: Número máximo de registros (padrão: 100, máximo: 500)
    """
    service = ProjectService(db)
    projects = await service.list_projects(skip=skip, limit=limit)
    
    return ProjectListResponse(
        total=len(projects),
        projects=projects
    )


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Busca projeto por ID.
    Requer autenticação.
    
    - **project_id**: ID único do projeto
    """
    try:
        service = ProjectService(db)
        project = await service.get_project(project_id)
        return project
    except ProjectNotFoundError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar projeto: {str(e)}"
        )


@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: UUID,
    data: ProjectUpdate,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Atualiza um projeto.
    Requer autenticação.
    
    - **project_id**: ID único do projeto
    - **data**: Dados para atualização
    """
    try:
        service = ProjectService(db)
        project = await service.update_project(project_id, data)
        return project
    except ProjectNotFoundError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar projeto: {str(e)}"
        )


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Deleta um projeto.
    Requer autenticação.
    
    - **project_id**: ID único do projeto
    """
    try:
        service = ProjectService(db)
        await service.delete_project(project_id)
        return None
    except ProjectNotFoundError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao deletar projeto: {str(e)}"
        )

