
def calculo_tolerancia(cantidad_cifras):
    tolerancia = 0.5*(10**(2-cantidad_cifras))
    return tolerancia

cantidad_cifras = float(input('Ingrese cantidad de cifras significativa: '))
print('Nivel de tolerancia es: ',calculo_tolerancia(cantidad_cifras))