import sympy as sp 
import math
import cmath

#solucionar la funcion valores+variables para  que trabaje con ec de grado 4 y 3 
# solucionar los retornos del metodo tartaglia
#mejorar la parte donde deltha es > 0 

x = sp.symbols("x")
u = sp.symbols("u")
poly  = sp.poly(24*x**4 - 3*x**3 + 2*x**2 + x - 2)

def valores_variables(polinomio):

    coeficientes = polinomio.all_coeffs()
    
    if coeficientes[0] > 1:
        primer_coeficiente = poly.coeffs()[0]

        #dividir el polinomio entre primer coeficiente
        px = sp.quo(poly, primer_coeficiente)

        nuevo_polinomio = px.all_coeffs()
        return nuevo_polinomio
    else:
        return coeficientes


valores = valores_variables(poly)
a = valores[1]
b = valores[2]
c = valores[3]
d = valores[4]

print(valores)
print(a, b, c, d)