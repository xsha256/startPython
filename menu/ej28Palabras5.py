 #! 8. Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que tienen más de 5 caracteres. El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.


def Cadena5Car(cadena):
    cadena = cadena.split()
    nuevaCad = []
    for palabra in cadena:
        if len(palabra) > 5:
            nuevaCad.append(palabra)
    print(nuevaCad)


cadena = input("Escribe una cadena: ")
Cadena5Car(cadena)