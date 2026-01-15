# Python WorkSpace 🐍

Este repositorio agrupa varios proyectos y ejercicios realizados en Python, enfocados tanto al aprendizaje como a la práctica de frameworks y funcionalidades comunes del lenguaje.

## 📁 Estructura del repositorio

### `API_PEPE_SEGURA`
Una API desarrollada con FastAPI que gestiona películas y usuarios. Incluye:
- Autenticación básica y JWT
- Rutas separadas para usuarios y películas
- Modelos y esquemas organizados por carpetas
- Imágenes estáticas para las películas

**Archivos destacados:**
- `main.py`: Punto de entrada de la aplicación.
- `routers/`: Rutas para autenticación y gestión de películas/usuarios.
- `db/`: Modelos y esquemas para la base de datos.

### `BoletinDeEjercicios`
Conjunto de ejercicios básicos de Python.

**Ejercicios incluidos:**
- `ej1.py` a `ej8.py`: Diversos ejercicios introductorios.

### `BoletinDeEjerciciosIntermedios2`
Ejercicios de nivel intermedio organizados en dos secciones:
- **`EjercicioListas`**: Ejercicios con listas (`Ejercicio1.py` a `Ejercicio11.py`)
- **`EjerciciosFicheros`**: Lectura y escritura de ficheros con Python, incluyendo ejemplos con `.csv` y `.txt`

### `flight_api` 🛫
**API de Búsqueda de Vuelos Baratos** - Nueva aplicación FastAPI para buscar vuelos económicos, con enfoque especial en encontrar las mejores ofertas para el fin de semana.

**Características:**
- 🔍 Búsqueda de vuelos por origen, destino y fecha
- 🎯 **Endpoint especializado para vuelos de fin de semana** (más baratos)
- 💰 Filtrado por precio máximo
- 📊 Ordenamiento automático por precio
- 📚 Documentación interactiva (Swagger/ReDoc)

**Archivos destacados:**
- `main.py`: Aplicación principal FastAPI
- `routers/flights.py`: Endpoints de búsqueda de vuelos
- `services/flight_service.py`: Lógica de búsqueda
- `models/flight.py`: Modelos de datos Pydantic
- `README.md`: Documentación completa de la API

**Cómo ejecutar:**
```bash
cd flight_api
pip install -r requirements.txt
uvicorn main:app --reload
# Visita http://localhost:8000/docs
```

### `flight-frontend` ⚛️
**Frontend React para la API de Vuelos** - Interfaz web moderna desarrollada con React y Vite para interactuar con la API de búsqueda de vuelos.

**Características:**
- ✈️ Búsqueda de vuelos con interfaz intuitiva
- 🎉 Vista especializada para vuelos de fin de semana
- 📱 Diseño responsive y adaptable
- 🎨 Interfaz moderna con CSS personalizado
- ⚡ Hot Module Replacement (HMR) con Vite

**Archivos destacados:**
- `src/App.jsx`: Componente principal de la aplicación
- `src/components/FlightSearch.jsx`: Componente de búsqueda de vuelos
- `src/components/WeekendFlights.jsx`: Componente de vuelos de fin de semana
- `src/components/FlightResults.jsx`: Componente de resultados
- `README.md`: Documentación completa del frontend

**Cómo ejecutar:**
```bash
# Terminal 1: Backend (desde el directorio raíz)
cd flight_api
pip install -r requirements.txt
python -m uvicorn flight_api.main:app --reload

# Terminal 2: Frontend
cd flight-frontend
npm install
npm run dev
# Visita http://localhost:5173
```

### `FastAPI`
Pruebas y ejemplos sueltos relacionados con FastAPI y anotaciones de tipo en Python (`type_hints.py`).

### `notas.csv`
Archivo de ejemplo utilizado en el de manejo de ficheros.

---

## 🚀 Cómo ejecutar la API

1. Asegúrate de tener Python 3.10+ instalado.
2. Instala las dependencias necesarias:
   ```bash
   pip install fastapi uvicorn
