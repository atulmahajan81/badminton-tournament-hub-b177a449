# backend/routers/matches.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas import MatchCreate, MatchResponse, ScoreCreate, ScoreResponse
from backend.models import Match, Score
from backend.dependencies import get_db
from backend.services.match_service import MatchService

router = APIRouter()

@router.post("/matches", response_model=MatchResponse)
async def schedule_match(match_create: MatchCreate, db: AsyncSession = Depends(get_db)):
    match = await MatchService.schedule_match(db, match_create)
    return match

@router.put("/matches/{id}/scores", response_model=ScoreResponse)
async def update_match_scores(id: str, score_create: ScoreCreate, db: AsyncSession = Depends(get_db)):
    score = await MatchService.update_scores(db, id, score_create)
    return score