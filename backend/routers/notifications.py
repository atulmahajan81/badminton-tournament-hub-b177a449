# backend/routers/notifications.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas import NotificationCreate, NotificationResponse
from backend.models import Notification
from backend.dependencies import get_db
from backend.services.notification_service import NotificationService

router = APIRouter()

@router.get("/notifications", response_model=list[NotificationResponse])
async def get_notifications(skip: int = 0, limit: int = 10, user_id: str, db: AsyncSession = Depends(get_db)):
    notifications = await NotificationService.get_notifications(db, user_id, skip=skip, limit=limit)
    return notifications

@router.post("/notifications", response_model=NotificationResponse)
async def create_notification(notification_create: NotificationCreate, db: AsyncSession = Depends(get_db)):
    notification = await NotificationService.create_notification(db, notification_create)
    return notification