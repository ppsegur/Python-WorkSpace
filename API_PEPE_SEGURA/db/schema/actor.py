def actor_schema(actor) -> dict:
    return {
        "id": str(actor["_id"]),
        "name": actor["name"],
        "birthdate": actor["birthdate"],
        "nationality": actor["nationality"],
        "biography": actor["biography"],
        "photo": actor["photo"]
    }


def actors_schema(actors) -> list:
    return [actor_schema(actor) for actor in actors]
