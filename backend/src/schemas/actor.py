from pydantic import BaseModel
from datetime import date

class ActorCreate(BaseModel):
    name : str
    surname : str
    birthdate : date