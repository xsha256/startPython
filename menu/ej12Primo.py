import math
#! Dado un número entero, crea un algoritmo que determine si es primo o no


def EsPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        
    return True

def Primo(n):
    if EsPrimo(n):
        print(f"{n}: es primo")
    else:
        print(f"{n}: no es primo")

Primo(2)
Primo(4)
Primo(5)
Primo(59)
Primo(10)
Primo(21)
Primo(97)