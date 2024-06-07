import pandas as pd
import sympy as sp 
import math
from sympy import symbols

x = sp.symbols("x")

iteracion = 1
Es = 0.5 * 10 ** (2 - 3)
fx = x**3 -13*x - 12
X0 = 4.5
X1 = 5.5
X2 = 5

def f(x):
    return (x**3 -13*x - 12) 

def evaluacion_fx(X0, X1, X2):
    fx0 = f(X0)
    fx1 = f(X1)
    fx2 = f(X2)

    return fx0, fx1, fx2

df = pd.DataFrame(columns=["Iteracion", " X0", "X1", "X2", "D", "Xr", "Error Aproximado"])

while True:

    fx0, fx1, fx2 = evaluacion_fx(X0, X1, X2)

    h0 = X1 - X0
    h1 = X2 - X1

    #et0 = &0, et1 = &1
    et0 = (fx1 - fx0)/h0
    et1 = (fx2- fx1)/h1

    a = (et1 - et0)/(h1 + h0)
    b = (a * h1) + et1
    c = fx2
    
    D = math.sqrt((b ** 2) - (4 * a * c))

    if abs(b + D) > abs(b - D):
        Xr = X2 + (((-2) * c)/((b**2) + D))
    else:
        Xr = X2 + (((-2) * c)/((b**2) - D))

    Ea = abs(((Xr - X2)/Xr)*100)

    df.loc[iteracion-1] = [iteracion, X0, X1, X2, D, Xr, Ea]

    if(Ea < Es):
        break
    else:
        X0 = X1
        X1 = X2
        X2 = Xr
        
    iteracion += 1

print(df)
print('Es',Es)
print('Ecuacion: ',fx)
print('Raiz: ', Xr)
print('Con un error de: ', Ea,'%')
print('Con ',iteracion,'iteraciones')

        







