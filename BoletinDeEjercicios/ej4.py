#EJERCICIO 4

#Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
#- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.


cad = input("Introduce una cadena de texto: ")
# Primera letra de cada palabra 

def primera_mayuscula(cad):
    for palabra in cad:
        print(palabra.capitalize(), end = "")

primera_mayuscula(cad)

