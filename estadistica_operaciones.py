import numpy as np
def media_Mediana(listado, n):
    ##Proceso de la media aritmetica
    suma = 0
    for i in listado:
        suma = suma + i
    global media
    media = suma/n
    print('la media aritmetica: ', media)
    ## proceso mediana
    longitud = len(listado)
    ##Proceso de Mediana
    print()
    print('Inicio de proceso de mediana')
    if n % 2 == 0: ## cuando es par 
        print('Cuando es una valor par: ')
        posicio_lista = n/2
        print('Esta es la media(Posición del sistema): ', posicio_lista)
        print(listado)
        at=float(input('Ingresar valor de la posición 1\nDonde te indico el sistema: '))
        print()
        bt=float(input('Ingresar valor de la posición 2\nLa posición siguiente de donte te indico el sistema: '))
        resultado=(at+bt)/2
        print('Tu mediana es: ', resultado)
        
    else:## cuando es impar
        print('logitud de la lista: ',longitud)
        mediana = (n + 1) / 2
        print('Impar \nLa mediana esta en esta posicion: ', mediana)
        

def Varianza(listado,n ):
    print()
    print('Varianza cuadrada:\nLa distancia exacta, en promedio y al cuadrado que hay entre los valores de una variable y su respectivo promedio aritmetico: ')
    media=float(input('Ingresa valor de la media arrojado: '))
    ##filter (media_Mediana, media)
    suma=0
    for i in listado:
        
        operacion = (i-media)**2
        suma= suma + operacion
        
    n=n-1
    s2=suma/n
    print()
    s=np.sqrt(s2)
    print('Desviación estandar:\nLa distancia exacta y en promedio que existe entre los valores de la variable y su respectivo promedio aritmetico')
    print('Desviación estandar: ', s)
    
    
    print('varianza cuadrada es: ', s2)
        

        