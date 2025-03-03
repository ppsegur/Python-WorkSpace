from fastapi import FastAPI
from pydantic import BaseModel
#from typing import Union


app = FastAPI()

#Inicia el server : uvicorn users:app --reload

#Entidad User
class User(BaseModel):
    name: str
    email: str
    username: str
    age: int

users_list = [User(id=1,name="Pepe Segura", email="pepe@example.com", username="pepe", age=30),
              User(id=2 ,name="Juan Perez", email="juan@example.com", username="juan", age=25),
              User(id=3,name="Maria Lopez", email="marial@example.com", username="marial", age=35)]




@app.get("/users")
async def usersListJson():
    return users_list 
#ASI DEVUELVE UN JSON de la lista de usuarios


@app.get("/users/{user_id}")
async def userfindById(user_id: int):
    user = filter(lambda user: user.id ==id , users_list)
    try:
        return list(user)[0]
    except: 
        return {"error":"No se ha encontardo usuarios con ese user "}


#ASI DEVUELVE UN JSON de un usuario en concreto

@app.get("/user/")
async def userfindById(user_id: int, name:str):
    return search_user(user_id, name)


def search_user(id):
    user = filter(lambda user: user.id ==id , users_list)   
    try:
        return list(user)[0]
    except: 
        return {"error":"No se ha encontardo usuarios con ese user "}
#Para pasr un parametro lo haremos con /{parametro}
#Para pasar un parametro opcional lo haremos con /{parametro:tipo}


@app.post("/user")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"error":"El usuario ya existe"}
    
    users_list.append(user)
    return user
#ASI DEVUELVE UN JSON de un usuario en concreto creado

@app.put("/user/{user_id}")
async def update_user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error":"No se ha encontardo usuarios con ese user "}
   
    return user
    
        


#ASI DEVUELVE UN JSON de un usuario en concreto actualizado

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user_id:
            del users_list(index)
            found = True
            
    if not found:
        return {"error":"No se ha encontardo usuarios con ese user "}
#Códigos de estatus
#200 OK
#201 Created
#204 No Content
#400 Bad Request
#404 Not Found
#405 Method Not Allowed
#500 Internal Server Error
#503 Service Unavailable
#504 Gateway Timeout
#206 Partial Content
#401 Unauthorized
#403 Forbidden
#429 Too Many Requests
#409 Conflict
#412 Precondition Failed
#413 Payload Too Large
#415 Unsupported Media Type
#416 Range Not Satisfiable
#417 Expectation Failed
#418 I'm a teapot
#422 Unprocessable Entity
#426 Upgrade Required
#428 Precondition Required
#431 Request Header Fields Too Large
#451 Unavailable For Legal Reasons
#500 Internal Server Error


