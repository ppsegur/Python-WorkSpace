from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel



app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    name: str
    email: str
    username: str
    disable: bool

class UserInDB(User):
    password: str

    

users_db = {
    "pepe":{
        "name": "Pepe Segura",
        "email": "pepe@example.com",
        "username": "pepe",
        "disable": False,
        "password": "1234"
    },
        "pepe2":{
        "name": "Pepe2 Segura",
        "email": "pepe2@example.com",
        "username": "pepe2",
        "disable": True,
        "password": "1234"
    },
}

def search_user(username: str):
    if username in users_db:
        return UserInDB(**users_db[username])
    return None

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    return user



@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = search_user(form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    if not user.password == form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    if user.disable:
        raise HTTPException(status_code=400, detail="User is disabled")
    
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    return user

@app.get("/users/{username}")
async def read_user(username: str):
    user = search_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/")
async def read_users():
    return users_db
