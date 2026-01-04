"""
Endpoints para gestão de documentos.
"""
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Optional

from app.api.v1.deps import get_db_session, get_current_user_dep
from app.services.document_service import DocumentService
from app.schemas.document import DocumentResponse, DocumentListResponse
from app.core.exceptions import (
    DocumentNotFoundError,
    FileTooLargeError,
    InvalidFileTypeError,
    ValidationError
)

router = APIRouter()


@router.post("", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
async def upload_document(
    file: UploadFile = File(...),
    reference_id: Optional[str] = Form(None),
    project_id: Optional[str] = Form(None),
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Faz upload de documento para Google File Search e salva metadata no PostgreSQL.
    Requer autenticação.
    
    - **file**: Arquivo a ser enviado
    - **reference_id**: ID da referência relacionada (opcional)
    - **project_id**: ID do projeto relacionado (opcional)
    """
    try:
        # Lê conteúdo do arquivo
        content = await file.read()
        
        # Converte IDs se fornecidos
        ref_uuid = UUID(reference_id) if reference_id else None
        proj_uuid = UUID(project_id) if project_id else None
        
        # Upload via service
        service = DocumentService(db)
        document = await service.upload_document(
            file_content=content,
            filename=file.filename,
            user_id=user["user_id"],  # Adiciona user_id
            mime_type=file.content_type,
            reference_id=ref_uuid,
            project_id=proj_uuid
        )
        
        return document
        
    except (FileTooLargeError, InvalidFileTypeError, ValidationError) as e:
        # Exceções de validação já têm status code apropriado
        raise e
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"ID inválido: {str(e)}"
        )
    except DocumentNotFoundError as e:
        # Exceção customizada já tem status code
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao fazer upload: {str(e)}"
        )


@router.get("", response_model=DocumentListResponse)
async def list_documents(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    reference_id: Optional[UUID] = Query(None, description="Filtrar por referência"),
    project_id: Optional[UUID] = Query(None, description="Filtrar por projeto"),
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Lista documentos do usuário autenticado, opcionalmente filtrados por referência ou projeto.
    Requer autenticação.
    
    - **skip**: Número de registros para pular (paginação)
    - **limit**: Número máximo de registros (padrão: 100, máximo: 500)
    - **reference_id**: Filtrar por ID da referência (opcional)
    - **project_id**: Filtrar por ID do projeto (opcional)
    """
    service = DocumentService(db)
    documents = await service.list_documents(
        skip=skip,
        limit=limit,
        user_id=user["user_id"],
        reference_id=reference_id,
        project_id=project_id
    )
    
    return DocumentListResponse(
        total=len(documents),
        documents=documents
    )


@router.get("/{document_id}", response_model=DocumentResponse)
async def get_document(
    document_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Busca documento por ID do usuário autenticado.
    Requer autenticação.
    
    - **document_id**: ID único do documento
    """
    try:
        service = DocumentService(db)
        document = await service.get_document(document_id, user_id=user["user_id"])
        return document
    except DocumentNotFoundError as e:
        # Exceção customizada já tem status code apropriado
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar documento: {str(e)}"
        )


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(
    document_id: UUID,
    db: AsyncSession = Depends(get_db_session),
    user: dict = Depends(get_current_user_dep)
):
    """
    Deleta documento do usuário autenticado.
    Requer autenticação.
    
    - **document_id**: ID único do documento
    """
    try:
        service = DocumentService(db)
        await service.delete_document(document_id, user_id=user["user_id"])
        return None
    except DocumentNotFoundError as e:
        # Exceção customizada já tem status code apropriado
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao deletar documento: {str(e)}"
        )


