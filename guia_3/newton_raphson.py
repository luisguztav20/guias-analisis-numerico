import math
import pandas as pd
import sympy as sp 
from math import e

x = sp.symbols("x")

Es = 0.5 * 10 ** (2 - 4)
xi = 0
iteracion = 1
aprox_anterior = 0
aprox_actual = 0

fx = (1/(e**x)) - x

#Funcion para calcular la primera derivada de f(x) y la guarda en fx_prima
def calculo_derivada (fx):
    fx_prima =fx.diff(x)
    return fx_prima

def f(x):
    return (1/(e**x) - x) 

df = pd.DataFrame(columns=["Iteracion", " Xi", "f(Xi)", "f'(Xi)", "Xi+1", "Error Aproximado"])

print('Intervalo [',xi,']')

while True: 
    fxi= f(xi)

   #calculo de la derivada
    fx_prima = calculo_derivada(fx)

    #Se evalua el valor actual de xi en la primera derivada
    fx_prima_evaluada = fx_prima.subs(x, xi)

    #calculo para encontrar la raiz aproximada
    xi1 = xi - (fxi/fx_prima_evaluada)

    Ea = abs(((xi1 - aprox_anterior)/xi1)*100)

    df.loc[iteracion-1] = [iteracion, xi, fxi, fx_prima_evaluada, xi1, Ea]
   
    if Ea < Es:
        break
    else:
       xi = xi1
    
    aprox_anterior = xi1
    iteracion += 1

print(df)
print('Funcion: ',fx)
print('La Raiz es: ', xi1)
print('Con un error de: ', Ea,'%')
print('Con ',iteracion,'iteraciones')