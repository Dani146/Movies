from pydantic import BaseModel
from datetime import date

class SeriesCreate(BaseModel):
    title: str
    user_rating: float
    critic_rating: float
    duration_min_episode: int
    description: str
    release_date: date
    country_of_production: str
