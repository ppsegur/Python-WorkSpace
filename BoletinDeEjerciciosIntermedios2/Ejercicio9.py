# Generar una lista de tuplas 

list_a = 1, 2, 3,4,5,6,7,8,9
list_b = 2, 7, 1, 12

#Creamos una lista de tuplas con los números iguales de ambas listas
Tuplas = [(i, j) for i in list_a for j in list_b if i == j]


#Imprimimos la lista de tuplas
print(Tuplas)
