
#! Crea un algoritmo que calcule el factorial de un número entero.
def Factorial():
    op = "si"
    while op == "si":
        n = int(input("Introduce un número: "))
        fac = 1
        for i in range(1, n+1):
            fac = fac * i

        print(fac)
        choose = input("Quieres introducir otro numero? 'si' o 'no': ")
        op = choose.lower()