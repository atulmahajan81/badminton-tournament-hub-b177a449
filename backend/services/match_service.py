# backend/services/match_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from backend.models import Match, Score
from backend.schemas import MatchCreate, ScoreCreate

class MatchService:

    @staticmethod
    async def schedule_match(db: AsyncSession, match_create: MatchCreate):
        match = Match(
            tournament_id=match_create.tournament_id,
            player1_id=match_create.player1_id,
            player2_id=match_create.player2_id,
            umpire_id=match_create.umpire_id,
            scheduled_time=match_create.scheduled_time
        )
        db.add(match)
        try:
            await db.commit()
            await db.refresh(match)
            return match
        except IntegrityError:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Match could not be scheduled")

    @staticmethod
    async def update_scores(db: AsyncSession, match_id: str, score_create: ScoreCreate):
        match = await db.get(Match, match_id)
        if not match:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Match not found")

        score = Score(
            match_id=match_id,
            player1_score=score_create.player1_score,
            player2_score=score_create.player2_score
        )
        db.add(score)
        try:
            await db.commit()
            await db.refresh(score)
            return score
        except IntegrityError:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Scores could not be updated")