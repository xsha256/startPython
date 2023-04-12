
def LetraDNI():
    letraDNI = "TRWAGMYFPDXBNJZSQVHLCKE"

    op = "si"
    while op == "si":

        numero = input("Pon el número de tu DNI: ")
        if len(str(numero)) == 8 and str(numero).isnumeric():

            resto = int(numero) % 23
            print(f"La letra del DNI introducido es: {letraDNI[resto]}")
            choose = input("Quieres buscar otra letra del DNI? 'si' o 'no': ")
            op = choose.lower()
            

        else:
            print("DNI inválido")

    print("¡Hasta luego!")

