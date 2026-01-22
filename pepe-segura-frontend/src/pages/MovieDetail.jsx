import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getMovie, getReviews, getRatings, getFilmAverageRating } from '../services/api';
import './MovieDetail.css';

function MovieDetail() {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [averageRating, setAverageRating] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const movieRes = await getMovie(id);
        setMovie(movieRes.data);

        // Get all reviews and filter by film_id
        const reviewsRes = await getReviews();
        const filmReviews = reviewsRes.data.filter(r => r.film_id === parseInt(id));
        setReviews(filmReviews);

        // Get average rating
        try {
          const avgRes = await getFilmAverageRating(id);
          setAverageRating(avgRes.data.average_rating);
        } catch (err) {
          console.log('No ratings yet');
        }
      } catch (err) {
        setError('Failed to load movie details');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [id]);

  if (loading) return <div className="loading">Loading...</div>;
  if (error) return <div className="error">{error}</div>;
  if (!movie) return <div className="error">Movie not found</div>;

  return (
    <div className="movie-detail">
      <Link to="/movies" className="back-link">← Back to Movies</Link>
      
      <div className="movie-detail-content">
        <div className="movie-poster-large">
          <img 
            src={`http://localhost:8000/${movie.portada}`} 
            alt={movie.nombre}
            onError={(e) => {
              e.target.src = 'https://via.placeholder.com/400x600?text=No+Image';
            }}
          />
        </div>

        <div className="movie-details">
          <h1>{movie.nombre}</h1>
          <div className="movie-meta">
            <span className="year">{movie.anio}</span>
            <span className="genre">{movie.genero}</span>
            <span className="duration">{movie.duracion} min</span>
          </div>
          
          <div className="movie-info-section">
            <h3>Director</h3>
            <p>{movie.director}</p>
          </div>

          {averageRating && (
            <div className="movie-info-section">
              <h3>Average Rating</h3>
              <div className="rating-display">
                <span className="rating-score">⭐ {averageRating.toFixed(1)}</span>
                <span className="rating-count">({reviews.length} reviews)</span>
              </div>
            </div>
          )}
        </div>
      </div>

      <div className="reviews-section">
        <h2>Reviews</h2>
        {reviews.length > 0 ? (
          <div className="reviews-list">
            {reviews.map(review => (
              <div key={review.id} className="review-card">
                <div className="review-header">
                  <span className="review-rating">⭐ {review.rating}</span>
                  <span className="review-date">{review.date}</span>
                </div>
                <p className="review-comment">{review.comment}</p>
                <span className="review-user">User #{review.user_id}</span>
              </div>
            ))}
          </div>
        ) : (
          <p className="no-reviews">No reviews yet. Be the first to review!</p>
        )}
      </div>
    </div>
  );
}

export default MovieDetail;
