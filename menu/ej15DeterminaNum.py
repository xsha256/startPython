
#! Crea un algoritmo que determine si un número es positivo, negativo o cero.

def determinaNum():
    num = int(input("Introduce un numero "))
    if num > 0:
        print(f"El numero {num} es: positivo")
    elif num < 0:
        print(f"El numero {num} es: negativo")

    else:
        print(f"El numero {num} es: cero")


