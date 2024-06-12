from fastapi import APIRouter, Depends

from app.api.auth.dependencies import get_current_user
from app.api.schemas.users import Users
from app.dao.dao_users import UsersDAO

router = APIRouter(prefix='/currency', tags=['Currency Exchange'])


@router.get('', response_model=list[Users])
async def get_users(user: Users = Depends(get_current_user)):  # -> list[Users]:
    return await UsersDAO.get_all_users()
