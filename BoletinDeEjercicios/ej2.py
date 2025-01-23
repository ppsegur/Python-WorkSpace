#EJERCICIO 2
#Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
#- Equilibrado significa que estos delimitadores se abren y cierran en orden y de forma correcta.
#- Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
#- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#- Expresión no balanceada: { a * ( c + d ) ] - 5 }

# Función que comprueba si una expresión está balanceada dependiend de sus parentesis , llaves y corchetes
def esta_balanceada(expresion):
    # Diccionario de pares de delimitadores
    pares = {'(': ')', '{': '}', '[': ']'}
    #Lista vacia para almacenar los delimitadores
    pila = []

    for caracter in expresion:
        # Si el caracter es un delimitador de apertura, lo añadimos a la pila
        if caracter in pares.keys():
            pila.append(caracter)
            # Si el caracter es un delimitador de cierre, comprobamos si coincide con el último delimitador de apertura
        elif caracter in pares.values():
            if not pila or pares[pila.pop()] != caracter:
                return False

    # La pila debe estar vacía al final si todo está balanceado
    return not pila


# Ejemplos de uso
expresion1 = "{ [ a * ( c + d ) ] - 5 }"
expresion2 = "{ a * ( c + d ) ] - 5 }"

print(esta_balanceada(expresion1))  
print(esta_balanceada(expresion2)) 
