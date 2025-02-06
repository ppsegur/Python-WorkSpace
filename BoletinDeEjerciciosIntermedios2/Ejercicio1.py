# Encuentra todos los números del 1 al 1000 que sean divisibles por 7

DelUnoCIen = list(range(1, 1001))

DivisiblePorSiete = [numero for numero in DelUnoCIen if numero % 7 == 0]

print(DivisiblePorSiete)
