""""
Supongamos que se tiene que medir la longitud de un puente y de un
remache, obteniéndose 9999cm y 9cm, respectivamente. Si los valores ver-
daderos son 10000cm y 10cm, usando Python calcula en cada caso:

El error verdadero.
Los errores relativos.
Los errores porcentuales.
"""

def calculo_error(valor_real, valor_aprox):
    
    error_verdadero = valor_real - valor_aprox
    error_relativo = error_verdadero/ valor_real
    error_porcentual = abs(error_relativo * 100)
    print('\nMedida real: ',str(valor_real),'cm\t Medida obtenida: ',str(valor_aprox),'cm')
    print('Error verdadero: ',str(error_verdadero),'cm')
    print('Error relativo: ',str(error_relativo),'cm')
    print('Error porcentual: ',str(error_porcentual),'%')
    print('********************************')


calculo_error(10000, 9999)
calculo_error(10, 9)