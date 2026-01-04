"""
Autenticação usando Clerk.
"""
from typing import Optional
from fastapi import HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from clerk_sdk_python import Clerk
from app.core.config import settings
from app.core.exceptions import AuthenticationError


# Security scheme para Swagger
security = HTTPBearer(auto_error=False)


class ClerkAuth:
    """Classe para gerenciar autenticação com Clerk."""
    
    def __init__(self):
        """Inicializa cliente do Clerk."""
        if not settings.CLERK_SECRET_KEY:
            # Se não configurado, permite operação sem auth (modo desenvolvimento)
            self.clerk = None
            self.enabled = False
        else:
            self.clerk = Clerk(bearer_auth_token=settings.CLERK_SECRET_KEY)
            self.enabled = True
    
    async def verify_token(self, token: str) -> dict:
        """
        Verifica token JWT do Clerk e retorna dados do usuário.
        
        Args:
            token: Token JWT do Clerk
            
        Returns:
            Dict com dados do usuário (user_id, email, etc)
            
        Raises:
            AuthenticationError: Se token inválido ou expirado
        """
        if not self.enabled:
            # Modo desenvolvimento - retorna usuário mock
            return {
                "user_id": "dev_user_123",
                "email": "dev@example.com",
                "first_name": "Dev",
                "last_name": "User"
            }
        
        try:
            # Verifica token com Clerk
            user = self.clerk.users.get_user(token)
            
            return {
                "user_id": user.get("id"),
                "email": user.get("email_addresses", [{}])[0].get("email_address") if user.get("email_addresses") else None,
                "first_name": user.get("first_name"),
                "last_name": user.get("last_name"),
                "clerk_user": user  # Objeto completo do Clerk
            }
        except Exception as e:
            raise AuthenticationError(f"Token inválido ou expirado: {str(e)}")
    
    async def get_current_user(
        self,
        credentials: Optional[HTTPAuthorizationCredentials] = None
    ) -> dict:
        """
        Dependency para obter usuário autenticado.
        
        Args:
            credentials: Credenciais HTTP Bearer
            
        Returns:
            Dict com dados do usuário autenticado
            
        Raises:
            HTTPException: Se não autenticado
        """
        if not self.enabled:
            # Modo desenvolvimento - permite acesso sem token
            return {
                "user_id": "dev_user_123",
                "email": "dev@example.com",
                "first_name": "Dev",
                "last_name": "User"
            }
        
        if not credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token de autenticação requerido",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        token = credentials.credentials
        
        try:
            user_data = await self.verify_token(token)
            return user_data
        except AuthenticationError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
                headers={"WWW-Authenticate": "Bearer"},
            )


# Instância global
clerk_auth = ClerkAuth()


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = security
) -> dict:
    """
    Dependency FastAPI para obter usuário autenticado.
    
    Usage:
        @router.get("/protected")
        async def protected_route(user: dict = Depends(get_current_user)):
            user_id = user["user_id"]
            ...
    """
    return await clerk_auth.get_current_user(credentials)


async def get_optional_user(
    credentials: Optional[HTTPAuthorizationCredentials] = security
) -> Optional[dict]:
    """
    Dependency FastAPI para obter usuário autenticado (opcional).
    Retorna None se não autenticado (útil para rotas públicas).
    
    Usage:
        @router.get("/public-or-private")
        async def route(user: Optional[dict] = Depends(get_optional_user)):
            if user:
                # Usuário autenticado
                ...
            else:
                # Usuário anônimo
                ...
    """
    try:
        return await clerk_auth.get_current_user(credentials)
    except HTTPException:
        return None

