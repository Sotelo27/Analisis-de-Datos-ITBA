
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def ejercicio_1(datos):
    #Ejercicio 1,comprobacion:
    lista = datos[datos["Quimica"] != datos["Quimica"].max()]
    print(lista["Apellido"])

def ejercicio_2(datos):
    #Ejercicio 2,comprobacion:
    print("\n",datos,"\n")
    lista = datos['Quimica'].value_counts().idxmax()
    print("\nComprobacion 1: ",lista) 

def ejercicio_3(datos):
    #Ejercicio 3,comprobacion
    print("\n",datos,"\n")
    error = datos[datos["Goles a favor"] - datos["Goles en contra"]!= datos["Diferencia de gol"]]
    print("\n",error["Equipo"],"\n")

def ejercicio_4(archivo):
    #Ejercicio 4,comprobacion        
    datos = archivo.to_dict("list")  
    time = datos["Ganados"]
    signal = datos["Puntos"]  
    plt.plot(time,signal, "b--")  
    plt.ylabel("Tension[v]")
    plt.xlabel("Tiempo[s]")
    plt.grid()
    plt.savefig("Plot 11_a.png",dpi=300) 
    plt.show()
    

def ejercicio_5(archivo):
    #Ejercicio 5,comprobacion
    datos = archivo.to_dict("list") 
    chanel1 = datos["Puntos"]
    chanel2 = datos["Ganados"]
    plt.plot(chanel1,chanel2, ".-.")
    plt.ylabel("Channel 1 [V]")
    plt.xlabel("Channel 2 [V]")
    plt.grid()
    plt.savefig("Plot.png",dpi=300)
    plt.show()

def ejercicio_6():
    #Ejercicio 6,comprobacion
    x = np.arange(0, 2*3.14, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.subplot(2, 2, 3)
    plt.plot(x, y1, 'b-')
    plt.subplot(2,2,1)
    plt.plot(x,y2,"r-.")
    plt.subplot(2,2,1)
    plt.subplot(2, 2, 4)
    plt.plot(x, y1, 'w-')
    plt.subplot(2,2,2)
    plt.plot(x,y2,"p-.")
    plt.tight_layout() 
    plt.show()
    pass

def ejercicio_7(datos):
    #Ejercicio 7,comprobacion
    archivo = datos.loc[ (datos['Primer Parcial'] >= 6) & (datos['Segundo Parcial'] >= 6) & (datos['TP Final'] >= 6) ]
    print(archivo)
    print("\n\n")
    archivo = datos[ (datos['Primer Parcial'] >= 6) & (datos['Segundo Parcial'] >= 6) & (datos['TP Final'] >= 6) ]
    print(archivo)


def ejercicio_8(datos):
    #Ejercicio 8,comprobacion
    datos.loc[["Velez Sarfield","Boca Juniors","River Plate","Estudiantes"],["Partidos"]] = 14
    print(datos.loc[datos["Partidos"] != 14,["Puntos"]])
    

def ejercicio_9(datos):
    #Ejercicio 9,comprobacion
    data = datos.to_dict("list")
    notas = data["notas"]
    plt.hist(notas, range(12), align = 'left', rwidth=0.75)
    plt.show()

def ejercicio_10():
    #Ejercicio 10,comprobacion
    x = np.arange(0, 2*3.14, 0.1)
    y = np.sin(x)
    y2 = np.cos(x)
    plt.plot(x,y,"r--",label ="IEEE")
    plt.legend()
    plt.show()
    
def main():
    datos = pd.read_excel("Datos.xlsx")
    tabla = pd.read_excel("Tabla1.xlsx")
    tabla_2 = pd.read_excel("Tabla1.xlsx",index_col = "Equipo")
    parciales = pd.read_excel("Evaluaciones.xlsx")
    archivo = pd.read_excel("notas.xlsx")
    print("\n---- Ejercicio 1 -----\n")
    ejercicio_1(datos) #Esta bien
    print("\n---- Ejercicio 2 -----\n")
    ejercicio_2(datos) #Esta bien
    print("\n---- Ejercicio 3 -----\n")
    ejercicio_3(tabla) #Esta bien
    print("\n---- Ejercicio 4 -----\n")
    #ejercicio_4(tabla) #Esta bien
    print("\n---- Ejercicio 5 -----\n")
    #ejercicio_5(tabla) #Esta bien
    print("\n---- Ejercicio 6 -----\n")
    #ejercicio_6() #Esta bien
    print("\n---- Ejercicio 7 -----\n")
    #ejercicio_7(parciales)  Dudoso
    print("\n---- Ejercicio 8 -----\n")
    ejercicio_8(tabla_2) #Esta bien
    print("\n---- Ejercicio 9 -----\n")
    #ejercicio_9(archivo) Esta bien
    print("\n---- Ejercicio 10 -----\n")
    ejercicio_10() #


    



main()
    



