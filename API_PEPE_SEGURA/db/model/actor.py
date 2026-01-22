from pydantic import BaseModel
from typing import Optional


class Actor(BaseModel):
    id: Optional[str]
    name: str
    birthdate: str
    nationality: str
    biography: str
    photo: str
