from fastapi import FastAPI 
from routers import users, peliculas
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Routers
app.include_router(users.router)
app.include_router(peliculas.router)
app.mount("/static", StaticFiles(directory="static"), 
          name="static")



#Crear un endpoint que devuelva un mensaje de bienvenida
#Algo básico para empezar nuesttros toques con FastAPI
@app.get("/")
async def root():
   return {"message": "Hello fastAPI"}
   #Cual es el protocolo de comunicación que se está utilizando?
   #HTTP
    #Cual es el método de comunicación que se está utilizando?
    #GET
    #Cual es el recurso que se está solicitando?
    #"/"
    #Este get forma parte de las comunicaciones disponibles 
    #en el protocolo HTTP
    #Tienes para documnetacion sin necesidad de hacer nada
    #COn swagger o redoc

    #

