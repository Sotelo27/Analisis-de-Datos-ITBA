import pandas as pd
datos = pd.read_excel("Datos.xlsx")
suma = sum(datos["Quimica"])
total = len(datos["Quimica"])
promedio = suma / total
print("El promedio de notas es de {} ".format(promedio))