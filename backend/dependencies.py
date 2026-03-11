# backend/dependencies.py

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.auth import Auth
from backend.models import User

async def get_current_user(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = Auth.decode_token(token)
    if payload is None:
        raise credentials_exception
    user = await db.get(User, payload.get("sub"))
    if user is None:
        raise credentials_exception
    return user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}