from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/ratings",
    tags=["ratings"],
    responses={404: {"description": "Not found"}}
)


class Rating(BaseModel):
    id: int
    film_id: int
    user_id: int
    score: float
    date: str


ratings_list = [
    Rating(id=1, film_id=1, user_id=1, score=9.5, date="2024-01-15"),
    Rating(id=2, film_id=1, user_id=2, score=9.0, date="2024-01-16"),
    Rating(id=3, film_id=2, user_id=1, score=9.3, date="2024-01-17"),
    Rating(id=4, film_id=5, user_id=3, score=8.8, date="2024-01-18"),
    Rating(id=5, film_id=10, user_id=2, score=9.7, date="2024-01-19"),
    Rating(id=6, film_id=6, user_id=1, score=9.0, date="2024-01-20"),
    Rating(id=7, film_id=9, user_id=3, score=8.5, date="2024-01-21"),
]


@router.get("/")
async def get_ratings(film_id: Optional[int] = None, user_id: Optional[int] = None):
    if film_id:
        return [r for r in ratings_list if r.film_id == film_id]
    if user_id:
        return [r for r in ratings_list if r.user_id == user_id]
    return ratings_list


@router.get("/{rating_id}")
async def get_rating_by_id(rating_id: int):
    rating = filter(lambda r: r.id == rating_id, ratings_list)
    try:
        return list(rating)[0]
    except:
        raise HTTPException(status_code=404, detail="Rating not found")


@router.get("/film/{film_id}/average")
async def get_average_rating(film_id: int):
    film_ratings = [r for r in ratings_list if r.film_id == film_id]
    if not film_ratings:
        raise HTTPException(status_code=404, detail="No ratings found for this film")
    
    avg = sum(r.score for r in film_ratings) / len(film_ratings)
    return {
        "film_id": film_id,
        "average_rating": round(avg, 2),
        "total_ratings": len(film_ratings)
    }


def search_rating(id):
    rating = filter(lambda r: r.id == id, ratings_list)
    try:
        return list(rating)[0]
    except:
        return {"error": "Rating not found"}


@router.post("/", status_code=201)
async def create_rating(rating: Rating):
    if type(search_rating(rating.id)) == Rating:
        raise HTTPException(status_code=409, detail="Rating already exists")
    ratings_list.append(rating)
    return {"message": "Rating created successfully", "rating": rating}


@router.put("/{rating_id}")
async def update_rating(rating_id: int, rating: Rating):
    found = False
    for index, saved_rating in enumerate(ratings_list):
        if saved_rating.id == rating_id:
            ratings_list[index] = rating
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Rating not found")
    return {"message": "Rating updated successfully", "rating": rating}


@router.delete("/{rating_id}")
async def delete_rating(rating_id: int):
    found = False
    for index, saved_rating in enumerate(ratings_list):
        if saved_rating.id == rating_id:
            ratings_list.pop(index)
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Rating not found")
    return {"message": "Rating deleted successfully"}
