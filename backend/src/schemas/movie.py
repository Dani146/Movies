from pydantic import BaseModel
from src.schemas.genre import Genre
class MovieCreate(BaseModel):
    title: str
    year: int
    score: float
    description: str
    genre: list[Genre]