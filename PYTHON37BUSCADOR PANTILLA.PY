# vamos a realizar una aplicacion para buscar empleados de la plantilla por su turno
# pediremos al usuario el turno que desea buscar
# mostraremos el apellido y la funcion de los empleados del turno determinado
import oracledb

connection=oracledb.connect(user='SYSTEM', password='oracle',dsn='localhost/xe')

print ("Buscador plantilla por turno")
print("Introduzca un turno(T,M,N)")
data = input()
cursor = connection.cursor()
sql="select 'apellido`, 'funcion' from plantilla where turno= '" + data+"'"
cursor.execute(sql)
#recorremos los datos del cursor
for apellido, funcion in cursor:
    print(apellido +",funcion:"funcion)
cursor.close()
connection.close()
print("Fin de BBDD")
            
