from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Flight(BaseModel):
    """Modelo para representar un vuelo"""
    id: str = Field(..., description="ID único del vuelo")
    origin: str = Field(..., description="Ciudad/aeropuerto de origen")
    destination: str = Field(..., description="Ciudad/aeropuerto de destino")
    departure_date: datetime = Field(..., description="Fecha y hora de salida")
    arrival_date: datetime = Field(..., description="Fecha y hora de llegada")
    price: float = Field(..., description="Precio del vuelo en euros")
    airline: str = Field(..., description="Aerolínea")
    duration_minutes: int = Field(..., description="Duración del vuelo en minutos")
    available_seats: Optional[int] = Field(None, description="Asientos disponibles")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "VY1234",
                "origin": "MAD",
                "destination": "BCN",
                "departure_date": "2024-01-20T10:30:00",
                "arrival_date": "2024-01-20T11:45:00",
                "price": 45.99,
                "airline": "Vueling",
                "duration_minutes": 75,
                "available_seats": 12
            }
        }


class FlightSearchRequest(BaseModel):
    """Modelo para la solicitud de búsqueda de vuelos"""
    origin: str = Field(..., description="Ciudad/aeropuerto de origen")
    destination: str = Field(..., description="Ciudad/aeropuerto de destino")
    departure_date: str = Field(..., description="Fecha de salida (YYYY-MM-DD)")
    return_date: Optional[str] = Field(None, description="Fecha de regreso (YYYY-MM-DD)")
    max_price: Optional[float] = Field(None, description="Precio máximo")
    
    class Config:
        json_schema_extra = {
            "example": {
                "origin": "MAD",
                "destination": "BCN",
                "departure_date": "2024-01-20",
                "return_date": "2024-01-22",
                "max_price": 100.0
            }
        }


class WeekendFlightRequest(BaseModel):
    """Modelo para búsqueda de vuelos de fin de semana"""
    origin: str = Field(..., description="Ciudad/aeropuerto de origen")
    destination: str = Field(..., description="Ciudad/aeropuerto de destino")
    max_price: Optional[float] = Field(None, description="Precio máximo")
    
    class Config:
        json_schema_extra = {
            "example": {
                "origin": "MAD",
                "destination": "BCN",
                "max_price": 150.0
            }
        }
