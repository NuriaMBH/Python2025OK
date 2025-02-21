# Pediremos al usuario un texto numérico
# “1234”

# Debemos sumar cada carácter del texto y mostrar la suma de cada número/letra
# La suma es 10

print("Suma numeros texto string")
print("Introduzca un texto numérico")
textoNumeros = input()
suma = 0
#RECORREMOS CADA LETRA DEL TERXTO
longitud = len(textoNumeros)
#recorremos cada letra del texto
for i in range (longitud):
    #almacenamos cada letra
    letra= textoNumeros[i]
    #covertimos cada letra a integer
    numero = int(letra)
    #sumamos cada numero 
    suma = suma + numero
print("La suma de "+textoNumeros + " es" +str(suma))
print("Fin de programa")