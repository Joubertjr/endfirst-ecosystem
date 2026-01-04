"""
Endpoints para gestão de playbooks.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Optional

from app.api.v1.deps import get_db_session, get_current_user_dep
from app.services.playbook_service import PlaybookService
from app.schemas.playbook import (
    PlaybookCreate,
    PlaybookUpdate,
    PlaybookResponse,
    PlaybookListResponse
)
from app.core.exceptions import PlaybookNotFoundError, ValidationError

router = APIRouter()


@router.post("", response_model=PlaybookResponse, status_code=status.HTTP_201_CREATED)
async def create_playbook(
    data: PlaybookCreate,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Cria um novo playbook.
    Requer autenticação.
    
    - **name**: Nome do playbook
    - **description**: Descrição (opcional)
    - **template**: Template Markdown com variáveis {{var_name}}
    - **category**: Categoria (opcional)
    - **is_active**: Se está ativo (padrão: true)
    """
    try:
        service = PlaybookService(db)
        playbook = await service.create_playbook(data, user_id=user["user_id"])
        return playbook
    except ValidationError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar playbook: {str(e)}"
        )


@router.get("", response_model=PlaybookListResponse)
async def list_playbooks(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    category: Optional[str] = Query(None, description="Filtrar por categoria"),
    is_active: Optional[bool] = Query(None, description="Filtrar por status ativo"),
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Lista playbooks, opcionalmente filtrados por categoria e status.
    Requer autenticação.
    
    - **skip**: Número de registros para pular (paginação)
    - **limit**: Número máximo de registros (padrão: 100, máximo: 500)
    - **category**: Categoria para filtrar (opcional)
    - **is_active**: Filtrar por status ativo (opcional)
    """
    service = PlaybookService(db)
    playbooks = await service.list_playbooks(
        skip=skip,
        limit=limit,
        category=category,
        is_active=is_active,
        user_id=user["user_id"]
    )
    
    return PlaybookListResponse(
        total=len(playbooks),
        playbooks=playbooks
    )


@router.get("/{playbook_id}", response_model=PlaybookResponse)
async def get_playbook(
    playbook_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Busca playbook por ID.
    Requer autenticação.
    
    - **playbook_id**: ID único do playbook
    """
    try:
        service = PlaybookService(db)
        playbook = await service.get_playbook(playbook_id, user_id=user["user_id"])
        return playbook
    except PlaybookNotFoundError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar playbook: {str(e)}"
        )


@router.put("/{playbook_id}", response_model=PlaybookResponse)
async def update_playbook(
    playbook_id: UUID,
    data: PlaybookUpdate,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Atualiza um playbook.
    Requer autenticação.
    
    - **playbook_id**: ID único do playbook
    - **data**: Dados para atualização
    """
    try:
        service = PlaybookService(db)
        playbook = await service.update_playbook(playbook_id, data, user_id=user["user_id"])
        return playbook
    except (PlaybookNotFoundError, ValidationError) as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar playbook: {str(e)}"
        )


@router.delete("/{playbook_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_playbook(
    playbook_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Deleta um playbook.
    Requer autenticação.
    
    - **playbook_id**: ID único do playbook
    """
    try:
        service = PlaybookService(db)
        await service.delete_playbook(playbook_id, user_id=user["user_id"])
        return None
    except PlaybookNotFoundError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao deletar playbook: {str(e)}"
        )

