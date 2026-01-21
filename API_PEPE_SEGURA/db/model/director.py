from pydantic import BaseModel
from typing import Optional


class Director(BaseModel):
    id: Optional[str]
    name: str
    birthdate: str
    nationality: str
    biography: str
    photo: str
    awards: str
