    #! Crea un algoritmo que determine si un número es capicúa o no.

def Capicua():
    op = "si"
    while op == "si":

        num=int(input("Introduce un numero entero "))
        numReverso = str(num)[::-1]
        if str(numReverso) == str(num):
            print(f"El número {num} es capicúa")
        else:
            print(f"El número {num} no es capicúa")

        choose = input("Quieres introducir otro numero? 'si' o 'no': ")
        op = choose.lower()
