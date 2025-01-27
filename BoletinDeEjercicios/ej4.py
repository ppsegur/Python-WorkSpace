#EJERCICIO 4

#Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
#- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.


def primera_mayuscula(cad):
    resultado = []  
    inicio_palabra = True  

    for char in cad:
        if inicio_palabra and char.isalpha():  
            if 'a' <= char <= 'z':
                resultado.append(chr(ord(char) - 32))
            else:
                resultado.append(char) 
            inicio_palabra = False 
        else:
            if char == ' ': 
                inicio_palabra = True
            resultado.append(char) 

    return ''.join(resultado)


cad = input("Introduce una cadena de texto: ")
resultado = primera_mayuscula(cad)
print(resultado)