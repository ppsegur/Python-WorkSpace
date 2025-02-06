#Contar el número de espacios en una cadena

#Creamos una variable que guarde la cadena de texto
Cadena = "Hola Mundo, como estas?"
#Ahoora definimos la funcion que cuente espacios de una cadena de caracterees
def ContarEspacios(cadena):
    #Creamos una variable que guarde el número de espacios
    Espacios = 0

    for i in cadena:
        if i == " ":
            Espacios += 1
    return Espacios

print(ContarEspacios(Cadena))