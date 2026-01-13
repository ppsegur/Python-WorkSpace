"""
FastAPI - Buscador de Vuelos Baratos
=====================================

API para buscar vuelos baratos, especialmente enfocada en encontrar
las mejores ofertas para el fin de semana.

Características:
- Búsqueda de vuelos por origen, destino y fecha
- Endpoint especializado para vuelos de fin de semana
- Filtrado por precio máximo
- Ordenamiento automático por precio

Nota: Esta es una implementación de demostración con datos simulados.
Para conectar con APIs reales como Skyscanner, se requeriría:
- API Key de Skyscanner (https://developers.skyscanner.net/)
- Configuración de autenticación OAuth
- Manejo de rate limiting

Autor: Pepe Segura
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import flights

# Crear aplicación FastAPI
app = FastAPI(
    title="API de Búsqueda de Vuelos",
    description="API para encontrar los vuelos más baratos, especialmente para el fin de semana",
    version="1.0.0",
    contact={
        "name": "Pepe Segura",
        "url": "https://github.com/ppsegur/Python-WorkSpace"
    }
)

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(flights.router)


@app.get("/", tags=["Inicio"])
async def root():
    """
    Endpoint raíz que proporciona información sobre la API.
    """
    return {
        "message": "API de Búsqueda de Vuelos Baratos 🛫",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "redoc": "/redoc",
            "airports": "/flights/airports",
            "search": "/flights/search",
            "weekend_cheapest": "/flights/weekend/cheapest"
        },
        "descripcion": "API para encontrar los vuelos más baratos del fin de semana",
        "nota": "Esta es una versión de demostración con datos simulados. Para producción se conectaría con Skyscanner API."
    }


@app.get("/health", tags=["Salud"])
async def health_check():
    """
    Endpoint de health check para monitoreo.
    """
    return {
        "status": "healthy",
        "service": "flight-search-api"
    }
