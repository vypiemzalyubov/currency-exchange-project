import uvicorn
from fastapi import FastAPI

from app.api.auth.router import router as user_router
from app.api.endpoints.router import router as currency_router

app = FastAPI()

app.include_router(user_router)
app.include_router(currency_router)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
