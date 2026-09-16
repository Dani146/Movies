from fastapi import FastAPI

from src.app import router as movie_router
from src.actors import router as actor_router
from src.db import Movie, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(movie_router)
app.include_router(actor_router)

@app.get("/")
async def root():
    return {"message": "Welcome to main screen"}