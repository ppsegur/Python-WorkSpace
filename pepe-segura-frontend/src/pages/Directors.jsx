import { useState, useEffect } from 'react';
import { getDirectors } from '../services/api';
import './Directors.css';

function Directors() {
  const [directors, setDirectors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDirectors = async () => {
      try {
        const response = await getDirectors();
        setDirectors(response.data);
      } catch (err) {
        setError('Failed to load directors');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchDirectors();
  }, []);

  if (loading) return <div className="loading">Loading directors...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="directors-page">
      <header className="directors-header">
        <h1>🎥 Directors</h1>
        <p>Learn about visionary directors</p>
      </header>

      <div className="directors-grid">
        {directors.map(director => (
          <div key={director.id} className="director-card">
            <div className="director-photo">
              <img 
                src={`http://localhost:8000/${director.photo}`} 
                alt={director.name}
                onError={(e) => {
                  e.target.src = 'https://via.placeholder.com/200x200?text=Director';
                }}
              />
            </div>
            <div className="director-info">
              <h3>{director.name}</h3>
              <p className="director-nationality">🌍 {director.nationality}</p>
              <p className="director-birthdate">📅 {director.birthdate}</p>
              {director.awards && (
                <p className="director-awards">🏆 {director.awards}</p>
              )}
              <p className="director-bio">{director.biography}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Directors;
