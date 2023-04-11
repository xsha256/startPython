

def bisiestoONo(anyo):
    if anyo % 4 == 0 and anyo % 100 != 0:
        print(f"{anyo} es bisiesto")
    elif anyo%400 == 0 :
        print(f"{anyo} es bisiesto")
    else:
        print(f"{anyo} no es bisiesto")

bisiestoONo(2000)
bisiestoONo(2024)
bisiestoONo(2023)
bisiestoONo(2010)
