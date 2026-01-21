from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/directors",
    tags=["directors"],
    responses={404: {"description": "Not found"}}
)


class Director(BaseModel):
    id: int
    name: str
    birthdate: str
    nationality: str
    biography: str
    photo: str
    awards: str


directors_list = [
    Director(id=1, name="Francis Ford Coppola", birthdate="1939-04-07", nationality="USA", biography="Director of The Godfather trilogy", photo="static/coppola.jpg", awards="5 Academy Awards"),
    Director(id=2, name="Quentin Tarantino", birthdate="1963-03-27", nationality="USA", biography="Acclaimed director known for unique style", photo="static/tarantino.jpg", awards="2 Academy Awards"),
    Director(id=3, name="Christopher Nolan", birthdate="1970-07-30", nationality="UK", biography="Master of complex narratives", photo="static/nolan.jpg", awards="Multiple nominations"),
    Director(id=4, name="David Fincher", birthdate="1962-08-28", nationality="USA", biography="Known for psychological thrillers", photo="static/fincher.jpg", awards="Multiple nominations"),
    Director(id=5, name="Steven Spielberg", birthdate="1946-12-18", nationality="USA", biography="One of the most influential directors", photo="static/spielberg.jpg", awards="3 Academy Awards"),
]


@router.get("/")
async def get_directors():
    return directors_list


@router.get("/{director_id}")
async def get_director_by_id(director_id: int):
    director = filter(lambda d: d.id == director_id, directors_list)
    try:
        return list(director)[0]
    except:
        raise HTTPException(status_code=404, detail="Director not found")


def search_director(id):
    director = filter(lambda d: d.id == id, directors_list)
    try:
        return list(director)[0]
    except:
        return {"error": "Director not found"}


@router.post("/", status_code=201)
async def create_director(director: Director):
    if type(search_director(director.id)) == Director:
        raise HTTPException(status_code=409, detail="Director already exists")
    directors_list.append(director)
    return {"message": "Director created successfully", "director": director}


@router.put("/{director_id}")
async def update_director(director_id: int, director: Director):
    found = False
    for index, saved_director in enumerate(directors_list):
        if saved_director.id == director_id:
            directors_list[index] = director
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Director not found")
    return {"message": "Director updated successfully", "director": director}


@router.delete("/{director_id}")
async def delete_director(director_id: int):
    found = False
    for index, saved_director in enumerate(directors_list):
        if saved_director.id == director_id:
            directors_list.pop(index)
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Director not found")
    return {"message": "Director deleted successfully"}
