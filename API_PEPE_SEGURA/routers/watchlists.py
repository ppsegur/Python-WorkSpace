from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(
    prefix="/watchlists",
    tags=["watchlists"],
    responses={404: {"description": "Not found"}}
)


class Watchlist(BaseModel):
    id: int
    user_id: int
    name: str
    description: str
    film_ids: List[int]
    created_date: str


watchlists_list = [
    Watchlist(id=1, user_id=1, name="Must Watch Classics", description="Classic films I need to see", film_ids=[1, 2, 3, 10], created_date="2024-01-10"),
    Watchlist(id=2, user_id=1, name="Nolan Collection", description="All Christopher Nolan films", film_ids=[5, 6], created_date="2024-01-11"),
    Watchlist(id=3, user_id=2, name="Action Pack", description="Best action movies", film_ids=[6, 9], created_date="2024-01-12"),
    Watchlist(id=4, user_id=3, name="Weekend Picks", description="Movies for the weekend", film_ids=[4, 7, 8], created_date="2024-01-13"),
]


@router.get("/")
async def get_watchlists(user_id: Optional[int] = None):
    if user_id:
        return [w for w in watchlists_list if w.user_id == user_id]
    return watchlists_list


@router.get("/{watchlist_id}")
async def get_watchlist_by_id(watchlist_id: int):
    watchlist = filter(lambda w: w.id == watchlist_id, watchlists_list)
    try:
        return list(watchlist)[0]
    except:
        raise HTTPException(status_code=404, detail="Watchlist not found")


def search_watchlist(id):
    watchlist = filter(lambda w: w.id == id, watchlists_list)
    try:
        return list(watchlist)[0]
    except:
        return {"error": "Watchlist not found"}


@router.post("/", status_code=201)
async def create_watchlist(watchlist: Watchlist):
    if type(search_watchlist(watchlist.id)) == Watchlist:
        raise HTTPException(status_code=409, detail="Watchlist already exists")
    watchlists_list.append(watchlist)
    return {"message": "Watchlist created successfully", "watchlist": watchlist}


@router.put("/{watchlist_id}")
async def update_watchlist(watchlist_id: int, watchlist: Watchlist):
    found = False
    for index, saved_watchlist in enumerate(watchlists_list):
        if saved_watchlist.id == watchlist_id:
            watchlists_list[index] = watchlist
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Watchlist not found")
    return {"message": "Watchlist updated successfully", "watchlist": watchlist}


@router.delete("/{watchlist_id}")
async def delete_watchlist(watchlist_id: int):
    found = False
    for index, saved_watchlist in enumerate(watchlists_list):
        if saved_watchlist.id == watchlist_id:
            watchlists_list.pop(index)
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Watchlist not found")
    return {"message": "Watchlist deleted successfully"}


@router.post("/{watchlist_id}/films/{film_id}")
async def add_film_to_watchlist(watchlist_id: int, film_id: int):
    watchlist = search_watchlist(watchlist_id)
    if type(watchlist) != Watchlist:
        raise HTTPException(status_code=404, detail="Watchlist not found")
    
    if film_id not in watchlist.film_ids:
        watchlist.film_ids.append(film_id)
        return {"message": "Film added to watchlist"}
    else:
        raise HTTPException(status_code=409, detail="Film already in watchlist")


@router.delete("/{watchlist_id}/films/{film_id}")
async def remove_film_from_watchlist(watchlist_id: int, film_id: int):
    watchlist = search_watchlist(watchlist_id)
    if type(watchlist) != Watchlist:
        raise HTTPException(status_code=404, detail="Watchlist not found")
    
    if film_id in watchlist.film_ids:
        watchlist.film_ids.remove(film_id)
        return {"message": "Film removed from watchlist"}
    else:
        raise HTTPException(status_code=404, detail="Film not found in watchlist")
