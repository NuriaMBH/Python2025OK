#vamos a probar una consulta para BUSCAR un departamento
# por su ID. 
#pediremos al usuario el ID del departamento
#si el depasrtamento no existe, mostraremos un mensaje.
# Si existe,  pintamos los datos.
import oracledb

connection=oracledb.connect(user='SYSTEM', password='oracle',dsn='localhost/xe')

print ("Conectado a BBDD")
print("Introduzca nombre de departamento")
data = input()
cursor = connection.cursor()
sql="select * from DEPT where DEPT_NO="+data
cursor.execute(sql)
#como estamos buscando por PK, solamente nos puede devolver una fila
row = cursor.fetchone()
#debemos comprobar si la fila tiene contenido
if(not row):
    print ("no existe el departamento")
else:
    #dibujamos los datos
    nombre =row[1]
    localidad= row[2]
    print(nombre +","+localidad)
cursor.close()
connection.close()
print("Fin de BBDD")
            