#EJERCICIO 3
#Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
#- out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
#- out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
 
str1 = "hola"
str2 = "adios"

#Ahora debemos imprimir dos cadenas out1 y out2 que contengan los caracteres que no estén presentes en la otra cadena
def caracteres_no_comunes(str1, str2):
    #Conjunto de caracteres que no están en la otra cadena
    out1 = set(str1) - set(str2)
    out2 = set(str2) - set(str1)
    return ''.join(out1), ''.join(out2)

print(caracteres_no_comunes(str1, str2)) #('hl', 'is')


