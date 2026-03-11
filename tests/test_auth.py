# test_auth.py

import pytest

@pytest.mark.asyncio
async def test_register_user(async_client):
    """Test user registration with valid data"""
    response = await async_client.post("/api/v1/users/register", json={"email": "user@example.com", "password": "password123"})
    assert response.status_code == 201
    assert "user_id" in response.json()

@pytest.mark.asyncio
async def test_login_user(async_client, test_user):
    """Test user login with valid credentials"""
    response = await async_client.post("/api/v1/users/login", json={"email": "user@example.com", "password": "password123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_invalid_login(async_client):
    """Test user login with invalid credentials"""
    response = await async_client.post("/api/v1/users/login", json={"email": "user@example.com", "password": "wrongpassword"})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_token_refresh(async_client, refresh_token):
    """Test refreshing access token with a valid refresh token"""
    response = await async_client.post("/api/v1/users/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_logout(async_client, auth_headers):
    """Test logging out an authenticated user"""
    response = await async_client.post("/api/v1/users/logout", headers=auth_headers)
    assert response.status_code == 200
    assert "message" in response.json()