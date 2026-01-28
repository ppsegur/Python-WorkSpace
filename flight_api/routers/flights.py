from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Literal
from ..models.flight import Flight, FlightSearchRequest, WeekendFlightRequest
from ..services.flight_service import FlightService

router = APIRouter(
    prefix="/flights",
    tags=["Vuelos"]
)

# Instancia del servicio de vuelos
flight_service = FlightService()


@router.get("/airports", summary="Obtener aeropuertos disponibles")
async def get_airports():
    """
    Obtiene la lista de aeropuertos disponibles para búsquedas.
    """
    return {
        "airports": flight_service.get_available_airports(),
        "message": "Códigos IATA de aeropuertos disponibles"
    }


@router.get("/search", summary="Buscar vuelos")
async def search_flights(
    origin: str = Query(..., description="Código del aeropuerto de origen (ej: MAD)"),
    destination: str = Query(..., description="Código del aeropuerto de destino (ej: BCN)"),
    departure_date: str = Query(..., description="Fecha de salida (formato: YYYY-MM-DD)"),
    return_date: Optional[str] = Query(None, description="Fecha de regreso (formato: YYYY-MM-DD)"),
    max_price: Optional[float] = Query(None, description="Precio máximo del vuelo")
):
    """
    Busca vuelos según los criterios especificados.
    
    - **origin**: Código IATA del aeropuerto de origen
    - **destination**: Código IATA del aeropuerto de destino
    - **departure_date**: Fecha de salida en formato YYYY-MM-DD
    - **return_date**: (Opcional) Fecha de regreso
    - **max_price**: (Opcional) Precio máximo
    
    Devuelve una lista de vuelos ordenados por precio.
    """
    try:
        flights = flight_service.search_flights(
            origin=origin.upper(),
            destination=destination.upper(),
            departure_date=departure_date,
            return_date=return_date,
            max_price=max_price
        )
        
        return {
            "search_criteria": {
                "origin": origin.upper(),
                "destination": destination.upper(),
                "departure_date": departure_date,
                "return_date": return_date,
                "max_price": max_price
            },
            "results_count": len(flights),
            "flights": flights
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Fecha inválida: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar vuelos: {str(e)}")


@router.get("/weekend/cheapest", summary="Vuelos más baratos del fin de semana")
async def get_cheapest_weekend_flights(
    origin: str = Query(..., description="Código del aeropuerto de origen (ej: MAD)"),
    destination: str = Query(..., description="Código del aeropuerto de destino (ej: BCN)"),
    max_price: Optional[float] = Query(None, description="Precio máximo del vuelo")
):
    """
    **Obtiene los vuelos más baratos para el próximo fin de semana.**
    
    Esta es la funcionalidad principal solicitada: devolver los vuelos más baratos
    para viajar el fin de semana (viernes/sábado -> domingo).
    
    - **origin**: Código IATA del aeropuerto de origen
    - **destination**: Código IATA del aeropuerto de destino  
    - **max_price**: (Opcional) Precio máximo por vuelo
    
    Retorna:
    - Fechas del próximo fin de semana
    - Top 5 vuelos de ida más baratos (viernes o sábado)
    - Top 5 vuelos de vuelta más baratos (domingo)
    - La combinación más barata (ida + vuelta)
    
    **Nota**: Esta implementación usa datos simulados. Para conectar con
    Skyscanner u otros portales reales, se necesitaría:
    - API Key de Skyscanner
    - Implementar autenticación OAuth
    - Manejar rate limiting y paginación
    """
    try:
        weekend_flights = flight_service.get_weekend_flights(
            origin=origin.upper(),
            destination=destination.upper(),
            max_price=max_price
        )
        
        return {
            "search_criteria": {
                "origin": origin.upper(),
                "destination": destination.upper(),
                "max_price": max_price
            },
            **weekend_flights
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar vuelos de fin de semana: {str(e)}")


@router.post("/weekend/cheapest", summary="Vuelos más baratos del fin de semana (POST)")
async def post_cheapest_weekend_flights(request: WeekendFlightRequest):
    """
    Versión POST del endpoint de vuelos de fin de semana.
    Útil para búsquedas más complejas con body JSON.
    """
    try:
        weekend_flights = flight_service.get_weekend_flights(
            origin=request.origin.upper(),
            destination=request.destination.upper(),
            max_price=request.max_price
        )
        
        return {
            "search_criteria": {
                "origin": request.origin.upper(),
                "destination": request.destination.upper(),
                "max_price": request.max_price
            },
            **weekend_flights
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar vuelos de fin de semana: {str(e)}")


@router.get("/search/advanced", summary="Búsqueda avanzada con filtros y ordenación")
async def advanced_search_flights(
    origin: str = Query(..., description="Código del aeropuerto de origen (ej: MAD)"),
    destination: str = Query(..., description="Código del aeropuerto de destino (ej: BCN)"),
    departure_date: str = Query(..., description="Fecha de salida (formato: YYYY-MM-DD)"),
    return_date: Optional[str] = Query(None, description="Fecha de regreso (formato: YYYY-MM-DD)"),
    max_price: Optional[float] = Query(None, description="Precio máximo del vuelo"),
    min_price: Optional[float] = Query(None, description="Precio mínimo del vuelo"),
    airline: Optional[str] = Query(None, description="Filtrar por aerolínea específica"),
    sort_by: Literal["price", "duration", "departure"] = Query("price", description="Ordenar por: price, duration, departure"),
    order: Literal["asc", "desc"] = Query("asc", description="Orden: asc (ascendente), desc (descendente)"),
    limit: Optional[int] = Query(None, description="Limitar número de resultados", ge=1, le=100)
):
    """
    Búsqueda avanzada de vuelos con múltiples filtros y opciones de ordenación.
    
    **Filtros disponibles:**
    - **max_price**: Precio máximo
    - **min_price**: Precio mínimo
    - **airline**: Filtrar por aerolínea específica
    
    **Opciones de ordenación:**
    - **sort_by**: Campo por el que ordenar (price, duration, departure)
    - **order**: Orden ascendente (asc) o descendente (desc)
    - **limit**: Limitar número de resultados
    
    Esta funcionalidad mejora la API de vuelos permitiendo búsquedas más específicas.
    """
    try:
        flights = flight_service.search_flights(
            origin=origin.upper(),
            destination=destination.upper(),
            departure_date=departure_date,
            return_date=return_date,
            max_price=max_price
        )
        
        # Aplicar filtro de precio mínimo
        if min_price:
            flights = [f for f in flights if f.price >= min_price]
        
        # Filtrar por aerolínea
        if airline:
            flights = [f for f in flights if f.airline.lower() == airline.lower()]
        
        # Ordenar según criterio
        if sort_by == "price":
            flights.sort(key=lambda x: x.price, reverse=(order == "desc"))
        elif sort_by == "duration":
            flights.sort(key=lambda x: x.duration_minutes, reverse=(order == "desc"))
        elif sort_by == "departure":
            flights.sort(key=lambda x: x.departure_date, reverse=(order == "desc"))
        
        # Limitar resultados
        if limit:
            flights = flights[:limit]
        
        return {
            "search_criteria": {
                "origin": origin.upper(),
                "destination": destination.upper(),
                "departure_date": departure_date,
                "return_date": return_date,
                "filters": {
                    "max_price": max_price,
                    "min_price": min_price,
                    "airline": airline,
                    "sort_by": sort_by,
                    "order": order,
                    "limit": limit
                }
            },
            "results_count": len(flights),
            "flights": flights
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Parámetro inválido: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar vuelos: {str(e)}")


@router.get("/airlines", summary="Obtener lista de aerolíneas disponibles")
async def get_airlines():
    """
    Obtiene la lista de aerolíneas disponibles en el sistema.
    Útil para filtrar búsquedas por aerolínea específica.
    """
    return {
        "airlines": flight_service.AIRLINES,
        "message": "Aerolíneas disponibles en el sistema"
    }

