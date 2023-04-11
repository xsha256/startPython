 #! 5. Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh"). El programa debe utilizar un bucle `for` para recorrer la cadena y construir la cadena invertida.

def Convertir(cadena):
    cadenaReversa = ""
    for palabra in cadena:
        cadenaReversa = palabra + cadenaReversa 

    print(cadenaReversa)


cadena = input("Escribe una cadena: ")
Convertir(cadena)