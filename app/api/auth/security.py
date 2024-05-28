from datetime import datetime, timedelta
from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.core.config import settings
from app.dao.dao_register_user import AuthUserDAO
from app.exceptions import IncorrectEmailOrPasswordException

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_delta:
        expire = expire + expires_delta
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET,
        settings.ALGORITHM
    )
    return encoded_jwt


# def decode_access_token(token: str):
#     try:
#         payload = jwt.decode(token, settings.JWT_SECRET, settings.ALGORITHM)
#         username: str = payload.get('sub')
#         if username is None:
#             raise IncorrectEmailOrPasswordException
#         return username
#     except JWTError:
#         raise IncorrectEmailOrPasswordException


async def authenticate_user(email: EmailStr, password: str):
    user = await AuthUserDAO.find_one_or_none(email=email)
    if not user and not verify_password(plain_password=password, hashed_password=user.password):
        return None
    return user
