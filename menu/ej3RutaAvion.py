# Algoritmo rutaAvionAlgoritmo rutaAvion

#   # Entrada
#       destino <- leer()
#       fecha <- leer()
#       vuelo <- leer()
#       llegadaAeropuerto <- leer()
#       checkIn <- leer()
#       embarcar <- leer()
#       llegada = ""
      
#   # Proceso 
# Repetir: 
#       Si destino es válido: 

#         Repetir: 
#           si fecha es válida:
#               compra vuelo

#               si llegadaAeropuerto >= 2 horas:
#                   hacer checkIn
#                   escribir("Has llegado con tiempo")
#               sino:
#                   hacer checkIn
#                   escribir("No has llegado con tiempo")
        
#               Si hora de terminar checkIn >= la ultima llamada:
#                   puedes embarcar
#                   haEmbarcado = True
#               sino:
#                   el avión sale en 15 minutos las puertas están cerradas
#                   haEmbarcado = False

#               Si el avión haLlegadoSinProblemas entonces 
#                   haLlegadoSinProblemas = True
#               Sino:
#                   haLlegadoSinProblemas = False

#               Si haEmbarcado y el avión haLlegadoSinProblemas entonces:
#                   llegada = verdadero 
#               sino:
#                   llegada = falso

#           sino:
#               opción <- ¿Queres elegir otra fecha si/no?
#               si opción = "no" entonces
#                   Break
#         hasta que opción = "no"

#       sino:
#          opción <- ¿Queres elegir otro destino o aeropuerto de salida si/no?
          
# hasta que opción = "no"
          
#   # Salida
#       Si llegada = verdadero:
#         escribir("La ruta: ", salida, destino)
#       Sino:
#         escribir("No ha salido, no se puede calcular la ruta")

# Fin algoritmo