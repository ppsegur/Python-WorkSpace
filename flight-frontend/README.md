# 🛫 Flight Frontend - Buscador de Vuelos Baratos

Frontend desarrollado en **React** con **Vite** para la API de búsqueda de vuelos baratos.

## 🌟 Características

- ✈️ **Búsqueda de vuelos**: Busca vuelos por origen, destino, fecha y precio
- 🎉 **Vuelos de fin de semana**: Encuentra las mejores ofertas para escapadas de fin de semana
- 📱 **Responsive**: Diseño adaptable a todos los dispositivos
- 🎨 **Interfaz moderna**: UI intuitiva y atractiva
- ⚡ **Rápido**: Construido con Vite para desarrollo ultrarrápido

## 🛠️ Tecnologías Utilizadas

- **React 19.2**: Framework JavaScript para interfaces de usuario
- **Vite 7.2**: Build tool moderno y rápido
- **CSS3**: Estilos personalizados con variables CSS
- **Fetch API**: Para comunicación con el backend FastAPI

## 📋 Prerrequisitos

- Node.js 18+ instalado
- npm o yarn
- Backend FastAPI ejecutándose en `http://localhost:8000`

## 🚀 Instalación

1. **Navega al directorio del frontend:**
   ```bash
   cd flight-frontend
   ```

2. **Instala las dependencias:**
   ```bash
   npm install
   ```

## 💻 Uso

### Modo Desarrollo

1. **Asegúrate de que el backend esté ejecutándose:**
   ```bash
   # En otra terminal, desde el directorio raíz
   cd flight_api
   uvicorn main:app --reload
   ```

2. **Inicia el servidor de desarrollo:**
   ```bash
   npm run dev
   ```

3. **Abre tu navegador en:**
   ```
   http://localhost:5173
   ```

### Build para Producción

```bash
npm run build
```

Los archivos optimizados se generarán en la carpeta `dist/`.

### Preview de Producción

```bash
npm run preview
```

## 📂 Estructura del Proyecto

```
flight-frontend/
├── src/
│   ├── components/
│   │   ├── FlightSearch.jsx       # Componente de búsqueda de vuelos
│   │   ├── FlightSearch.css
│   │   ├── WeekendFlights.jsx     # Componente de vuelos de fin de semana
│   │   ├── WeekendFlights.css
│   │   ├── FlightResults.jsx      # Componente de resultados
│   │   └── FlightResults.css
│   ├── App.jsx                     # Componente principal
│   ├── App.css
│   ├── main.jsx                    # Punto de entrada
│   └── index.css
├── public/                         # Archivos estáticos
├── index.html                      # HTML principal
├── vite.config.js                  # Configuración de Vite
└── package.json
```

## 🎯 Funcionalidades

### 1. Búsqueda de Vuelos

Permite buscar vuelos con los siguientes parámetros:
- **Origen**: Aeropuerto de salida
- **Destino**: Aeropuerto de llegada
- **Fecha de salida**: Cuándo quieres viajar
- **Fecha de regreso**: (Opcional) Para viajes de ida y vuelta
- **Precio máximo**: (Opcional) Filtra vuelos por precio

### 2. Vuelos de Fin de Semana

Encuentra automáticamente los vuelos más baratos para el próximo fin de semana:
- Calcula automáticamente las fechas del próximo fin de semana
- Muestra la mejor combinación de vuelos (ida + vuelta)
- Lista los 5 vuelos más baratos de ida
- Lista los 5 vuelos más baratos de vuelta
- Filtra por precio máximo opcional

## 🔧 Configuración

### Proxy API

El frontend está configurado para hacer proxy de las peticiones al backend:

```javascript
// vite.config.js
export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
})
```

Esto permite hacer peticiones a `/api/flights/...` que se redirigen automáticamente a `http://localhost:8000/flights/...`

## 🎨 Personalización

### Colores

Los colores se pueden personalizar en `src/App.css`:

```css
:root {
  --primary-color: #4a90e2;      /* Azul principal */
  --primary-dark: #357abd;        /* Azul oscuro */
  --success-color: #27ae60;       /* Verde para precios */
  --error-color: #e74c3c;         /* Rojo para errores */
  /* ... más variables */
}
```

## 📱 Responsive Design

La aplicación está optimizada para:
- 📱 Móviles (< 768px)
- 💻 Tablets (768px - 1024px)
- 🖥️ Desktop (> 1024px)

## 🐛 Solución de Problemas

### El backend no responde

Asegúrate de que el backend FastAPI esté ejecutándose:
```bash
cd ../flight_api
uvicorn main:app --reload
```

### Error de CORS

El backend ya está configurado para permitir peticiones desde cualquier origen en desarrollo. Si hay problemas, verifica la configuración de CORS en `flight_api/main.py`.

### Puerto 5173 en uso

Si el puerto 5173 está ocupado, puedes especificar otro:
```bash
npm run dev -- --port 3000
```

## 📝 Scripts Disponibles

- `npm run dev` - Inicia el servidor de desarrollo
- `npm run build` - Construye la aplicación para producción
- `npm run preview` - Preview de la build de producción
- `npm run lint` - Ejecuta el linter

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es parte del repositorio Python-WorkSpace de Pepe Segura.

## 👨‍💻 Autor

**Pepe Segura**
- GitHub: [@ppsegur](https://github.com/ppsegur)

## 🙏 Agradecimientos

- API de vuelos construida con FastAPI
- React y Vite por las herramientas increíbles
- Todos los desarrolladores que contribuyen al ecosistema open source

---

**Nota**: Esta es una aplicación de demostración con datos simulados. Para conectar con APIs reales de vuelos como Skyscanner, se necesitaría:
- API Key de Skyscanner
- Implementar autenticación OAuth
- Manejar rate limiting y caché
