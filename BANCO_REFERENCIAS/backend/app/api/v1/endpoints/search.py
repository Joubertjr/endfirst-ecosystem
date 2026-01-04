"""
Endpoints para busca semântica RAG.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.deps import get_db_session, get_optional_user_dep
from app.services.search_service import SearchService
from app.schemas.search import SearchRequest, SearchResponse
from app.core.exceptions import InvalidQueryError, ValidationError, GoogleFileSearchError

router = APIRouter()


@router.post("", response_model=SearchResponse)
async def search_documents(
    request: SearchRequest,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_optional_user_dep)
):
    """
    Busca semântica usando RAG no Google File Search.
    Autenticação opcional - se autenticado, busca apenas nos documentos do usuário.
    
    - **query**: Query de busca em linguagem natural (mínimo 3 caracteres)
    - **max_results**: Número máximo de resultados (padrão: 10, máximo: 50)
    """
    try:
        service = SearchService(db)
        # Filtra busca por user_id se autenticado
        user_id = user["user_id"] if user else None
        result = await service.search_semantic(request, user_id=user_id)
        return result
    except (InvalidQueryError, ValidationError) as e:
        # Exceções de validação já têm status code apropriado
        raise e
    except GoogleFileSearchError as e:
        # Exceção customizada já tem status code
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro na busca: {str(e)}"
        )


