import math
import pandas as pd

Es = 0.5 * 10 ** (2 - 4)
xi_1 = 0
xi = 1
iteracion = 1
aprox_anterior = 0
aprox_actual = 0

#funcion para evaluar el valor de xi en f(x)
def f(x):
    return ((x**3) - math.cos(x)) 

df = pd.DataFrame(columns=["Iteracion", " Xi-1", "Xi", "f(Xi-1)", "f(Xi)", "Xi+1", "Error Aproximado"])

print('Intervalo [', xi_1,',',xi,']')

while True: 
    #se evalua el valor actual de xi en f(xi) y f(xi-1)
    fxi_1= f(xi_1)
    fxi = f(xi)

    #calculo para encontrar la raiz aproximada
    xi1 = xi - ((fxi*(xi_1 - xi))/(fxi_1 - fxi))

    Ea = abs(((xi1 - aprox_anterior)/xi1)*100)

    df.loc[iteracion-1] = [iteracion, xi_1, xi, fxi_1, fxi, xi1, Ea]
   
    if Ea <Es:
        break
    else:
        xi_1 = xi
        xi = xi1
    
    aprox_anterior = xi1
    iteracion += 1

print(df)
print('La Raiz es: ', xi1)
print('Con un error de: ', Ea,'%')
print('Con ',iteracion,'iteraciones')