
def Palindromo(cadena):
    #! lower(): para convertir a minúsculas
    #! replace(): para eliminar espacios en blanco
    cadenaOri = cadena.lower().replace(" ", "")

    #! invertir la cadena
    cadenaReversa = cadenaOri[::-1]

    if cadenaOri == cadenaReversa:
        print(f"La cadena {cadenaOri} es un palíndromo")
    else:
        print(f"La cadena {cadenaOri} no es un palíndromo")

Palindromo("Radar")
Palindromo("lol")
Palindromo("Ojo")
Palindromo("hola")
Palindromo("A Santa at NASA")