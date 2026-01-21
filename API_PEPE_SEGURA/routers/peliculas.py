from fastapi import APIRouter, HTTPException 
from pydantic import BaseModel

router = APIRouter(prefix="/peliculas", 
                   tags=["peliculas"], 
                   responses={404: {"description": "Not found"}})

class Film(BaseModel):
    id: int
    nombre: str
    director: str
    genero: str
    duracion: int
    anio: int
    portada: str

peliculas_list = [Film(id=1, nombre="El Padrino", director="Francis Ford Coppola", genero="Drama", duracion=175, anio=1972, portada="static/El_Padrino.jpg"),
                Film(id=2, nombre="El Padrino II", director="Francis Ford Coppola", genero="Drama", duracion=202, anio=1974, portada="static/El_Padrino_II.jpg"),
                Film(id=3, nombre="El Padrino III", director="Francis Ford Coppola", genero="Drama", duracion=162, anio=1990 , portada="static/El_Padrino_III.jpg"),
                Film(id=4, nombre="Pulp Fiction", director="Quentin Tarantino", genero="Crime", duracion=154, anio=1994, portada="static/pulp_fiction.jpg"),
                Film(id=5, nombre="Inception", director="Christopher Nolan", genero="Sci-Fi", duracion=148, anio=2010, portada="static/inception.jpg"),
                Film(id=6, nombre="The Dark Knight", director="Christopher Nolan", genero="Action", duracion=152, anio=2008, portada="static/dark_knight.jpg"),
                Film(id=7, nombre="Fight Club", director="David Fincher", genero="Drama", duracion=139, anio=1999, portada="static/fight_club.jpg"),
                Film(id=8, nombre="Forrest Gump", director="Robert Zemeckis", genero="Drama", duracion=142, anio=1994, portada="static/forrest_gump.jpg"),
                Film(id=9, nombre="The Matrix", director="Lana Wachowski, Lilly Wachowski", genero="Sci-Fi", duracion=136, anio=1999, portada="static/matrix.jpg"),
                Film(id=10, nombre="The Shawshank Redemption", director="Frank Darabont", genero="Drama", duracion=142, anio=1994, portada="static/shawshank.jpg")]
             


@router.get("/")
async def peliculasListJson():
    return peliculas_list


@router.get("/{pelicula_id}")
async def peliculafindById(pelicula_id: int):
    film = filter(lambda pelicula: pelicula.id == pelicula_id, peliculas_list)
    try:
        return list(film)[0]
    except:
        raise HTTPException(status_code=404, detail="No existen peliculas con ese nombre")
    
@router.get("/")
async def peliculafindById(pelicula_id: int, nombre: str):
    return search_pelicula(pelicula_id, nombre)

def search_pelicula(id):
    pelicula = filter(lambda pelicula: pelicula.id == id, peliculas_list)
    try:
        return list(pelicula)[0]
    except:
        return {"error": "No se ha encontrado peliculas con ese nombre"}

@router.post("/", status_code=201)
async def create_pelicula(film: Film):
    if type(search_pelicula(film.id)) == Film:
        raise HTTPException(status_code=204, detail="La pelicula ya existe")
    peliculas_list.append(film)
    return {"message": "Film creada"}

@router.put("/{pelicula_id}")
async def update_pelicula(pelicula_id: int, film: Film):
    if type(search_pelicula(pelicula_id)) == film:
        peliculas_list[pelicula_id - 1] = film
        return {"message": "Pelicula actualizada"}
    else:
        raise HTTPException(status_code=404, detail="No existe la pelicula")

@router.delete("/{pelicula_id}")
async def delete_pelicula(pelicula_id: int):
    if type(search_pelicula(pelicula_id)) == Film:
        peliculas_list.pop(pelicula_id - 1)
        return {"message": "Pelicula eliminada"}
    else:
        raise HTTPException(status_code=404, detail="No existe la pelicula")






