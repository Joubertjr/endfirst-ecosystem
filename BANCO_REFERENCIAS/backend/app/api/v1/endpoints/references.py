"""
Endpoints para gestão de referências.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Optional

from app.api.v1.deps import get_db_session, get_current_user_dep
from app.services.reference_service import ReferenceService
from app.schemas.reference import (
    ReferenceCreate,
    ReferenceUpdate,
    ReferenceResponse,
    ReferenceListResponse
)
from app.core.exceptions import ReferenceNotFoundError

router = APIRouter()


@router.post("", response_model=ReferenceResponse, status_code=status.HTTP_201_CREATED)
async def create_reference(
    data: ReferenceCreate,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Cria uma nova referência.
    Requer autenticação.
    
    - **title**: Título da referência
    - **category**: Categoria (opcional)
    - **subject**: Assunto (opcional)
    - **sources**: Fontes (opcional)
    - **concepts**: Conceitos (opcional)
    - **description**: Descrição (opcional)
    """
    try:
        service = ReferenceService(db)
        reference = await service.create_reference(data)
        return reference
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar referência: {str(e)}"
        )


@router.get("", response_model=ReferenceListResponse)
async def list_references(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    category: Optional[str] = Query(None, description="Filtrar por categoria"),
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Lista referências, opcionalmente filtradas por categoria.
    Requer autenticação.
    
    - **skip**: Número de registros para pular (paginação)
    - **limit**: Número máximo de registros (padrão: 100, máximo: 500)
    - **category**: Categoria para filtrar (opcional)
    """
    service = ReferenceService(db)
    references = await service.list_references(skip=skip, limit=limit, category=category)
    
    return ReferenceListResponse(
        total=len(references),
        references=references
    )


@router.get("/{reference_id}", response_model=ReferenceResponse)
async def get_reference(
    reference_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Busca referência por ID.
    Requer autenticação.
    
    - **reference_id**: ID único da referência
    """
    try:
        service = ReferenceService(db)
        reference = await service.get_reference(reference_id)
        return reference
    except ReferenceNotFoundError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar referência: {str(e)}"
        )


@router.put("/{reference_id}", response_model=ReferenceResponse)
async def update_reference(
    reference_id: UUID,
    data: ReferenceUpdate,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Atualiza uma referência.
    Requer autenticação.
    
    - **reference_id**: ID único da referência
    - **data**: Dados para atualização
    """
    try:
        service = ReferenceService(db)
        reference = await service.update_reference(reference_id, data)
        return reference
    except ReferenceNotFoundError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar referência: {str(e)}"
        )


@router.delete("/{reference_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_reference(
    reference_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Deleta uma referência.
    Requer autenticação.
    
    - **reference_id**: ID único da referência
    """
    try:
        service = ReferenceService(db)
        await service.delete_reference(reference_id)
        return None
    except ReferenceNotFoundError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao deletar referência: {str(e)}"
        )

