import sympy as sp
import math
import numpy as np

x = sp.symbols('x')

Xn = [1,2,3,4]
fx = sp.ln(x)

def eval_fx(Xn, fx): #Funcion para evaluar todos los puntos Xn 
    
    valores_evaluados = []
    
    for valor_x in Xn:
        x_evaludo = fx.subs(x, valor_x)
        valores_evaluados.append(x_evaludo)
        
    return valores_evaluados #retorna una lista de los f(xn) evaluados en la funcion 

valores_evaluados = eval_fx(Xn, fx)
print(Xn)
print(valores_evaluados)

# Hacer un for que me devuela las variables x0, x1, x2, xn y fxn con sus valores
for indice_xn, valor_xn in enumerate(Xn):
    #xn guarda el nombre de la variable x0, x1, xn
    xn = f"x{indice_xn}"
    globals()[xn] = valor_xn #asigno al nombre de la variable el valor de la lista 

    for indice_fxn, valor_fxn in enumerate(valores_evaluados):
        fxn = f"fx{indice_fxn}"
        globals()[fxn] = valor_fxn

def poly_grado_2(fx1, fx2, b1, x2, x0, x1):
    b2 = ( ((fx2 - fx1) / (x2 - x1)) - b1 ) / (x2 - x0)
    print('b2 =', b2)
        
    p2 = ( b0 + sp.expand( b1 * (x - x0)) + sp.expand( b2 * (x - x0)*(x - x1)) )

    return b2, p2

def poly_grado_3(fx2, fx3, b2, x0, x2, x3):
    b3 = ( ((fx3 - fx2) / (x3 - x2)) - b2 ) / (x3 - x0)
    print('b3 =', b3)

    p3 = ( b0 + sp.expand( b1 * (x - x0)) + sp.expand( b2 * (x - x0)*(x - x1) ) + sp.expand( b3 * (x - x0)*(x - x1)*(x - x2)) )

    return b3, p3

def poly_grado_4(fx3, fx4, b3, x0, x3, x4):
    b4 = ( ((fx4 - fx3) / (x4 - x3)) - b3 ) / (x4 - x0)
    print('b4 =', b4)

    p4 = ( b0 + sp.expand( b1 * (x - x0)) + sp.expand( b2 * (x - x0)*(x - x1) ) + sp.expand( b3 * (x - x0)*(x - x1)*(x - x2)) +
            sp.expand( b4 * (x - x0)*(x - x1)*(x - x2)*(x - x3)))

    return b4, p4


b0 = fx0
b1 = (fx1 - b0)/(x1 - x0)
print(b0, b1)
print(x2)

        
if len(Xn) == 3:
    b2, p2 = poly_grado_2(fx1, fx2, b1, x2, x0, x1)
    print(p2)

elif len(Xn) == 4:
    b2, p2 = poly_grado_2(fx1, fx2, b1, x2, x0, x1)
    b3, p3 = poly_grado_3(fx2, fx3, b2, x0, x2, x3)
    print(p3)

