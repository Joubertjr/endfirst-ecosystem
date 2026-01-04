"""
Service para gestão de playbooks.
Business logic para operações de playbooks.
"""
from typing import Optional, List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.playbook_repository import PlaybookRepository
from app.core.playbook_parser import PlaybookParser
from app.schemas.playbook import PlaybookCreate, PlaybookUpdate, PlaybookResponse
from app.core.exceptions import ValidationError, PlaybookNotFoundError
import logging

logger = logging.getLogger(__name__)


class PlaybookService:
    """Service para operações de playbooks."""
    
    def __init__(self, db: AsyncSession):
        """
        Inicializa service com sessão do banco.
        
        Args:
            db: Sessão assíncrona do SQLAlchemy
        """
        self.db = db
        self.playbook_repo = PlaybookRepository(db)
        self.parser = PlaybookParser()
    
    async def create_playbook(self, data: PlaybookCreate, user_id: Optional[str] = None) -> PlaybookResponse:
        """
        Cria um novo playbook.
        
        Args:
            data: Dados do playbook
            user_id: ID do usuário
            
        Returns:
            PlaybookResponse do playbook criado
            
        Raises:
            ValidationError: Se template inválido
        """
        # Valida template
        if not self.parser.validate_template(data.template):
            raise ValidationError("Template inválido. Verifique o formato das variáveis.")
        
        playbook = await self.playbook_repo.create(
            name=data.name,
            description=data.description,
            template=data.template,
            category=data.category,
            is_active=data.is_active,
            user_id=user_id
        )
        
        await self.db.commit()
        logger.info(f"Playbook criado: {playbook.id} - {playbook.name}")
        
        return PlaybookResponse.model_validate(playbook)
    
    async def get_playbook(self, playbook_id: UUID, user_id: Optional[str] = None) -> PlaybookResponse:
        """
        Busca playbook por ID.
        
        Args:
            playbook_id: ID do playbook
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            PlaybookResponse
            
        Raises:
            PlaybookNotFoundError: Se playbook não encontrado
        """
        playbook = await self.playbook_repo.get_by_id(playbook_id, user_id=user_id)
        if not playbook:
            raise PlaybookNotFoundError(str(playbook_id))
        
        return PlaybookResponse.model_validate(playbook)
    
    async def list_playbooks(
        self,
        skip: int = 0,
        limit: int = 100,
        category: Optional[str] = None,
        is_active: Optional[bool] = None,
        user_id: Optional[str] = None
    ) -> List[PlaybookResponse]:
        """
        Lista playbooks, opcionalmente filtrados.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros
            category: Categoria para filtrar (opcional)
            is_active: Filtrar por status ativo (opcional)
            user_id: ID do usuário para filtrar (opcional)
            
        Returns:
            Lista de PlaybookResponse
        """
        playbooks = await self.playbook_repo.list_all(
            skip=skip,
            limit=limit,
            category=category,
            is_active=is_active,
            user_id=user_id
        )
        return [PlaybookResponse.model_validate(pb) for pb in playbooks]
    
    async def update_playbook(
        self,
        playbook_id: UUID,
        data: PlaybookUpdate,
        user_id: Optional[str] = None
    ) -> PlaybookResponse:
        """
        Atualiza um playbook.
        
        Args:
            playbook_id: ID do playbook
            data: Dados para atualização
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            PlaybookResponse atualizado
            
        Raises:
            PlaybookNotFoundError: Se playbook não encontrado
            ValidationError: Se template inválido
        """
        # Valida template se fornecido
        if data.template is not None:
            if not self.parser.validate_template(data.template):
                raise ValidationError("Template inválido. Verifique o formato das variáveis.")
        
        playbook = await self.playbook_repo.update(
            playbook_id=playbook_id,
            name=data.name,
            description=data.description,
            template=data.template,
            category=data.category,
            is_active=data.is_active,
            user_id=user_id
        )
        
        await self.db.commit()
        logger.info(f"Playbook atualizado: {playbook.id} - {playbook.name}")
        
        return PlaybookResponse.model_validate(playbook)
    
    async def delete_playbook(self, playbook_id: UUID, user_id: Optional[str] = None) -> bool:
        """
        Deleta um playbook.
        
        Args:
            playbook_id: ID do playbook
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            True se deletado com sucesso
            
        Raises:
            PlaybookNotFoundError: Se playbook não encontrado
        """
        deleted = await self.playbook_repo.delete(playbook_id, user_id=user_id)
        await self.db.commit()
        
        logger.info(f"Playbook deletado: {playbook_id}")
        return deleted
    
    def extract_variables(self, playbook_id: UUID, user_id: Optional[str] = None) -> List[str]:
        """
        Extrai variáveis de um playbook.
        
        Args:
            playbook_id: ID do playbook
            user_id: ID do usuário (opcional)
            
        Returns:
            Lista de nomes de variáveis
            
        Note:
            Esta função é síncrona porque não precisa de DB, apenas lê o template.
            O playbook deve ser obtido primeiro.
        """
        # Esta função deve ser usada após obter o playbook
        # Por enquanto retorna lista vazia, será usado no AnalysisService
        return []

