import axios from 'axios';

// API Base URL - Update this if backend is deployed elsewhere
const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Movies (Peliculas)
export const getMovies = () => api.get('/peliculas/');
export const getMovie = (id) => api.get(`/peliculas/${id}`);
export const createMovie = (movie) => api.post('/peliculas/', movie);
export const updateMovie = (id, movie) => api.put(`/peliculas/${id}`, movie);
export const deleteMovie = (id) => api.delete(`/peliculas/${id}`);

// Actors
export const getActors = () => api.get('/actors/');
export const getActor = (id) => api.get(`/actors/${id}`);
export const createActor = (actor) => api.post('/actors/', actor);
export const updateActor = (id, actor) => api.put(`/actors/${id}`, actor);
export const deleteActor = (id) => api.delete(`/actors/${id}`);

// Directors
export const getDirectors = () => api.get('/directors/');
export const getDirector = (id) => api.get(`/directors/${id}`);
export const createDirector = (director) => api.post('/directors/', director);
export const updateDirector = (id, director) => api.put(`/directors/${id}`, director);
export const deleteDirector = (id) => api.delete(`/directors/${id}`);

// Reviews
export const getReviews = () => api.get('/reviews/');
export const getReview = (id) => api.get(`/reviews/${id}`);
export const createReview = (review) => api.post('/reviews/', review);
export const updateReview = (id, review) => api.put(`/reviews/${id}`, review);
export const deleteReview = (id) => api.delete(`/reviews/${id}`);

// Genres
export const getGenres = () => api.get('/genres/');
export const getGenre = (id) => api.get(`/genres/${id}`);

// Watchlists
export const getWatchlists = () => api.get('/watchlists/');
export const getWatchlist = (id) => api.get(`/watchlists/${id}`);
export const createWatchlist = (watchlist) => api.post('/watchlists/', watchlist);
export const updateWatchlist = (id, watchlist) => api.put(`/watchlists/${id}`, watchlist);
export const deleteWatchlist = (id) => api.delete(`/watchlists/${id}`);

// Ratings
export const getRatings = () => api.get('/ratings/');
export const getRating = (id) => api.get(`/ratings/${id}`);
export const getFilmAverageRating = (filmId) => api.get(`/ratings/film/${filmId}/average`);
export const createRating = (rating) => api.post('/ratings/', rating);
export const updateRating = (id, rating) => api.put(`/ratings/${id}`, rating);
export const deleteRating = (id) => api.delete(`/ratings/${id}`);

// Users
export const getUsers = () => api.get('/users');
export const getUser = (id) => api.get(`/users/${id}`);

// Health & Stats
export const getHealth = () => api.get('/health');
export const getStats = () => api.get('/stats');

export default api;
