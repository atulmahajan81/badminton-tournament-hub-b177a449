# test_services.py

import pytest
from unittest.mock import Mock
from backend.services.user_service import UserService

@pytest.mark.asyncio
async def test_user_service_create_user(async_session):
    """Test creating a user service layer function"""
    user_service = UserService(async_session)
    user = await user_service.create_user(email="service@example.com", password="password123")
    assert user.email == "service@example.com"

@pytest.mark.asyncio
async def test_user_service_create_user_duplicate(async_session):
    """Test creating a user with an email that already exists"""
    user_service = UserService(async_session)
    await user_service.create_user(email="service@example.com", password="password123")
    with pytest.raises(ValueError):
        await user_service.create_user(email="service@example.com", password="password123")