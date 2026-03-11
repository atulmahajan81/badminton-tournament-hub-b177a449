# test_pagination.py

import pytest

@pytest.mark.asyncio
async def test_list_tournaments_pagination(async_client):
    """Test tournament list pagination"""
    response = await async_client.get("/api/v1/tournaments?page=1&limit=10")
    assert response.status_code == 200
    assert "tournaments" in response.json()
    assert len(response.json()["tournaments"]) <= 10

@pytest.mark.asyncio
async def test_list_tournaments_invalid_page(async_client):
    """Test tournament list with invalid page number"""
    response = await async_client.get("/api/v1/tournaments?page=-1&limit=10")
    assert response.status_code == 422