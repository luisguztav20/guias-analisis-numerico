import sympy as sp

# para que el algoritmo calcule automaicamente el polinomio de grado n debo validar la cantidad de puntos 
# en la lista ejemplo: si la lista es de dimension 3 el algoritmo calcula el polinomio de grado 2

x = sp.symbols('x')

Xn = [0, 1, 2]

fxn = [1, 2.718, 54.598]

#print('Ingrese una opcion:')
#opcion = int(input('1. Polinomio primer grado\n2. Polinomio segundo grado\n3. Polinomio tercer grado\n4. Polinomio cuarto grado\n:'))


if (len(Xn) == 2):
    x0, x1 = Xn
    fx0, fx1 = fxn

    p1 = sp.expand(fx0 * ( (x - x1) / (x0 - x1) )) + sp.expand(fx1 * ( (x - x0) / (x1 - x0) ))
    
    print('Polinomio de interpolacion de Lagrange de grado 1')
    print('P1 =',p1)
    
elif (len(Xn) == 3):
    x0, x1, x2 = Xn
    fx0, fx1, fx2 = fxn
    
    p2 = ( sp.expand( fx0 * ((x -x1) * (x - x2)) / ((x0 - x1) * (x0 - x2)) ) + 
           sp.expand( fx1 * ((x -x0) * (x - x2)) / ((x1 - x0) * (x1 - x2)) ) +
           sp.expand( fx2 * ((x -x0) * (x - x1)) / ((x2 - x0) * (x2 - x1)) ) 
         )
    
    print('Polinomio de interpolacion de Lagrange de grado 2')
    print('P2 =',p2)

elif (len(Xn) == 4):
    x0, x1, x2, x3 = Xn
    fx0, fx1, fx2, fx3 = fxn
    
    p3 = ( sp.expand( fx0 * ((x - x1) * (x - x2) * (x - x3))  / ((x0 - x1) * (x0 - x2) * (x0 - x3)) ) +
           sp.expand( fx1 * ((x - x0) * (x - x2) * (x - x3))  / ((x1 - x0) * (x1 - x2) * (x1 - x3)) ) +
           sp.expand( fx2 * ((x - x0) * (x - x1) * (x - x3))  / ((x2 - x0) * (x2 - x1) * (x2 - x3)) ) +
           sp.expand( fx3 * ((x - x0) * (x - x1) * (x - x2))  / ((x3 - x0) * (x3 - x1) * (x3 - x2)) )
         )
    
    print('Polinomio de interpolacion de Lagrange de grado 3')
    print('P3 =',p3)

elif (len(Xn) == 5):
     x0, x1, x2, x3, x4 = Xn
     fx0, fx1, fx2, fx3, fx4 = fxn
    
     p4 = ( sp.expand( (fx0 * ((x - x1) * (x - x2) * (x - x3) * (x - x4))  / ((x0 - x1) * (x0 - x2) * (x0 - x3) * (x0 - x4))), rational=False) +
            sp.expand( (fx1 * ((x - x0) * (x - x2) * (x - x3) * (x - x4))  / ((x1 - x0) * (x1 - x2) * (x1 - x3) * (x1 - x4))), rational=False) +
            sp.expand( (fx2 * ((x - x0) * (x - x1) * (x - x3) * (x - x4))  / ((x2 - x0) * (x2 - x1) * (x2 - x3) * (x2 - x4))), rational=False) +
            sp.expand( (fx3 * ((x - x0) * (x - x1) * (x - x2) * (x - x4))  / ((x3 - x0) * (x3 - x1) * (x3 - x2) * (x3 - x4))), rational=False) +
            sp.expand( (fx4 * ((x - x0) * (x - x1) * (x - x2) * (x - x3))  / ((x4 - x0) * (x4 - x1) * (x4 - x2) * (x4 - x3))), rational=False)
         )
     print('Polinomio de interpolacion de Lagrange de grado 4')
     print('P4 =',p4)
    
    
