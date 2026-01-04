"""
Service para gestão de análises.
Business logic para operações de análises.
"""
from typing import Optional, List, Dict, Any
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analysis_repository import AnalysisRepository
from app.repositories.playbook_repository import PlaybookRepository
from app.core.playbook_parser import PlaybookParser
from app.services.search_service import SearchService
from app.schemas.analysis import AnalysisCreate, AnalysisResponse
from app.schemas.search import SearchRequest
from app.core.exceptions import PlaybookNotFoundError, AnalysisNotFoundError, ValidationError
import logging

logger = logging.getLogger(__name__)


class AnalysisService:
    """Service para operações de análises."""
    
    def __init__(self, db: AsyncSession):
        """
        Inicializa service com sessão do banco.
        
        Args:
            db: Sessão assíncrona do SQLAlchemy
        """
        self.db = db
        self.analysis_repo = AnalysisRepository(db)
        self.playbook_repo = PlaybookRepository(db)
        self.parser = PlaybookParser()
        self.search_service = SearchService(db)
    
    async def create_analysis(
        self,
        data: AnalysisCreate,
        user_id: Optional[str] = None
    ) -> AnalysisResponse:
        """
        Cria uma nova análise.
        
        Args:
            data: Dados da análise
            user_id: ID do usuário
            
        Returns:
            AnalysisResponse da análise criada
            
        Raises:
            PlaybookNotFoundError: Se playbook não encontrado
        """
        # Verifica se playbook existe
        playbook = await self.playbook_repo.get_by_id(data.playbook_id, user_id=user_id)
        if not playbook:
            raise PlaybookNotFoundError(str(data.playbook_id))
        
        if not playbook.is_active:
            raise ValidationError("Playbook não está ativo")
        
        analysis = await self.analysis_repo.create(
            playbook_id=data.playbook_id,
            parameters=data.parameters,
            reference_id=data.reference_id,
            project_id=data.project_id,
            user_id=user_id
        )
        
        await self.db.commit()
        logger.info(f"Análise criada: {analysis.id} - playbook_id={data.playbook_id}")
        
        return AnalysisResponse.model_validate(analysis)
    
    async def trigger_analysis(
        self,
        analysis_id: UUID,
        user_id: Optional[str] = None
    ) -> AnalysisResponse:
        """
        Dispara execução de uma análise.
        Renderiza template e executa busca semântica.
        
        Args:
            analysis_id: ID da análise
            user_id: ID do usuário
            
        Returns:
            AnalysisResponse com resultado
            
        Raises:
            AnalysisNotFoundError: Se análise não encontrada
        """
        analysis = await self.analysis_repo.get_by_id(analysis_id, user_id=user_id)
        if not analysis:
            raise AnalysisNotFoundError(str(analysis_id))
        
        # Busca playbook
        playbook = await self.playbook_repo.get_by_id(analysis.playbook_id, user_id=user_id)
        if not playbook:
            raise PlaybookNotFoundError(str(analysis.playbook_id))
        
        try:
            # Atualiza status para processing
            await self.analysis_repo.update(analysis_id, status="processing", user_id=user_id)
            await self.db.commit()
            
            # Renderiza template
            parameters = analysis.parameters or {}
            rendered_query = self.parser.render(playbook.template, parameters)
            
            logger.info(f"Executando análise {analysis_id} com query: {rendered_query[:100]}...")
            
            # Executa busca semântica
            search_request = SearchRequest(query=rendered_query, max_results=10)
            search_result = await self.search_service.search_semantic(search_request, user_id=user_id)
            
            # Salva resultado
            result_data = {
                "query": rendered_query,
                "answer": search_result.answer,
                "sources": search_result.sources,
                "processing_time_ms": search_result.processing_time_ms
            }
            
            await self.analysis_repo.update(
                analysis_id,
                status="completed",
                result=result_data,
                user_id=user_id
            )
            await self.db.commit()
            
            logger.info(f"Análise {analysis_id} completada com sucesso")
            
            # Busca análise atualizada
            updated_analysis = await self.analysis_repo.get_by_id(analysis_id, user_id=user_id)
            return AnalysisResponse.model_validate(updated_analysis)
            
        except Exception as e:
            logger.error(f"Erro ao executar análise {analysis_id}: {str(e)}", exc_info=True)
            
            # Salva erro
            await self.analysis_repo.update(
                analysis_id,
                status="failed",
                error_message=str(e),
                user_id=user_id
            )
            await self.db.commit()
            
            # Re-raise para propagar erro
            raise
    
    async def get_analysis(self, analysis_id: UUID, user_id: Optional[str] = None) -> AnalysisResponse:
        """
        Busca análise por ID.
        
        Args:
            analysis_id: ID da análise
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            AnalysisResponse
            
        Raises:
            AnalysisNotFoundError: Se análise não encontrada
        """
        analysis = await self.analysis_repo.get_by_id(analysis_id, user_id=user_id)
        if not analysis:
            raise AnalysisNotFoundError(str(analysis_id))
        
        return AnalysisResponse.model_validate(analysis)
    
    async def list_analyses(
        self,
        skip: int = 0,
        limit: int = 100,
        playbook_id: Optional[UUID] = None,
        status: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> List[AnalysisResponse]:
        """
        Lista análises, opcionalmente filtradas.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros
            playbook_id: Filtrar por playbook (opcional)
            status: Filtrar por status (opcional)
            user_id: ID do usuário para filtrar (opcional)
            
        Returns:
            Lista de AnalysisResponse
        """
        analyses = await self.analysis_repo.list_all(
            skip=skip,
            limit=limit,
            playbook_id=playbook_id,
            status=status,
            user_id=user_id
        )
        return [AnalysisResponse.model_validate(a) for a in analyses]
    
    async def delete_analysis(self, analysis_id: UUID, user_id: Optional[str] = None) -> bool:
        """
        Deleta uma análise.
        
        Args:
            analysis_id: ID da análise
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            True se deletada com sucesso
            
        Raises:
            AnalysisNotFoundError: Se análise não encontrada
        """
        deleted = await self.analysis_repo.delete(analysis_id, user_id=user_id)
        await self.db.commit()
        
        logger.info(f"Análise deletada: {analysis_id}")
        return deleted

