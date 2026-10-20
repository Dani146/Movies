from pydantic import BaseModel


class SeriesInteractionUpdate(BaseModel):
    liked: bool | None = None
    watched: bool | None = None 
    warchlist: bool | None = None
    favourite: bool | None = None
    rating: float | None = None
