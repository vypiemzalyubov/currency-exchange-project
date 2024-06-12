import pytest

from app.dao.dao_users import UsersDAO


@pytest.mark.parametrize(
    'user_id, email, is_exists',
    [
        (1, 'test_user1@example.com', True),
        (2, 'test_user2@example.com', True),
        (5, 'test_user5@example.com', False),
    ],
)
async def test_find_user_by_id(user_id, email, is_exists):
    user = await UsersDAO.get_user_by_id(user_id)

    if is_exists:
        assert user
        assert user.user_id == user_id
        assert user.email == email
    else:
        assert not user
