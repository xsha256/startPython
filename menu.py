from termcolor import colored
from menu.ej1LetraDNI import * 
# from menu.ej2Salario import * 
# from menu.ej3RutaAvion import * 
# from menu.ej4AreaPerimetro import * 
# from menu.ej5MayorMenor import * 
# from menu.ej6CelAFah import * 
# from menu.ej7ParImpar import * 
# from menu.ej8BisiestoONo import * 


while True:
    print(colored("Menú:", "blue"))
    print(colored("1. Calcular la letra del DNI Español", "green"))
    print(colored("2. Calcular el salario de un empleado", "red"))
    print(colored("3. Determinar la ruta para llegar a una ciudad por avión. [Con base de datos]", "white"))
    print(colored("4. Calcular el área y perímetro de un círculo dado su radio", "blue"))
    print(colored("5. Dada una lista de números enteros, determinar cuál es el mayor y cuál es el menor", "red"))
    print(colored("6. Convertir grados Celsius a Fahrenheit", "green"))
    print(colored("7. Determinar si un número entero es par o impar", "yellow"))
    print(colored("8. Determinar si un año es bisiesto o no", "green"))
    print(colored("9. Determinar si una cadena de texto es un palíndromo o no", "green"))
    print(colored("10. Ordenar alfabéticamente una lista de nombres", "green"))
    print(colored("11. Calcular el factorial de un número entero", "green"))
    print(colored("12. Determinar si un número entero es primo o no", "green"))
    print(colored("13. Calcular el área y volumen de un cubo dado su lado", "green"))
    print(colored("14. Calcular la suma de todos los números pares de una lista de números enteros", "green"))
    print(colored("15. Determinar si un número es positivo, negativo o cero", "green"))
    print(colored("16. Calcular la media de una lista de números enteros", "green"))
    print(colored("17. Juego: adivinar un número aleatorio entre 1 y 100", "green"))
    print(colored("18. Determinar si una cadena de texto es un anagrama de otra cadena de texto", "green"))
    print(colored("19. Eliminar los números duplicados de una lista de números enteros", "green"))
    print(colored("20. Determinar si un número es capicúa o no", "green"))
    opcion = input(colored("Seleccione una opción (1-20) o escriba '0' para cerrar el programa: ", "blue"))

    if opcion == "0":
        break
    elif opcion == "1":
        print(LetraDNI())
        