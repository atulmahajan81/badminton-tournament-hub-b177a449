# backend/models.py

from sqlalchemy import Column, String, ForeignKey, DateTime, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base
import uuid

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    registrations = relationship("Registration", back_populates="user")

    def validate_role(self):
        valid_roles = ['admin', 'organizer', 'player', 'umpire']
        if self.role not in valid_roles:
            raise ValueError(f"Role {self.role} is invalid. Must be one of {valid_roles}")

class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)
    rules = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    matches = relationship("Match", back_populates="tournament")
    registrations = relationship("Registration", back_populates="tournament")

class Match(Base):
    __tablename__ = 'matches'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tournament_id = Column(UUID(as_uuid=True), ForeignKey('tournaments.id'), nullable=False)
    player1_id = Column(UUID(as_uuid=True), nullable=False)
    player2_id = Column(UUID(as_uuid=True), nullable=False)