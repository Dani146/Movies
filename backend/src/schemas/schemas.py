from pydantic import BaseModel
from datetime import date

class DirectorCreate(BaseModel):
    name: str
    surname: str
    birthdate: date
    biography: str

class ActorCreate(BaseModel):
    name : str
    surname : str
    birthdate : date
    biography: str


class GenreCreate(BaseModel):

    genre: str

class MovieCreate(BaseModel):
    title: str
    user_rating: float
    critic_rating: float
    duration_min: int
    description: str
    release_date: date
    country_of_production: str

class SeriesCreate(BaseModel):
    title: str
    user_rating: float
    critic_rating: float
    duration_min_episode: int
    description: str
    release_date: date
    country_of_production: str

class MovieInteractionUpdate(BaseModel):
    liked: bool | None = None
    watched: bool | None = None 
    warchlist: bool | None = None
    favourite: bool | None = None
    rating: float | None = None


class SeriesInteractionUpdate(BaseModel):
    liked: bool | None = None
    watched: bool | None = None 
    warchlist: bool | None = None
    favourite: bool | None = None
    rating: float | None = None



class UserCreate(BaseModel):
    username : str
    password: str

    
