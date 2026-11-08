from fastapi import APIRouter

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/")
async def get_movies():
    return ["Intersterlar", "inception"]