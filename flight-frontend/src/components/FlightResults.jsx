import './FlightResults.css'

function FlightResults({ results }) {
  const formatDate = (dateString) => {
    const date = new Date(dateString)
    return date.toLocaleDateString('es-ES', { 
      weekday: 'short', 
      year: 'numeric', 
      month: 'short', 
      day: 'numeric' 
    })
  }

  const formatTime = (dateString) => {
    const date = new Date(dateString)
    return date.toLocaleTimeString('es-ES', { 
      hour: '2-digit', 
      minute: '2-digit' 
    })
  }

  const formatDuration = (minutes) => {
    const hours = Math.floor(minutes / 60)
    const mins = minutes % 60
    return `${hours}h ${mins}m`
  }

  if (!results || !results.flights || results.flights.length === 0) {
    return (
      <div className="no-results">
        <p>😔 No se encontraron vuelos con los criterios especificados</p>
      </div>
    )
  }

  return (
    <div className="flight-results">
      <div className="results-header">
        <h2>Resultados de Búsqueda</h2>
        <div className="search-info">
          <p>
            <strong>{results.search_criteria.origin}</strong> → <strong>{results.search_criteria.destination}</strong>
          </p>
          <p>Salida: {results.search_criteria.departure_date}</p>
          {results.search_criteria.return_date && (
            <p>Regreso: {results.search_criteria.return_date}</p>
          )}
          {results.search_criteria.max_price && (
            <p>Precio máximo: €{results.search_criteria.max_price}</p>
          )}
        </div>
        <p className="results-count">
          {results.results_count} vuelo{results.results_count !== 1 ? 's' : ''} encontrado{results.results_count !== 1 ? 's' : ''}
        </p>
      </div>

      <div className="flights-list">
        {results.flights.map((flight, index) => (
          <div key={flight.id} className="flight-card">
            <div className="flight-rank">
              #{index + 1}
            </div>
            <div className="flight-details">
              <div className="flight-header">
                <h3>{flight.airline}</h3>
                <span className="flight-id">{flight.id}</span>
              </div>
              
              <div className="flight-route">
                <div className="route-info">
                  <div className="airport-info">
                    <span className="airport-code">{flight.origin}</span>
                    <span className="time">{formatTime(flight.departure_date)}</span>
                    <span className="date">{formatDate(flight.departure_date)}</span>
                  </div>
                  
                  <div className="flight-duration">
                    <div className="duration-line">
                      <span className="plane-icon">✈️</span>
                    </div>
                    <span className="duration-text">{formatDuration(flight.duration_minutes)}</span>
                  </div>
                  
                  <div className="airport-info">
                    <span className="airport-code">{flight.destination}</span>
                    <span className="time">{formatTime(flight.arrival_date)}</span>
                    <span className="date">{formatDate(flight.arrival_date)}</span>
                  </div>
                </div>
              </div>

              <div className="flight-footer">
                <div className="flight-price">
                  <span className="price-amount">€{flight.price.toFixed(2)}</span>
                  <span className="price-label">por persona</span>
                </div>
                {flight.available_seats && (
                  <div className="seats-info">
                    {flight.available_seats} asientos disponibles
                  </div>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default FlightResults
