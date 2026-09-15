from fastapi import APIRouter, HTTPException
from src.schemas.movie import MovieCreate

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
def create_movie(movie: MovieCreate):
    movie_id = max(movies_list.keys(), default=0) + 1
    movies_list[movie_id] = movie
    return movie

@router.delete("/movie/{id}")
def delete_movie(id: int):
    del movies_list[id]