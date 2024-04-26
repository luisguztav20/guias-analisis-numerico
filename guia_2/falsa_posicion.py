import math
from math import e
import pandas as pd

Es = 0.5 * 10 ** (2 - 3)
x1 = 0
xu = 1
iteracion = 1
aprox_anterior = 0
aprox_actual = 0

def f(x):
    return (( e**-x)-x) 

df = pd.DataFrame(columns=["Iteracion", "x1", "xu", "f(x1)", "f(xu)", "xr", "f(xr)", "f(x1)*f(xr)", "Condicion", "Error Aproximado"])

print('Intervalo [', x1,',',xu,']')

while True:
    fx1 = f(x1)
    fxu = f(xu)
    xr = xu - (fxu*(x1-xu)/(fx1-fxu))
    fxr = f(xr)
    producto = fx1*fxr

    if producto < 0:
        condicon = '< 0'
    else:
        condicon = '> 0'

    Ea = abs(((xr - aprox_anterior)/xr)*100)

    df.loc[iteracion-1] = [iteracion, x1, xu, fx1, fxu, xr, fxr, producto, condicon,  Ea]
   
    if producto < 0:
        xu = xr
    elif producto > 0:
        x1 = xr
    else:
        break
    if Ea < Es:
        break
    
    aprox_anterior = xr
    iteracion += 1

print(df)
print('La Raiz es: ', xr)
print('Con un error de: ', Ea,'%')
print('Con ',iteracion,'iteraciones')


