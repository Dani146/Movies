from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.db import Movie, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/welcome")
async def root():
    return {"message": "Welcome to What to Watch!"}

@app.get("/main")
async def root():
    return {"message" : "Welcome to main screen"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)