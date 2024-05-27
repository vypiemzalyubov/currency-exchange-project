from fastapi import APIRouter, HTTPException, Response, status

from app.api.auth.schemas import UserAuth, UserRegister
from app.api.auth.security import (
    authenticate_user,
    create_access_token,
    get_password_hash,
)
from app.dao.dao_register_user import AuthUserDAO

router = APIRouter(
    prefix='/auth',
    tags=['Auth User']
)


@router.post('/register')
async def register_user(user_data: UserRegister):
    existing_user = await AuthUserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    hashed_password = get_password_hash(user_data.password)
    await AuthUserDAO.add_user(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )


@router.post('/login')
async def login_user(response: Response, user_data: UserAuth):
    user = await authenticate_user(email=user_data.email, password=user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({'sub': user})
    response.set_cookie('currency_exchange_token', access_token, httponly=True)
    return {'user_id': user, 'access_token': access_token}
