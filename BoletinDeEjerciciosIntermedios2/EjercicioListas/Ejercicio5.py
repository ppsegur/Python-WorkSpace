# Obtén el índice y el valor como una tupla para los elementos de la lista 
# “hi”, 4, 8.99, 'apple', ('t,b','n'). 
# El resultado se vería así (índice, valor), (índice, valor)

lista = ["hi", 4, 8.99, 'apple', ('t,b','n')]

#Creamos una lista de tuplas con los indices y valores de la lista
Tuplas = [(i, lista[i]) for i in range(len(lista))]

print(Tuplas)

