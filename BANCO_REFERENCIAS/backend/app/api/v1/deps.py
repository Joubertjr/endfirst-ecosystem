"""
Dependencies do FastAPI (deps.py).
Shared dependencies para endpoints.
"""
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.core.database import get_db
from app.core.auth import get_current_user, get_optional_user

# Re-export get_db para usar nos endpoints
get_db_session = get_db

# Re-export auth dependencies
get_current_user_dep = get_current_user
get_optional_user_dep = get_optional_user
