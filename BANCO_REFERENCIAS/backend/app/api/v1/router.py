"""
Router principal da API v1.
Agrega todos os endpoints.
"""
from fastapi import APIRouter

from app.api.v1.endpoints import documents, search, references, projects, playbooks, analysis

api_router = APIRouter()

# Inclui routers de cada módulo
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(search.router, prefix="/search", tags=["search"])
api_router.include_router(references.router, prefix="/references", tags=["references"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(playbooks.router, prefix="/playbooks", tags=["playbooks"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])


