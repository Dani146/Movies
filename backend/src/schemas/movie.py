from pydantic import BaseModel

class MovieCreate(BaseModel):
    id: int
    title: str
    score: float
    year: int
    