import math
#! Dado un número entero, crea un algoritmo que determine si es primo o no


def EsPrimo(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
            
        return True

def Primo():
    op = "si"
    while op == "si":
        n = int(input("Introduce un número: "))
        if EsPrimo(n):
            print(f"{n}: es primo")
        else:
            print(f"{n}: no es primo")
        choose = input("Quieres introducir otro numero? 'si' o 'no': ")
        op = choose.lower()
        
