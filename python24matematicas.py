#los import se realizan lo primero de nuestro codigo
#from libreria24matematicas import sumarNumeros,restarNumeros,mostrarMenu
#si necesitas alguna formula, pero si necesitas toda la linreria
import libreria24matematicas
#te la trae entera

#codigo logico
print("Calculadora metodos")
numero1= 9 
numero2= 19
libreria24matematicas.mostrarMenu()
opcion = int(input())
resultado= 0
if (opcion == 1):
    resultado = libreria24matematicas.sumarNumeros(numero1,numero2)
elif (opcion == 2):
    resultado= libreria24matematicas.restarNumeros(numero1,numero2)
elif(opcio== 3):
    resultado = libreria24matematicas.multiplicarNumeros(numero1,numero2)
else:
    print ("No ha seleccionado una opción correcta")
print("Resultado",resultado)
print ("Fin de programa")