# test_models.py

import pytest
from sqlalchemy.exc import IntegrityError
from backend.models import User, Tournament

@pytest.mark.asyncio
async def test_user_model_constraints(async_session):
    """Test the uniqueness constraint on the User model's email field"""
    user = User(email="duplicate@example.com", password_hash="hashed", role="player")
    async_session.add(user)
    await async_session.commit()
    duplicate_user = User(email="duplicate@example.com", password_hash="hashed", role="player")
    async_session.add(duplicate_user)
    with pytest.raises(IntegrityError):
        await async_session.commit()

@pytest.mark.asyncio
async def test_tournament_model(async_session):
    """Test creating a Tournament with valid data"""
    tournament = Tournament(name="Championship", location="Stadium", date="2023-12-12", rules="Standard")
    async_session.add(tournament)
    await async_session.commit()
    assert tournament.id is not None