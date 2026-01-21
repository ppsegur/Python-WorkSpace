def watchlist_schema(watchlist) -> dict:
    return {
        "id": str(watchlist["_id"]),
        "user_id": watchlist["user_id"],
        "name": watchlist["name"],
        "description": watchlist["description"],
        "film_ids": watchlist["film_ids"],
        "created_date": watchlist["created_date"]
    }


def watchlists_schema(watchlists) -> list:
    return [watchlist_schema(watchlist) for watchlist in watchlists]
