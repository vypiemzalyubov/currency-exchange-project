from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from app.api.endpoints.router import get_users

router = APIRouter(prefix='/pages', tags=['Frontend'])

templates = Jinja2Templates(directory='app/templates')

@router.get('/users')
async def get_users_page(request: Request, users=Depends(get_users)):
    return templates.TemplateResponse(name='users.html', context={'request': request, 'users': users})
