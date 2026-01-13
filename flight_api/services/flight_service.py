from typing import List
from datetime import datetime, timedelta
from ..models.flight import Flight
import random


class FlightService:
    """
    Servicio para buscar vuelos.
    
    Nota: Esta es una implementación de demostración con datos simulados.
    Para conectar con APIs reales como Skyscanner, se necesitaría:
    - API Key de Skyscanner (https://developers.skyscanner.net/)
    - Librería como 'skyscanner-python' o requests para llamadas HTTP
    - Manejo de autenticación y rate limiting
    """
    
    # Datos de aerolíneas populares en España
    AIRLINES = ["Vueling", "Ryanair", "Iberia", "Air Europa", "EasyJet"]
    
    # Aeropuertos principales en España
    AIRPORTS = {
        "MAD": "Madrid",
        "BCN": "Barcelona", 
        "AGP": "Málaga",
        "PMI": "Palma de Mallorca",
        "SVQ": "Sevilla",
        "VLC": "Valencia",
        "ALC": "Alicante",
        "BIO": "Bilbao"
    }
    
    def __init__(self):
        """Inicializa el servicio de vuelos"""
        pass
    
    def _generate_mock_flights(
        self, 
        origin: str, 
        destination: str, 
        departure_date: datetime,
        num_flights: int = 10
    ) -> List[Flight]:
        """
        Genera vuelos simulados para demostración.
        
        En producción, esto haría una llamada a la API de Skyscanner:
        API endpoint ejemplo: https://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/{market}/{currency}/{locale}/{originPlace}/{destinationPlace}/{outboundPartialDate}
        """
        flights = []
        
        for i in range(num_flights):
            # Generar horarios aleatorios
            hour = random.randint(6, 22)
            minute = random.choice([0, 15, 30, 45])
            departure = departure_date.replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            # Duración del vuelo (varía según distancia)
            duration = random.randint(60, 180)
            arrival = departure + timedelta(minutes=duration)
            
            # Precio base dependiendo de la aerolínea y día
            base_price = random.uniform(30, 200)
            
            # Aerolínea aleatoria
            airline = random.choice(self.AIRLINES)
            
            # Ajustar precio según aerolínea
            if airline in ["Ryanair", "EasyJet"]:
                base_price *= 0.7  # Low cost
            elif airline == "Iberia":
                base_price *= 1.3  # Premium
            
            flight = Flight(
                id=f"{airline[:2].upper()}{random.randint(1000, 9999)}",
                origin=origin,
                destination=destination,
                departure_date=departure,
                arrival_date=arrival,
                price=round(base_price, 2),
                airline=airline,
                duration_minutes=duration,
                available_seats=random.randint(5, 150)
            )
            flights.append(flight)
        
        return flights
    
    def search_flights(
        self,
        origin: str,
        destination: str,
        departure_date: str,
        return_date: str = None,
        max_price: float = None
    ) -> List[Flight]:
        """
        Busca vuelos según los criterios especificados.
        
        Args:
            origin: Código del aeropuerto de origen (ej: "MAD")
            destination: Código del aeropuerto de destino (ej: "BCN")
            departure_date: Fecha de salida en formato YYYY-MM-DD
            return_date: Fecha de regreso en formato YYYY-MM-DD (opcional)
            max_price: Precio máximo del vuelo (opcional)
        
        Returns:
            Lista de vuelos encontrados
        """
        # Convertir fecha de string a datetime
        dep_date = datetime.strptime(departure_date, "%Y-%m-%d")
        
        # Generar vuelos simulados
        flights = self._generate_mock_flights(origin, destination, dep_date)
        
        # Filtrar por precio máximo si se especifica
        if max_price:
            flights = [f for f in flights if f.price <= max_price]
        
        # Ordenar por precio
        flights.sort(key=lambda x: x.price)
        
        return flights
    
    def get_weekend_flights(
        self,
        origin: str,
        destination: str,
        max_price: float = None
    ) -> dict:
        """
        Obtiene los vuelos más baratos para el próximo fin de semana.
        
        Busca vuelos para viajar viernes-domingo o sábado-domingo.
        
        Args:
            origin: Código del aeropuerto de origen
            destination: Código del aeropuerto de destino
            max_price: Precio máximo del vuelo (opcional)
        
        Returns:
            Diccionario con vuelos de ida y vuelta para el fin de semana
        """
        # Calcular el próximo fin de semana
        today = datetime.now()
        days_until_friday = (4 - today.weekday()) % 7
        if days_until_friday == 0 and today.hour >= 12:
            days_until_friday = 7
        
        next_friday = today + timedelta(days=days_until_friday)
        next_saturday = next_friday + timedelta(days=1)
        next_sunday = next_friday + timedelta(days=2)
        
        # Buscar vuelos de ida (viernes o sábado)
        friday_flights = self._generate_mock_flights(
            origin, destination, next_friday, num_flights=8
        )
        saturday_flights = self._generate_mock_flights(
            origin, destination, next_saturday, num_flights=8
        )
        
        # Buscar vuelos de vuelta (domingo)
        sunday_return_flights = self._generate_mock_flights(
            destination, origin, next_sunday, num_flights=8
        )
        
        # Combinar vuelos de ida
        outbound_flights = friday_flights + saturday_flights
        
        # Filtrar por precio si se especifica
        if max_price:
            outbound_flights = [f for f in outbound_flights if f.price <= max_price]
            sunday_return_flights = [f for f in sunday_return_flights if f.price <= max_price]
        
        # Ordenar por precio
        outbound_flights.sort(key=lambda x: x.price)
        sunday_return_flights.sort(key=lambda x: x.price)
        
        # Retornar los 5 más baratos de cada uno
        result = {
            "weekend_dates": {
                "friday": next_friday.strftime("%Y-%m-%d"),
                "saturday": next_saturday.strftime("%Y-%m-%d"),
                "sunday": next_sunday.strftime("%Y-%m-%d")
            },
            "outbound_flights": outbound_flights[:5],
            "return_flights": sunday_return_flights[:5],
            "cheapest_combination": None
        }
        
        # Calcular la combinación más barata
        if outbound_flights and sunday_return_flights:
            cheapest_out = outbound_flights[0]
            cheapest_ret = sunday_return_flights[0]
            result["cheapest_combination"] = {
                "outbound": cheapest_out,
                "return": cheapest_ret,
                "total_price": round(cheapest_out.price + cheapest_ret.price, 2)
            }
        
        return result
    
    def get_available_airports(self) -> dict:
        """Retorna la lista de aeropuertos disponibles"""
        return self.AIRPORTS
