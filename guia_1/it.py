import math

valor_evaluar = 3.141592
valor_verdadero = math.log(1 + float(valor_evaluar))
valor_anterior = 0
iteracion = 1
valores_aproximados = []
errores_aproximados = []
errores_verdaderos = []

def error_verdadero(valor_verdadero, valor_actual):
    er = valor_verdadero - valor_actual
    return er

def calculo_tolerancia(cantidad_cifras):
    tolerancia = 0.5*(10**(2-cantidad_cifras))
    return float(tolerancia)

def error_aproximado(valor_actual, valor_anterior):
    error_aprox = abs(((valor_actual - valor_anterior)/valor_actual)*100)
    return error_aprox

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

tolerancia = calculo_tolerancia(3)

while True:
    if iteracion == 1:
        valor_actual = (-1)**(iteracion - 1)*((valor_evaluar**((2*iteracion)-1))/factorial((2*iteracion)-1))
        valores_aproximados.append(valor_actual)
        ev = error_verdadero(valor_verdadero, valor_actual)
        errores_verdaderos.append(ev)
        valor_anterior = valor_actual
        ea = "-"
        errores_aproximados.append(ea)
        iteracion += 1
    else:
        valor_actual = (-1)**(iteracion - 1)*((valor_evaluar**((2*iteracion)-1))/factorial((2*iteracion)-1))
        valores_aproximados.append(valor_actual)
        ev = error_verdadero(valor_verdadero, valor_actual)
        errores_verdaderos.append(ev)
        ea = error_aproximado(valor_actual, valor_anterior)
        errores_aproximados.append(ea)

        if ea > tolerancia:
            iteracion += 1
            valor_anterior = valor_actual
        else:
            print('Valor verdadero: ',valor_verdadero)
            print('El valor aproximado es: ',str(valor_actual))
            print('Con un error aproximado de: ',str(ea))
            print('Con ',str(iteracion),' iteraciones\n')
            break

print('Valor aproximado')
for iteracion, celda in enumerate(valores_aproximados):
    print(str(iteracion+1),'  |',str(celda))
print('\nError aproximado')
for iteracion, celda in enumerate(errores_aproximados):
    print(str(iteracion+1),'  |',str(celda))
print('\nError verdadero')
for iteracion, celda in enumerate(errores_verdaderos):
    print(str(iteracion+1),'  |',str(celda))
