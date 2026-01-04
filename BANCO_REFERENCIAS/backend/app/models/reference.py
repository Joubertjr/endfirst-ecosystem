"""
Model SQLAlchemy para referências externas.
"""
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.core.database import Base


class Reference(Base):
    """Model de referência externa (2.400+ fontes)."""
    
    __tablename__ = "references"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(500), nullable=False)
    category = Column(String(100), index=True)
    subject = Column(Text)
    sources = Column(Text)  # JSON array como string
    concepts = Column(Text)  # JSON array como string
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self) -> str:
        return f"<Reference(id={self.id}, title='{self.title}')>"


