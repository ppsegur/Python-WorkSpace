#Encuentra todas las palabras en una cadena que tengan menos de 4 letras
cadena = "A los yaks amarillos les gusta gritar y bostezar ayer cantaban mientras comían ñames asquerosos"
#Creamos una lista de las palabras que tienen menos de 4 letras
Palabras = [palabra for palabra in cadena.split() if len(palabra) < 4]
#Imprimimos la lista de palabras
print(Palabras)
