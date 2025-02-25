import oracledb
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("buscador de oficios")

sqloficios="select distinct OFICIO from EMP"
cursor =connection.cursor()
cursor.execute(sqloficios)
contador = 1
#NECESITAMOS EL ALMACENAR EL DATO DE CADA OFICIO
listaoficios= []
for row in cursor:
        print(f"{contador} - {row[0]}")
        listaoficios.append(row[0])
        contador=contador +1
cursor.close()
print("Seleccione una opción")
opcion=int(input())
oficio= listaoficios[opcion - 1]

sqlempleados="select *from EMP where OFICIO=:p1"
cursor = connection.cursor()
cursor.execute(sqlempleados,(oficio,))
for row in cursor:
    print(row)
cursor.close()
connection.close()
print("Fin de programa")