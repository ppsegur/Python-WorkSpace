#Crea una lista de todas las consonantes de la cadena 
# “A los yaks amarillos les gusta gritar y bostezar y 
# ayer cantaban mientras comían ñames asquerosos”

lista = ["A", "los", "yaks", "amarillos", "les", "gusta", "gritar", "y", "bostezar", "y", "ayer", "cantaban", "mientras", "comían", "ñames", "asquerosos"]

#Creamos una lista de las consonantes con su condición 
Consonantes = [letra for palabra in lista for letra in palabra if letra.lower() in "aeiouáéíóú"]

print(Consonantes)