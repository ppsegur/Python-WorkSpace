def film_schema(film) -> dict:
    return {"id": str(film["_id"]),
            "title": film["title"],
            "year": film["year"],
            "director": film["director"],
            "genre": film["genre"],
            "country": film["country"],
            "language": film["language"],
            "plot": film["plot"],
            "poster": film["poster"],
            "imdbRating": film["imdbRating"],
            "imdbID": film["imdbID"]}



def film_schema(filmes) -> list:
    return [film_schema(film) for film in filmes]