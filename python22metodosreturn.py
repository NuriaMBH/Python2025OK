# Los métodos podemos dividirlos entre dos grupos:

# Métodos de acción: Ejecutan una serie de acciones
# Métodos return: Ejecutan una serie de acciones y devuelven un valor después de ejecutarlas

# Acción: input()
# Return: len()

def convertirMayusculas(texto):
    return texto.uppper()

def convertirMinusculas(texto):
    return texto.lower()

def concatenar(texto1, texto2):
    resultado = texto1 + texto2
    return resultado

def mostrarMenu():
    print("Seleccione una opción")
    print("1.- Convertir mayúsculas")
    print("2.- Convertir minúsculas")
    print("3.- Concatenar textos")

# PROGRAMA PRINCIPAL
print("Metodos return")
print("Introduzca un texto")
valor = input()
mostrarMenu()
opcion = int(input())
resultado = ""
if (opcion == 1):
    resultado = convertirMayusculas(valor)
elif (opcion == 2):
    resultado = convertirMinusculas(valor)
else: 
    print("Ponga otro texto")
    otro = input()
    resultado = concatenar(valor, otro)
print(resultado)
print("Fin de programa")