import { useState, useEffect } from 'react'
import './App.css'
import FlightSearch from './components/FlightSearch'
import WeekendFlights from './components/WeekendFlights'

function App() {
  const [activeTab, setActiveTab] = useState('search')
  const [airports, setAirports] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchAirports()
  }, [])

  const fetchAirports = async () => {
    try {
      const response = await fetch('/api/flights/airports')
      if (!response.ok) {
        throw new Error('Error al cargar aeropuertos')
      }
      const data = await response.json()
      // Transform the airports object to an array
      if (data && data.airports && typeof data.airports === 'object') {
        const airportsArray = Object.entries(data.airports).map(([code, name]) => ({
          code,
          name
        }))
        setAirports(airportsArray)
      } else {
        throw new Error('Formato de datos de aeropuertos inválido')
      }
      setLoading(false)
    } catch (err) {
      setError(err.message || 'Error al cargar aeropuertos')
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>🛫 Buscador de Vuelos Baratos</h1>
        <p>Encuentra los mejores precios para tu próximo viaje</p>
      </header>

      <nav className="app-nav">
        <button
          className={`tab-button ${activeTab === 'search' ? 'active' : ''}`}
          onClick={() => setActiveTab('search')}
        >
          🔍 Buscar Vuelos
        </button>
        <button
          className={`tab-button ${activeTab === 'weekend' ? 'active' : ''}`}
          onClick={() => setActiveTab('weekend')}
        >
          🎉 Vuelos de Fin de Semana
        </button>
      </nav>

      <main className="app-main">
        {loading && (
          <div className="loading">
            <div className="loading-spinner"></div>
            <p>Cargando aeropuertos...</p>
          </div>
        )}
        {error && <div className="error">Error: {error}</div>}
        
        {!loading && !error && (
          <>
            {activeTab === 'search' && <FlightSearch airports={airports} />}
            {activeTab === 'weekend' && <WeekendFlights airports={airports} />}
          </>
        )}
      </main>

      <footer className="app-footer">
        <p>💡 Esta es una aplicación de demostración con datos simulados</p>
        <p>API: FastAPI | Frontend: React + Vite</p>
      </footer>
    </div>
  )
}

export default App
