from pydantic import BaseModel
from datetime import date

class MovieCreate(BaseModel):
    title: str
    user_rating: float
    critic_rating: float
    duration_min: int
    description: str
    release_date: date
    country_of_production: str
