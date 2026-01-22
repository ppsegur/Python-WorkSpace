# Pepe Segura Frontend

React frontend application for the API Pepe Segura - Entertainment & Movie Management System.

## Overview

This is a modern, responsive React application that provides a user-friendly interface to interact with the API Pepe Segura backend. The frontend allows users to browse movies, actors, directors, reviews, watchlists, and genres.

## Features

- 🎬 **Movies Browser** - Browse and filter movies by genre with detailed movie pages
- 🎭 **Actors Gallery** - View actor profiles and biographies
- 🎥 **Directors Gallery** - Explore director information and filmographies
- ⭐ **Reviews System** - Read film reviews and ratings
- 📝 **Watchlists** - View curated movie collections
- 🎨 **Genres** - Explore movie categories
- 📊 **Dashboard** - View statistics and API health status

## Technology Stack

- **React 19** - Modern UI library
- **React Router** - Client-side routing
- **Axios** - HTTP client for API calls
- **Vite** - Fast build tool and dev server
- **CSS3** - Modern styling with gradients and animations

## Prerequisites

- Node.js 16+ and npm
- API Pepe Segura backend running on `http://localhost:8000`

## Installation & Running

1. Navigate to the frontend directory:
```bash
cd pepe-segura-frontend
```

2. Install dependencies (already done):
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:5173`

## API Configuration

The frontend connects to the backend API at `http://localhost:8000`. Update `src/services/api.js` to change this.

## Available Routes

- `/` - Home page with statistics
- `/movies` - Browse all movies
- `/movies/:id` - Movie details
- `/actors` - View all actors
- `/directors` - View all directors
- `/reviews` - Browse reviews
- `/watchlists` - View watchlists
- `/genres` - Explore genres

## Author

Pepe Segura
