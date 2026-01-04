"""
Model SQLAlchemy para documentos.
"""
from sqlalchemy import Column, String, BigInteger, DateTime, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.core.database import Base


class Document(Base):
    """Model de documento indexado no Google File Search."""
    
    __tablename__ = "documents"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    google_file_id = Column(String(255), unique=True, nullable=False, index=True)
    filename = Column(String(500), nullable=False)
    file_type = Column(String(50))
    file_size_bytes = Column(BigInteger)
    upload_date = Column(DateTime(timezone=True), server_default=func.now())
    document_metadata = Column(JSON, name="metadata")  # name="metadata" mantém nome no DB
    status = Column(String(50), default="active")
    
    # User ID (Clerk user ID) - Multi-tenant
    user_id = Column(String, nullable=True, index=True)  # Nullable para permitir migração
    
    # Foreign keys (opcional)
    reference_id = Column(UUID(as_uuid=True), ForeignKey("references.id"), nullable=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    
    def __repr__(self) -> str:
        return f"<Document(id={self.id}, filename='{self.filename}')>"


