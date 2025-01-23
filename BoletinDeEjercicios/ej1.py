#EJERCICIO 1
# Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
#- Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
#- En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
#- El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse. 

# Diccionario para la conversión entre texto y código morse
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '\'': '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '
}

# Invertir el diccionario para la conversión de morse a texto
MORSE_TO_TEXT_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

#Función que convierte texto a morse
texto = input("Introduce el texto a convertir a morse: ")
Lista = []

for caracter in texto:
    if caracter.islower():
        caracter = caracter.upper()
    Lista.append(MORSE_CODE_DICT[caracter])
print(" ".join(Lista))


#Función que convierte morse a texto
textoM = input("Introduce el texto morse a convertir a texto: ")
ListaM = textoM.split(" ")
palabra = ""
for codigo in ListaM:  # Cambiamos el nombre de la variable del bucle
    Letra = [key for key, value in MORSE_CODE_DICT.items() if value == codigo]
    if Letra:
        letra = Letra[0]
        palabra += letra
    elif codigo == "": 
        palabra += " "
print(palabra)



