 #! Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.

def Duplicados():
    op = "si"
    while op == "si":
        lista = input("Introduce una lista de números separados por espacios: ").split()
        nuevaLista = []
        for num in lista:
            if int(num) not in nuevaLista:
                nuevaLista.append(int(num))

        print(f"La nueva lista sin repetidos es: {nuevaLista}")
        
        choose = input("Quieres introducir otra lista de numeros? 'si' o 'no': ")
        op = choose.lower()



