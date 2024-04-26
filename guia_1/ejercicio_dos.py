""""
Escribe un programa que permita al usuario ingresar los montos de las compras de
un cliente (se desconoce la cantidad de datos que cargará), si el usuario ingresa el
monto 0 terminar el proceso de ingreso de más datos. Si ingresa un monto negativo,
no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar,
informar el total a pagar con el siguiente formato:

Compras: $XX.XX
Descuento del X%: $XX.XX
Total a pagar: $XX.XX

Teniendo en cuenta que, si las ventas superan el monto total de 1000 se le debe
aplicar un 25% de descuento, si están en el rango entre 700 y 1000 se le aplica un
descuento del 15% y si es mayor a 250 un descuento del 5%.
"""
montos = []

def calculo_descuento(total_compras):
    if monto_total >= 1000:
        descuento = monto_total * 0.25
        total_pago = monto_total - descuento
        print('Compras: $',monto_total)
        print('Descuento: $',descuento)
        print('Total a pagar: $',total_pago)
    elif monto_total >= 700 and monto_total < 1000:
            descuento = monto_total * 0.15
            total_pago = monto_total - descuento
            print('Compras: $',monto_total)
            print('Descuento: $',descuento)
            print('Total a pagar: $',total_pago)
    elif monto_total > 250 and monto_total < 700:
            descuento = monto_total * 0.05
            total_pago = monto_total - descuento
            print('Compras: $',monto_total)
            print('Descuento: $',descuento)
            print('Total a pagar: $',total_pago)
    else:
        print('Su compra no aplica descuentos')
        print('Total a pagar: $',monto_total)
 
while True:

    try:
        monto = float(input('Ingrese monto de su compra (0 para terminar): '))
        if len(montos) == 0 and monto == 0:
            print('No ingreso ningun dato')
            break
        elif monto == 0:
            print('Valores ingresados correctamente')
            break
        elif monto > 0:
            montos.append(monto)
        else:
            print('No se pueden ingresar valores negativos')
    except:
        print('El valor ingresado no es correcto')

if len(montos) > 0:
     monto_total = sum(montos)
     calculo_descuento(monto_total)
else:
     print('Ingrese valores para calcular su descuento')

