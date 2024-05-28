from datetime import datetime

from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt

from app.core.config import settings
from app.dao.dao_users import UsersDAO
from app.exceptions import (
    ExpiredTokenException,
    IncorrectEmailOrPasswordException,
    IncorrectTokenFormatException,
    TokenAbsentException,
)


def get_token(request: Request):
    token = request.cookies.get('currency_exchange_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, settings.ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise ExpiredTokenException
    user_id: str = payload.get('sub')
    if not user_id:
        raise IncorrectEmailOrPasswordException
    user = await UsersDAO.get_user_by_id(int(user_id))
    if not user:
        raise IncorrectEmailOrPasswordException
    return user
