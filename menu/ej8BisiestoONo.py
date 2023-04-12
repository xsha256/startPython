

def bisiestoONo():
    op = "si"
    while op == "si":
        anyo = int(input("Intoduce un año: "))

        if anyo % 4 == 0 and anyo % 100 != 0:
            print(f"{anyo} es bisiesto")
        elif anyo % 400 == 0:
            print(f"{anyo} es bisiesto")
        else:
            print(f"{anyo} no es bisiesto")

        choose = input("Quieres introducir otro año? 'si' o 'no': ")
        op = choose.lower()
