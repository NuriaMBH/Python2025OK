import oracledb

connection=oracledb.connect(user='SYSTEM', password='oracle',dsn='localhost/xe')

sql = "select * from DEPT"
cursor = connection.cursor()
cursor.execute(sql)
for numero, nombre, localidad in cursor:
   print(str(numero) + ":" + nombre + "," + localidad)

#para recorrer un cursos se utilizan bucles for 
#for objeto(row) in cursor:
#for row in cursor:
   ## print (row)
    #si deseamos extraer datos de alguna columna
    #podemos realizarlo por el indice
   # print (row[0])
    #tambien podemos recuperar los datos por nombre de columna.
    #PERO ESTO SOLAMENTE ES COMPATIBLE CON ALGUNAS BBDD
    #EL CURSOS SOLAMENTE SE PUEDE LEER UNA VEZ
    #SI DESEAMOS LEER DE NUEVO DEBEMOS EJECUTAR DE NUEVO
   # fila = cursor.fetchone()
    #print(fila)
    #nombre=row.DNOMBRE
    #print(nombre)
cursor.close()
connection.close()
print ("Fin de BBDD")
