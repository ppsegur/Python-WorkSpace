import { useState } from 'react'
import './WeekendFlights.css'

function WeekendFlights({ airports }) {
  const [searchParams, setSearchParams] = useState({
    origin: '',
    destination: '',
    maxPrice: ''
  })
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [validationErrors, setValidationErrors] = useState({})

  const validateForm = () => {
    const errors = {}

    // Validate origin and destination
    if (searchParams.origin && searchParams.destination && searchParams.origin === searchParams.destination) {
      errors.destination = 'El destino debe ser diferente al origen'
    }

    // Validate price
    if (searchParams.maxPrice && parseFloat(searchParams.maxPrice) <= 0) {
      errors.maxPrice = 'El precio debe ser mayor a 0'
    }

    setValidationErrors(errors)
    return Object.keys(errors).length === 0
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setSearchParams(prev => ({
      ...prev,
      [name]: value
    }))
    // Clear validation error for this field
    if (validationErrors[name]) {
      setValidationErrors(prev => {
        const newErrors = { ...prev }
        delete newErrors[name]
        return newErrors
      })
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!validateForm()) {
      return
    }

    setLoading(true)
    setError(null)
    setResults(null)

    try {
      const params = new URLSearchParams({
        origin: searchParams.origin,
        destination: searchParams.destination,
      })

      if (searchParams.maxPrice) {
        params.append('max_price', searchParams.maxPrice)
      }

      const response = await fetch(`/api/flights/weekend/cheapest?${params}`)
      if (!response.ok) {
        throw new Error('Error al buscar vuelos de fin de semana')
      }

      const data = await response.json()
      setResults(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const formatDate = (dateString) => {
    const date = new Date(dateString)
    return date.toLocaleDateString('es-ES', { 
      weekday: 'long', 
      year: 'numeric', 
      month: 'long', 
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

  return (
    <div className="weekend-flights">
      <div className="search-form-container">
        <h2>Vuelos de Fin de Semana más Baratos</h2>
        <p className="subtitle">Encuentra las mejores ofertas para tu escapada de fin de semana</p>
        
        <form onSubmit={handleSubmit} className="search-form">
          <div className="form-row">
            <div className="form-group">
              <label htmlFor="origin">Origen</label>
              <select
                id="origin"
                name="origin"
                value={searchParams.origin}
                onChange={handleInputChange}
                className={validationErrors.origin ? 'invalid' : ''}
                required
              >
                <option value="">Selecciona aeropuerto</option>
                {airports.map(airport => (
                  <option key={airport.code} value={airport.code}>
                    {airport.code} - {airport.name}
                  </option>
                ))}
              </select>
              {validationErrors.origin && (
                <span className="error-text">{validationErrors.origin}</span>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="destination">Destino</label>
              <select
                id="destination"
                name="destination"
                value={searchParams.destination}
                onChange={handleInputChange}
                className={validationErrors.destination ? 'invalid' : ''}
                required
              >
                <option value="">Selecciona aeropuerto</option>
                {airports.map(airport => (
                  <option key={airport.code} value={airport.code}>
                    {airport.code} - {airport.name}
                  </option>
                ))}
              </select>
              {validationErrors.destination && (
                <span className="error-text">{validationErrors.destination}</span>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="maxPrice">Precio Máximo (€) (opcional)</label>
              <input
                type="number"
                id="maxPrice"
                name="maxPrice"
                value={searchParams.maxPrice}
                onChange={handleInputChange}
                className={validationErrors.maxPrice ? 'invalid' : ''}
                min="0"
                step="0.01"
                placeholder="Ej: 150.00"
              />
              {validationErrors.maxPrice && (
                <span className="error-text">{validationErrors.maxPrice}</span>
              )}
            </div>
          </div>

          <button type="submit" className="search-button" disabled={loading}>
            {loading ? '🔍 Buscando...' : '🎉 Buscar Vuelos de Fin de Semana'}
          </button>
        </form>
      </div>

      {error && (
        <div className="error-message">
          ❌ {error}
        </div>
      )}

      {results && results.weekend_dates && (
        <div className="weekend-results">
          <div className="weekend-info">
            <h3>📅 Próximo Fin de Semana</h3>
            <p><strong>Salida:</strong> {formatDate(results.weekend_dates.friday || results.weekend_dates.saturday || results.weekend_dates.departure)}</p>
            <p><strong>Regreso:</strong> {formatDate(results.weekend_dates.sunday || results.weekend_dates.return)}</p>
          </div>

          {results.best_combination && (
            <div className="best-combination">
              <h3>✨ Mejor Combinación</h3>
              <div className="price-highlight">
                <span className="price">€{results.best_combination.total_price.toFixed(2)}</span>
                <span className="label">Precio Total (ida + vuelta)</span>
              </div>

              <div className="combination-details">
                <div className="flight-card best">
                  <div className="flight-header">
                    <h4>✈️ Vuelo de Ida</h4>
                    <span className="airline">{results.best_combination.outbound.airline}</span>
                  </div>
                  <div className="flight-info">
                    <div className="route">
                      <span className="airport">{results.best_combination.outbound.origin}</span>
                      <span className="arrow">→</span>
                      <span className="airport">{results.best_combination.outbound.destination}</span>
                    </div>
                    <div className="times">
                      <span>{formatTime(results.best_combination.outbound.departure_date)}</span>
                      <span className="duration">{formatDuration(results.best_combination.outbound.duration_minutes)}</span>
                      <span>{formatTime(results.best_combination.outbound.arrival_date)}</span>
                    </div>
                    <div className="price-info">
                      <span className="price">€{results.best_combination.outbound.price.toFixed(2)}</span>
                    </div>
                  </div>
                </div>

                <div className="flight-card best">
                  <div className="flight-header">
                    <h4>✈️ Vuelo de Vuelta</h4>
                    <span className="airline">{results.best_combination.return.airline}</span>
                  </div>
                  <div className="flight-info">
                    <div className="route">
                      <span className="airport">{results.best_combination.return.origin}</span>
                      <span className="arrow">→</span>
                      <span className="airport">{results.best_combination.return.destination}</span>
                    </div>
                    <div className="times">
                      <span>{formatTime(results.best_combination.return.departure_date)}</span>
                      <span className="duration">{formatDuration(results.best_combination.return.duration_minutes)}</span>
                      <span>{formatTime(results.best_combination.return.arrival_date)}</span>
                    </div>
                    <div className="price-info">
                      <span className="price">€{results.best_combination.return.price.toFixed(2)}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}

          <div className="flight-lists">
            <div className="flight-list">
              <h3>🛫 Vuelos de Ida ({results.outbound_flights.length})</h3>
              {results.outbound_flights.map((flight, index) => (
                <div key={flight.id} className="flight-card">
                  <div className="flight-header">
                    <span className="rank">#{index + 1}</span>
                    <span className="airline">{flight.airline}</span>
                  </div>
                  <div className="flight-info">
                    <div className="route">
                      <span className="airport">{flight.origin}</span>
                      <span className="arrow">→</span>
                      <span className="airport">{flight.destination}</span>
                    </div>
                    <div className="times">
                      <span>{formatTime(flight.departure_date)}</span>
                      <span className="duration">{formatDuration(flight.duration_minutes)}</span>
                      <span>{formatTime(flight.arrival_date)}</span>
                    </div>
                    <div className="price-info">
                      <span className="price">€{flight.price.toFixed(2)}</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            <div className="flight-list">
              <h3>🛬 Vuelos de Vuelta ({results.return_flights.length})</h3>
              {results.return_flights.map((flight, index) => (
                <div key={flight.id} className="flight-card">
                  <div className="flight-header">
                    <span className="rank">#{index + 1}</span>
                    <span className="airline">{flight.airline}</span>
                  </div>
                  <div className="flight-info">
                    <div className="route">
                      <span className="airport">{flight.origin}</span>
                      <span className="arrow">→</span>
                      <span className="airport">{flight.destination}</span>
                    </div>
                    <div className="times">
                      <span>{formatTime(flight.departure_date)}</span>
                      <span className="duration">{formatDuration(flight.duration_minutes)}</span>
                      <span>{formatTime(flight.arrival_date)}</span>
                    </div>
                    <div className="price-info">
                      <span className="price">€{flight.price.toFixed(2)}</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default WeekendFlights
