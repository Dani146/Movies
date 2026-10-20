from pydantic import BaseModel

class GenreCreate(BaseModel):

    genre: str