import { useState, useEffect } from 'react';
import { getWatchlists, getMovies } from '../services/api';
import './Watchlists.css';

function Watchlists() {
  const [watchlists, setWatchlists] = useState([]);
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [watchlistsRes, moviesRes] = await Promise.all([
          getWatchlists(),
          getMovies()
        ]);
        setWatchlists(watchlistsRes.data);
        setMovies(moviesRes.data);
      } catch (err) {
        setError('Failed to load watchlists');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const getMovieNames = (filmIds) => {
    return filmIds.map(id => {
      const movie = movies.find(m => m.id === id);
      return movie ? movie.nombre : `Film #${id}`;
    });
  };

  if (loading) return <div className="loading">Loading watchlists...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="watchlists-page">
      <header className="watchlists-header">
        <h1>📝 Watchlists</h1>
        <p>Curated collections of must-watch films</p>
      </header>

      <div className="watchlists-grid">
        {watchlists.map(watchlist => (
          <div key={watchlist.id} className="watchlist-card">
            <div className="watchlist-header">
              <h3>{watchlist.name}</h3>
              <span className="watchlist-count">{watchlist.film_ids.length} films</span>
            </div>
            <p className="watchlist-description">{watchlist.description}</p>
            <div className="watchlist-films">
              <h4>Films in this list:</h4>
              <ul>
                {getMovieNames(watchlist.film_ids).map((name, index) => (
                  <li key={index}>{name}</li>
                ))}
              </ul>
            </div>
            <div className="watchlist-footer">
              <span className="watchlist-user">By User #{watchlist.user_id}</span>
              <span className="watchlist-date">Created: {watchlist.created_date}</span>
            </div>
          </div>
        ))}
      </div>

      {watchlists.length === 0 && (
        <div className="no-watchlists">
          <p>No watchlists yet. Create your first one!</p>
        </div>
      )}
    </div>
  );
}

export default Watchlists;
