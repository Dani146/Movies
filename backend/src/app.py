from fastapi import APIRouter, HTTPException
from src.schemas.movie import MovieCreate
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from uuid import UUID
from src.db import Movie, get_async_session
from sqlalchemy import select


router = APIRouter()

#  retrieves all Movie objects from the database
@router.get("/movies_list")
async def get_movie_list(session: AsyncSession = Depends(get_async_session)):

    result = await session.execute(select(Movie))
    movies = result.scalars().all()
    return movies
# retrieve movie by its UUID id , raise error if there is no movie to be found in database
@router.get("/movie/{id}")
async def get_movie(id: UUID,
                    session: AsyncSession = Depends(get_async_session)):

    movie = await session.get(Movie, id)

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="movie was not found"
        )

    return movie
# creates a movie entity and sends it to database and saves
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

   
# takes a UUID and deletes the Movie with that primary key
@router.delete("/movie/{id}")
async def delete_movie(id: UUID,
                 session: AsyncSession = Depends(get_async_session)):

    movie = await session.get(Movie, id)

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie was not found"
        )

    
    await session.delete(movie)
    await session.commit()

    return {"message": "movie was deleted sucessfully"}

