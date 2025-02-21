print("Lista con python")
listaNumeros = [12,56,77,88,99,22]
#REALIZAMOS UN BUCLE PARA MOSTRAR LOS NUMERO ACTUALMENTE
listaNumeros.sort()
#ordena la lista ascendente
#hay que incluir reverse = True
listaNumeros.sort(reverse = True)
# LAS LISTAS COMINEZAN EN CERO Y FINALIZAN EN LEN
print("Numero 0: ", listaNumeros[0])
print("Numero1: ", listaNumeros[1])
listaNombres = ["Ana", "Lucas","Adrían", "Diana", "Antonia" "Lucas"]
print("Nombre 2:", listaNombres[2])
print("Nombre 4: ", listaNombres [4])

#append CREA UN NUEVO ELEMENTO EN LA LISTA AL FINAL
listaNombres.append("Lucia")
print("Nombre 5: ", listaNombre [5])
#inser() CREA UN ELEMNTO NUEVO EN UNA POSICION NDE LA LISTA
listaNombres.insert(4, "Inflittrado")
#el metodo remove()elimina un objeto dentro de la lista
#si hay repetidos, elimina elprimero dentro de la lista y si no lo encuentra de error
listaNombres.remove("Lucas")
listaNombres.remove("Lucasssss")#dará error
#listaNombres.pop(6)
#listaNombres.clear
#vamos a recorrer todos los elementos de la lista y mostrar
#su posición
for i in range(len(listaNombres)):
    print (str(i) + "=" listaNombres[i])