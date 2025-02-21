--insertar un nuevo registro en plantilla
--la persona se llama cabrales,sala 4, enfermera, M
---trabaja en el hospital de el carmen
--el ID sera el maximo en la consulta
select * from PLANTILLA
insert into PLANTILLA( empleado_No, apellido, sala_cod, funcion, turno, HOSPITAL_COD)
values
((select MAX(EMPLEADO_NO) + 1 from PLANTILLA),'cabrales', 4,'enfermera','M',54);
(select HOSPITAL_COD from HOSPITAL where NOMBRE='el carmen'));
--2 ELIMINAR LAS PERSONAS DE LA PLANTILLA
--QUE No TENGAN HOSPITAL

select HOSPITAL_COD from HOSPITAL;
select * from PLANTILLA

delete from PLANTILLA where HOSPITAL_COD not in
((select HOSPITAL_COD from HOSPITAL);

select * from PLANTILLA