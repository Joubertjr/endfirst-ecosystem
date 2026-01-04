"""
Schemas Pydantic para Document (DTOs).
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID


class DocumentBase(BaseModel):
    """Schema base para Document."""
    filename: str = Field(..., description="Nome do arquivo")
    file_type: Optional[str] = Field(None, description="Tipo do arquivo")
    file_size_bytes: Optional[int] = Field(None, description="Tamanho em bytes")
    reference_id: Optional[UUID] = Field(None, description="ID da referência relacionada")
    project_id: Optional[UUID] = Field(None, description="ID do projeto relacionado")


class DocumentCreate(DocumentBase):
    """Schema para criação de documento."""
    google_file_id: str = Field(..., description="ID do arquivo no Google File Search")


class DocumentResponse(DocumentBase):
    """Schema para resposta de documento."""
    id: UUID
    google_file_id: str
    upload_date: datetime
    status: str
    document_metadata: Optional[dict] = None
    
    class Config:
        from_attributes = True
        populate_by_name = True
    
    class Config:
        from_attributes = True


class DocumentListResponse(BaseModel):
    """Schema para lista de documentos."""
    total: int
    documents: list[DocumentResponse]


