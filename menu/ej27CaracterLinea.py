 #!7. Crea un programa que le pida al usuario una cadena de caracteres y luego imprima cada carácter en una línea separada. El programa debe utilizar un bucle `for` para recorrer la cadena.


def CadenaCar(cadena):
    for caracter in cadena:
        print(caracter)
        print()


cadena = input("Escribe una cadena: ")
CadenaCar(cadena)