# backend/services/tournament_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from backend.models import Tournament
from backend.schemas import TournamentCreate
from sqlalchemy.orm import selectinload

class TournamentService:

    @staticmethod
    async def create_tournament(db: AsyncSession, tournament_create: TournamentCreate):
        tournament = Tournament(
            name=tournament_create.name,
            location=tournament_create.location,
            date=tournament_create.date,
            rules=tournament_create.rules
        )
        db.add(tournament)
        try:
            await db.commit()
            await db.refresh(tournament)
            return tournament
        except IntegrityError:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tournament could not be created")

    @staticmethod
    async def get_tournaments_paginated(db: AsyncSession, cursor: str = None, limit: int = 10):
        query = select(Tournament)
        if cursor:
            query = query.filter(Tournament.id > cursor)
        query = query.order_by(Tournament.id).limit(limit)
        result = await db.execute(query)
        tournaments = result.scalars().all()
        return tournaments