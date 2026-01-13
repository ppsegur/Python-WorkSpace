# Guía Rápida - API de Vuelos Baratos 🛫

## ¿Qué hace esta API?

Esta API te permite buscar **los vuelos más baratos del fin de semana** entre diferentes ciudades españolas.

## Inicio Rápido

### 1. Instalar dependencias
```bash
cd flight_api
pip install -r requirements.txt
```

### 2. Ejecutar la API
```bash
uvicorn main:app --reload
```

La API estará disponible en: **http://localhost:8000**

### 3. Ver la documentación interactiva
Abre en tu navegador: **http://localhost:8000/docs**

## Endpoints Principales

### 🎯 Vuelos del Fin de Semana (Endpoint Principal)

**GET** `/flights/weekend/cheapest`

Este es el endpoint principal que resuelve el problema solicitado: **encontrar los vuelos más baratos del fin de semana**.

**Parámetros:**
- `origin` (requerido): Código del aeropuerto de origen (ej: MAD)
- `destination` (requerido): Código del aeropuerto de destino (ej: BCN)
- `max_price` (opcional): Precio máximo por vuelo

**Ejemplo:**
```bash
curl "http://localhost:8000/flights/weekend/cheapest?origin=MAD&destination=BCN"
```

**Respuesta:**
```json
{
  "weekend_dates": {
    "friday": "2026-01-16",
    "saturday": "2026-01-17", 
    "sunday": "2026-01-18"
  },
  "outbound_flights": [...],  // Top 5 vuelos de ida más baratos
  "return_flights": [...],    // Top 5 vuelos de vuelta más baratos
  "cheapest_combination": {
    "outbound": {...},
    "return": {...},
    "total_price": 78.49      // Precio total más barato (ida + vuelta)
  }
}
```

### ✈️ Otros Endpoints

**Ver aeropuertos disponibles:**
```bash
curl http://localhost:8000/flights/airports
```

**Buscar vuelos por fecha específica:**
```bash
curl "http://localhost:8000/flights/search?origin=MAD&destination=BCN&departure_date=2026-01-20"
```

## Aeropuertos Disponibles

- **MAD**: Madrid
- **BCN**: Barcelona
- **AGP**: Málaga
- **PMI**: Palma de Mallorca
- **SVQ**: Sevilla
- **VLC**: Valencia
- **ALC**: Alicante
- **BIO**: Bilbao

## Notas Importantes

⚠️ **Esta implementación usa datos simulados** para demostración. Los vuelos y precios son generados aleatoriamente.

✅ **Para producción**, se conectaría con APIs reales como:
- Skyscanner API
- Amadeus API
- Kiwi.com API

📖 **Documentación completa**: Ver `README.md` para más detalles sobre cómo integrar con APIs reales.
