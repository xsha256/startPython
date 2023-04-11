 #! 2. Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.

from datetime import datetime, timedelta
from pytz import timezone  
import pytz 

def ZonaHoraria(zona):
    try:
        print(datetime.now(pytz.timezone(zona)))
    except: 
        print("No has puesto la zona corretamente")


zona = input("Pon tu zona horaria(continente/ciudad): ")
ZonaHoraria(zona)