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
      setAirports(data.airports || [])
      setLoading(false)
    } catch (err) {
      setError(err.message)
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
        {loading && <div className="loading">Cargando aeropuertos...</div>}
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
