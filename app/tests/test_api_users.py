import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    'username, email, password, status_code',
    [
        ('user1', 'user1@example.com', 'pass1', 200),
        ('user11', 'user1@example.com', 'pass1', 409),
        ('user', 'example.com', 'pass1', 422),
    ],
)
async def test_register_user(
    async_client: AsyncClient, username, email, password, status_code
):
    response = await async_client.post(
        '/auth/register',
        json={'username': username, 'email': email, 'password': password},
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    'email, password, status_code',
    [
        ('test_user1@example.com', 'testpass1', 200),
        ('test_user2@example.com', 'testpass2', 200),
        ('fake_user@example.com', 'fakepass', 401),
    ],
)
async def test_login_user(async_client: AsyncClient, email, password, status_code):
    response = await async_client.post(
        '/auth/login',
        json={'email': email, 'password': password},
    )

    assert response.status_code == status_code


async def test_get_all_users(auth_client: AsyncClient):
    response = await auth_client.get('/currency')

    assert response.status_code == 200
    assert len(response.json()) > 0
