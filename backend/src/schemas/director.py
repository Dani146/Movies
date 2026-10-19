from pydantic import BaseModel
from datetime import date

class DirectorCreate(BaseModel):
    name: str
    surname: str
    birthdate: date
    biography: str