def review_schema(review) -> dict:
    return {
        "id": str(review["_id"]),
        "film_id": review["film_id"],
        "user_id": review["user_id"],
        "rating": review["rating"],
        "comment": review["comment"],
        "date": review["date"]
    }


def reviews_schema(reviews) -> list:
    return [review_schema(review) for review in reviews]
