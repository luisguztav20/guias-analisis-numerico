import sympy as sp

x = sp.symbols('x')

Xn = [2, 2.25, 4]
fx = 1/x

#Para una interpolacion linal solo necesitamos x0, x1, y0, y1

def eval_fx(Xn, fx): #Funcion para evaluar todos los puntos Xn 
    
    valores_evaluados = []
    
    for valor_x in Xn:
        x_evaludo = fx.subs(x, valor_x)
        valores_evaluados.append(x_evaludo)
        
    return valores_evaluados #retorna una lista de los f(xn) evaluados en la funcion 

def eval_poli(polinomio, valor_x): #Funcion para evaluar puntos en el polinomio lineal encontrado 
    return print(polinomio.subs(x, valor_x))
    
    
valores_evaluados = eval_fx(Xn, fx)#Pasamos la lista de los puntos

#Asignamos valores x0, x1, x2, y0, y1, y3
x0, x1, x2 = Xn
fx0, fx1, fx2 = valores_evaluados


Px = ((fx1 - fx0)/(x1 - x0))*(x -x0) + fx0 

Px_ordenado = sp.simplify(Px)

print('Polinomonio de interpolacion lineal de la funcion: f(x) =', fx, '\n', Px_ordenado)

#eval_poli(Px_ordenado, 3)
