# test_integration.py

import pytest

@pytest.mark.asyncio
async def test_full_user_flow(async_client):
    """Test full user flow from registration to creating and deleting a tournament"""
    # Register
    reg_response = await async_client.post("/api/v1/users/register", json={"email": "flowuser@example.com", "password": "password123"})
    assert reg_response.status_code == 201
    user_id = reg_response.json()["user_id"]

    # Login
    login_response = await async_client.post("/api/v1/users/login", json={"email": "flowuser@example.com", "password": "password123"})
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]
    auth_headers = {"Authorization": f"Bearer {access_token}"}

    # Create Tournament
    tournament_response = await async_client.post(
        "/api/v1/tournaments",
        json={"name": "Test Tournament", "location": "Test Venue", "date": "2023-10-10", "rules": "None"},
        headers=auth_headers
    )
    assert tournament_response.status_code == 201
    tournament_id = tournament_response.json()["tournament_id"]

    # Delete Tournament (Assuming endpoint exists)
    delete_response = await async_client.delete(f"/api/v1/tournaments/{tournament_id}", headers=auth_headers)
    assert delete_response.status_code == 204