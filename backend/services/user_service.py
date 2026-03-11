# backend/services/user_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from backend.models import User
from backend.schemas import UserCreate, UserResponse
from backend.auth import Auth
from backend.cache import cache_result

class UserService:

    @staticmethod
    @cache_result(ttl=300)
    async def get_user_by_email_cached(db: AsyncSession, email: str):
        query = select(User).filter(User.email == email)
        result = await db.execute(query)
        return result.scalars().first()

    @staticmethod
    async def create_user(db: AsyncSession, user_create: UserCreate):
        user = User(
            email=user_create.email,
            password_hash=Auth.get_password_hash(user_create.password),
            role=user_create.role
        )
        db.add(user)
        try:
            await db.commit()
            await db.refresh(user)
            return user
        except IntegrityError:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User could not be created")

    @staticmethod
    async def authenticate_user(db: AsyncSession, email: str, password: str):
        user = await UserService.get_user_by_email_cached(db, email)
        if user and Auth.verify_password(password, user.password_hash):
            return user
        return None