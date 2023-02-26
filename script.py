import matplotlib.pyplot as plt
from estadistica_operaciones import *

import numpy as np

def organizacion():
    for recorrido in range(1, len(listado)):
        for posicion in range(len(listado) - recorrido):
            if listado[posicion]>listado[posicion+1]:
                temp = listado[posicion]
                listado[posicion]=listado[posicion+1]
                listado[posicion+1]=temp
       
n = int(input("número de datos: "))
listado = []
tipo_Dato=str(input('¿Que tipo de dato ingresaras? coloca el nombre ejem: centigrados, kilometros, psi:\n'))
print()
for i in range(n):
    numero= float(input("ingresa los valores: "))
    listado.append(numero)

#mostrar datos
print(listado)
##mostrar datos en grafica desorganizada
print()
organizacion()
print(listado)
print()

media_Mediana(listado, n)
Varianza(listado, n)

plt.plot(listado, label=tipo_Dato, color='black')
plt.legend()
plt.ylabel(tipo_Dato)
plt.xlabel('Cantidad de muestras')
plt.title('tus graficos')
plt.grid(b=True)
plt.show()
