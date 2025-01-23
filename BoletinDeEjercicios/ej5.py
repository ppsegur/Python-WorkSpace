#EJERCICIO 5
#Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
#- La función recibirá dos parámetros:
#     - Un array que sólo puede contener String con las palabras "run" o "jump"
#     - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
#- La función imprimirá cómo ha finalizado la carrera:
#     - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
#     - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#     - Si hace "run" en "|" (valla), se variará la pista por "/".
#- La función retornará un Boolean que indique si ha superado la carrera. Para ello tiene que realizar la opción correcta en cada tramo de la pista.

acciones = ["run", "jump", "run", "jump"]
pista = "_|_|"

def carrera_obstaculos(acciones, pista):
    pista = list(pista)
    
    # Recorrer las acciones y la pista
    for i in range(len(acciones)):
        accion = acciones[i]
        tramo = pista[i]

        # Verificar si la acción es correcta
        if accion == "run" and tramo == "_":
            continue  
        elif accion == "jump" and tramo == "|":
            continue  
        elif accion == "run" and tramo == "|":
            pista[i] = "/"
        elif accion == "jump" and tramo == "_":
            pista[i] = "x"  
        else:
            return False  # Si no cumple con las condiciones, retorna False
    
    # Convertir la lista de nuevo a string
    pista_final = ''.join(pista)
    print(f"Pista final: {pista_final}")
    
    # Si no hay 'x' ni '/' en la pista final, la carrera fue superada
    return "x" not in pista_final and "/" not in pista_final


print("¿Superaste la carrera?", carrera_obstaculos(acciones, pista))
