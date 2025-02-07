# Ejercicio 7 Obtén solamente los números en una oración como 'En 1984 hubo 13 casos de protesta con más de 1000 asistentes'


lista = [ 'En', '1984', 'hubo', '13' ,'casos',  'de', 'protesta ','con' 'más', 'de' ,'1000' ,'asistentes']

listaNumeros = [palabra for palabra in lista if palabra.isnumeric()]

print(listaNumeros)