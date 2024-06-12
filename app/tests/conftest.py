import json

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import insert

from app.core.config import settings
from app.database import Base, async_session_maker, engine
from app.main import app as fastapi_app
from app.models.models import Users


@pytest.fixture(scope='session', autouse=True)
async def prepare_db():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f'app/tests/mock/mock_{model}.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    users = open_mock_json('users')

    async with async_session_maker() as session:
        add_users = insert(Users).values(users)

        await session.execute(add_users)
        await session.commit()


@pytest.fixture(scope='function')
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=fastapi_app), base_url='http://test'
    ) as ac:
        yield ac


@pytest.fixture(scope='function')
async def auth_client():
    async with AsyncClient(
        transport=ASGITransport(app=fastapi_app), base_url='http://test'
    ) as ac:
        await ac.post(
            '/auth/login',
            json={'email': 'test_user1@example.com', 'password': 'testpass1'},
        )
        assert ac.cookies['currency_exchange_token']
        yield ac


@pytest.fixture(scope='function')
async def session():
    async with async_session_maker() as session:
        yield session
