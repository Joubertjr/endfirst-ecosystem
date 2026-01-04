"""
Banco de Referências - Backend API
Sistema de gestão de conhecimento com RAG usando Google Gemini File Search

Stack: FastAPI + PostgreSQL (Neon) + Google File Search
Arquitetura: Repository Pattern + Service Layer + DTO Pattern
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base

# Importar models para criar tabelas
from app.models import Document, Reference, Project, Analysis

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Sistema de gestão de conhecimento com RAG (Retrieval-Augmented Generation)",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Executado ao iniciar a aplicação."""
    # Cria tabelas do banco de dados
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Banco de dados inicializado!")


@app.get("/")
async def root():
    """Informações da API"""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "ok",
        "message": "Sistema de gestão de conhecimento com RAG",
        "stack": {
            "backend": "FastAPI",
            "database": "PostgreSQL (Neon)",
            "vector_db": "Google File Search",
            "python": "3.12+"
        },
        "docs": "/api/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# TODO: Adicionar routers
# from app.api.v1.endpoints import documents, search, references, projects, analysis
# app.include_router(documents.router, prefix="/api/v1/documents", tags=["documents"])
# app.include_router(search.router, prefix="/api/v1/search", tags=["search"])
# app.include_router(references.router, prefix="/api/v1/references", tags=["references"])
# app.include_router(projects.router, prefix="/api/v1/projects", tags=["projects"])
# app.include_router(analysis.router, prefix="/api/v1/analysis", tags=["analysis"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )

