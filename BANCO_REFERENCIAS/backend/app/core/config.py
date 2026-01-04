"""
Configurações da aplicação usando Pydantic Settings.
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configurações da aplicação."""
    
    # Application
    APP_NAME: str = "Banco de Referências API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # Database (PostgreSQL - Docker ou local)
    DATABASE_URL: str = "postgresql+asyncpg://banco_ref:banco_ref_password@postgres:5432/banco_referencias"
    
    # Google Gemini (OBRIGATÓRIO)
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-2.5-flash"
    
    # Google File Search Store
    FILE_STORE_ID: Optional[str] = None  # Será criado automaticamente se None
    
    # CORS
    ALLOWED_ORIGINS: list[str] = ["*"]  # type: ignore
    
    # Authentication (Clerk)
    CLERK_SECRET_KEY: Optional[str] = None  # Secret key do Clerk
    CLERK_PUBLISHABLE_KEY: Optional[str] = None  # Publishable key (para frontend)
    CLERK_FRONTEND_API: Optional[str] = None  # Frontend API URL (opcional)
    
    # Cache (Redis)
    REDIS_URL: Optional[str] = "redis://localhost:6379/0"
    
    # File Upload Limits
    MAX_FILE_SIZE_MB: int = 50  # Tamanho máximo de arquivo em MB
    MAX_FILE_SIZE_BYTES: int = 50 * 1024 * 1024  # 50MB em bytes
    
    # Allowed File Types
    ALLOWED_FILE_TYPES: list[str] = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # .docx
        "application/msword",  # .doc
        "text/plain",  # .txt
        "text/markdown",  # .md
        "application/json",  # .json
    ]
    
    # Search Limits
    MIN_QUERY_LENGTH: int = 3
    MAX_QUERY_LENGTH: int = 500
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Instância global de settings
settings = Settings()

