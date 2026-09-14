from fastapi import APIRouter
from src.schemas.movie import MovieCreate

router = APIRouter()

movies_list = {}

@router.get("/movies_list")
def get_movie_list():
    return movies_list

# add a post tomorrow