import sympy as sp 
from sympy import I
import math
import cmath

x = sp.symbols("x")
u = sp.symbols("u")
poly  = sp.poly(24*x**4 - 3*x**3 + 2*x**2 + x - 2)

#funcion para llevar el polinomio a la forma x^4 + ax^3 + bx^2 + cx + d dividiendo entre el coeficiente del primer termino
def valores_variables(polinomio):
    
    if polinomio.coeffs()[0] > 1:
        #seleccionar el primer coefiente para dividir el polinomio
        primer_coeficiente = polinomio.coeffs()[0]

        #dividir el polinomio entre primer coeficiente
        px = sp.quo(polinomio, primer_coeficiente)

        coeficientes = px.all_coeffs()

        return coeficientes #Retornamos una lista con los nuevos coeficientes
    else:
        #sino el polino esta en la forma  x^3 + ax^2 + bx + c solo necesitamos los coefientes
        coeficientes = polinomio.all_coeffs()

        return coeficientes

def tartaglia(polinomio):
    valores = valores_variables(polinomio) #almacenamos en una lista retornada en una variable

    #asignamos valores 
    a = valores[1]
    b = valores[2]
    c = valores[3]

    #print('a =', a ,', b =', b ,', c =', c)

    p = (3*b - (a**2))/3
    q = ((2*a**3) - 9*a*b + 27*c)/27
    delta = ((q/2)**2) + ((p/3)**3)

    #print('p =', p)
    #print('q =', q)
    #print('delta =', delta)

    if delta == 0: # delta = 0 la solucion son 2 raices reales o 1 raiz real
        if (p == 0) and (q == 0):
            raiz = -(a/3)

            return raiz
        else:
            raiz_1 = -((3*q)/(2*p)) - (a/3)
            raiz_2 = -(4*(p**2))/(9*q) - (a/3)

            return raiz_1

    elif delta > 0: # delta > 0 tiene una raiz real y una imaginaria
        raiz_real = math.cbrt(-(q/2) + math.sqrt(delta)) + math.cbrt(-(q/2) - math.sqrt(delta)) - (a/3)

        u = math.cbrt(-(q/2) + math.sqrt(delta))
        v = math.cbrt(-(q/2) - math.sqrt(delta))

        #print('u =', u)
        #print('v =', v)

        raiz_imag = (-(u + v)/2) - (a/3) + (sp.sqrt(3)/2) * (u - v)*I

        return raiz_real 
    else:
        tetha = math.acos((-q/2)/(math.sqrt(-(p/3)**3)))
        #k=0
        raiz_1 = 2 * (math.sqrt(- (p/3))) * math.cos((tetha + (2 * 0 * math.pi))/3) - (a/3)
        #k=1
        raiz_2 = 2 * (math.sqrt(- (p/3))) * math.cos((tetha + (2 * 1 * math.pi))/3) - (a/3)
        #k=2
        raiz_3 = 2 * (math.sqrt(- (p/3))) * math.cos((tetha + (2 * 2 * math.pi))/3) - (a/3)

        return raiz_1

valores = valores_variables(poly)

#asignamos los valores de las variables a, b, c ,d
a = valores[1]
b = valores[2]
c = valores[3]
d = valores[4]

print('a =', a ,', b =', b ,', c =', c , ', d =', d)

p = (8 * b - 3 * (a**2))/8
q = ((8 * c) - (4 * a * b) + (a**3))/8
r = (256 * d - 64 * a * c + 16 * (a**2) * b - 3 * (a**4))/256

print('p = ', p)
print('q = ', q)
print('r = ', r.evalf())
 
#construir la ecuacion cubica 
new_poly = sp.poly(u**3 - ((p/2) * u**2) - (r * u) + ((4 * p * r - (q**2))/8 ))

#aplicar metodo tartaglia
print('\nPolinomio grado 3: ', new_poly ,'\n')

#obtenemos el valor de u mediante tartaglia
u = tartaglia(new_poly) # 
print('u = ',u)

v = math.sqrt((2*u)-p)
w = -(q/(2*v))
print('v = ', v)
print('w = ', w)

#calculos de las raices
x_1 = ((v + cmath.sqrt((v**2) - 4*(u - w)))/2) - a/4
x_2 = ((v - cmath.sqrt((v**2) - 4*(u - w)))/2) - a/4
x_3 = (-v + (cmath.sqrt((v**2) - 4*(u + w))))/2 -a/4
x_4 = (-v - (cmath.sqrt((v**2) - 4*(u + w))))/2 -a/4

#Mostramos la solucion
print('\nSoluciones de la ecuacion ', poly)
print('\nRaiz 1 =' , x_1 , '\nRaiz 2 =' , x_2 ,'\nRaiz 3 =' , x_3 ,'\nRaiz 4 =' , x_4)

