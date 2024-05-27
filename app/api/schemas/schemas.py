from datetime import datetime

from pydantic import BaseModel, EmailStr


class Users(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    hashed_password: str
    created_date: datetime

    class Config:
        from_attributes = True
