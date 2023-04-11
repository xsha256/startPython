def CalNumPares():

    op = "si"
    while op == "si":
        numeros = input("Introduce una lista de números separados por espacios: ").split()
        pares = 0
        for num in numeros:
            if int(num) % 2 == 0:
                pares = pares + int(num)
        print(f"La suma de todos los numeros pares: {pares}")
        choose = input("Quieres introducir otra lista de numeros? 'si' o 'no': ")
        op = choose.lower()


