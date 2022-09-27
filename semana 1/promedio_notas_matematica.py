import pandas as pd
#Obtener el promedio general sólo para aquellos alumnos que aprobaron Matemática (con nota >= 6) en el archivo Datos.xlsx.
datos = pd.read_excel("Datos.xlsx") 
aprobadosMate = datos[(datos['Matematica']>=6)]
promedios = (aprobadosMate["Quimica"] + aprobadosMate["Matematica"] + aprobadosMate["Fisica"])/3

promedio_general = sum(promedios)/len(promedios)

print("El promedio general es %0.2f " % promedio_general)


