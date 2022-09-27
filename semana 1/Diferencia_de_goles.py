import pandas as pd
print("-----Mi solucion-----")
tabla = pd.read_excel("Tabla1.xlsx") 
datos = tabla.to_dict("list")
contador = 0
diferencia_goles = []
while contador < len(datos["Goles a favor"]):
    diferencia_goles.append(datos["Goles a favor"][contador] - datos["Goles en contra"][contador])
    contador += 1
datos["Diferencia de goles"] = diferencia_goles
print(datos)

print("\n\n-----Solucion ITBA-----")

archivo = pd.read_excel("Tabla1.xlsx")

data = archivo.to_dict("list") # diccionario de listas.
#La clave de los diccionarios es el nombre de la columna
#El contenido de los diccionarios es una lista con el contenido de la columna



print("Diferencias de gol:")

for i in range(len(data["Equipo"])):
    print(data["Equipo"][i], ":", data["Goles a favor"][i] - data["Goles en contra"][i])



    
