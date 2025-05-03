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

### `FastAPI`
Pruebas y ejemplos sueltos relacionados con FastAPI y anotaciones de tipo en Python (`type_hints.py`).

### `notas.csv`
Archivo de ejemplo  utilizado en el de manejo de ficheros.

---

## 🚀 Cómo ejecutar la API

1. Asegúrate de tener Python 3.10+ instalado.
2. Instala las dependencias necesarias:
   ```bash
   pip install fastapi uvicorn
