def CalNumPares(lista):
    pares = 0 
    for num in lista:
        if num % 2 == 0:
            pares = pares + num
    print(f"La suma de todos los numeros pares: {pares}")


lista = [1, 2, 4, 5, 6, 10, 10]
CalNumPares(lista)