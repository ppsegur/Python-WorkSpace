from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/actors",
    tags=["actors"],
    responses={404: {"description": "Not found"}}
)


class Actor(BaseModel):
    id: int
    name: str
    birthdate: str
    nationality: str
    biography: str
    photo: str


actors_list = [
    Actor(id=1, name="Robert De Niro", birthdate="1943-08-17", nationality="USA", biography="Legendary American actor", photo="static/deniro.jpg"),
    Actor(id=2, name="Al Pacino", birthdate="1940-04-25", nationality="USA", biography="Iconic actor known for The Godfather", photo="static/pacino.jpg"),
    Actor(id=3, name="Leonardo DiCaprio", birthdate="1974-11-11", nationality="USA", biography="Oscar-winning actor", photo="static/dicaprio.jpg"),
    Actor(id=4, name="Tom Hanks", birthdate="1956-07-09", nationality="USA", biography="Beloved American actor", photo="static/hanks.jpg"),
    Actor(id=5, name="Morgan Freeman", birthdate="1937-06-01", nationality="USA", biography="Distinguished actor with iconic voice", photo="static/freeman.jpg"),
]


@router.get("/")
async def get_actors():
    return actors_list


@router.get("/{actor_id}")
async def get_actor_by_id(actor_id: int):
    actor = filter(lambda a: a.id == actor_id, actors_list)
    try:
        return list(actor)[0]
    except:
        raise HTTPException(status_code=404, detail="Actor not found")


def search_actor(id):
    actor = filter(lambda a: a.id == id, actors_list)
    try:
        return list(actor)[0]
    except:
        return {"error": "Actor not found"}


@router.post("/", status_code=201)
async def create_actor(actor: Actor):
    if type(search_actor(actor.id)) == Actor:
        raise HTTPException(status_code=409, detail="Actor already exists")
    actors_list.append(actor)
    return {"message": "Actor created successfully", "actor": actor}


@router.put("/{actor_id}")
async def update_actor(actor_id: int, actor: Actor):
    found = False
    for index, saved_actor in enumerate(actors_list):
        if saved_actor.id == actor_id:
            actors_list[index] = actor
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Actor not found")
    return {"message": "Actor updated successfully", "actor": actor}


@router.delete("/{actor_id}")
async def delete_actor(actor_id: int):
    found = False
    for index, saved_actor in enumerate(actors_list):
        if saved_actor.id == actor_id:
            actors_list.pop(index)
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Actor not found")
    return {"message": "Actor deleted successfully"}
