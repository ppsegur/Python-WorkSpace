import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link to="/" className="nav-logo">
          🎬 API Pepe Segura
        </Link>
        <ul className="nav-menu">
          <li className="nav-item">
            <Link to="/" className="nav-link">Home</Link>
          </li>
          <li className="nav-item">
            <Link to="/movies" className="nav-link">Movies</Link>
          </li>
          <li className="nav-item">
            <Link to="/actors" className="nav-link">Actors</Link>
          </li>
          <li className="nav-item">
            <Link to="/directors" className="nav-link">Directors</Link>
          </li>
          <li className="nav-item">
            <Link to="/reviews" className="nav-link">Reviews</Link>
          </li>
          <li className="nav-item">
            <Link to="/watchlists" className="nav-link">Watchlists</Link>
          </li>
          <li className="nav-item">
            <Link to="/genres" className="nav-link">Genres</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
