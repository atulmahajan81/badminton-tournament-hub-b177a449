# test_users.py

import pytest

@pytest.mark.asyncio
async def test_create_user(async_client):
    """Test creating a new user"""
    response = await async_client.post("/api/v1/users/register", json={"email": "newuser@example.com", "password": "password123"})
    assert response.status_code == 201
    assert "user_id" in response.json()

@pytest.mark.asyncio
async def test_get_user(async_client, auth_headers):
    """Test retrieving user details"""
    # Assuming a GET /api/v1/users/{id} endpoint exists
    response = await async_client.get("/api/v1/users/1", headers=auth_headers)
    assert response.status_code == 200
    assert "email" in response.json()

@pytest.mark.asyncio
async def test_update_user(async_client, auth_headers):
    """Test updating user details"""
    # Assuming a PUT /api/v1/users/{id} endpoint exists
    response = await async_client.put("/api/v1/users/1", json={"email": "updated@example.com"}, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["email"] == "updated@example.com"

@pytest.mark.asyncio
async def test_delete_user(async_client, auth_headers):
    """Test deleting a user"""
    # Assuming a DELETE /api/v1/users/{id} endpoint exists
    response = await async_client.delete("/api/v1/users/1", headers=auth_headers)
    assert response.status_code == 204