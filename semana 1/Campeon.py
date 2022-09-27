import pandas as pd
print("-----Mi solucion-----")
tabla = pd.read_excel("Tabla1.xlsx") 
datos = tabla.to_dict("list")
ganador = 0
perdedor = sum(datos["Puntos"])
for i in range(len(datos["Equipo"])):
    puntos = datos["Puntos"][i]
    if puntos > ganador:
        ganador = puntos
        equipo_ganador = i
    if perdedor > puntos:
        perdedor = puntos
        equipo_perdedor = i
print("El equipo campeon es {} con un total de {} puntos".format(datos["Equipo"][equipo_ganador],datos["Puntos"][equipo_ganador]))
print("El equipo ultimo en la tabla es {} con un total de {} puntos".format(datos["Equipo"][equipo_perdedor],datos["Puntos"][equipo_perdedor]))


print("\n\n -----Solucion ITBA -----")
import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx", index_col ="Equipo") 
# Indicamos que la columna de indexación será Equipo.

data = archivo.to_dict("index")

data_tuple = data.items() # provocamos que los datos esten como una lista de la forma (clave, contenido)

def criterioDeOrden(item): # esta función determina el criterio de orden
    clave, contenido = item
    return contenido["Puntos"] # indicamos que al criterio le importa los puntos

data_ordenada = sorted(data_tuple, reverse=True, key=criterioDeOrden)

ganador = data_ordenada[0][0] # el primer 0 indica que es el primer elemento (el ganador), el segundo 0 indica que nos interesa la clave (si fuera un 1 sería el contenido)
perdedor = data_ordenada[-1][0] # el primer -1 indica que es el utimo elemento (el perdedor), el segundo 0 indica que nos interesa la clave (si fuera un 1 sería el contenido)

print(ganador,"resulto campeón con",data[ganador]["Puntos"],"puntos")
print(perdedor,"resulto último con", data[perdedor]["Puntos"],"puntos")


    