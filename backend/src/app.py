from fastapi import APIRouter, HTTPException
from src.schemas.movie import MovieCreate
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.db import get_async_session

from src.db import Movie, get_async_session
router = APIRouter()

movies_list = {}

@router.get("/movies_list")
def get_movie_list():
    return movies_list

@router.get("/movie/{id}")
def get_movie(id: int):
    if id not in movies_list:
        raise HTTPException(
            status_code=404,
            detail="Movie was not found"
        )

    return movies_list[id]

# add a post tomorrow

@router.post("/movies_list")
async def create_movie(movie: MovieCreate,
                       session: AsyncSession = Depends(get_async_session)):

    new_movie = Movie(
        title = movie.title,
        year = movie.year,
        score = movie.score,
        description = movie.description
    )
    session.add(new_movie)

    await session.commit()

    await session.refresh(new_movie)

    return new_movie

   

@router.delete("/movie/{id}")
def delete_movie(id: int):
    if id not in movies_list:
        raise HTTPException(
            status_code=404,
            detail="Movie was not found to delete"
        )
    del movies_list[id]