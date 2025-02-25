import oracledb

print("eliminar enfermo")
print("introduzca inscripcion para borrar")
data= input()
sql="delete from ENFERMO where inscripcion=" + data
connection=oracledb.connect(user='SYSTEM', password='oracle',dsn='localhost/xe')
cursor = connection.cursor()
#no existe diferencia un cursor ejecuta consultas y simplemente i son de 
#seleccion se recorrent  y si son de acción recuperamos su valor mediante rowcount
cursor.execute(sql)
afectados = cursor.rowcount
print("registros eliminados "+ str(afectados))
cursor.close()
connection.close()
print("fin de programa BBDD")
