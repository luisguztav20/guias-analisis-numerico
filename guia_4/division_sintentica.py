import sympy as sp 

#baristown

coeficientes = [1, 0, -4, 0, -1, 0, 4]

x_1 = 2
x_2 = 1

new_coeficientes = []
new_coeff_1 = new_coeff_2 = coeficientes[0]
new_coeficientes.append(coeficientes[0])

for coeficiente in coeficientes[1:-2]:
    new_coeff_1 = new_coeff_1 * x_1 + coeficiente
    new_coeff_2 = new_coeff_2 * x_2 + new_coeff_1
    new_coeficientes.append(new_coeff_2)

print(new_coeficientes)