from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
    responses={404: {"description": "Not found"}}
)


class Review(BaseModel):
    id: int
    film_id: int
    user_id: int
    rating: float
    comment: str
    date: str


reviews_list = [
    Review(id=1, film_id=1, user_id=1, rating=9.5, comment="Masterpiece! One of the best films ever made.", date="2024-01-15"),
    Review(id=2, film_id=1, user_id=2, rating=9.0, comment="Incredible storytelling and performances.", date="2024-01-16"),
    Review(id=3, film_id=2, user_id=1, rating=9.3, comment="Even better than the first one!", date="2024-01-17"),
    Review(id=4, film_id=5, user_id=3, rating=8.8, comment="Mind-bending and brilliant.", date="2024-01-18"),
    Review(id=5, film_id=10, user_id=2, rating=9.7, comment="A true cinematic triumph.", date="2024-01-19"),
]


@router.get("/")
async def get_reviews(film_id: Optional[int] = None, user_id: Optional[int] = None):
    if film_id:
        return [r for r in reviews_list if r.film_id == film_id]
    if user_id:
        return [r for r in reviews_list if r.user_id == user_id]
    return reviews_list


@router.get("/{review_id}")
async def get_review_by_id(review_id: int):
    review = filter(lambda r: r.id == review_id, reviews_list)
    try:
        return list(review)[0]
    except:
        raise HTTPException(status_code=404, detail="Review not found")


def search_review(id):
    review = filter(lambda r: r.id == id, reviews_list)
    try:
        return list(review)[0]
    except:
        return {"error": "Review not found"}


@router.post("/", status_code=201)
async def create_review(review: Review):
    if type(search_review(review.id)) == Review:
        raise HTTPException(status_code=409, detail="Review already exists")
    reviews_list.append(review)
    return {"message": "Review created successfully", "review": review}


@router.put("/{review_id}")
async def update_review(review_id: int, review: Review):
    found = False
    for index, saved_review in enumerate(reviews_list):
        if saved_review.id == review_id:
            reviews_list[index] = review
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Review not found")
    return {"message": "Review updated successfully", "review": review}


@router.delete("/{review_id}")
async def delete_review(review_id: int):
    found = False
    for index, saved_review in enumerate(reviews_list):
        if saved_review.id == review_id:
            reviews_list.pop(index)
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Review not found")
    return {"message": "Review deleted successfully"}
