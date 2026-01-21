def genre_schema(genre) -> dict:
    return {
        "id": str(genre["_id"]),
        "name": genre["name"],
        "description": genre["description"]
    }


def genres_schema(genres) -> list:
    return [genre_schema(genre) for genre in genres]
