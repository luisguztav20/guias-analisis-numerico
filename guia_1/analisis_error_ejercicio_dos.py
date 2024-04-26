

iteracion = 1
valor_real = 8.0
def calculo_error(valor_real, valor_aprox):
    
    error_verdadero = valor_real - valor_aprox
    error_relativo = error_verdadero/ valor_real
    error_porcentual = abs(error_relativo * 100)
    print('\nMedida real: ',str(valor_real),'ohmios\t Medida obtenida: ',str(valor_aprox),'ohmios')
    print('Error verdadero: ',str(error_verdadero),'ohmios')
    print('Error relativo: ',str(error_relativo),'ohmios')
    print('Error porcentual: ',str(error_porcentual),'%')
    print('********************************')

while iteracion <= 5:
    valor_aprox = float(input('Ingrese medicion {}: '.format(iteracion)))
    print('Calculos error medicion {}:'.format(iteracion))
    calculo_error(valor_real, valor_aprox)
    iteracion += 1
