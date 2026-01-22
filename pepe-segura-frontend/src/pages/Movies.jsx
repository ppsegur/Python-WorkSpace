import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getMovies, getGenres } from '../services/api';
import './Movies.css';

function Movies() {
  const [movies, setMovies] = useState([]);
  const [genres, setGenres] = useState([]);
  const [selectedGenre, setSelectedGenre] = useState('all');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [moviesRes, genresRes] = await Promise.all([
          getMovies(),
          getGenres()
        ]);
        setMovies(moviesRes.data);
        setGenres(genresRes.data);
      } catch (err) {
        setError('Failed to load movies. Please make sure the API is running on http://localhost:8000');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const filteredMovies = selectedGenre === 'all' 
    ? movies 
    : movies.filter(movie => movie.genero === selectedGenre);

  if (loading) {
    return <div className="loading">Loading movies...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="movies-page">
      <header className="movies-header">
        <h1>🎬 Movies Collection</h1>
        <p>Browse our extensive library of films</p>
      </header>

      <div className="filters">
        <label htmlFor="genre-filter">Filter by Genre:</label>
        <select 
          id="genre-filter"
          value={selectedGenre} 
          onChange={(e) => setSelectedGenre(e.target.value)}
          className="genre-select"
        >
          <option value="all">All Genres</option>
          {genres.map(genre => (
            <option key={genre.id} value={genre.name}>
              {genre.name}
            </option>
          ))}
        </select>
        <span className="movie-count">{filteredMovies.length} movies</span>
      </div>

      <div className="movies-grid">
        {filteredMovies.map(movie => (
          <Link to={`/movies/${movie.id}`} key={movie.id} className="movie-card">
            <div className="movie-poster">
              <img 
                src={`http://localhost:8000/${movie.portada}`} 
                alt={movie.nombre}
                onError={(e) => {
                  e.target.src = 'https://via.placeholder.com/300x450?text=No+Image';
                }}
              />
            </div>
            <div className="movie-info">
              <h3>{movie.nombre}</h3>
              <p className="movie-year">{movie.anio}</p>
              <p className="movie-genre">{movie.genero}</p>
              <p className="movie-director">Director: {movie.director}</p>
              <p className="movie-duration">{movie.duracion} min</p>
            </div>
          </Link>
        ))}
      </div>

      {filteredMovies.length === 0 && (
        <div className="no-movies">
          <p>No movies found for the selected genre.</p>
        </div>
      )}
    </div>
  );
}

export default Movies;
