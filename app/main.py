from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import engine
from app.my_movies.router import router as payment_router
from app.user.router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    # Отключение от базы данных при завершении приложения
    await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(payment_router, prefix='/movies')
app.include_router(user_router)
