#
#EJERCICIO 7
#Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
#- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#- La función recibe un listado que contiene pares, representando cada jugada.
#- El par puede contener combinaciones de "R" (piedra), "P" (papel)  o "S" (tijera).
#- Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".


partida = [("R","S"), ("S","R"), ("P","S")]

def piedra_papel_tijera(partida):
    player1_victoria = 0 
    player2_victoria = 0

    for jugada in partida:
        p1,p2 = jugada
    
        if p1 == p2:
            continue #Empate
        elif (p1 == "R" and p2 == "S") or (p1 == "S" and p2 == "P") or (p1 == "P" and p2 == "R"):
            player1_victoria += 1
        else:
            player2_victoria += 1
    #Lo sacamos de la función para que sea más legible  y funcione bien
    if player1_victoria > player2_victoria:
        return "Player 1"
    elif player1_victoria < player2_victoria:
        return "Player 2"
    else:
        return "Tie"
    
print(piedra_papel_tijera(partida)) #Player 2

