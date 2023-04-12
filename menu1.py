from prettytable import PrettyTable
from termcolor import colored
import os
from menu.ej1LetraDNI import * 
from menu.ej2Salario import * 
from menu.ej3RutaAvion import * 
from menu.ej4AreaPerimetro import * 
from menu.ej5MayorMenor import * 
#Jose Javier 
from menu import ej6CelAFah
from menu import ej7ParImpar
from menu import ej8BisiestoONo
from menu import ej9Palíndromo
from menu import ej10Ordenar
from menu import ej11Factorial
from menu import ej12Primo
from menu import ej13Cubo
from menu import ej14Suma
#Jorge
from menu import ej15DeterminaNum
from menu import ej16XBar
from menu import ej17Aleatorio
from menu import ej18Anagrama
from menu import ej19Duplicados
from menu import ej20Capicua

while True:
    os.system('clear')
    tabla = PrettyTable()
    tabla.field_names = ["#", "Descripción"]
    tabla.align["Descripción"] = "l"
    tabla.add_row([colored("1", "blue"), colored("Calcular la letra del DNI Español", "green")])
    tabla.add_row([colored("2", "blue"), colored("Calcular el salario de un empleado", "red")])
    tabla.add_row([colored("3", "blue"), colored("Determinar la ruta para llegar a una ciudad por avión. [Con base de datos]", "white")])
    tabla.add_row([colored("4", "blue"), colored("Calcular el área y perímetro de un círculo dado su radio", "blue")])
    tabla.add_row([colored("5", "blue"), colored("Dada una lista de números enteros, determinar cuál es el mayor y cuál es el menor", "red")])
    tabla.add_row([colored("6", "blue"), colored("Convertir grados Celsius a Fahrenheit", "green")])
    tabla.add_row([colored("7", "blue"), colored("Determinar si un número entero es par o impar", "yellow")])
    tabla.add_row([colored("8", "blue"), colored("Determinar si un año es bisiesto o no", "white")])
    tabla.add_row([colored("9", "blue"), colored("Determinar si una cadena de texto es un palíndromo o no", "red")])
    tabla.add_row([colored("10", "blue"), colored("Ordenar alfabéticamente una lista de nombres", "blue")])
    tabla.add_row([colored("11", "blue"), colored("Calcular el factorial de un número entero", "yellow")])
    tabla.add_row([colored("12", "blue"), colored("Determinar si un número entero es primo o no", "grey")])
    tabla.add_row([colored("13", "blue"), colored("Calcular el área y volumen de un cubo dado su lado", "magenta")])
    tabla.add_row([colored("14", "blue"), colored("Calcular la suma de todos los números pares de una lista de números enteros", "cyan")])
    tabla.add_row([colored("15", "blue"), colored("Determinar si un número es positivo, negativo o cero", "red")])
    tabla.add_row([colored("16", "blue"), colored("Calcular la media de una lista de números enteros", "blue")])
    tabla.add_row([colored("17", "blue"), colored("Juego: adivinar un número aleatorio entre 1 y 100", "white")])
    tabla.add_row([colored("18", "blue"), colored("Determinar si una cadena de texto es un anagrama de otra cadena de texto", "green")])
    tabla.add_row([colored("19", "blue"), colored("Eliminar los números duplicados de una lista de números enteros", "yellow")])
    tabla.add_row([colored("20", "blue"), colored("Determinar si un número es capicúa o no", "red")])

    print(colored(tabla.get_string(), "blue"))
    opcion = input(colored("Seleccione una opción (1-20) o escriba '0' para cerrar el programa: ", "blue"))

    if opcion == "0":
        print("¡Hasta luego!")
        break
    elif opcion == "1":
        print(LetraDNI())
    elif opcion == "2":
        print(salarioBase())
    elif opcion == "3":
        print("No esta hecho")
    elif opcion == "4":
        print(CalcularAreaPer())
    elif opcion == "5":
        print(CalcularMayMen())
            # Jose Javier 6/7/8/9/10/11/12/13/14
    elif opcion == "6":
        print(ej6CelAFah.celAfah())
    elif opcion == "7":
        print(ej7ParImpar.parImpar())
    elif opcion == "8":
        print(ej8BisiestoONo.bisiestoONo())
    elif opcion == "9":
        print(ej9Palíndromo.Palindromo())
    elif opcion == "10":
        print(ej10Ordenar.Ordenar())
    elif opcion == "11":
        print(ej11Factorial.Factorial())
    elif opcion == "12":
        print(ej12Primo.Primo())
    elif opcion == "13":
        print(ej13Cubo.CalCubo())
    elif opcion == "14":
        print(ej14Suma.CalNumPares())
     # Jorge 15/16/17/18/19/20
    elif opcion == "15":
        ej15DeterminaNum.determinaNum()
    elif opcion == "16":
        ej16XBar.XBar()
    elif opcion == "17":
        ej17Aleatorio.Aleatorio()
    elif opcion == "18":
        ej18Anagrama.Anagrama()
    elif opcion == "19":
        ej19Duplicados.Duplicados()
    elif opcion == "20":
        ej20Capicua.Capicua()
        
