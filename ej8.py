"""
EJERCICIO 8
¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron contra otras bondadosas que no quieren que el mal reine sobre sus tierras.
Cada raza tiene asociado un "valor" entre 1 y 5:
- Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),  Númenóreanos (4), Elfos (5)
- Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),  Huargos (3), Trolls (5)
Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
- El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la suma del valor del ejército y el número de integrantes.
- Cada ejército puede estar compuesto por un número de integrantes variable  de cada raza.
- Tienes total libertad para modelar los datos del ejercicio.
Ej: 1 Peloso pierde contra 1 Orco
    2 Pelosos empatan contra 1 Orco
    3 Pelosos ganan a 1 Orco
"""

#Diccionarios de razas con su valor
ejercito1Bien= { "Pelosos": 1, "Sureños buenos": 2, "Enanos": 3, "Númenóreanos": 4, "Elfos": 5}
ejercito2Mal= { "Sureños malos": 2, "Orcos": 2, "Goblins": 2, "Huargos": 3, "Trolls": 5}

#Función que calcula el resultado de la guerra
def guerra(ejercito1,ejercito2):
    suma1 = sum(ejercito1.values())
    suma2 = sum(ejercito2.values())

    if suma1 > suma2:
        return "El bien ha ganado"
    elif suma1 < suma2:
        return "El mal ha ganado"
    else:
        return "Empate"
    
#Imprimimos el resultado de la guerra
print(guerra(ejercito1Bien,ejercito2Mal)) 

