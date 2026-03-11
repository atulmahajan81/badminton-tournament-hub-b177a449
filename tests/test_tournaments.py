# test_tournaments.py

import pytest

@pytest.mark.asyncio
async def test_create_tournament(async_client, auth_headers):
    """Test creating a new tournament"""
    response = await async_client.post("/api/v1/tournaments", json={"name": "Open Cup", "location": "City Arena", "date": "2023-11-01", "rules": "Standard"}, headers=auth_headers)
    assert response.status_code == 201
    assert "tournament_id" in response.json()

@pytest.mark.asyncio
async def test_list_tournaments(async_client):
    """Test listing all tournaments"""
    response = await async_client.get("/api/v1/tournaments")
    assert response.status_code == 200
    assert "tournaments" in response.json()

@pytest.mark.asyncio
async def test_register_player_for_tournament(async_client, auth_headers):
    """Test player registration for a tournament"""
    response = await async_client.post("/api/v1/tournaments/1/register", json={"player_id": "player-uuid"}, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["registration_status"] == "registered"