
#! Crea un algoritmo que calcule el factorial de un número entero.
def Factorial(n):
    fac = 1

    for i in range(1, n+1):
        fac = fac * i

    print(fac)


Factorial(5)
Factorial(6)
Factorial(7)
Factorial(8)
