from fastapi import APIRouter, Depends, Request

from app.api.auth.dependencies import get_current_user
from app.api.schemas.schemas import Users
from app.dao.dao_users import UsersDAO

router = APIRouter(
    prefix='/currency',
    tags=['Currency Exchange']
)


@router.get('')
async def get_users(user: Users = Depends(get_current_user)): #-> list[Users]:
    return user
    # return await UsersDAO.get_all_users()
