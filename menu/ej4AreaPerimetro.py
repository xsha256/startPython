
#todo: Op 1
# #! π = 3.14159
# pi = 3.14159
# area = 0 
# perimetro = 0

# op = "si"
# while op == "si":

#     radio = input("Introduce el radio del círculo: ")
#     if str(radio).isnumeric():

#         #! Área = π × radio²
#         area = pi * int(radio) ** 2

#         #! Perímetro = 2 × π × radio
#         perimetro = 2 * pi * int(radio)

#         print(f"El área es: {area:.2f} ")
#         print(f"El perímetro es: {perimetro:.2f} ")
#         choose = input("Quieres calcular otra vez el área y perímetro de un círculo 'si' o 'no': ")
#         op = choose.lower()

#     else:
#         print("Radio inválido")

# print("¡Hasta luego!")

#todo: Op 2
def CalcularAreaPer(radio):
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

    else:
        print("Radio inválido")
    


CalcularAreaPer(5)
CalcularAreaPer(0)
CalcularAreaPer(1)
