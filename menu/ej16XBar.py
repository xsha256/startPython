# ! Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista

def XBar():
    lista = [1, 2, 3, 4, 5, 6, 10]
    print("La lista dada es ")
    print(lista)
    n = 0
    suma = 0
    for num in lista:
                suma = num + suma
                n = n + 1
    xbar = suma/n
    print(f"x̄  = {suma} / {n}")
    print(f"La media de la lista: {xbar:.2f}")


# lista = [1, 2, 3, 4, 5, 6, 10]
# XBar(lista)
