#calcular salario de trabajadores
#pediremos a un usuario las horas trabajadas, precio hora y los kms
#el trabajador tendra horas extras a partir de la hora 36
#cada una extra sera 2 euros mas
# solamentente mostraremos mensajes:
# si el trabajador hace menos de 100 km las dietas son locales
# si el trabajador hace entre 101 y 500 km las dientas son provinciales
# si hace mas km serán nacionales
# si el precio final es menor a 250euros sin retenciones
# si es entre 251 y 600 20% de retención
# si es mayor 40% retención
# numero horas: 40
# horas extra: 4
# precio hora:20
# salario base: 36 *20
# salario extra 4*22
# salario total: salario base +salario extra
print("Calculo salario de trabajadores")
print("Introduzca horas del trabajador")
horas= int(input())
print("Introduzca km del trabajador")
km = int(input())
print("Introduzca precio hora del trabajador")
preciohora= int(input())
print("Introduzca precio hora extra del trabajador")
precioextra= int(input())
horas=0
horasextra=0 
km =0
preciohorareciohora=0
precioextra=0

if(km>=100):
    print ("Dieta local")
elif(km<=101 and km>=500):
    print ("Dieta provincial")
else:
    print ("Dieta Nacional")
multiplica= preciohora * horas
multiplica=precioextra * horasextra
#SOLUCION#
print("Ejemplo Horas extra")
print("Horas trabajadas")
horasTrabajadas = int(input())
print("Precio hora")
precioHora = int(input())
print("Kilometros recorridos")
km = int(input())
horasExtra = 0
salarioExtra = 0
salarioBase = 0
salarioTotal = 0
dietas = ""
retencion = ""
#PREGUNTAMOS SI TENEMOS HORAS EXTRA
if (horasTrabajadas > 36):
    #HORAS EXTRA
    horasExtra = horasTrabajadas - 36
    salarioBase = precioHora * 36
    salarioExtra = horasExtra * (precioHora + 2)
else:
    #NO HA HECHO HORAS EXTRA
    horasExtra = 0
    salarioExtra = 0
    salarioBase = horasTrabajadas * precioHora
salarioTotal = salarioBase + salarioExtra
if (km <= 100):
    dietas = "LOCALES"
elif (km >= 101 and km <= 500):
    dietas = "PROVINCIALES"
else:
    dietas= "NACIONALES"
if (salarioTotal < 250):
    retencion = "SIN RETENCION"
elif (salarioTotal >= 250 and salarioTotal <= 600):
    retencion = "20% Retencion"
else:
    retencion = "40% Retención"
#INFORME
print("Informe de salario")
print("Horas trabajadas ", horasTrabajadas)
print("Horas extra ", horasExtra)
print("Precio hora ", precioHora)
print("Precio extra ", (precioHora + 2))
print("Salario base ", salarioBase)
print("Salario extra ", salarioExtra)
print("Salario total ", salarioTotal)
print("Retenciones ", retencion)
print("Dietas ", dietas)
