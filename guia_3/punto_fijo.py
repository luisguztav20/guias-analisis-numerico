import math
import pandas as pd
import sympy as sp
from sympy import sqrt

x = sp.symbols("x")

Es = 0.5 * 10 ** (2 - 4)
xi = 5
iteracion = 1
aprox_anterior = 0
aprox_actual = 0

fx = x**2 - 10*x + 7
gx = (10*x - 7)**(1/2)

#funcion para calcular la derivada de g(x) y me devuelve una variable que guarda la derivada
def calculo_derivada (gx):
    gx_prima =gx.diff(x)
    return gx_prima

#funcion para evaluar xi
def g(x):
    return (10*x - 7)**(1/2)

df = pd.DataFrame(columns=["Iteracion", " Xi", "g(Xi)", "Error Aproximado", "cenvergencia"])

print('Intervalo [',xi,']')

while True:

    gxi = g(xi)

    Ea = abs(((gxi - aprox_anterior)/gxi)*100)

    #prueba de convergenai
    gx_prima = calculo_derivada(gx) #devuelve la derivada de g(x)
    convergencia = gx_prima.subs(x, xi) #Evalua el valor actual de xi en la derivada de g(x)

    df.loc[iteracion-1] = [iteracion, xi, gxi, Ea, convergencia]
   
    if Ea < Es:
        break
    else:
       xi = gxi
    
    aprox_anterior = gxi
    iteracion += 1

print(df)
print('Funcion: ',fx)
print('La Raiz es: ', gxi)
print('Con un error de: ', Ea,'%')
print('Con ',iteracion,'iteraciones')