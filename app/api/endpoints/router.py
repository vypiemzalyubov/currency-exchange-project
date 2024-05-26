from fastapi import APIRouter

from app.api.schemas.schemas import Users
from app.dao_users import UsersDAO

router = APIRouter(
    prefix='/currency',
    tags=['Currency Exchange']
)


@router.get('')
async def get_users() -> list[Users]:
    return await UsersDAO.get_all_users()

# @router.get('')
# async def get_user() -> Users:# -> Any:
#     return await UsersDAO.get_user_by_id()