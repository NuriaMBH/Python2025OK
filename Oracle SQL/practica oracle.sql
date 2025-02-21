--1. MOSTRAR TODOS LOS DATOS DE LOS EMPLEADOS DE NUESTRA TABLA EMP
select * from EMP
-- Mostrar el apellido , oficio, salario anual, con las dos extras para aquellos empleados con comisión mayor de 100000.
select APELLIDO, OFICIO,(SALARIO+COMISION) as TOTAL from EMP where (SALARIO + COMISION ) >100000;
--IDEM DEL ANTERIOR , PERO PARA AQUELLOS EMPLEADOS QUE SU SALARIO ANUAL   (CON EXTRA) SUPERE LAS 750000 PTAS.
select  as TOTAL from EMP (SALARIO *2)>750000;
