from fastapi import FastAPI 


app = FastAPI()


#Crear una función
def root():
    return "Hello World"
