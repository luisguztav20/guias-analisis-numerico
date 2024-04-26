import math
import pandas as pd
import sympy as sp 
from math import e

x = sp.symbols("x")

Es = 0.5 * 10 ** (2 - 4)
xi = 1
iteracion = 1
aprox_anterior = 0
aprox_actual = 0

fx = (1/(e**x)) - x

#Funcion para calcular la primera derivada de f(x) y la guarda en fx_prima
def calculo_derivada (fx):
    fx_prima =fx.diff(x)
    return fx_prima

#Funcion para calcular la segunda derivada de f(x) y la guarda en fx_dos_prima
def calculo_sda_derivada (fx):
    fx_dos_prima =fx.diff(x)
    return fx_dos_prima

#funcion para evaluar el valor de xi en f(x)
def f(x):
    return (1/(e**x) - x) 

df = pd.DataFrame(columns=["Iteracion", " Xi", "f(Xi)", "f'(Xi)", "f''(Xi)", "Xi+1", "Error Aproximado"])

print('Intervalo [',xi,']')

while True: 
    fxi= f(xi)
    #calculo de la primera derivada
    fx_prima = calculo_derivada(fx)

    #Se evalua el valor actual de xi en la primera derivada
    fx_prima_eval = fx_prima.subs(x, xi)

    #Calculo de la segunda derivada
    fx_dos_prima = calculo_sda_derivada(fx_prima)
    #Se evalua el valor actual de xi en la segunda derivada
    fx_dos_prima_eval = fx_dos_prima.subs(x, xi)

    #calculo para encontrar la raiz aproximada
    xi1 = xi - (fxi*fx_prima_eval/(fx_prima_eval**2)-(fxi*fx_dos_prima_eval))

    Ea = abs(((xi1 - aprox_anterior)/xi1)*100)

    df.loc[iteracion-1] = [iteracion, xi, fxi, fx_prima_eval, fx_dos_prima_eval, xi1, Ea]
   
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