import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Movies from './pages/Movies';
import MovieDetail from './pages/MovieDetail';
import Actors from './pages/Actors';
import Directors from './pages/Directors';
import Reviews from './pages/Reviews';
import Watchlists from './pages/Watchlists';
import Genres from './pages/Genres';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Navbar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/movies" element={<Movies />} />
            <Route path="/movies/:id" element={<MovieDetail />} />
            <Route path="/actors" element={<Actors />} />
            <Route path="/directors" element={<Directors />} />
            <Route path="/reviews" element={<Reviews />} />
            <Route path="/watchlists" element={<Watchlists />} />
            <Route path="/genres" element={<Genres />} />
          </Routes>
        </main>
        <footer className="footer">
          <p>© 2024 API Pepe Segura - Entertainment & Movie Management System</p>
          <p>Version 2.0.0</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
