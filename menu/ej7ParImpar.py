
def parImpar():
    op = "si"
    while op == "si":

        num = int(input("Escribe un número: "))

        if num%2 == 0:
                print(f"{num} es par")
        else:
                print(f"{num} es impar")
        
        choose = input("Quieres introducir otro numero? 'si' o 'no': ")
        op = choose.lower()

