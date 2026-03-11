# backend/routers/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas import UserResponse
from backend.models import User
from backend.dependencies import get_db, get_current_user
from backend.services.user_service import UserService

router = APIRouter()

@router.get("/users/", response_model=list[UserResponse])
async def list_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    users = await UserService.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{id}", response_model=UserResponse)
async def get_user(id: str, db: AsyncSession = Depends(get_db)):
    user = await UserService.get_user(db, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.put("/users/{id}", response_model=UserResponse)
async def update_user(id: str, user_update: UserResponse, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.id != id and current_user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    user = await UserService.update_user(db, id, user_update)
    return user

@router.delete("/users/{id}")
async def delete_user(id: str, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.id != id and current_user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    await UserService.delete_user(db, id)
    return {"message": "User deleted successfully"}