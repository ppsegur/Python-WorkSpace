#EJERCICIO 6
#Crea una función que reciba dos array, un booleano y retorne un array.
#- Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
#- Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
#- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
booleano = False

#Función que recibe dos array, un booleano y retorna un array distinto dependiendo del booleano 
def elemets_comunes_ono(array1, array2, booleano):
    if booleano:
        return [element for element in array1 if element in array2]
    else:
        return [element for element in array1 if element not in array2] + [element for element in array2 if element not in array1]
    
print(elemets_comunes_ono(array1, array2, booleano)) #[4, 5]
