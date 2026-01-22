def rating_schema(rating) -> dict:
    return {
        "id": str(rating["_id"]),
        "film_id": rating["film_id"],
        "user_id": rating["user_id"],
        "score": rating["score"],
        "date": rating["date"]
    }


def ratings_schema(ratings) -> list:
    return [rating_schema(rating) for rating in ratings]
