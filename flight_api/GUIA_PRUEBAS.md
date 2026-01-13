# Guía de Uso del Cliente de Pruebas
# ===================================

Este documento explica cómo usar el cliente de pruebas (`test_client.py`) para verificar el correcto funcionamiento de la API de búsqueda de vuelos.

## 📋 Descripción

El cliente de pruebas es un script Python que realiza llamadas HTTP a todos los endpoints de la API para verificar que funcionan correctamente. Incluye 8 tests diferentes que cubren toda la funcionalidad de la API.

## 🔧 Requisitos Previos

1. Python 3.10 o superior instalado
2. Las dependencias del proyecto instaladas:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Formas de Ejecutar los Tests

### Opción 1: Script Automático (Recomendado)

El script `run_tests.sh` automatiza todo el proceso:

```bash
cd flight_api
./run_tests.sh
```

Este script:
1. ✅ Instala las dependencias necesarias
2. ✅ Inicia el servidor FastAPI
3. ✅ Ejecuta todos los tests automáticamente
4. ✅ Detiene el servidor al finalizar

### Opción 2: Manual en 2 Terminales

#### Terminal 1 - Servidor:
```bash
cd /home/runner/work/Python-WorkSpace/Python-WorkSpace
uvicorn flight_api.main:app --reload
```

#### Terminal 2 - Tests:
```bash
cd /home/runner/work/Python-WorkSpace/Python-WorkSpace/flight_api
python3 test_client.py
```

### Opción 3: Desde el directorio raíz

```bash
# Terminal 1 - Servidor
uvicorn flight_api.main:app --reload

# Terminal 2 - Tests
python3 flight_api/test_client.py
```

## 🧪 Tests Incluidos

El cliente de pruebas ejecuta los siguientes tests:

### 1. **Endpoint Raíz**
- **Endpoint**: `GET /`
- **Propósito**: Verificar información básica de la API
- **Resultado esperado**: Información sobre endpoints disponibles

### 2. **Health Check**
- **Endpoint**: `GET /health`
- **Propósito**: Verificar estado del servicio
- **Resultado esperado**: Status "healthy"

### 3. **Lista de Aeropuertos**
- **Endpoint**: `GET /flights/airports`
- **Propósito**: Obtener aeropuertos disponibles
- **Resultado esperado**: Lista de códigos IATA y nombres

### 4. **Búsqueda de Vuelos**
- **Endpoint**: `GET /flights/search`
- **Datos de entrada**:
  - Origen: MAD (Madrid)
  - Destino: BCN (Barcelona)
  - Fecha: Mañana
  - Precio máximo: 100€
- **Resultado esperado**: Lista de vuelos ordenados por precio

### 5. **Vuelos de Fin de Semana (GET)**
- **Endpoint**: `GET /flights/weekend/cheapest`
- **Datos de entrada**:
  - Origen: MAD (Madrid)
  - Destino: AGP (Málaga)
  - Precio máximo: 150€
- **Resultado esperado**: 
  - Top 5 vuelos de ida
  - Top 5 vuelos de vuelta
  - Combinación más barata

### 6. **Vuelos de Fin de Semana (POST)**
- **Endpoint**: `POST /flights/weekend/cheapest`
- **Datos de entrada** (JSON):
  ```json
  {
    "origin": "BCN",
    "destination": "VLC",
    "max_price": 120
  }
  ```
- **Resultado esperado**: Vuelos del fin de semana para Barcelona → Valencia

### 7. **Múltiples Rutas**
- **Propósito**: Probar varias rutas populares
- **Rutas probadas**:
  - Madrid → Palma de Mallorca
  - Barcelona → Sevilla
  - Valencia → Bilbao
- **Resultado esperado**: Vuelos disponibles para todas las rutas

### 8. **Filtrado por Precio**
- **Propósito**: Comparar resultados con y sin límite de precio
- **Pruebas**:
  - Sin límite de precio
  - Con límite de 50€ por vuelo
- **Resultado esperado**: Menos resultados con límite de precio

## 📊 Interpretación de Resultados

### Resultado Exitoso
```
✅ PASS - Endpoint Raíz
✅ PASS - Health Check
✅ PASS - Lista de Aeropuertos
...
Total: 8/8 tests pasados (100.0%)
🎉 ¡TODOS LOS TESTS PASARON EXITOSAMENTE!
```

### Resultado con Errores
```
✅ PASS - Endpoint Raíz
❌ FAIL - Health Check
...
Total: 7/8 tests pasados (87.5%)
⚠️  1 test(s) fallaron. Revisar logs arriba.
```

## 🔍 Datos de Entrada Utilizados

El cliente utiliza los siguientes datos de prueba:

### Aeropuertos
- **MAD**: Madrid
- **BCN**: Barcelona
- **AGP**: Málaga
- **VLC**: Valencia
- **PMI**: Palma de Mallorca
- **SVQ**: Sevilla
- **BIO**: Bilbao
- **ALC**: Alicante

### Parámetros de Búsqueda
- Fechas: Calculadas dinámicamente (próximo fin de semana)
- Precios máximos: 50€, 100€, 120€, 150€
- Rutas variadas entre principales ciudades españolas

## 🐛 Solución de Problemas

### Error: "No se puede conectar a la API"
**Causa**: El servidor no está corriendo
**Solución**: 
```bash
uvicorn flight_api.main:app --reload
```

### Error: "Module not found"
**Causa**: Falta instalar dependencias
**Solución**:
```bash
pip install -r requirements.txt
```

### Error: "Address already in use"
**Causa**: El puerto 8000 ya está en uso
**Solución**:
```bash
# Encuentra el proceso
lsof -i :8000
# Mata el proceso
kill -9 <PID>
# O usa otro puerto
uvicorn flight_api.main:app --reload --port 8001
```

## 📝 Personalización

### Cambiar URL de la API
Edita la variable `API_BASE_URL` en `test_client.py`:
```python
API_BASE_URL = "http://localhost:8001"  # Cambiar puerto
```

### Agregar Nuevos Tests
Agrega una nueva función en `test_client.py`:
```python
def test_mi_nuevo_test():
    """Test personalizado"""
    print_section("Mi Nuevo Test")
    # ... tu código aquí
    return True  # o False si falla
```

Luego agrégala a la lista de tests:
```python
tests = [
    # ... tests existentes
    ("Mi Nuevo Test", test_mi_nuevo_test),
]
```

## 📚 Documentación Adicional

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **README principal**: Ver `README.md` en el mismo directorio

## 💡 Consejos

1. **Ejecuta primero el script automático** (`run_tests.sh`) para una verificación rápida
2. **Usa la documentación Swagger** en `/docs` para probar endpoints manualmente
3. **Revisa los logs** si un test falla para entender el problema
4. **Los datos son simulados**, así que los vuelos y precios son aleatorios cada vez

## 🎯 Objetivo de los Tests

Este cliente de pruebas demuestra que:
1. ✅ La API está correctamente configurada
2. ✅ Todos los endpoints responden correctamente
3. ✅ Los modelos de datos son válidos
4. ✅ El filtrado y ordenamiento funcionan
5. ✅ Los cálculos de fin de semana son correctos
6. ✅ Las combinaciones de vuelos se calculan bien
7. ✅ La API maneja diferentes rutas y parámetros
8. ✅ El sistema está listo para uso o integración
