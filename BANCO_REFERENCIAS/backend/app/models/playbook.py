"""
Model SQLAlchemy para playbooks (templates de análise).
"""
from sqlalchemy import Column, String, Text, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.core.database import Base


class Playbook(Base):
    """Model de playbook (template de análise)."""
    
    __tablename__ = "playbooks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    template = Column(Text, nullable=False)  # Template Markdown com variáveis
    category = Column(String(100), index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(String(255), nullable=True, index=True)  # Multi-tenant
    
    def __repr__(self) -> str:
        return f"<Playbook(id={self.id}, name='{self.name}')>"

