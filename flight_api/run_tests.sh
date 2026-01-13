#!/bin/bash

# Script para ejecutar tests de la API de Vuelos
# ================================================

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                              ║"
echo "║           Script de Ejecución de Tests - API de Vuelos                      ║"
echo "║                                                                              ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar si estamos en el directorio correcto
if [ ! -f "main.py" ]; then
    echo -e "${RED}❌ Error: Este script debe ejecutarse desde el directorio flight_api${NC}"
    echo "   Ejecuta: cd flight_api && ./run_tests.sh"
    exit 1
fi

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Error: Python 3 no está instalado${NC}"
    exit 1
fi

echo -e "${YELLOW}📦 Paso 1: Instalando dependencias...${NC}"
pip install -r requirements.txt > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Dependencias instaladas correctamente${NC}"
else
    echo -e "${RED}❌ Error al instalar dependencias${NC}"
    exit 1
fi

echo ""
echo -e "${YELLOW}🚀 Paso 2: Iniciando servidor FastAPI...${NC}"
echo "   URL: http://localhost:8000"
echo "   Docs: http://localhost:8000/docs"
echo ""

# Iniciar el servidor en background
uvicorn main:app --reload > /tmp/fastapi_server.log 2>&1 &
SERVER_PID=$!

# Guardar PID para poder detener el servidor después
echo $SERVER_PID > /tmp/fastapi_server.pid

# Esperar a que el servidor esté listo
echo -e "${YELLOW}⏳ Esperando a que el servidor esté listo...${NC}"
sleep 5

# Verificar si el servidor está corriendo
if ps -p $SERVER_PID > /dev/null; then
    echo -e "${GREEN}✅ Servidor iniciado correctamente (PID: $SERVER_PID)${NC}"
else
    echo -e "${RED}❌ Error: El servidor no se inició correctamente${NC}"
    echo "   Revisa los logs en /tmp/fastapi_server.log"
    exit 1
fi

echo ""
echo -e "${YELLOW}🧪 Paso 3: Ejecutando tests del cliente...${NC}"
echo ""

# Ejecutar el cliente de pruebas
python3 test_client.py

TEST_RESULT=$?

echo ""
echo -e "${YELLOW}🛑 Paso 4: Deteniendo servidor...${NC}"

# Detener el servidor
kill $SERVER_PID 2>/dev/null
rm /tmp/fastapi_server.pid

if [ $TEST_RESULT -eq 0 ]; then
    echo -e "${GREEN}✅ Todos los tests completados${NC}"
else
    echo -e "${YELLOW}⚠️  Algunos tests pueden haber fallado. Revisa el output arriba.${NC}"
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════════════════"
echo ""
echo "💡 Comandos útiles:"
echo "   - Para ver logs del servidor: tail -f /tmp/fastapi_server.log"
echo "   - Para ejecutar el servidor manualmente: uvicorn main:app --reload"
echo "   - Para ejecutar solo los tests: python3 test_client.py"
echo "   - Para ver la documentación: http://localhost:8000/docs (con servidor activo)"
echo ""
