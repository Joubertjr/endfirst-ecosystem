"""
Repository para análises (PostgreSQL).
"""
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.models.analysis import Analysis
from app.core.exceptions import AnalysisNotFoundError


class AnalysisRepository:
    """Repository para operações CRUD de análises."""
    
    def __init__(self, db: AsyncSession):
        """
        Inicializa repository com sessão do banco.
        
        Args:
            db: Sessão assíncrona do SQLAlchemy
        """
        self.db = db
    
    async def create(
        self,
        playbook_id: UUID,
        parameters: Optional[dict] = None,
        reference_id: Optional[UUID] = None,
        project_id: Optional[UUID] = None,
        user_id: Optional[str] = None
    ) -> Analysis:
        """
        Cria uma nova análise.
        
        Args:
            playbook_id: ID do playbook
            parameters: Parâmetros para o template
            reference_id: ID da referência (opcional)
            project_id: ID do projeto (opcional)
            user_id: ID do usuário
            
        Returns:
            Analysis criada
        """
        analysis = Analysis(
            playbook_id=playbook_id,
            parameters=parameters or {},
            reference_id=reference_id,
            project_id=project_id,
            user_id=user_id,
            status="pending"
        )
        
        self.db.add(analysis)
        await self.db.flush()
        await self.db.refresh(analysis)
        
        return analysis
    
    async def get_by_id(self, analysis_id: UUID, user_id: Optional[str] = None) -> Optional[Analysis]:
        """
        Busca análise por ID.
        
        Args:
            analysis_id: ID da análise
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            Analysis ou None se não encontrada
        """
        stmt = select(Analysis).where(Analysis.id == analysis_id)
        
        if user_id:
            stmt = stmt.where(Analysis.user_id == user_id)
        
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def list_all(
        self,
        skip: int = 0,
        limit: int = 100,
        playbook_id: Optional[UUID] = None,
        status: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> List[Analysis]:
        """
        Lista análises, opcionalmente filtradas.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros
            playbook_id: Filtrar por playbook (opcional)
            status: Filtrar por status (opcional)
            user_id: ID do usuário para filtrar (opcional)
            
        Returns:
            Lista de análises
        """
        stmt = select(Analysis)
        
        if user_id:
            stmt = stmt.where(Analysis.user_id == user_id)
        
        if playbook_id:
            stmt = stmt.where(Analysis.playbook_id == playbook_id)
        
        if status:
            stmt = stmt.where(Analysis.status == status)
        
        stmt = stmt.order_by(Analysis.created_at.desc()).offset(skip).limit(limit)
        result = await self.db.execute(stmt)
        
        return list(result.scalars().all())
    
    async def update(
        self,
        analysis_id: UUID,
        status: Optional[str] = None,
        result: Optional[dict] = None,
        error_message: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Analysis:
        """
        Atualiza uma análise.
        
        Args:
            analysis_id: ID da análise
            status: Status (opcional)
            result: Resultado (opcional)
            error_message: Mensagem de erro (opcional)
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            Analysis atualizada
            
        Raises:
            AnalysisNotFoundError: Se análise não encontrada
        """
        analysis = await self.get_by_id(analysis_id, user_id=user_id)
        if not analysis:
            raise AnalysisNotFoundError(str(analysis_id))
        
        if status is not None:
            analysis.status = status
        if result is not None:
            analysis.result = result
        if error_message is not None:
            analysis.error_message = error_message
        
        await self.db.flush()
        await self.db.refresh(analysis)
        
        return analysis
    
    async def delete(self, analysis_id: UUID, user_id: Optional[str] = None) -> bool:
        """
        Deleta uma análise.
        
        Args:
            analysis_id: ID da análise
            user_id: ID do usuário para verificar ownership (opcional)
            
        Returns:
            True se deletada
            
        Raises:
            AnalysisNotFoundError: Se análise não encontrada
        """
        analysis = await self.get_by_id(analysis_id, user_id=user_id)
        if not analysis:
            raise AnalysisNotFoundError(str(analysis_id))
        
        await self.db.delete(analysis)
        await self.db.flush()
        
        return True

