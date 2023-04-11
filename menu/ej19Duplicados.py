 #! Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.

def Duplicados():
    lista = [1, 2, 3, 3, 4, 5, 6, 1, 2]
    print("la lista dada es: ")
    print(lista)
    nuevaLista = []
    for num in lista:
        if num not in nuevaLista:
            nuevaLista.append(num)

    print(f"La nueva lista sin repetidos es: {nuevaLista}")



# Duplicados(lista)