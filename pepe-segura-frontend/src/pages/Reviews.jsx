import { useState, useEffect } from 'react';
import { getReviews, getMovies } from '../services/api';
import './Reviews.css';

function Reviews() {
  const [reviews, setReviews] = useState([]);
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [reviewsRes, moviesRes] = await Promise.all([
          getReviews(),
          getMovies()
        ]);
        setReviews(reviewsRes.data);
        setMovies(moviesRes.data);
      } catch (err) {
        setError('Failed to load reviews');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const getMovieName = (filmId) => {
    const movie = movies.find(m => m.id === filmId);
    return movie ? movie.nombre : `Film #${filmId}`;
  };

  if (loading) return <div className="loading">Loading reviews...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="reviews-page">
      <header className="reviews-header">
        <h1>⭐ Reviews</h1>
        <p>Read what others think about our films</p>
      </header>

      <div className="reviews-list">
        {reviews.map(review => (
          <div key={review.id} className="review-card">
            <div className="review-header">
              <h3>{getMovieName(review.film_id)}</h3>
              <span className="review-rating">⭐ {review.rating}/10</span>
            </div>
            <p className="review-comment">{review.comment}</p>
            <div className="review-footer">
              <span className="review-user">By User #{review.user_id}</span>
              <span className="review-date">{review.date}</span>
            </div>
          </div>
        ))}
      </div>

      {reviews.length === 0 && (
        <div className="no-reviews">
          <p>No reviews yet. Be the first to write one!</p>
        </div>
      )}
    </div>
  );
}

export default Reviews;
