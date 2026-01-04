"""
Schemas Pydantic para Reference (DTOs).
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID


class ReferenceBase(BaseModel):
    """Schema base para Reference."""
    title: str = Field(..., description="Título da referência", max_length=500)
    category: Optional[str] = Field(None, description="Categoria", max_length=100)
    subject: Optional[str] = Field(None, description="Assunto")
    sources: Optional[str] = Field(None, description="Fontes (JSON array como string)")
    concepts: Optional[str] = Field(None, description="Conceitos (JSON array como string)")
    description: Optional[str] = Field(None, description="Descrição")


class ReferenceCreate(ReferenceBase):
    """Schema para criação de referência."""
    pass


class ReferenceUpdate(BaseModel):
    """Schema para atualização de referência."""
    title: Optional[str] = Field(None, description="Título da referência", max_length=500)
    category: Optional[str] = Field(None, description="Categoria", max_length=100)
    subject: Optional[str] = Field(None, description="Assunto")
    sources: Optional[str] = Field(None, description="Fontes (JSON array como string)")
    concepts: Optional[str] = Field(None, description="Conceitos (JSON array como string)")
    description: Optional[str] = Field(None, description="Descrição")


class ReferenceResponse(ReferenceBase):
    """Schema para resposta de referência."""
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class ReferenceListResponse(BaseModel):
    """Schema para lista de referências."""
    total: int = Field(..., description="Total de referências")
    references: list[ReferenceResponse] = Field(..., description="Lista de referências")

