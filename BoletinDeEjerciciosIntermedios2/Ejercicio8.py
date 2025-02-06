#Dado numbers = range(20), se genera una lista 
# que contiene la palabra "par" si un número en
#  os números es par, y la palabra "impar" 
# si el número es impar.
#  El resultado se vería así: 
# "impar", "impar", "par".
#
numbers = range(20)

numeros = ["par" if numero % 2 == 0 else "impar" for numero in numbers]

print(numeros)
print(range(20))