import pandas as pd
import sympy as sp 
from sympy import symbols, Poly

x = sp.symbols("x")

Es = 0.5 * 10 ** (2 - 4)
px= sp.Poly("1 + 3*x + 5*x**2 + 6*x**3")
x0 = -0.45
r = 0
iteracion = 1

# Listas para almacenar los coeficientes y los exponentes
coeficientes = []
exponentes = []

def ordernar_polinomio(px):
    # Convertir a un objeto Poly
    px_poly = Poly(px, x)

    # Obtener todos los términos del polinomio
    todos_terminos = px_poly.all_terms()

    # Ordenar los términos en función del exponente
    px_ordenado = sorted(todos_terminos, key=lambda term: term[0], reverse=True)

    return px_ordenado

def obtener_terminos(coeficientes, exponentes):

    # Iterar sobre los términos ordenados
    for exponente, coeficiente in px_ordenado:
        coeficientes.append(coeficiente)
        exponentes.append(exponente[0])  

    return coeficientes, exponentes

def division(coeficientes, x0):
    nuevos_coeficientes = [] #Lista para almacenar los nuevos coeficientes 
    while True:
        #Para operar el primer coeficiente
        i = 0
        multiplicador = coeficientes[i]
        multiplicacion = multiplicador * x0
        nuevos_coeficientes.append(multiplicador)

        for iteracion in range(1, len(coeficientes)): #Emepezamos a iterar en la segunda posicion de la lista 
            r = multiplicacion + coeficientes[iteracion] # en multiplicacion se almacena el valor que se suma con el coeficiente
            multiplicador = r 
            multiplicacion = multiplicador * x0
            nuevos_coeficientes.append(r)
        break

    while True:
        i=0
        multiplicador = nuevos_coeficientes[i]
        multiplicacion = multiplicador * x0
        nuevos_coeficientes.pop()#Eliminamos la ultima posicion de la lista que corresponde a R 
        for iteracion in range(1, len(nuevos_coeficientes)): #Iteramos desde la segunda posicion en la lista
            s = multiplicacion + nuevos_coeficientes[iteracion]
            multiplicador = s 
            multiplicacion = multiplicador * x0

        break
        
    return r, s

def calculo_x1(r, s, x0):
    x1 = x0 - (r/s)
    return x1

df = pd.DataFrame(columns=["Iteracion", " Xi", "Error Aproximado"])


while True:
   
    px_ordenado = ordernar_polinomio(px, x)#Ordenamos px

    coeficnetes, exponentes = obtener_terminos(coeficientes, exponentes)#Obtenemos los coeficientes

    r, s = division(coeficientes, x0)#Realizamos la division sintetica para obtener r y s

    x1 = calculo_x1(r, s, x0)#Calculo x1

    Ea = abs(((x1 - x0)/x1)*100)
    df.loc[iteracion-1] = [iteracion, x1, Ea]

    if(Ea < Es):
        break
    else:
        x0 = x1
        
    iteracion += 1

print(df)
print('Es',Es)
print('Ecuacion: ',px)
print('Raiz: ', x1)
print('Con un error de: ', Ea,'%')
print('Con ',iteracion,'iteraciones')






