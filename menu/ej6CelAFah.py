
def celAfah():
    op = "si"
    while op == "si":
        cel = int(input("Introduce grados Celsius: "))
        fah = cel * 1.8 + 32
        print(f"{cel} Celsius en Fahrenheit = {fah} ")
        choose = input("Quieres introducir otro grado? 'si' o 'no': ")
        op = choose.lower()
