# backend/services/notification_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from backend.models import Notification
from backend.schemas import NotificationCreate
from backend.tasks import send_notification_task

class NotificationService:

    @staticmethod
    def create_notification_task(notification_create: NotificationCreate):
        send_notification_task.delay(notification_create)