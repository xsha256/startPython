def CalcularAreaPer():
        op = "si"
        while op == "si":
            radio = int(input("Escribe el radio: "))
            #! π = 3.14159
            pi = 3.14159
            area = 0 
            perimetro = 0

            if str(radio).isnumeric():

                #! Área = π × radio²
                area = pi * int(radio) ** 2

                #! Perímetro = 2 × π × radio
                perimetro = 2 * pi * int(radio)

                print(f"+------------------------------+")
                print(f"  El área es: {area:.2f}")
                print(f"  El perímetro es: {perimetro:.2f}")
                print(f"+------------------------------+")
                choose = input("Quieres calcular otro área y perímetro? 'si' o 'no': ")
                op = choose.lower()

            else:
                print("Radio inválido")


# CalcularAreaPer(5)
# CalcularAreaPer(0)
# CalcularAreaPer(1)
