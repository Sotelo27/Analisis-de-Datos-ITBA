import pandas as pd
def promedio_del_alumno(tabla:list, indice_alumno:int):
    alumno = tabla.loc[indice_alumno] 
    suma = alumno["Quimica"] + alumno["Fisica"] + alumno["Matematica"]
    promedio = suma / 3
    return promedio

def main():
    datos = pd.read_excel("Datos.xlsx")
    print("El promedio del alumno es {} ".format(promedio_del_alumno(datos,0)))

main()
    
    