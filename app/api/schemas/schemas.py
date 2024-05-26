from datetime import datetime

from pydantic import BaseModel


class Users(BaseModel):
    user_id: int
    username: str
    hashed_password: str
    favorite_coin: str
    created_date: datetime

    class Config:
        from_attributes = True
