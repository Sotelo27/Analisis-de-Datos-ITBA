import pandas as pd

datos2 = pd.read_excel("Datos2.xlsx") 
print("Datos:\n")
print(datos2)
datos2_matematica = datos2[ (datos2['Matematica'].notna()) & (datos2['Matematica'] != 'A')  ]

datos2_matematica = datos2_matematica['Matematica'] # Nos quedamos con la columna de interés

print('Notas válidas en Matemática: ')
print(datos2_matematica)