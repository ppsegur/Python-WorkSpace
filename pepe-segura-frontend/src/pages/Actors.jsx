import { useState, useEffect } from 'react';
import { getActors } from '../services/api';
import './Actors.css';

function Actors() {
  const [actors, setActors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActors = async () => {
      try {
        const response = await getActors();
        setActors(response.data);
      } catch (err) {
        setError('Failed to load actors');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchActors();
  }, []);

  if (loading) return <div className="loading">Loading actors...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="actors-page">
      <header className="actors-header">
        <h1>🎭 Actors</h1>
        <p>Discover talented performers</p>
      </header>

      <div className="actors-grid">
        {actors.map(actor => (
          <div key={actor.id} className="actor-card">
            <div className="actor-photo">
              <img 
                src={`http://localhost:8000/${actor.photo}`} 
                alt={actor.name}
                onError={(e) => {
                  e.target.src = 'https://via.placeholder.com/200x200?text=Actor';
                }}
              />
            </div>
            <div className="actor-info">
              <h3>{actor.name}</h3>
              <p className="actor-nationality">🌍 {actor.nationality}</p>
              <p className="actor-birthdate">📅 {actor.birthdate}</p>
              <p className="actor-bio">{actor.biography}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Actors;
