import { useState, useEffect } from 'react';
import { getGenres } from '../services/api';
import './Genres.css';

function Genres() {
  const [genres, setGenres] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchGenres = async () => {
      try {
        const response = await getGenres();
        setGenres(response.data);
      } catch (err) {
        setError('Failed to load genres');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchGenres();
  }, []);

  if (loading) return <div className="loading">Loading genres...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="genres-page">
      <header className="genres-header">
        <h1>🎨 Genres</h1>
        <p>Explore movie categories</p>
      </header>

      <div className="genres-grid">
        {genres.map(genre => (
          <div key={genre.id} className="genre-card">
            <h3>{genre.name}</h3>
            <p>{genre.description}</p>
          </div>
        ))}
      </div>

      {genres.length === 0 && (
        <div className="no-genres">
          <p>No genres available.</p>
        </div>
      )}
    </div>
  );
}

export default Genres;
