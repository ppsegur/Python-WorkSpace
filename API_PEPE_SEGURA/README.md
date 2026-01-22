# API Pepe Segura - Entertainment API 🎬

## Overview

A comprehensive FastAPI-based entertainment and movie management system with **8 complete entities** providing a full-featured movie database and user interaction platform.

## Version 2.0.0 - Big Update! 🚀

This major update expands the API from 2 basic entities (Users and Films) to a complete entertainment platform with 8 interconnected entities.

## Features

### Core Entities

1. **🎬 Movies (Peliculas)** - Complete movie database with details
2. **👥 Users** - User management and profiles
3. **🎭 Actors** - Actor profiles and biographies (NEW!)
4. **🎥 Directors** - Director information and filmographies (NEW!)
5. **⭐ Reviews** - User reviews with ratings and comments (NEW!)
6. **🎨 Genres** - Movie genre categorization (NEW!)
7. **📝 Watchlists** - Personal movie watchlists for users (NEW!)
8. **⭐ Ratings** - Film rating system with averages (NEW!)

## Quick Start

### Installation

```bash
# Install dependencies
pip install fastapi uvicorn pydantic pymongo

# Navigate to the API directory
cd API_PEPE_SEGURA

# Start the server
uvicorn main:app --reload
```

### Access the API

- **API Root**: http://localhost:8000/
- **Interactive Docs (Swagger)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc

## API Endpoints

### General Endpoints

- `GET /` - Welcome message and API information
- `GET /health` - Health check endpoint
- `GET /stats` - Get API statistics (entity counts)

### Movies (Peliculas)

- `GET /peliculas/` - List all movies
- `GET /peliculas/{id}` - Get movie by ID
- `POST /peliculas/` - Create new movie
- `PUT /peliculas/{id}` - Update movie
- `DELETE /peliculas/{id}` - Delete movie

### Users

- `GET /users` - List all users
- `GET /users/{id}` - Get user by ID
- `POST /user` - Create new user
- `PUT /user/{id}` - Update user
- `DELETE /user/{id}` - Delete user

### Actors 🎭

- `GET /actors/` - List all actors
- `GET /actors/{id}` - Get actor by ID
- `POST /actors/` - Create new actor
- `PUT /actors/{id}` - Update actor
- `DELETE /actors/{id}` - Delete actor

### Directors 🎥

- `GET /directors/` - List all directors
- `GET /directors/{id}` - Get director by ID
- `POST /directors/` - Create new director
- `PUT /directors/{id}` - Update director
- `DELETE /directors/{id}` - Delete director

### Reviews ⭐

- `GET /reviews/` - List all reviews (optional filters: ?film_id={id}, ?user_id={id})
- `GET /reviews/{id}` - Get review by ID
- `POST /reviews/` - Create new review
- `PUT /reviews/{id}` - Update review
- `DELETE /reviews/{id}` - Delete review

### Genres 🎨

- `GET /genres/` - List all genres
- `GET /genres/{id}` - Get genre by ID
- `POST /genres/` - Create new genre
- `PUT /genres/{id}` - Update genre
- `DELETE /genres/{id}` - Delete genre

### Watchlists 📝

- `GET /watchlists/` - List all watchlists (optional filter: ?user_id={id})
- `GET /watchlists/{id}` - Get watchlist by ID
- `POST /watchlists/` - Create new watchlist
- `PUT /watchlists/{id}` - Update watchlist
- `DELETE /watchlists/{id}` - Delete watchlist
- `POST /watchlists/{id}/films/{film_id}` - Add film to watchlist
- `DELETE /watchlists/{id}/films/{film_id}` - Remove film from watchlist

### Ratings ⭐

- `GET /ratings/` - List all ratings (optional filters: ?film_id={id}, ?user_id={id})
- `GET /ratings/{id}` - Get rating by ID
- `GET /ratings/film/{film_id}/average` - Get average rating for a film
- `POST /ratings/` - Create new rating
- `PUT /ratings/{id}` - Update rating
- `DELETE /ratings/{id}` - Delete rating

## Data Models

### Actor

```json
{
  "id": 1,
  "name": "Robert De Niro",
  "birthdate": "1943-08-17",
  "nationality": "USA",
  "biography": "Legendary American actor",
  "photo": "static/deniro.jpg"
}
```

### Director

```json
{
  "id": 1,
  "name": "Francis Ford Coppola",
  "birthdate": "1939-04-07",
  "nationality": "USA",
  "biography": "Director of The Godfather trilogy",
  "photo": "static/coppola.jpg",
  "awards": "5 Academy Awards"
}
```

### Review

```json
{
  "id": 1,
  "film_id": 1,
  "user_id": 1,
  "rating": 9.5,
  "comment": "Masterpiece! One of the best films ever made.",
  "date": "2024-01-15"
}
```

### Genre

```json
{
  "id": 1,
  "name": "Drama",
  "description": "Serious, plot-driven presentations depicting realistic characters"
}
```

### Watchlist

```json
{
  "id": 1,
  "user_id": 1,
  "name": "Must Watch Classics",
  "description": "Classic films I need to see",
  "film_ids": [1, 2, 3, 10],
  "created_date": "2024-01-10"
}
```

### Rating

```json
{
  "id": 1,
  "film_id": 1,
  "user_id": 1,
  "score": 9.5,
  "date": "2024-01-15"
}
```

## Example Usage

### Get all actors

```bash
curl http://localhost:8000/actors/
```

### Get average rating for a film

```bash
curl http://localhost:8000/ratings/film/1/average
```

### Get user's watchlists

```bash
curl http://localhost:8000/watchlists/?user_id=1
```

### Create a new review

```bash
curl -X POST http://localhost:8000/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": 6,
    "film_id": 7,
    "user_id": 1,
    "rating": 9.0,
    "comment": "Mind-blowing plot twists!",
    "date": "2024-01-20"
  }'
```

## API Statistics

Current database contains:
- 10 Films
- 5 Actors
- 5 Directors
- 5 Reviews
- 8 Genres
- 4 Watchlists
- 7 Ratings

## Technology Stack

- **FastAPI** - Modern, fast web framework
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server
- **Python 3.8+**

## Project Structure

```
API_PEPE_SEGURA/
├── main.py                 # Main application file
├── db/
│   ├── client.py          # Database client
│   ├── model/             # Pydantic models
│   │   ├── user.py
│   │   ├── film.py
│   │   ├── actor.py
│   │   ├── director.py
│   │   ├── review.py
│   │   ├── genre.py
│   │   ├── watchlist.py
│   │   └── rating.py
│   └── schema/            # MongoDB schemas
│       ├── user.py
│       ├── film.py
│       ├── actor.py
│       ├── director.py
│       ├── review.py
│       ├── genre.py
│       ├── watchlist.py
│       └── rating.py
├── routers/               # API routers
│   ├── users.py
│   ├── peliculas.py
│   ├── actors.py
│   ├── directors.py
│   ├── reviews.py
│   ├── genres.py
│   ├── watchlists.py
│   └── ratings.py
└── static/                # Static files (images, etc.)
```

## Future Enhancements

Potential improvements for future versions:
- Database integration (MongoDB, PostgreSQL)
- Authentication and authorization
- Search and filtering capabilities
- Pagination for large datasets
- Image upload functionality
- Social features (following users, sharing watchlists)
- Recommendation system
- Comments on reviews

## Contributing

This is an educational project. Feel free to fork and extend!

## License

MIT

## Author

Pepe Segura
