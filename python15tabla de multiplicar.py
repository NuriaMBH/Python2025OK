# Realizamos un programa nuevo en el que mostraremos la tabla de multiplicar de un número.
# Pediremos al usuario el número y le mostraremos la siguiente tabla
# 5 * 1 = 5
# 5 * 2 = 10

print("Tabla multiplicar")
print("Introduzca número")
numero = int(input())
for i in range(1, 11):
    operacion = numero * i
    print(str(numero) + " * " + str(i) + "=" + str(operacion))
print("Fin de programa")

