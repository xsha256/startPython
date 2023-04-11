 #! 11. Crea un programa en Python que tome una lista de números enteros y devuelva una nueva lista que contenga solo los números que son múltiplos de 3. El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar los números.

def Multiplos3(numeros):
    nuevaLista = []
    for num in numeros:
        if num % 3 == 0:
            nuevaLista.append(num)
    print(nuevaLista)


numeros = [1, 2, 5, 6, 7, 8, 10, 30, 23, 33]
Multiplos3(numeros)