#Parte 2
import matplotlib.pyplot as plt
import numpy as np

# Cantidad de puntos
n = 100
x = np.linspace(-5,5,n)
gaussiana = np.exp(-x**2/2)  # Expresión vectorizada, calcula el resultado uno a uno

plt.plot(x, gaussiana)
plt.show()