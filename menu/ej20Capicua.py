    #! Crea un algoritmo que determine si un número es capicúa o no.

def Capicua():
    num=int(input("Introduce un numero entero "))
    numReverso = str(num)[::-1]
    if str(numReverso) == str(num):
        print(f"El número {num} es capicúa")
    else:
        print(f"El número {num} no es capicúa")

#Capicua(111)
#Capicua(220)
#Capicua(331)
#Capicua(221122)