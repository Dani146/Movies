from pydantic import BaseModel
from datetime import date

class DirectorCreate(BaseModel):
    name: str
    surname: str
    birthdate: date | None = None
    biography: str | None = None

class ActorCreate(BaseModel):
    name : str
    surname : str
    birthdate : date | None = None
    biography: str | None = None


class GenreCreate(BaseModel):
    genre: str

class MovieCreate(BaseModel):
    title: str
    user_rating: float | None = None
    critic_rating: float | None = None
    duration_min: int | None = None
    description: str | None = None
    release_date: date | None = None
    country_of_production: str | None = None

class SeriesCreate(BaseModel):
    title: str
    user_rating: float | None = None
    critic_rating: float | None = None
    duration_min_episode: int | None = None
    description: str | None = None
    release_date: date | None = None
    country_of_production: str | None = None

class MovieInteractionUpdate(BaseModel):
    liked: bool | None = None
    watched: bool | None = None 
    watchlist: bool | None = None
    favourite: bool | None = None
    rating: float | None = None


class SeriesInteractionUpdate(BaseModel):
    liked: bool | None = None
    watched: bool | None = None 
    watchlist: bool | None = None
    favourite: bool | None = None
    rating: float | None = None

class UserCreate(BaseModel):
    username : str
    password: str

    
