from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/genres",
    tags=["genres"],
    responses={404: {"description": "Not found"}}
)


class Genre(BaseModel):
    id: int
    name: str
    description: str


genres_list = [
    Genre(id=1, name="Drama", description="Serious, plot-driven presentations depicting realistic characters"),
    Genre(id=2, name="Action", description="Fast-paced films featuring physical stunts and chases"),
    Genre(id=3, name="Comedy", description="Films designed to elicit laughter from the audience"),
    Genre(id=4, name="Sci-Fi", description="Science fiction films exploring futuristic concepts"),
    Genre(id=5, name="Thriller", description="Suspenseful films that keep viewers on edge"),
    Genre(id=6, name="Horror", description="Films designed to frighten and invoke fear"),
    Genre(id=7, name="Romance", description="Films focusing on love and romantic relationships"),
    Genre(id=8, name="Crime", description="Films involving criminal activities and investigations"),
]


@router.get("/")
async def get_genres():
    return genres_list


@router.get("/{genre_id}")
async def get_genre_by_id(genre_id: int):
    genre = filter(lambda g: g.id == genre_id, genres_list)
    try:
        return list(genre)[0]
    except:
        raise HTTPException(status_code=404, detail="Genre not found")


def search_genre(id):
    genre = filter(lambda g: g.id == id, genres_list)
    try:
        return list(genre)[0]
    except:
        return {"error": "Genre not found"}


@router.post("/", status_code=201)
async def create_genre(genre: Genre):
    if type(search_genre(genre.id)) == Genre:
        raise HTTPException(status_code=409, detail="Genre already exists")
    genres_list.append(genre)
    return {"message": "Genre created successfully", "genre": genre}


@router.put("/{genre_id}")
async def update_genre(genre_id: int, genre: Genre):
    found = False
    for index, saved_genre in enumerate(genres_list):
        if saved_genre.id == genre_id:
            genres_list[index] = genre
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Genre not found")
    return {"message": "Genre updated successfully", "genre": genre}


@router.delete("/{genre_id}")
async def delete_genre(genre_id: int):
    found = False
    for index, saved_genre in enumerate(genres_list):
        if saved_genre.id == genre_id:
            genres_list.pop(index)
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Genre not found")
    return {"message": "Genre deleted successfully"}
