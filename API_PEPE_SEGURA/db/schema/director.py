def director_schema(director) -> dict:
    return {
        "id": str(director["_id"]),
        "name": director["name"],
        "birthdate": director["birthdate"],
        "nationality": director["nationality"],
        "biography": director["biography"],
        "photo": director["photo"],
        "awards": director["awards"]
    }


def directors_schema(directors) -> list:
    return [director_schema(director) for director in directors]
