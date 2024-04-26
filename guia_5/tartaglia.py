import sympy as sp 
from sympy import I
import math

x = sp.symbols("x")
poly  = sp.poly(25*x**3 + 15*x**2 - 9*x + 1)

#funcion para asignar los valores a, b, c y dividir el polinomio para tenerlo en la forma general x^3 + ax^2 + bx + c
def valores_variables(polinomio):
    
    if polinomio.coeffs()[0] > 1:
        #seleccionar el primer coefiente para dividir el polinomio
        primer_coeficiente = polinomio.coeffs()[0]

        #dividir el polinomio entre primer coeficiente
        px = sp.quo(polinomio, primer_coeficiente)

        coeficientes = px.all_coeffs()

        return coeficientes
    else:
        #sino el polino esta en la forma  x^3 + ax^2 + bx + c solo necesitamos los coefientes
        coeficientes = polinomio.all_coeffs()

        return coeficientes


valores = valores_variables(poly)

#asignamos valores 
a = valores[1]
b = valores[2]
c = valores[3]

print('\na =', a ,'b =', b ,'c =', c)

p = (3*b - (a**2))/3
q = ((2*a**3) - 9*a*b + 27*c)/27
delta = ((q/2)**2) + ((p/3)**3)

print('p =', p)
print('q =', q)
print('delta =', delta)

if delta == 0: # delta = 0 la solucion son 2 raices reales o 1 raiz real
    if (p == 0) and (q == 0):
        raiz = -(a/3)
        print('\nLa ecuacion : ', poly, ' Tiene 1 raiz real')
        print('La raiz es: ', raiz, '\n')
    else:
        raiz_1 = -((3*q)/(2*p)) - (a/3)
        raiz_2 = -(4*(p**2))/(9*q) - (a/3)

        print('\nLa ecuacion : ', poly, ' Tiene 2 raices reales')
        print('Las raices son: ', raiz_1, ',', raiz_2, '\n')

elif delta > 0: # delta tienes una raiz real y una imaginaria
    raiz_real = math.cbrt(-(q/2) + math.sqrt(delta)) + math.cbrt(-(q/2) - math.sqrt(delta)) - (a/3)

    u = math.cbrt(-(q/2) + math.sqrt(delta))
    v = math.cbrt(-(q/2) - math.sqrt(delta))

    print('u =', u)
    print('v =', v)

    raiz_imag = (-(u + v)/2) - (a/3) + (sp.sqrt(3)/2) * (u - v)*I
    

    print('\nLa ecuacion : ', poly, ' Tiene 1 raiz real y 1 imaginaria')
    print('Raiz real: ', raiz_real)
    print('Raiz imaginaria: ', raiz_imag, '\n')

else:
    tetha = math.acos((-q/2)/(math.sqrt(-(p/3)**3)))
    while k < 4:
        k = 0
        raiz = 2 * (math.sqrt(- (p/3))) * math.cos((tetha + (2 * k * math.pi))/3) - (a/3)
        print('\nLa ecuacion ', poly, ' tiene 3 soluciones')
        print('Raiz ', k, '=', raiz , '\n')
        k += 1

    
    