from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserAuth(BaseModel):
    email: EmailStr
    password: str
