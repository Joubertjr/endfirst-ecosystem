"""
Schemas Pydantic para Search (busca semântica RAG).
"""
from pydantic import BaseModel, Field
from typing import List, Optional


class SearchRequest(BaseModel):
    """Schema para requisição de busca."""
    query: str = Field(..., min_length=3, description="Query de busca em linguagem natural")
    max_results: Optional[int] = Field(10, ge=1, le=50, description="Número máximo de resultados")


class SearchResponse(BaseModel):
    """Schema para resposta de busca."""
    query: str
    answer: str = Field(..., description="Resposta gerada via RAG")
    sources: List[str] = Field(default_factory=list, description="Fontes citadas")
    processing_time_ms: Optional[int] = None


