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

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setSearchParams(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
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
                required
              >
                <option value="">Selecciona aeropuerto</option>
                {airports.map(airport => (
                  <option key={airport.code} value={airport.code}>
                    {airport.code} - {airport.name}
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="destination">Destino</label>
              <select
                id="destination"
                name="destination"
                value={searchParams.destination}
                onChange={handleInputChange}
                required
              >
                <option value="">Selecciona aeropuerto</option>
                {airports.map(airport => (
                  <option key={airport.code} value={airport.code}>
                    {airport.code} - {airport.name}
                  </option>
                ))}
              </select>
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
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="returnDate">Fecha de Regreso (opcional)</label>
              <input
                type="date"
                id="returnDate"
                name="returnDate"
                value={searchParams.returnDate}
                onChange={handleInputChange}
              />
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
                min="0"
                step="0.01"
                placeholder="Ej: 100.00"
              />
            </div>
          </div>

          <button type="submit" className="search-button" disabled={loading}>
            {loading ? '🔍 Buscando...' : '🔍 Buscar Vuelos'}
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
