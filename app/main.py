import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from app.api.admin.auth import authentication_backend
from app.api.admin.views import UsersAdmin
from app.api.auth.router import router as user_router
from app.api.endpoints.router import router as currency_router
from app.database import engine
from app.images.router import router as images_router
from app.logger import logger
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


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info('Request handling time', extra={'process_time': round(process_time, 4)})
    response.headers['X-Process-Time'] = str(process_time)
    return response
    