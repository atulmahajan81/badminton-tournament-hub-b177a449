# backend/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas import UserCreate, UserResponse
from backend.models import User
from backend.auth import Auth
from backend.dependencies import get_db
from backend.services.user_service import UserService
from fastapi_limiter.depends import RateLimiter

router = APIRouter()

@router.post("/users/register", response_model=UserResponse)
async def register_user(user_create: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await UserService.get_user_by_email(db, user_create.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user = await UserService.create_user(db, user_create)
    return user

@router.post("/users/login", dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def login_user(email: str, password: str, db: AsyncSession = Depends(get_db)):
    user = await UserService.authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = Auth.create_access_token(data={"sub": str(user.id)})
    refresh_token = Auth.create_refresh_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "refresh_token": refresh_token}

@router.post("/users/refresh")
async def refresh_access_token(refresh_token: str):
    payload = Auth.decode_token(refresh_token)
    if not payload:
        raise HTTPException(status