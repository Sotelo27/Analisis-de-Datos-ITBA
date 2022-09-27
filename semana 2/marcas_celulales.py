import matplotlib.pyplot as plt

labels = ('Apple', 'Samsung', 'Huawei', 'Xiaomi', 'vivo', 'Oppo', 'Lenovo', 'Otros')
sizes = [72.3, 70.4, 56.2, 32.9, 31.5, 31.4, 11.7, 94.7] #Millones de unidades: 2019 Q4
colors = ['silver', 'royalblue', 'orangered', 'orange', 'cornflowerblue', 'green', 'red', 'grey']

fig = plt.figure(figsize=(6, 6))

plt.pie(sizes, labels=labels, colors=colors, autopct='%5.01f%%', pctdistance=0.85, startangle = 90)

# Dibujar un círculo blanco para mejorar la estética del gráfico
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

plt.show()