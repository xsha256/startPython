 #! 3. Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene. El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.


def CadenaCar(cadena):
    count = 0
    while(count < len(cadena)):
        count += 1
    return count

cadena = input("Escribe una frase: ").split()
print(CadenaCar(cadena))