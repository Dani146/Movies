from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..db import get_db
from ..db import Movie
from ..schemas import MovieCreate
router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/")
async def get_movies(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie))
    movies = result.scalars().all()

    return movies

@router.post("/add")
async def add_movie(
    movie : MovieCreate,
    db: AsyncSession = Depends(get_db)):

    new_movie = Movie(**movie.model_dump())
    db.add(new_movie)
    await db.commit()

    return {"message": "Movie added successfully"}