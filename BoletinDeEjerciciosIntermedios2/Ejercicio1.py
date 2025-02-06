# Encuentra todos los números del 1 al 1000 que sean divisibles por 7

#Creamos la lista de rango del 1 al cien 
DelUnoCIen = list(range(1, 1001))

#Aqui creamos una lista donde los números que se guardan son solo de la anterior lo que al dividir entre 7 su resto sea cero 
DivisiblePorSiete = [numero for numero in DelUnoCIen if numero % 7 == 0]

#Imprimimos la lista de los números divisibles por 7
print(DivisiblePorSiete)
