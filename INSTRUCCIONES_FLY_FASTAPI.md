# Instrucciones para Usar la Rama fly-fastApi

## 📋 Información de la Rama

La rama **fly-fastApi** ha sido creada exitosamente con un sistema completo de pruebas para la API de búsqueda de vuelos.

## 🔄 Cómo Acceder a la Rama

### Opción 1: Cambiar a la rama localmente

Si ya tienes el repositorio clonado:

```bash
cd Python-WorkSpace
git checkout fly-fastApi
```

### Opción 2: Clonar y acceder a la rama

```bash
git clone https://github.com/ppsegur/Python-WorkSpace.git
cd Python-WorkSpace
git checkout fly-fastApi
```

## 📂 Contenido de la Rama

Una vez en la rama `fly-fastApi`, encontrarás:

```
Python-WorkSpace/
├── RESUMEN_FLY_FASTAPI.md          # Resumen ejecutivo de la implementación
└── flight_api/
    ├── test_client.py               # Cliente de pruebas con 8 tests automatizados
    ├── run_tests.sh                 # Script de automatización de tests
    ├── GUIA_PRUEBAS.md             # Guía completa de uso y pruebas
    ├── README_FLY_FASTAPI.md       # Documentación detallada
    ├── requirements.txt             # Dependencias actualizadas (incluye requests)
    ├── main.py                      # API FastAPI principal
    ├── models/                      # Modelos Pydantic
    ├── routers/                     # Endpoints de la API
    └── services/                    # Lógica de negocio
```

## 🚀 Ejecutar las Pruebas

### Método 1: Script Automático (Recomendado)

```bash
cd flight_api
./run_tests.sh
```

Este script:
1. ✅ Instala las dependencias
2. ✅ Inicia el servidor FastAPI
3. ✅ Ejecuta todos los tests (8 en total)
4. ✅ Detiene el servidor automáticamente
5. ✅ Muestra un resumen de resultados

### Método 2: Manual (2 Terminales)

**Terminal 1 - Servidor:**
```bash
cd Python-WorkSpace
pip install -r flight_api/requirements.txt
uvicorn flight_api.main:app --reload
```

**Terminal 2 - Tests:**
```bash
cd Python-WorkSpace/flight_api
python3 test_client.py
```

## 📊 Qué Esperar

Al ejecutar los tests, verás:

```
🚀 INICIANDO PRUEBAS DE LA API DE BÚSQUEDA DE VUELOS

================================================================================
  TEST 1: Endpoint Raíz - Información de la API
================================================================================
✅ Status: 200 OK
...

================================================================================
  RESUMEN DE RESULTADOS
================================================================================
✅ PASS - Endpoint Raíz
✅ PASS - Health Check
✅ PASS - Lista de Aeropuertos
✅ PASS - Búsqueda de Vuelos
✅ PASS - Vuelos de Fin de Semana (GET)
✅ PASS - Vuelos de Fin de Semana (POST)
✅ PASS - Múltiples Rutas
✅ PASS - Filtrado por Precio

Total: 8/8 tests pasados (100.0%)
🎉 ¡TODOS LOS TESTS PASARON EXITOSAMENTE!
```

## 📖 Documentación Disponible

Una vez en la rama, lee estos archivos para más información:

1. **RESUMEN_FLY_FASTAPI.md** - Resumen ejecutivo de todo el proyecto
2. **flight_api/README_FLY_FASTAPI.md** - Documentación completa de implementación
3. **flight_api/GUIA_PRUEBAS.md** - Guía detallada de las pruebas
4. **flight_api/README.md** - Documentación de la API original

## 🌐 Acceder a la Documentación Interactiva

Con el servidor corriendo (`uvicorn flight_api.main:app --reload`):

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **API Root**: http://localhost:8000/

## 🧪 Tests Incluidos

1. **Endpoint Raíz** - Verifica información de la API
2. **Health Check** - Estado del servicio
3. **Lista de Aeropuertos** - Aeropuertos disponibles
4. **Búsqueda de Vuelos** - Madrid → Barcelona con límite de precio
5. **Vuelos de Fin de Semana (GET)** - Madrid → Málaga
6. **Vuelos de Fin de Semana (POST)** - Barcelona → Valencia
7. **Múltiples Rutas** - 3 rutas diferentes simultáneas
8. **Filtrado por Precio** - Comparación con/sin filtro

## 🎯 Datos de Ejemplo

Los tests usan datos realistas:

**Aeropuertos:**
- MAD (Madrid), BCN (Barcelona), AGP (Málaga)
- PMI (Palma de Mallorca), SVQ (Sevilla), VLC (Valencia)
- ALC (Alicante), BIO (Bilbao)

**Rutas de Prueba:**
- Madrid → Barcelona (max: 100€)
- Madrid → Málaga (max: 150€)
- Barcelona → Valencia (max: 120€)
- Y más...

## ✅ Verificación de Implementación

Para verificar que la rama está correctamente configurada:

```bash
# Verifica que estás en la rama correcta
git branch --show-current
# Debería mostrar: fly-fastApi

# Lista los archivos nuevos
ls -lah flight_api/
# Deberías ver: test_client.py, run_tests.sh, GUIA_PRUEBAS.md, etc.

# Ejecuta los tests
cd flight_api && ./run_tests.sh
```

## 🆘 Solución de Problemas

### Error: "Rama no encontrada"
```bash
git fetch origin
git checkout -b fly-fastApi origin/fly-fastApi
```

### Error: "Puerto 8000 en uso"
```bash
# Encuentra el proceso
lsof -i :8000
# Mata el proceso
kill -9 <PID>
```

### Error: "Módulo no encontrado"
```bash
pip install -r flight_api/requirements.txt
```

## 📞 Soporte

- Ver documentación en `flight_api/GUIA_PRUEBAS.md`
- Revisar ejemplos en `test_client.py`
- Consultar `RESUMEN_FLY_FASTAPI.md` para overview

## 🎉 Resultado Esperado

Si todo está bien:
- ✅ 8/8 tests pasan exitosamente
- ✅ API responde correctamente
- ✅ Datos de prueba funcionan
- ✅ Documentación completa disponible

---

**Nota**: La rama `fly-fastApi` está lista para uso inmediato. Todos los tests han sido ejecutados y verificados exitosamente.
