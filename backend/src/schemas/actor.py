from pydantic import BaseModel

class ActorCreate(BaseModel):
    name : str
    surname : str
    age : int