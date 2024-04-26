"""""
Escribe un programa que permita al usuario ingresar 6 números enteros ya sean
positivos o negativos. Al finalizar, 

- mostrar la sumatoria de los números negativos y 
- el promedio de los positivos. 

Considerar todas las validaciones necesarias y de ser
necesario indicar al usuario de algún error al introducir datos erróneos.
"""
numeros = []
numeros_negativos = []
numeros_positivos = []
sumas = []

print('Ingrese 6 numeros enteros positivos o negativos\n')
cantidad_numeros = 6

#ciclo para igresar numeros validando solo ingresos de numeros enteros positivos o negativos
while len(numeros) < 6:

    try:
        numero_ingresado = int(input('Ingrese un numero:'))
        numeros.append(numero_ingresado)
    except:
        print('No esta ingresando un numero')
    
#Separando numeros positivos y negativos
for numero in numeros:
    if numero < 0:
        numeros_negativos.append(numero)
    else:
        numeros_positivos.append(numero)

#Mostrando los resultados 
if len(numeros_negativos) > 0:
    suma_negativos = sum(numeros_negativos)
    print('\nLa suma es de los numeros negativos es: :',suma_negativos)

if len(numeros_positivos) > 0:
    suma_positivos = sum(numeros_positivos)
    cantidad_positivos = len(numeros_positivos)
    promedio_positivos = suma_positivos/cantidad_positivos
    print('\nEl promedio de los numeros positivo es: ', str(promedio_positivos))






