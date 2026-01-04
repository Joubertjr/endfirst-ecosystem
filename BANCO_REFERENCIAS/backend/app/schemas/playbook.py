"""
Schemas Pydantic para Playbook (DTOs).
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID


class PlaybookBase(BaseModel):
    """Schema base para Playbook."""
    name: str = Field(..., description="Nome do playbook", max_length=255)
    description: Optional[str] = Field(None, description="Descrição do playbook")
    template: str = Field(..., description="Template Markdown com variáveis")
    category: Optional[str] = Field(None, description="Categoria", max_length=100)
    is_active: bool = Field(True, description="Se playbook está ativo")


class PlaybookCreate(PlaybookBase):
    """Schema para criação de playbook."""
    pass


class PlaybookUpdate(BaseModel):
    """Schema para atualização de playbook."""
    name: Optional[str] = Field(None, description="Nome do playbook", max_length=255)
    description: Optional[str] = Field(None, description="Descrição")
    template: Optional[str] = Field(None, description="Template Markdown")
    category: Optional[str] = Field(None, description="Categoria", max_length=100)
    is_active: Optional[bool] = Field(None, description="Se está ativo")


class PlaybookResponse(PlaybookBase):
    """Schema para resposta de playbook."""
    id: UUID
    user_id: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class PlaybookListResponse(BaseModel):
    """Schema para lista de playbooks."""
    total: int = Field(..., description="Total de playbooks")
    playbooks: list[PlaybookResponse] = Field(..., description="Lista de playbooks")

