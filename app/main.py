import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from app.api.admin.auth import authentication_backend
from app.api.admin.views import UsersAdmin
from app.api.auth.router import router as user_router
from app.api.endpoints.router import router as currency_router
from app.database import engine
from app.images.router import router as images_router
from app.pages.router import router as pages_router

app = FastAPI()

app.mount('/static', StaticFiles(directory='app/static'), 'static')

app.include_router(user_router)
app.include_router(currency_router)
app.include_router(pages_router)
app.include_router(images_router)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['*'],
)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UsersAdmin)

# if __name__ == '__main__':
#     uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
