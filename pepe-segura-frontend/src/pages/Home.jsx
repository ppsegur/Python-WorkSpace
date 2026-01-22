import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getStats, getHealth } from '../services/api';
import './Home.css';

function Home() {
  const [stats, setStats] = useState(null);
  const [health, setHealth] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [statsRes, healthRes] = await Promise.all([
          getStats(),
          getHealth()
        ]);
        setStats(statsRes.data);
        setHealth(healthRes.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="home">
      <header className="hero">
        <h1>🎬 API Pepe Segura</h1>
        <p className="subtitle">Entertainment & Movie Management System</p>
        {health && (
          <div className="health-badge">
            Status: <span className="status-healthy">{health.status}</span>
          </div>
        )}
      </header>

      <section className="stats-section">
        <h2>Database Statistics</h2>
        {stats && (
          <div className="stats-grid">
            <div className="stat-card">
              <span className="stat-number">{stats.counts.films}</span>
              <span className="stat-label">Films</span>
            </div>
            <div className="stat-card">
              <span className="stat-number">{stats.counts.actors}</span>
              <span className="stat-label">Actors</span>
            </div>
            <div className="stat-card">
              <span className="stat-number">{stats.counts.directors}</span>
              <span className="stat-label">Directors</span>
            </div>
            <div className="stat-card">
              <span className="stat-number">{stats.counts.reviews}</span>
              <span className="stat-label">Reviews</span>
            </div>
            <div className="stat-card">
              <span className="stat-number">{stats.counts.genres}</span>
              <span className="stat-label">Genres</span>
            </div>
            <div className="stat-card">
              <span className="stat-number">{stats.counts.watchlists}</span>
              <span className="stat-label">Watchlists</span>
            </div>
            <div className="stat-card">
              <span className="stat-number">{stats.counts.ratings}</span>
              <span className="stat-label">Ratings</span>
            </div>
          </div>
        )}
      </section>

      <section className="features-section">
        <h2>Explore the Platform</h2>
        <div className="features-grid">
          <Link to="/movies" className="feature-card">
            <div className="feature-icon">🎬</div>
            <h3>Movies</h3>
            <p>Browse our collection of films</p>
          </Link>
          <Link to="/actors" className="feature-card">
            <div className="feature-icon">🎭</div>
            <h3>Actors</h3>
            <p>Discover talented performers</p>
          </Link>
          <Link to="/directors" className="feature-card">
            <div className="feature-icon">🎥</div>
            <h3>Directors</h3>
            <p>Learn about visionary directors</p>
          </Link>
          <Link to="/reviews" className="feature-card">
            <div className="feature-icon">⭐</div>
            <h3>Reviews</h3>
            <p>Read and write film reviews</p>
          </Link>
          <Link to="/watchlists" className="feature-card">
            <div className="feature-icon">📝</div>
            <h3>Watchlists</h3>
            <p>Manage your personal watchlists</p>
          </Link>
          <Link to="/genres" className="feature-card">
            <div className="feature-icon">🎨</div>
            <h3>Genres</h3>
            <p>Explore movie categories</p>
          </Link>
        </div>
      </section>
    </div>
  );
}

export default Home;
