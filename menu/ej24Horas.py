 #! 4. Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo, "19:30" se convertiría en "19:30"). La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.


from datetime import datetime

def convertir_hora(hora, pmAm):
    hora = (f"{hora}  {pmAm}")
    dt = datetime.strptime(hora, '%I:%M %p')
    dt.strftime('%H:%M')
    print(dt.strftime('%H:%M'))


hora = input("escribe una hora (hh:mm): ")
pmAm = input("La hora es pm o am? ").lower()

convertir_hora(hora, pmAm)