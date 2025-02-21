
import oracledb

connection=oracledb.connect(user='SYSTEM',password='oracle',dsn='localhost/xe')
sql="select * from DEPT"
#creamos un curso para realizar la consulta
cursor=connection.cursor()
#la consulta se ejecuta y recupera los datos a la vez
#al aplicar el metodo execute(SQL)
cursor.execute(sql)

#una vez que tenemos los datos en cursor, debemos extraerlos
#para recuperar los datos 
#tenemos un metodo llamado  fetchone() que nos devuelve una fila
#cada vez que ejecutemos fetchone() avanza ua fila
row= cursor.fetchone()
#pintamos la fila
print (row)
#pintamos la fila1
print (row)
#pintamos la fila2
print (row)
#pintamos la fila3
row= cursor.fetchone()
print (row)
#pintamos la fila 4
row= cursor.fetchone()
print (row)
#pintamos la fila???
row= cursor.fetchone()
print (row)
#por norma, siempre debemos liberar los recursos de bbdd
#cerrar todo
cursor.close()
connection.close()
print("fin de BBDD")