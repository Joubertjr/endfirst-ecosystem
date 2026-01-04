"""
Schemas Pydantic para Analysis (DTOs).
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from uuid import UUID


class AnalysisBase(BaseModel):
    """Schema base para Analysis."""
    playbook_id: UUID = Field(..., description="ID do playbook usado")
    reference_id: Optional[UUID] = Field(None, description="ID da referência relacionada")
    project_id: Optional[UUID] = Field(None, description="ID do projeto relacionado")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Parâmetros para o template")
    status: str = Field("pending", description="Status da análise")


class AnalysisCreate(AnalysisBase):
    """Schema para criação de análise."""
    pass


class AnalysisResponse(AnalysisBase):
    """Schema para resposta de análise."""
    id: UUID
    result: Optional[Dict[str, Any]] = Field(None, description="Resultado da análise")
    error_message: Optional[str] = Field(None, description="Mensagem de erro se falhou")
    user_id: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class AnalysisListResponse(BaseModel):
    """Schema para lista de análises."""
    total: int = Field(..., description="Total de análises")
    analyses: list[AnalysisResponse] = Field(..., description="Lista de análises")

