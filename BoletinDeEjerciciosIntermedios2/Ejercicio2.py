# Encuentra todos los números del 1 al 1000 que incluyan entre sus cifras al menos un 3.

#Creamos la lista de los numeros del 1 al 1000 
Numeros = list(range(1, 1001))

#Creamos una lista donde guardemos todos los número de la naterior lñista dónde se contenga un número 3 en algunas de sus cifras 
Tres = [numero for numero in Numeros if "3" in str(numero)]

#Imprimimos la lista de los números que contienen un 3 en alguna de sus cifras
print(Tres)
