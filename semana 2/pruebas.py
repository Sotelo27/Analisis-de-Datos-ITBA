import numpy as np
import matplotlib.pyplot as plt

# valores de los componentes
# genero un vector con tiempos para evaluar las funciones y plotear

t = np.arange(0, 1, 0.01)
y = np.exp(-t*2+1)

y2 = 1.25*np.exp(t*2-1)
plt.figure(figsize=(10,5))
plt.plot(t, y, "green",label="Demanda")
plt.plot(t, y2, "orange",label="Oferta")

plt.ylabel("Cantidad (Millones)")
plt.xlabel("Precio ($)")

# agregamos leyenda
plt.legend(loc="upper left")

# muestro el grafico que prepare
plt.savefig('ofdem.png')
plt.show()