


def CalcularMayMen():
    op = "si"
    while op == "si":
                numeros = input("Introduce una lista de números separados por espacios: ").split()
                mayor = float("-inf")
                menor =  float("inf")

                for numero in numeros:
                        if int(numero) >  mayor:   
                                mayor = int(numero) 
                        if int(numero) < menor:
                                menor = int(numero)

                print(f"El numero mayor es: {mayor}")
                print(f"El numero menor es: {menor}")

                choose = input("Quieres introducir otra lista de numeros? 'si' o 'no': ")
                op = choose.lower()


