from pydantic import BaseModel
from typing import Optional, List


class Watchlist(BaseModel):
    id: Optional[str]
    user_id: int
    name: str
    description: str
    film_ids: List[int]
    created_date: str
