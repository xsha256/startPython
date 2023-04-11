from termcolor import colored
from menu.ej1LetraDNI import * 
# from menu.ej2Salario import * 
# from menu.ej3RutaAvion import * 
# from menu.ej4AreaPerimetro import * 
# from menu.ej5MayorMenor import * 
# from menu.ej6CelAFah import * 
# from menu.ej7ParImpar import * 
# from menu.ej8BisiestoONo import * 
from menu import ej15DeterminaNum
from menu import ej16XBar
from menu import ej17Aleatorio
from menu import ej18Anagrama
from menu import ej19Duplicados
from menu import ej20Capicua


while True:
    print(colored("Menú:", "blue"))
    print(colored("1. Calcular la letra del DNI Español", "green"))
    print(colored("2. Calcular el salario de un empleado", "red"))
    print(colored("3. Determinar la ruta para llegar a una ciudad por avión. [Con base de datos]", "white"))
    print(colored("4. Calcular el área y perímetro de un círculo dado su radio", "blue"))
    print(colored("5. Dada una lista de números enteros, determinar cuál es el mayor y cuál es el menor", "red"))
    print(colored("6. Convertir grados Celsius a Fahrenheit", "green"))
    print(colored("7. Determinar si un número entero es par o impar", "yellow"))
    print(colored("8. Determinar si un año es bisiesto o no", "white"))
    print(colored("9. Determinar si una cadena de texto es un palíndromo o no", "red"))
    print(colored("10. Ordenar alfabéticamente una lista de nombres", "blue"))
    print(colored("11. Calcular el factorial de un número entero", "yellow"))
    print(colored("12. Determinar si un número entero es primo o no", "grey"))
    print(colored("13. Calcular el área y volumen de un cubo dado su lado", "magenta"))
    print(colored("14. Calcular la suma de todos los números pares de una lista de números enteros", "cyan"))
    print(colored("15. Determinar si un número es positivo, negativo o cero", "red"))
    print(colored("16. Calcular la media de una lista de números enteros", "blue"))
    print(colored("17. Juego: adivinar un número aleatorio entre 1 y 100", "white"))
    print(colored("18. Determinar si una cadena de texto es un anagrama de otra cadena de texto", "green"))
    print(colored("19. Eliminar los números duplicados de una lista de números enteros", "yellow"))
    print(colored("20. Determinar si un número es capicúa o no", "red"))
    opcion = input(colored("Seleccione una opción (1-20) o escriba '0' para cerrar el programa: ", "blue"))

    if opcion == "0":
        break
    elif opcion == "1":
        print(LetraDNI())
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
        