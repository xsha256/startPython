
def Ordenar():
    op = "si"
    while op == "si":
        lista = input("Introduce una lista separados con espacios: ")
        lista = lista.split()
        lista.sort()
        print(lista)

        choose = input("Quieres introducir otra lista? 'si' o 'no': ")
        op = choose.lower()
