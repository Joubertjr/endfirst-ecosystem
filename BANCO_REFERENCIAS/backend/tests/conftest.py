"""
Fixtures compartilhadas para testes.
"""
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from uuid import uuid4
from httpx import AsyncClient
from typing import AsyncGenerator

from app.core.config import settings
from app.core.database import Base, get_db, AsyncSessionLocal
from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.repositories.vector_repository import VectorRepository
from app.main import app


# Base para models de teste
TestBase = declarative_base()


@pytest.fixture
async def test_db_engine():
    """Cria engine de banco de dados para testes (SQLite in-memory)."""
    # SQLite em memória para testes rápidos
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        echo=False,
        future=True
    )
    
    # Cria todas as tabelas
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    # Limpa após testes
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    
    await engine.dispose()


@pytest.fixture
async def test_db_session(test_db_engine) -> AsyncGenerator[AsyncSession, None]:
    """Cria sessão de banco de dados para testes."""
    async_session_maker = async_sessionmaker(
        test_db_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    
    async with async_session_maker() as session:
        yield session


@pytest.fixture
async def override_get_db(test_db_session: AsyncSession):
    """Override da dependency get_db para usar sessão de teste."""
    async def _get_test_db():
        yield test_db_session
    
    app.dependency_overrides[get_db] = _get_test_db
    yield
    app.dependency_overrides.clear()


@pytest.fixture
async def async_client(override_get_db) -> AsyncGenerator[AsyncClient, None]:
    """Cliente HTTP assíncrono para testes de integração."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
def mock_vector_repository():
    """Mock do VectorRepository para testes."""
    repo = MagicMock(spec=VectorRepository)
    
    # Mock para upload_document
    repo.upload_document = MagicMock(return_value={
        "file_id": "test_file_id_123",
        "operation_name": "operations/test_operation"
    })
    
    # Mock para delete_file
    repo.delete_file = MagicMock(return_value=True)
    
    # Mock para search_semantic
    repo.search_semantic = MagicMock(return_value={
        "answer": "Esta é uma resposta de teste",
        "sources": ["documento1.pdf", "documento2.pdf"]
    })
    
    return repo


@pytest.fixture
def mock_db_session():
    """Mock de sessão do banco de dados."""
    session = AsyncMock(spec=AsyncSession)
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.close = AsyncMock()
    return session


@pytest.fixture
def mock_document_repository():
    """Mock do DocumentRepository."""
    return MagicMock(spec=DocumentRepository)


@pytest.fixture
def sample_document():
    """Documento de exemplo para testes."""
    return Document(
        id=uuid4(),
        google_file_id="test_file_id_123",
        filename="test_document.pdf",
        file_type="application/pdf",
        file_size_bytes=1024,
        status="active",
        user_id="test_user_123"
    )


@pytest.fixture
def sample_file_content():
    """Conteúdo de arquivo de exemplo para testes."""
    return b"Este é um arquivo de teste para upload"


@pytest.fixture
def sample_file_content_pdf():
    """Conteúdo PDF de exemplo para testes."""
    # PDF mínimo válido
    return b"%PDF-1.4\n1 0 obj\n<<\n/Type /Catalog\n>>\nendobj\nxref\n0 1\ntrailer\n<<\n/Root 1 0 R\n>>\n%%EOF"


@pytest.fixture
def mock_uuid():
    """Mock de UUID para testes."""
    test_uuid = uuid4()
    with patch('uuid.uuid4', return_value=test_uuid):
        yield test_uuid


@pytest.fixture
def mock_tempfile():
    """Mock de tempfile para testes."""
    with patch('tempfile.NamedTemporaryFile') as mock:
        mock_file = MagicMock()
        mock_file.name = "/tmp/test_file.pdf"
        mock_file.__enter__ = MagicMock(return_value=mock_file)
        mock_file.__exit__ = MagicMock(return_value=None)
        mock.return_value = mock_file
        yield mock_file


# Configuração de ambiente de testes
@pytest.fixture(autouse=True)
def setup_test_environment(monkeypatch):
    """Configura ambiente de testes."""
    # Mock variáveis de ambiente necessárias
    monkeypatch.setenv("GEMINI_API_KEY", "test_api_key")
    monkeypatch.setenv("FILE_STORE_ID", "test_store_id")
    monkeypatch.setenv("DATABASE_URL", "sqlite+aiosqlite:///:memory:")
    # Clerk não configurado para testes (modo desenvolvimento)
    monkeypatch.setenv("CLERK_SECRET_KEY", "")
