# Configuración de la API de Skyscanner

Este documento explica cómo configurar la integración con la API de Skyscanner para obtener datos reales de vuelos.

## Estado Actual

**✅ Implementación completada** - La infraestructura para integrar Skyscanner está lista
**⏳ Esperando API Key** - Actualmente usando datos simulados mientras se obtiene acceso a la API

## Obtener API Key de Skyscanner

### 1. Registro en Skyscanner

1. Visita el portal de desarrolladores: https://developers.skyscanner.net/
2. Crea una cuenta o inicia sesión
3. Solicita acceso a la API de búsqueda de vuelos
4. Una vez aprobado, obtendrás tu API key

### 2. Tipos de API Disponibles

Skyscanner ofrece diferentes endpoints:

- **Browse Routes API**: Rutas y precios agregados
- **Browse Quotes API**: Cotizaciones de vuelos
- **Live Pricing API**: Precios en tiempo real (requiere suscripción)

Nuestra implementación soporta Browse Routes y Browse Quotes.

## Configuración

### Opción 1: Variable de Entorno (Recomendado)

Configura la variable de entorno `SKYSCANNER_API_KEY`:

```bash
# Linux/Mac
export SKYSCANNER_API_KEY="tu_api_key_aqui"

# Windows CMD
set SKYSCANNER_API_KEY=tu_api_key_aqui

# Windows PowerShell
$env:SKYSCANNER_API_KEY="tu_api_key_aqui"
```

### Opción 2: Archivo .env

Crea un archivo `.env` en la raíz del proyecto:

```env
SKYSCANNER_API_KEY=tu_api_key_aqui
```

Luego instala python-dotenv:

```bash
pip install python-dotenv
```

Y cárgalo en `main.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

### Opción 3: Configuración Directa en Código

⚠️ **NO RECOMENDADO para producción** (expone la API key)

```python
from flight_api.services.skyscanner_service import SkyscannerService

service = SkyscannerService(api_key="tu_api_key_aqui")
```

## Verificar Configuración

Una vez configurada la API key, reinicia el servidor:

```bash
cd flight_api
uvicorn main:app --reload
```

Deberías ver en la consola:

```
✅ Skyscanner API configurada - usando datos reales
```

Si no está configurada, verás:

```
⚠️  Skyscanner API no configurada - usando datos simulados
   Para usar datos reales, configura SKYSCANNER_API_KEY
```

## Endpoints Disponibles

Una vez configurada la API, todos los endpoints funcionarán con datos reales:

### Búsqueda Básica
```bash
GET /api/flights/search?origin=MAD&destination=BCN&departure_date=2024-03-15
```

### Vuelos de Fin de Semana
```bash
GET /api/flights/weekend/cheapest?origin=MAD&destination=BCN
```

### Búsqueda Avanzada (Nueva Funcionalidad)
```bash
GET /api/flights/search/advanced?origin=MAD&destination=BCN&departure_date=2024-03-15&sort_by=price&order=asc&limit=10
```

## Características Implementadas

### ✅ Integración con Skyscanner
- Servicio completo de integración (`skyscanner_service.py`)
- Manejo de autenticación con API key
- Detección automática de configuración
- Fallback a datos simulados si no hay API key

### ✅ Búsqueda Avanzada
- Filtrado por precio (mínimo y máximo)
- Filtrado por aerolínea
- Ordenación por precio, duración o fecha
- Limitación de resultados
- Nuevo endpoint `/search/advanced`

### ✅ Endpoints Adicionales
- `GET /flights/airlines` - Lista de aerolíneas disponibles
- `GET /flights/search/advanced` - Búsqueda con filtros avanzados

## Estructura del Código

```
flight_api/
├── services/
│   ├── flight_service.py           # Servicio principal (usa Skyscanner o mock)
│   └── skyscanner_service.py       # ✨ NUEVO: Integración con Skyscanner
├── routers/
│   └── flights.py                  # ✨ ACTUALIZADO: Nuevos endpoints
└── models/
    └── flight.py                   # Modelos de datos
```

## Manejo de Errores

El sistema maneja automáticamente errores de la API:

1. **API key no configurada**: Usa datos simulados
2. **Error de red**: Intenta con datos simulados
3. **Rate limiting**: Retorna error 429
4. **API key inválida**: Retorna error 401

## Rate Limiting

⚠️ **Importante**: La API de Skyscanner tiene límites de tasa:

- **Free tier**: ~100 requests/día
- **Paid tier**: Según el plan contratado

El sistema no implementa caché actualmente. Para producción, considera:

```python
# Ejemplo de caché simple con TTL
from functools import lru_cache

@lru_cache(maxsize=100)
def search_with_cache(origin, dest, date):
    # ... búsqueda
```

## Próximos Pasos

Una vez obtenida la API key:

1. ✅ Configurar la variable de entorno
2. ✅ Reiniciar el servidor
3. ✅ Probar los endpoints
4. 🔄 Implementar caché (opcional)
5. 🔄 Configurar rate limiting (opcional)
6. 🔄 Añadir métricas y logging (opcional)

## Alternativas a Skyscanner

Si no se obtiene acceso a Skyscanner, se pueden integrar otras APIs:

- **Amadeus API**: https://developers.amadeus.com/
- **Kiwi.com (Tequila API)**: https://tequila.kiwi.com/
- **AviationStack**: https://aviationstack.com/
- **RapidAPI Flight APIs**: https://rapidapi.com/category/Travel

La arquitectura actual permite cambiar fácilmente de proveedor modificando solo `skyscanner_service.py`.

## Soporte

Para problemas o preguntas:

1. Verifica que la API key esté correctamente configurada
2. Revisa los logs del servidor para mensajes de error
3. Consulta la documentación de Skyscanner: https://developers.skyscanner.net/docs/

---

**Estado del Proyecto**: ✅ Listo para producción una vez obtenida la API key
