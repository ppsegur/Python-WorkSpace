from pydantic import BaseModel
from typing import Optional


class Review(BaseModel):
    id: Optional[str]
    film_id: int
    user_id: int
    rating: float
    comment: str
    date: str
