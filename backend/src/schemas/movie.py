from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    year: int
    score: float
    description: str
    