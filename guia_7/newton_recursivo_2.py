import sympy as sp

x = sp.symbols('x')

Xn = [1,2,3,4]
fx = sp.ln(x)
px = 0

valores_b = []


def eval_fx(Xn, fx): #Funcion para evaluar todos los puntos Xn 
    
    valores_evaluados = []
    
    for valor_x in Xn:
        x_evaludo = fx.subs(x, valor_x)
        valores_evaluados.append(x_evaludo)
        
    return valores_evaluados #retorna una lista de los f(xn) evaluados en la funcion 

valores_fx = eval_fx(Xn, fx)
print(Xn)
print(valores_fx)

i = 0 

while i < len(Xn):
    if i == 0:
        valores_b.append(float(valores_fx[i]))
        print('b',i,'=',valores_b[i])

    elif i == 1:
        valores_b.append(float(( (valores_fx[i] - valores_b[i-1] ) / (Xn[i] - Xn[i-1]))))

    else:
        valores_b.append( float((((valores_fx[i] - valores_fx[i-1]) / (Xn[i] - Xn[i-1]) ) - valores_b[i-1]) / (Xn[i] - Xn[0])) )
        print('b',i,'=',valores_b[i])

    i += 1

a = 0
binomios = 1
while a < len(Xn):

    if a > 0:
        binomios = binomios * (x-(Xn[a-1]))   
    px = sp.expand(px + valores_b[a] * binomios)   
    a += 1

print('Polinomio de grado',str(len(Xn)-1),'=', px.evalf() )
print('P(0.73) = ', px.subs(x, 0.73) )

