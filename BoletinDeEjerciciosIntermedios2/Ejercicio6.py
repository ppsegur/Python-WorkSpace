#Encuentra los números comunes en dos 
# listas (sin usar una tupla o conjunto) 
# lista_a = 1, 2, 3, 4, lista_b = 2, 3, 4, 5
lisat1 = [1, 2, 3, 4]
lista2 = [2, 3, 4, 5]
#Creamos una lista donde guardamos los números que se encuentran en ambas listas
Comunes = [numero for numero in lisat1 if numero in lista2]
#Imprimimos la lista de los números comunes
print(Comunes)
