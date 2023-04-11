

def CalCubo():
    op = "si"
    while op == "si":
        lado = int(input("Intoduce un lado(numero): "))
        area = 6 * lado^2
        volumen = lado^3
        print(f"El área del cubo: {area}")
        print(f"El volumen del cubo: {volumen}")

        choose = input("Quieres introducir otro lado? 'si' o 'no': ")
        op = choose.lower()


