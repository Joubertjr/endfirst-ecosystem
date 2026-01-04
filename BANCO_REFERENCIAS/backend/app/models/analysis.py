"""
Model SQLAlchemy para análises com playbooks.
"""
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.core.database import Base


class Analysis(Base):
    """Model de análise genérica com playbooks."""
    
    __tablename__ = "analyses"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    playbook_id = Column(UUID(as_uuid=True), ForeignKey("playbooks.id"), nullable=False, index=True)
    reference_id = Column(UUID(as_uuid=True), ForeignKey("references.id"), nullable=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    status = Column(String(50), default="pending", index=True)
    parameters = Column(JSON)  # Parâmetros para o template
    result = Column(JSON)  # Resultados da análise
    error_message = Column(Text)
    user_id = Column(String(255), nullable=True, index=True)  # Multi-tenant
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self) -> str:
        return f"<Analysis(id={self.id}, playbook_id={self.playbook_id}, status='{self.status}')>"


