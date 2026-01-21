from pydantic import BaseModel
from typing import Optional


class Rating(BaseModel):
    id: Optional[str]
    film_id: int
    user_id: int
    score: float
    date: str
