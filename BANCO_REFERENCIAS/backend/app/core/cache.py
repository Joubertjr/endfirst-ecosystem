"""
Cache Repository usando Redis.
"""
import json
from typing import Optional, Any
import redis.asyncio as redis
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)


class CacheRepository:
    """Repository para operações de cache usando Redis."""
    
    def __init__(self):
        """Inicializa cliente Redis."""
        self.redis_client: Optional[redis.Redis] = None
        self._enabled = bool(settings.REDIS_URL)
    
    async def connect(self):
        """Conecta ao Redis."""
        if not self._enabled:
            logger.warning("Cache desabilitado - REDIS_URL não configurado")
            return
        
        try:
            self.redis_client = await redis.from_url(
                settings.REDIS_URL or "redis://localhost:6379/0",
                encoding="utf-8",
                decode_responses=True
            )
            await self.redis_client.ping()
            logger.info("✅ Cache Redis conectado")
        except Exception as e:
            logger.warning(f"⚠️ Erro ao conectar ao Redis: {e}. Cache desabilitado.")
            self.redis_client = None
            self._enabled = False
    
    async def disconnect(self):
        """Desconecta do Redis."""
        if self.redis_client:
            await self.redis_client.close()
            logger.info("Cache Redis desconectado")
    
    async def get(self, key: str) -> Optional[Any]:
        """
        Obtém valor do cache.
        
        Args:
            key: Chave do cache
            
        Returns:
            Valor do cache ou None se não encontrado
        """
        if not self._enabled or not self.redis_client:
            return None
        
        try:
            value = await self.redis_client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            logger.error(f"Erro ao obter do cache: {e}")
            return None
    
    async def set(
        self,
        key: str,
        value: Any,
        ttl: int = 900  # 15 minutos padrão
    ) -> bool:
        """
        Define valor no cache.
        
        Args:
            key: Chave do cache
            value: Valor para armazenar
            ttl: Time to live em segundos (padrão: 15 minutos)
            
        Returns:
            True se sucesso
        """
        if not self._enabled or not self.redis_client:
            return False
        
        try:
            await self.redis_client.setex(
                key,
                ttl,
                json.dumps(value, default=str)  # default=str para serializar datetime
            )
            return True
        except Exception as e:
            logger.error(f"Erro ao definir no cache: {e}")
            return False
    
    async def delete(self, key: str) -> bool:
        """
        Deleta chave do cache.
        
        Args:
            key: Chave para deletar
            
        Returns:
            True se deletado
        """
        if not self._enabled or not self.redis_client:
            return False
        
        try:
            await self.redis_client.delete(key)
            return True
        except Exception as e:
            logger.error(f"Erro ao deletar do cache: {e}")
            return False
    
    async def delete_pattern(self, pattern: str) -> int:
        """
        Deleta todas as chaves que correspondem ao padrão.
        
        Args:
            pattern: Padrão para buscar (ex: "search:*")
            
        Returns:
            Número de chaves deletadas
        """
        if not self._enabled or not self.redis_client:
            return 0
        
        try:
            keys = await self.redis_client.keys(pattern)
            if keys:
                return await self.redis_client.delete(*keys)
            return 0
        except Exception as e:
            logger.error(f"Erro ao deletar padrão do cache: {e}")
            return 0


# Instância global do cache
cache_repo = CacheRepository()

