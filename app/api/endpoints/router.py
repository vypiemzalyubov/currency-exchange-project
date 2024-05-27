from fastapi import APIRouter, Request

from app.api.schemas.schemas import Users
from app.dao.dao_users import UsersDAO

router = APIRouter(
    prefix='/currency',
    tags=['Currency Exchange']
)


@router.get('')
async def get_users(request: Request): #-> list[Users]:
    print(request.cookies)
    print(request.client)
    print(request.url)
