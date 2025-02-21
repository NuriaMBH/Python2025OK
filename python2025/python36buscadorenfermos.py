# debemos buscar un enfermo por su inscripcion
# pediremos el dato por pantalla en el programa
# si el enfermo existe, mostramos su APELLIDO y su DIRECCION
# si no existe, lo indicamos por pantalla
import oracledb

connection=oracledb.connect(user='SYSTEM', password='oracle',dsn='localhost/xe')

print ("Conectado a BBDD")
print("Introduzca nombre de inscripción")
data = input()
cursor = connection.cursor()
sql="select apellido, direccion from enfermo where inscripcion="+data
cursor.execute(sql)
#como estamos buscando por PK, solamente nos puede devolver una fila
row = cursor.fetchone()
#debemos comprobar si la fila tiene contenido
if(not row):
    print ("no existe el inscripcion")
else:
    #dibujamos los datos
    apellido =row[0]
    direccion= row[1]
    print(apellido +","+ direccion)
cursor.close()
connection.close()
print("Fin de BBDD")