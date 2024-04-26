import sympy as sp

x, x0, x1, x2 = sp.symbols('x x0 x1 x2')

Xn = [2, 2.25, 4]
fx = 1/x


#Para una interpolacion cuadratica necesitamos x0, x1, x2,  y0, y1, y2

def eval_fx(Xn, fx): #Funcion para evaluar todos los puntos Xn 
    
    valores_evaluados = []
    
    for valor_x in Xn:
        x_evaludo = fx.subs(x, valor_x)
        valores_evaluados.append(x_evaludo)
        
    return valores_evaluados #retorna una lista de los f(xn) evaluados en la funcion 

def eval_poli(polinomio, valor_x): #Funcion para evaluar puntos en el polinomio lineal encontrado 
    return print(polinomio.subs(x, valor_x))

valores_evaluados = eval_fx(Xn, fx)#Pasamos la lista de los puntos
print(valores_evaluados)
#Asignamos valores x0, x1, x2, y0, y1, y3
x0, x1, x2 = Xn
fx0, fx1, fx2 = valores_evaluados

b0 = fx0
b1 = ((fx1 - fx0))/(x1 - x0)
b2 =  (((fx2 - fx1) / (x2 -x1)) - (b1)) / (x2 - x0)
#fact1 = x -x0
#fact2 = x - x1
Px = (b0 + (sp.expand(b1*(x -x0))) + (sp.expand(b2*((x -x0) * (x - x1))))) 

Px_ordenado = sp.sympify(Px)#Ordenar el polinomio si viene desordenado

print('Polinomonio de interpolacion cuadratico de la funcion: f(x) =', fx, '\n', Px_ordenado)
#eval_poli(Px_ordenado, 3)
