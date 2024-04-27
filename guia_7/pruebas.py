# Obtener la lista de valores desde el usuario
valores = input("Ingrese una lista de valores separados por coma: ").split(',')

# Crear variables dinámicamente
for i, valor in enumerate(valores):
    # Usar el prefijo 'valor_' seguido del índice para nombrar las variables
    nombre_variable = f"valor_{i + 1}"
    # Asignar el valor a la variable con el nombre generado dinámicamente
    globals()[nombre_variable] = valor

# Ahora puedes acceder a las variables utilizando sus nombres generados dinámicamente
print(valor_1)
print(valor_2)
print(valor_3)