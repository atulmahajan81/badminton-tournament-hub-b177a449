# backend/routers/tournaments.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas import TournamentCreate, TournamentResponse
from backend.models import Tournament
from backend.dependencies import get_db
from backend.services.tournament_service import TournamentService

router = APIRouter()

@router.post("/tournaments", response_model=TournamentResponse)
async def create_tournament(tournament_create: TournamentCreate, db: AsyncSession = Depends(get_db)):
    tournament = await TournamentService.create_tournament(db, tournament_create)
    return tournament

@router.get("/tournaments", response_model=list[TournamentResponse])
async def list_tournaments(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    tournaments = await TournamentService.get_tournaments(db, skip=skip, limit=limit)
    return tournaments