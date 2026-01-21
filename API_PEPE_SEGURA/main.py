from fastapi import FastAPI 
from routers import users, peliculas, actors, directors, reviews, genres, watchlists, ratings
from fastapi.staticfiles import StaticFiles

# API metadata and documentation
app = FastAPI(
    title="API Pepe Segura - Entertainment API",
    description="""
    # 🎬 Entertainment & Movie Management API
    
    A comprehensive API for managing movies, users, and entertainment content.
    
    ## Features
    
    * **Movies** - Complete movie database with details
    * **Users** - User management and profiles
    * **Actors** - Actor profiles and biographies
    * **Directors** - Director information and filmographies
    * **Reviews** - User reviews and ratings for films
    * **Genres** - Movie genre categorization
    * **Watchlists** - Personal movie watchlists for users
    * **Ratings** - Film rating system with averages
    
    ## Endpoints
    
    All endpoints support standard CRUD operations (Create, Read, Update, Delete).
    """,
    version="2.0.0",
    contact={
        "name": "Pepe Segura",
        "email": "pepe@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

#Routers - Now with 8 complete entities!
app.include_router(users.router)
app.include_router(peliculas.router)
app.include_router(actors.router)
app.include_router(directors.router)
app.include_router(reviews.router)
app.include_router(genres.router)
app.include_router(watchlists.router)
app.include_router(ratings.router)

app.mount("/static", StaticFiles(directory="static"), 
          name="static")



@app.get("/", tags=["root"])
async def root():
    """
    Welcome endpoint - Returns API information and available endpoints
    """
    return {
        "message": "Welcome to API Pepe Segura - Entertainment API",
        "version": "2.0.0",
        "status": "active",
        "entities": {
            "users": "/users",
            "peliculas": "/peliculas",
            "actors": "/actors",
            "directors": "/directors",
            "reviews": "/reviews",
            "genres": "/genres",
            "watchlists": "/watchlists",
            "ratings": "/ratings"
        },
        "documentation": {
            "swagger": "/docs",
            "redoc": "/redoc"
        }
    }


@app.get("/health", tags=["health"])
async def health_check():
    """
    Health check endpoint - Verify API is running
    """
    return {
        "status": "healthy",
        "api": "API Pepe Segura",
        "version": "2.0.0"
    }


@app.get("/stats", tags=["statistics"])
async def get_stats():
    """
    Get API statistics - Number of entities and records
    """
    from routers.peliculas import peliculas_list
    from routers.actors import actors_list
    from routers.directors import directors_list
    from routers.reviews import reviews_list
    from routers.genres import genres_list
    from routers.watchlists import watchlists_list
    from routers.ratings import ratings_list
    
    return {
        "total_entities": 8,
        "counts": {
            "films": len(peliculas_list),
            "actors": len(actors_list),
            "directors": len(directors_list),
            "reviews": len(reviews_list),
            "genres": len(genres_list),
            "watchlists": len(watchlists_list),
            "ratings": len(ratings_list)
        }
    }

