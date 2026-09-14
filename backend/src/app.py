from fastapi import APIRouter

router = APIRouter()

movies_list = {}

@router.get("/movies_list")
def get_movie_list():
    return movies_list