"""
Endpoints para gestão de análises.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Optional

from app.api.v1.deps import get_db_session, get_current_user_dep
from app.services.analysis_service import AnalysisService
from app.schemas.analysis import (
    AnalysisCreate,
    AnalysisResponse,
    AnalysisListResponse
)
from app.core.exceptions import AnalysisNotFoundError, PlaybookNotFoundError, ValidationError

router = APIRouter()


@router.post("", response_model=AnalysisResponse, status_code=status.HTTP_201_CREATED)
async def create_analysis(
    data: AnalysisCreate,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Cria uma nova análise.
    Requer autenticação.
    
    - **playbook_id**: ID do playbook a usar
    - **parameters**: Parâmetros para o template (opcional)
    - **reference_id**: ID da referência relacionada (opcional)
    - **project_id**: ID do projeto relacionado (opcional)
    """
    try:
        service = AnalysisService(db)
        analysis = await service.create_analysis(data, user_id=user["user_id"])
        return analysis
    except (PlaybookNotFoundError, ValidationError) as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar análise: {str(e)}"
        )


@router.post("/{analysis_id}/trigger", response_model=AnalysisResponse)
async def trigger_analysis(
    analysis_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Dispara execução de uma análise.
    Renderiza template e executa busca semântica.
    Requer autenticação.
    
    - **analysis_id**: ID da análise a executar
    """
    try:
        service = AnalysisService(db)
        analysis = await service.trigger_analysis(analysis_id, user_id=user["user_id"])
        return analysis
    except (AnalysisNotFoundError, PlaybookNotFoundError) as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao executar análise: {str(e)}"
        )


@router.get("", response_model=AnalysisListResponse)
async def list_analyses(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    playbook_id: Optional[UUID] = Query(None, description="Filtrar por playbook"),
    status: Optional[str] = Query(None, description="Filtrar por status (pending, processing, completed, failed)"),
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Lista análises, opcionalmente filtradas por playbook e status.
    Requer autenticação.
    
    - **skip**: Número de registros para pular (paginação)
    - **limit**: Número máximo de registros (padrão: 100, máximo: 500)
    - **playbook_id**: Filtrar por playbook (opcional)
    - **status**: Filtrar por status (opcional)
    """
    service = AnalysisService(db)
    analyses = await service.list_analyses(
        skip=skip,
        limit=limit,
        playbook_id=playbook_id,
        status=status,
        user_id=user["user_id"]
    )
    
    return AnalysisListResponse(
        total=len(analyses),
        analyses=analyses
    )


@router.get("/{analysis_id}", response_model=AnalysisResponse)
async def get_analysis(
    analysis_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Busca análise por ID.
    Requer autenticação.
    
    - **analysis_id**: ID único da análise
    """
    try:
        service = AnalysisService(db)
        analysis = await service.get_analysis(analysis_id, user_id=user["user_id"])
        return analysis
    except AnalysisNotFoundError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar análise: {str(e)}"
        )


@router.delete("/{analysis_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_analysis(
    analysis_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Deleta uma análise.
    Requer autenticação.
    
    - **analysis_id**: ID único da análise
    """
    try:
        service = AnalysisService(db)
        await service.delete_analysis(analysis_id, user_id=user["user_id"])
        return None
    except AnalysisNotFoundError as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao deletar análise: {str(e)}"
        )

