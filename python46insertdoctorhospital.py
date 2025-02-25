# QUEREMOS UN PROGRMA QUE NOS PERMITA INSERTAR UN DOCTOR EN UN HOSPITAL DETERMINADO.
# EL PROGRAMA TENDRA QUE AYUDARNOS PARA INDICARNOS EN QUE HOSPITAL VAMOS A INSERTAR AL DOCTOR
# DENTRO DE NUESTRO PROGRAMA DEBEMOS PEDIR LOS SIGUIENTES DATOS:
#     1- APELLIDOS DEL DOCTOR
#     2- ESPECIALIDAD
#     3_ SALARIO
# MOSTRAREMOS UN MENU PARA QUE SELECIONEMOS EL HOSPITAL QUE DESEEMOS
# 1- LA PAZ
# 2- GENERALO
# 3- EL CARMEN
# ...
# INSERTAREMOS EL DOCTOR EN DICHO HOSPITAL
# EL ID DEL DOCTOR LO DEBEMOS RECUPERAR DE LA BASE DE DATOS COMO EL MAXIMO ID DEL DOCTOR(OTRA CONSULTA)
import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("------INSERT DOCTOR HOSPITAL-----")
print("Introduzca un Apellido")
apellido = input()
print("Especialidad del doctor")
espe = input()
print("Salario del doctor")
salario = int(input())
sqlhospitales = "select * from HOSPITAL"
cursor = connection.cursor()
cursor.execute(sqlhospitales)
contador = 1
listaHospitales = []
for row in cursor:
    listaHospitales.append(row[0])
    print(f"{contador}) {row[1]}")
    contador += 1
cursor.close()
print("Seleccione un hospital para el Doctor")
opcion = int(input()) - 1
idhospital = listaHospitales[opcion]
sqlmaxId = "select MAX(DOCTOR_NO) + 1 as MAXIMO from DOCTOR"
cursor = connection.cursor()
cursor.execute(sqlmaxId)
row = cursor.fetchone()
iddoctor = row[0]
cursor.close()
sqlinsert = """
    insert into DOCTOR values (:idhospital, :iddoctor
    , :apellido, :espe, :salario)
"""
cursor = connection.cursor()
cursor.execute(sqlinsert, (idhospital,iddoctor,apellido, espe, salario))
registros = cursor.rowcount
print(f"Doctores insertados: {registros}")
connection.commit()
cursor.close()
connection.close()
print("Fin de programa")