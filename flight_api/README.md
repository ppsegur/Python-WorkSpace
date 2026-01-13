# API de Búsqueda de Vuelos Baratos 🛫

FastAPI application para buscar vuelos baratos, con enfoque especial en encontrar las mejores ofertas para el fin de semana.

## 📋 Descripción

Esta API proporciona endpoints para buscar vuelos entre diferentes aeropuertos españoles, con una funcionalidad especial para encontrar **los vuelos más baratos del fin de semana**.

### Características principales:

- ✅ Búsqueda de vuelos por origen, destino y fecha
- ✅ **Endpoint especializado para vuelos de fin de semana** (viernes/sábado → domingo)
- ✅ Filtrado por precio máximo
- ✅ Ordenamiento automático por precio (más baratos primero)
- ✅ Documentación interactiva automática (Swagger/ReDoc)
- ✅ Combinaciones óptimas de ida y vuelta

## 🚀 Instalación y Ejecución

### Prerrequisitos

- Python 3.10 o superior
- pip

### Pasos de instalación

1. **Navega al directorio del proyecto:**
   ```bash
   cd flight_api
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```bash
   uvicorn main:app --reload
   ```

   O desde el directorio raíz del repositorio:
   ```bash
   uvicorn flight_api.main:app --reload
   ```

4. **Accede a la API:**
   - API: http://localhost:8000
   - Documentación Swagger: http://localhost:8000/docs
   - Documentación ReDoc: http://localhost:8000/redoc

## 📚 Endpoints Disponibles

### 1. Inicio
```
GET /
```
Información general sobre la API.

### 2. Lista de Aeropuertos
```
GET /flights/airports
```
Obtiene la lista de aeropuertos disponibles con sus códigos IATA.

**Ejemplo de respuesta:**
```json
{
  "airports": {
    "MAD": "Madrid",
    "BCN": "Barcelona",
    "AGP": "Málaga",
    ...
  }
}
```

### 3. Buscar Vuelos
```
GET /flights/search?origin=MAD&destination=BCN&departure_date=2024-01-20
```

**Parámetros:**
- `origin` (requerido): Código IATA del aeropuerto de origen
- `destination` (requerido): Código IATA del aeropuerto de destino
- `departure_date` (requerido): Fecha de salida (YYYY-MM-DD)
- `return_date` (opcional): Fecha de regreso (YYYY-MM-DD)
- `max_price` (opcional): Precio máximo del vuelo

**Ejemplo de respuesta:**
```json
{
  "search_criteria": {
    "origin": "MAD",
    "destination": "BCN",
    "departure_date": "2024-01-20"
  },
  "results_count": 10,
  "flights": [
    {
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
  ]
}
```

### 4. 🎯 Vuelos Más Baratos del Fin de Semana (Principal)
```
GET /flights/weekend/cheapest?origin=MAD&destination=BCN
```

**Este es el endpoint principal solicitado en el issue.**

Busca automáticamente los vuelos más baratos para el próximo fin de semana:
- **Ida**: Viernes o Sábado
- **Vuelta**: Domingo

**Parámetros:**
- `origin` (requerido): Código IATA del aeropuerto de origen
- `destination` (requerido): Código IATA del aeropuerto de destino
- `max_price` (opcional): Precio máximo por vuelo

**Ejemplo de respuesta:**
```json
{
  "search_criteria": {
    "origin": "MAD",
    "destination": "BCN",
    "max_price": null
  },
  "weekend_dates": {
    "friday": "2024-01-19",
    "saturday": "2024-01-20",
    "sunday": "2024-01-21"
  },
  "outbound_flights": [
    {
      "id": "RY1234",
      "origin": "MAD",
      "destination": "BCN",
      "departure_date": "2024-01-19T18:30:00",
      "price": 35.99,
      "airline": "Ryanair",
      ...
    }
  ],
  "return_flights": [
    {
      "id": "VY5678",
      "origin": "BCN",
      "destination": "MAD",
      "departure_date": "2024-01-21T20:00:00",
      "price": 42.50,
      "airline": "Vueling",
      ...
    }
  ],
  "cheapest_combination": {
    "outbound": {...},
    "return": {...},
    "total_price": 78.49
  }
}
```

También disponible como POST:
```
POST /flights/weekend/cheapest
Content-Type: application/json

{
  "origin": "MAD",
  "destination": "BCN",
  "max_price": 100.0
}
```

## 🧪 Ejemplos de Uso

### Usando curl

```bash
# Obtener aeropuertos disponibles
curl http://localhost:8000/flights/airports

# Buscar vuelos más baratos del fin de semana
curl "http://localhost:8000/flights/weekend/cheapest?origin=MAD&destination=BCN"

# Buscar con precio máximo
curl "http://localhost:8000/flights/weekend/cheapest?origin=MAD&destination=AGP&max_price=80"
```

### Usando Python

```python
import requests

# Buscar vuelos del fin de semana
response = requests.get(
    "http://localhost:8000/flights/weekend/cheapest",
    params={
        "origin": "MAD",
        "destination": "BCN",
        "max_price": 100
    }
)

data = response.json()
print(f"Total precio más barato: {data['cheapest_combination']['total_price']}€")
```

## 📁 Estructura del Proyecto

```
flight_api/
├── main.py                 # Aplicación principal FastAPI
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
├── models/
│   ├── __init__.py
│   └── flight.py          # Modelos Pydantic para vuelos
├── routers/
│   ├── __init__.py
│   └── flights.py         # Endpoints de vuelos
└── services/
    ├── __init__.py
    └── flight_service.py  # Lógica de búsqueda de vuelos
```

## 🔌 Integración con Skyscanner (Futuro)

Esta implementación actual usa **datos simulados** para demostración. Para conectar con Skyscanner u otros portales reales de vuelos, se necesitaría:

### Pasos para integración real:

1. **Obtener API Key:**
   - Registrarse en [Skyscanner API](https://developers.skyscanner.net/)
   - Obtener credenciales de API

2. **Instalar librerías adicionales:**
   ```bash
   pip install requests python-dotenv
   ```

3. **Configurar credenciales:**
   ```bash
   # .env
   SKYSCANNER_API_KEY=tu_api_key_aqui
   ```

4. **Modificar `flight_service.py`:**
   - Reemplazar `_generate_mock_flights()` con llamadas HTTP a Skyscanner API
   - Implementar manejo de rate limiting
   - Parsear respuestas de la API real

### Ejemplo de llamada a Skyscanner API:

```python
import requests

def search_flights_skyscanner(origin, destination, date):
    url = f"https://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/ES/EUR/es-ES/{origin}/{destination}/{date}"
    headers = {"apiKey": os.getenv("SKYSCANNER_API_KEY")}
    response = requests.get(url, headers=headers)
    return response.json()
```

## 🛠️ Tecnologías Utilizadas

- **FastAPI**: Framework web moderno para Python
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI

## 📝 Notas

- Los datos de vuelos actuales son simulados para propósitos de demostración
- Los precios y disponibilidad son generados aleatoriamente
- La estructura está preparada para fácil integración con APIs reales
- Los aeropuertos incluidos son los principales de España

## 👨‍💻 Autor

Pepe Segura - [GitHub](https://github.com/ppsegur)

## 📄 Licencia

Este proyecto es parte del repositorio Python-WorkSpace.
