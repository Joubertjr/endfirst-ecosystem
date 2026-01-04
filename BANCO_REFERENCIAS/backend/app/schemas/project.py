"""
Schemas Pydantic para Project (DTOs).
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID


class ProjectBase(BaseModel):
    """Schema base para Project."""
    name: str = Field(..., description="Nome do projeto", max_length=255)
    description: Optional[str] = Field(None, description="Descrição do projeto")
    documentation_path: Optional[str] = Field(None, description="Caminho da documentação")


class ProjectCreate(ProjectBase):
    """Schema para criação de projeto."""
    pass


class ProjectUpdate(BaseModel):
    """Schema para atualização de projeto."""
    name: Optional[str] = Field(None, description="Nome do projeto", max_length=255)
    description: Optional[str] = Field(None, description="Descrição do projeto")
    documentation_path: Optional[str] = Field(None, description="Caminho da documentação")


class ProjectResponse(ProjectBase):
    """Schema para resposta de projeto."""
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class ProjectListResponse(BaseModel):
    """Schema para lista de projetos."""
    total: int = Field(..., description="Total de projetos")
    projects: list[ProjectResponse] = Field(..., description="Lista de projetos")

