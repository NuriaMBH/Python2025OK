# necesitamos un progrma para mostrar los empleados de la plantilla de un determinado turno
# debemos seleccionar un turno de una serie de opciones 
# y mostraremos los datos de la plantilla de dicho turno.


import oracledb
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("Selecciona turno")

sqlturnos="""
select distinct TURNO, case TURNO
when 'T' then 'TARDE'
when 'M' then 'MAÑANA'
else 'NOCHE'
end as VALOR
    from PLANTILLA"""
cursor =connection.cursor()
cursor.execute(sqlturnos)
contador = 1
#NECESITAMOS EL ALMACENAR EL DATO DE CADA TURNO
listaturnos= []
for row in cursor:
        print(f"{contador} - {row[1]}")
        listaturnos.append(row[0])
        contador=contador +1
cursor.close()
print("Seleccione una opción")
opcion=int(input())
turno = listaturnos[opcion - 1]
sqlplantilla="select *from PLANTILLA where turno=:p1"
cursor = connection.cursor()
cursor.execute(sqlplantilla,(turno,))
for row in cursor:
    print(row)
cursor.close()
connection.close()
print("Fin de programa")