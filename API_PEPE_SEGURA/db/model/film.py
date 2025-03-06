from pydantic import BaseModel
from typing import Optional


class Film(BaseModel):
    id: Optional[str]
    title: str
    director: str
    year: int
    genre: str
    rating: float
    duration: int
    actors: str
    plot: str
    poster: str
    trailer: str
    country: str