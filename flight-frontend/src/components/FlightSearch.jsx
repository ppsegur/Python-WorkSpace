import { useState } from 'react'
import FlightResults from './FlightResults'
import './FlightSearch.css'

function FlightSearch({ airports }) {
  const [searchParams, setSearchParams] = useState({
    origin: '',
    destination: '',
    departureDate: '',
    returnDate: '',
    maxPrice: ''
  })
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [validationErrors, setValidationErrors] = useState({})

  const validateForm = () => {
    const errors = {}
    const today = new Date()
    today.setHours(0, 0, 0, 0)

    // Validate origin and destination
    if (searchParams.origin && searchParams.destination && searchParams.origin === searchParams.destination) {
      errors.destination = 'El destino debe ser diferente al origen'
    }

    // Validate departure date
    if (searchParams.departureDate) {
      const departureDate = new Date(searchParams.departureDate)
      if (departureDate < today) {
        errors.departureDate = 'La fecha de salida debe ser hoy o posterior'
      }
    }

    // Validate return date
    if (searchParams.returnDate && searchParams.departureDate) {
      const departureDate = new Date(searchParams.departureDate)
      const returnDate = new Date(searchParams.returnDate)
      if (returnDate <= departureDate) {
        errors.returnDate = 'La fecha de regreso debe ser posterior a la de salida'
      }
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
        departure_date: searchParams.departureDate,
      })

      if (searchParams.returnDate) {
        params.append('return_date', searchParams.returnDate)
      }
      if (searchParams.maxPrice) {
        params.append('max_price', searchParams.maxPrice)
      }

      const response = await fetch(`/api/flights/search?${params}`)
      if (!response.ok) {
        throw new Error('Error al buscar vuelos')
      }

      const data = await response.json()
      setResults(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flight-search">
      <div className="search-form-container">
        <h2>Buscar Vuelos</h2>
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
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="departureDate">Fecha de Salida</label>
              <input
                type="date"
                id="departureDate"
                name="departureDate"
                value={searchParams.departureDate}
                onChange={handleInputChange}
                className={validationErrors.departureDate ? 'invalid' : ''}
                required
              />
              {validationErrors.departureDate && (
                <span className="error-text">{validationErrors.departureDate}</span>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="returnDate">Fecha de Regreso (opcional)</label>
              <input
                type="date"
                id="returnDate"
                name="returnDate"
                value={searchParams.returnDate}
                onChange={handleInputChange}
                className={validationErrors.returnDate ? 'invalid' : ''}
              />
              {validationErrors.returnDate && (
                <span className="error-text">{validationErrors.returnDate}</span>
              )}
            </div>
          </div>

          <div className="form-row">
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
                placeholder="Ej: 100.00"
              />
              {validationErrors.maxPrice && (
                <span className="error-text">{validationErrors.maxPrice}</span>
              )}
            </div>
          </div>

          <button type="submit" className="search-button" disabled={loading}>
            {loading ? (
              <>
                <span className="button-spinner"></span>
                Buscando...
              </>
            ) : (
              '🔍 Buscar Vuelos'
            )}
          </button>
        </form>
      </div>

      {error && (
        <div className="error-message">
          ❌ {error}
        </div>
      )}

      {results && <FlightResults results={results} />}
    </div>
  )
}

export default FlightSearch
