"""
Test Client para la API de Búsqueda de Vuelos
==============================================

Este script demuestra el uso de la API de búsqueda de vuelos con datos de entrada
de prueba. Realiza varias llamadas a los endpoints de la API para verificar su
correcto funcionamiento.

Autor: Pepe Segura
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Dict, Any


# Configuración de la API
API_BASE_URL = "http://localhost:8000"


def print_section(title: str):
    """Imprime un separador de sección"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def print_response(response: requests.Response):
    """Imprime la respuesta de la API de forma legible"""
    if response.status_code == 200:
        print(f"✅ Status: {response.status_code} OK")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    else:
        print(f"❌ Status: {response.status_code}")
        print(response.text)


def test_root_endpoint():
    """Test 1: Verificar endpoint raíz"""
    print_section("TEST 1: Endpoint Raíz - Información de la API")
    
    try:
        response = requests.get(f"{API_BASE_URL}/")
        print_response(response)
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_health_check():
    """Test 2: Verificar health check"""
    print_section("TEST 2: Health Check")
    
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        print_response(response)
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_get_airports():
    """Test 3: Obtener lista de aeropuertos"""
    print_section("TEST 3: Lista de Aeropuertos Disponibles")
    
    try:
        response = requests.get(f"{API_BASE_URL}/flights/airports")
        print_response(response)
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_search_flights():
    """Test 4: Buscar vuelos con parámetros específicos"""
    print_section("TEST 4: Búsqueda de Vuelos - Madrid a Barcelona")
    
    # Calcular fecha para mañana
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    params = {
        "origin": "MAD",
        "destination": "BCN",
        "departure_date": tomorrow,
        "max_price": 100
    }
    
    print(f"📋 Parámetros de búsqueda:")
    print(json.dumps(params, indent=2))
    print()
    
    try:
        response = requests.get(f"{API_BASE_URL}/flights/search", params=params)
        print_response(response)
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_weekend_flights_get():
    """Test 5: Buscar vuelos de fin de semana (GET)"""
    print_section("TEST 5: Vuelos Más Baratos del Fin de Semana (GET) - Madrid a Málaga")
    
    params = {
        "origin": "MAD",
        "destination": "AGP",
        "max_price": 150
    }
    
    print(f"📋 Parámetros de búsqueda:")
    print(json.dumps(params, indent=2))
    print()
    
    try:
        response = requests.get(
            f"{API_BASE_URL}/flights/weekend/cheapest",
            params=params
        )
        print_response(response)
        
        if response.status_code == 200:
            data = response.json()
            if "cheapest_combination" in data and data["cheapest_combination"]:
                combo = data["cheapest_combination"]
                print(f"\n💰 COMBINACIÓN MÁS BARATA:")
                print(f"   Total: {combo['total_price']}€")
                print(f"   Ida: {combo['outbound']['airline']} - {combo['outbound']['price']}€")
                print(f"   Vuelta: {combo['return']['airline']} - {combo['return']['price']}€")
        
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_weekend_flights_post():
    """Test 6: Buscar vuelos de fin de semana (POST)"""
    print_section("TEST 6: Vuelos Más Baratos del Fin de Semana (POST) - Barcelona a Valencia")
    
    payload = {
        "origin": "BCN",
        "destination": "VLC",
        "max_price": 120
    }
    
    print(f"📋 Body de la petición:")
    print(json.dumps(payload, indent=2))
    print()
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/flights/weekend/cheapest",
            json=payload
        )
        print_response(response)
        
        if response.status_code == 200:
            data = response.json()
            if "cheapest_combination" in data and data["cheapest_combination"]:
                combo = data["cheapest_combination"]
                print(f"\n💰 COMBINACIÓN MÁS BARATA:")
                print(f"   Total: {combo['total_price']}€")
                print(f"   Ida: {combo['outbound']['airline']} - {combo['outbound']['price']}€")
                print(f"   Vuelta: {combo['return']['airline']} - {combo['return']['price']}€")
        
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_different_routes():
    """Test 7: Probar diferentes rutas populares"""
    print_section("TEST 7: Prueba de Múltiples Rutas Populares")
    
    routes = [
        {"origin": "MAD", "destination": "PMI", "name": "Madrid → Palma de Mallorca"},
        {"origin": "BCN", "destination": "SVQ", "name": "Barcelona → Sevilla"},
        {"origin": "VLC", "destination": "BIO", "name": "Valencia → Bilbao"},
    ]
    
    all_success = True
    
    for route in routes:
        print(f"\n🛫 Probando ruta: {route['name']}")
        print("-" * 60)
        
        try:
            response = requests.get(
                f"{API_BASE_URL}/flights/weekend/cheapest",
                params={
                    "origin": route["origin"],
                    "destination": route["destination"]
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Ruta disponible")
                print(f"   Fechas del fin de semana: {data['weekend_dates']}")
                print(f"   Vuelos de ida encontrados: {len(data['outbound_flights'])}")
                print(f"   Vuelos de vuelta encontrados: {len(data['return_flights'])}")
                
                if data.get("cheapest_combination"):
                    combo = data["cheapest_combination"]
                    print(f"   💰 Precio total más barato: {combo['total_price']}€")
            else:
                print(f"❌ Error en la ruta: {response.status_code}")
                all_success = False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            all_success = False
    
    return all_success


def test_price_filtering():
    """Test 8: Probar filtrado por precio"""
    print_section("TEST 8: Filtrado por Precio - Comparación con y sin límite")
    
    params_no_limit = {
        "origin": "MAD",
        "destination": "BCN"
    }
    
    params_with_limit = {
        "origin": "MAD",
        "destination": "BCN",
        "max_price": 50
    }
    
    try:
        print("🔍 Búsqueda SIN límite de precio:")
        print("-" * 60)
        response1 = requests.get(
            f"{API_BASE_URL}/flights/weekend/cheapest",
            params=params_no_limit
        )
        
        if response1.status_code == 200:
            data1 = response1.json()
            print(f"✅ Vuelos de ida encontrados: {len(data1['outbound_flights'])}")
            if data1.get("cheapest_combination"):
                print(f"💰 Precio más barato: {data1['cheapest_combination']['total_price']}€")
        
        print("\n🔍 Búsqueda CON límite de precio (máx. 50€ por vuelo):")
        print("-" * 60)
        response2 = requests.get(
            f"{API_BASE_URL}/flights/weekend/cheapest",
            params=params_with_limit
        )
        
        if response2.status_code == 200:
            data2 = response2.json()
            print(f"✅ Vuelos de ida encontrados: {len(data2['outbound_flights'])}")
            if data2.get("cheapest_combination"):
                print(f"💰 Precio más barato: {data2['cheapest_combination']['total_price']}€")
        
        return response1.status_code == 200 and response2.status_code == 200
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def run_all_tests():
    """Ejecuta todos los tests"""
    print("\n" + "🚀" * 40)
    print("  INICIANDO PRUEBAS DE LA API DE BÚSQUEDA DE VUELOS")
    print("🚀" * 40)
    
    tests = [
        ("Endpoint Raíz", test_root_endpoint),
        ("Health Check", test_health_check),
        ("Lista de Aeropuertos", test_get_airports),
        ("Búsqueda de Vuelos", test_search_flights),
        ("Vuelos de Fin de Semana (GET)", test_weekend_flights_get),
        ("Vuelos de Fin de Semana (POST)", test_weekend_flights_post),
        ("Múltiples Rutas", test_different_routes),
        ("Filtrado por Precio", test_price_filtering),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"\n❌ Error ejecutando {test_name}: {e}")
            results.append((test_name, False))
    
    # Resumen final
    print_section("RESUMEN DE RESULTADOS")
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n{'=' * 80}")
    print(f"  Total: {passed}/{total} tests pasados ({(passed/total)*100:.1f}%)")
    print(f"{'=' * 80}\n")
    
    if passed == total:
        print("🎉 ¡TODOS LOS TESTS PASARON EXITOSAMENTE!")
    else:
        print(f"⚠️  {total - passed} test(s) fallaron. Revisar logs arriba.")


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║           Test Client - API de Búsqueda de Vuelos Baratos                   ║
║                                                                              ║
║  Este script prueba todos los endpoints de la API con datos de ejemplo      ║
║                                                                              ║
║  REQUISITOS:                                                                 ║
║  1. La API debe estar corriendo en http://localhost:8000                    ║
║  2. Ejecutar primero: uvicorn flight_api.main:app --reload                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Verificar que la API está disponible
    print("🔍 Verificando disponibilidad de la API...")
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            print("✅ API disponible y funcionando\n")
            run_all_tests()
        else:
            print(f"❌ API respondió con código: {response.status_code}")
            print("Por favor, verifica que la API esté corriendo correctamente.")
    except requests.exceptions.ConnectionError:
        print("❌ No se puede conectar a la API")
        print(f"   Asegúrate de que la API esté corriendo en {API_BASE_URL}")
        print("   Ejecuta: uvicorn flight_api.main:app --reload")
    except Exception as e:
        print(f"❌ Error: {e}")
