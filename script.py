import matplotlib.pyplot as plt
def organizacion():
    for recorrido in range(1, len(listado)):
        for posicion in range(len(listado) - recorrido):
            if listado[posicion]>listado[posicion+1]:
                temp = listado[posicion]
                listado[posicion]=listado[posicion+1]
                listado[posicion+1]=temp
                print('organizada\n',listado)
                print('longitud: ',len(listado))
                
                
def media_Mediana():
    suma = 0
    for i in listado:
        suma = suma + i
    media = suma/cantidad
    print('la media: ', media)
    ## proceso mediana
    longitud = len(listado)

    if cantidad % 2 == 0: ## cuando es par 
        print('Cuando es una valor par: ')
        posicio_lisa = cantidad/2
        print('Esta es la media: ', posicio_lisa)
        at=float(input('Ingresar valor de la posición 1: '))
        bt=float(input('Ingresar valor de la posición 2: '))
        resultado=(at+bt)/2
        print('Tu mediana es: ', resultado)
    else:## cuando es impar
        print('logitud: ',longitud)
        mediana = (cantidad + 1) / 2
        print('Impar \nla mediana esta en esta posicion: ', mediana)
        
        
        
        
       
cantidad = int(input("cantidad de datos: "))
listado = []
for i in range(cantidad):
    numero= float(input("ingresa los valores: "))
    listado.append(numero)
print(listado)
plt.plot(listado)
plt.show()
organizacion()
media_Mediana()
plt.plot(listado)
plt.show()
##print(numero)
