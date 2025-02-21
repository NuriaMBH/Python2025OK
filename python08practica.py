#CALCULAR DIA DE NACIMIENTO DE SEMANA

# Lo que necesito SOBRE TODO es hacer el programa, pero que probéis la depuración de código.
# Tenemos que tener la tabla de días de la semana para la correspondencia comenzando en sábado:

# Debemos pedir el día, el número de mes y el año que el usuario haya nacido.
# A partir de esto datos hay que calcular lo siguiente para averiguar el día de la semana de nacimiento:
# Ejemplo  15/06/1997

# Hay que tener en cuenta el mes para realizar el cálculo

# Si el mes es Enero, el Mes será 13 y restaremos uno al año. 
# Si el Mes es Febrero, el Mes será 14 y restaremos uno al año.

# Para poder calcular el número final de la semana debemos seguir los siguientes pasos:

# Multiplicar el Mes más 1 por 3 y dividirlo entre 5

#  ((6 + 1) * 3) / 5   4

# Dividir el año entre 4
#   1997 / 4   499

# Dividir el año entre 100

#   1997 / 100  19

# Dividir el año entre 400

#   1997 / 400  4

# Sumar el dia, el doble del mes, el año, el resultado de la operación 1, el resultado de la operación 2, menos el resultado de la operación 3 más la operación 4 más 2.

#   15 + (6 * 2) + 1997 + 4 + 499 - 19 + 4 + 2  2514

# Dividir el resultado anterior entre 7.

#   2514 / 7  359

# Restar el número del paso 5 con el número del paso 6 por 7.

#  	  2514 – (359 * 7)  1

# Miramos la tabla y vemos que el número 1 corresponde a DOMINGO



from math import trunc
print("Dia nacimiento de la semana")
#LOS DATOS SON NUMEROS, DEBEMOS CONVERTIR
#LO QUE EL USUARIO ESTA ESCRIBIENDO
print("Introduzca día")
dia = int(input())
print("Introduzca mes")
mes = int(input())
print("Introduzca año")
anyo = int(input())
if (mes == 1):
    mes = 13
    anyo = anyo - 1
elif (mes == 2):
    mes = 14
    anyo = anyo - 1
op1 = trunc(((mes + 1) * 3) / 5)
op2 = trunc( anyo / 4)
op3 = trunc( anyo / 100)
op4 = trunc( anyo / 400)
# 5.	Sumar el dia, el doble del mes, el año
# , el resultado de la operación 1, el resultado de la operación 2
# , menos el resultado de la operación 3 más la operación 4 más 2.
op5 = trunc( dia + (mes * 2) + anyo + op1 + op2 - op3 + op4 + 2)
op6 = trunc(op5 / 7)
resultado = trunc( op5 - (op6 * 7))
diaSemana = ""
if (resultado == 0):
    diaSemana = "SABADO"
elif (resultado == 1):
    diaSemana = "DOMINGO"
elif (resultado == 2):
    diaSemana = "LUNES"
elif (resultado == 3):
    diaSemana = "MARTES"
elif (resultado == 4):
    diaSemana = "MIERCOLES"
elif (resultado == 5):
    diaSemana = "JUEVES"
elif (resultado == 6):
    diaSemana = "VIERNES"
print(diaSemana)
print("Fin de programa")
 

