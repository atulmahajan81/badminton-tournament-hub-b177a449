# conftest.py

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from backend.main import app
from backend.database import Base
from backend.auth import create_access_token, create_refresh_token

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

@pytest.fixture(scope="session")
async def async_engine():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()

@pytest.fixture(scope="function")
async def async_session(async_engine):
    async with SessionLocal() as session:
        yield session

@pytest.fixture(scope="function")
async def async_client(async_session):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture(scope="function")
def access_token() -> str:
    return create_access_token(data={"sub": "testuser@example.com"})

@pytest.fixture(scope="function")
def refresh_token() -> str:
    return create_refresh_token(data={"sub": "testuser@example.com"})

@pytest.fixture(scope="function")
async def test_user(async_session):
    # Create a test user in the database (omitted for brevity)
    pass

@pytest.fixture(scope="function")
async def auth_headers(access_token):
    return {"Authorization": f"Bearer {access_token}"}