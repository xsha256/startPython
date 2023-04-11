


def CalcularMayMen():
        numeros = input("Introduce una lista de numeros separados por espacios: ").split()
        print (numeros)
        print(type(numeros))
        mayor = float("-inf")
        menor =  float("inf")

        for numero in numeros:
                if int(numero) >  mayor:   
                        mayor = int(numero) 
                if int(numero) < menor:
                        menor = int(numero)

        print(f"El numero mayor es: {mayor}")
        print(f"El numero menor es: {menor}")


