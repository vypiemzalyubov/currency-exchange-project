import shutil

from fastapi import APIRouter, Depends, UploadFile

from app.api.auth.dependencies import get_current_user
from app.api.schemas.users import Users

router = APIRouter(prefix='/images', tags=['Download images'])


@router.post('/users')
async def add_user_avatar(file: UploadFile, user: Users = Depends(get_current_user)):
    with open(f'app/static/images/{user.user_id}.webp', 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)
