# Vamos a realizar un ejemplo para demostrar la conjetura de Collatz
# La conjetura dice lo siguiente:
# Todo número positivo siempre llegará a ser 1 cumpliendo estas dos condiciones:
# Si el número es PAR, dividimos entre 2
# Si el número es IMPAR, multiplicamos * 3 y sumamos 1
# 6, 3, 10, 5, 16, 8, 4, 2, 1

print ("conjetura de Collatz")
print("Introduzca un numero")
numero = int(input())
while (numero!= 1):
    if (numero % 2 == 0):
        numero = int(numero /2)
    else:
        numero = numero * 3 + 1
    print(numero)
print("Fin de programa")