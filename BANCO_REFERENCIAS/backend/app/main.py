"""
Banco de Referências - Backend API
Sistema de gestão de conhecimento com RAG usando Google Gemini File Search

Stack: FastAPI + PostgreSQL (Neon) + Google File Search
Arquitetura: Repository Pattern + Service Layer + DTO Pattern
"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import make_asgi_app
from app.core.config import settings
from app.core.database import engine, Base

# Configurar logging
logging.basicConfig(
    level=logging.INFO if settings.DEBUG else logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# Importar models para criar tabelas
from app.models import Document, Reference, Project, Analysis, Playbook

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
    try:
        # Cria tabelas do banco de dados
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("✅ Banco de dados inicializado!")
    except Exception as e:
        logger.error(f"⚠️ Erro ao inicializar banco: {e}", exc_info=True)
        # Não quebra a aplicação se DB não estiver disponível ainda
    
    # Conecta ao cache
    from app.core.cache import cache_repo
    await cache_repo.connect()


@app.on_event("shutdown")
async def shutdown_event():
    """Executado ao encerrar a aplicação."""
    from app.core.cache import cache_repo
    await cache_repo.disconnect()


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
            "database": "PostgreSQL (Docker)",
            "vector_db": "Google File Search",
            "python": "3.12+"
        },
        "docs": "/api/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# Routers da API
from app.api.v1.router import api_router
app.include_router(api_router, prefix="/api/v1")

# Métricas Prometheus
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )

