# backend/schemas.py

from pydantic import BaseModel, EmailStr, Field, ConfigDict
from uuid import UUID
from datetime import datetime, date

class UserBase(BaseModel):
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

class TournamentBase(BaseModel):
    name: str
    location: str
    date: date
    rules: str

    model_config = ConfigDict(from_attributes=True)

class TournamentCreate(TournamentBase):
    pass

class TournamentResponse(TournamentBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

class MatchBase(BaseModel):
    tournament_id: UUID
    player1_id: UUID
    player2_id: UUID
    umpire_id: UUID
    scheduled_time: datetime

    model_config = ConfigDict(from_attributes=True)

class MatchCreate(MatchBase):
    pass

class MatchResponse(MatchBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

class ScoreBase(BaseModel):
    match_id: UUID
    player1_score: int
    player2_score: int

    model_config = ConfigDict(from_attributes=True)

class ScoreCreate(ScoreBase):
    pass

class ScoreResponse(ScoreBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

class NotificationBase(BaseModel):
    user_id: UUID
    message: str

    model_config = ConfigDict(from_attributes=True)

class NotificationCreate(NotificationBase):
    pass

class NotificationResponse(NotificationBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

class RegistrationBase(BaseModel):
    user_id: UUID
    tournament_id: UUID

    model_config = ConfigDict(from_attributes=True)

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationResponse(RegistrationBase):
    id: UUID
    created_at: datetime
    updated_at: datetime