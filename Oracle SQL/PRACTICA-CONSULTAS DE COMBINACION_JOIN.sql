--Seleccionar el apellido, oficio, salario, numero de departamento y su nombre 
--de todos los empleados cuyo salario sea mayor de 300000

select EMP.APELLIDO, EMP.OFICIO, EMP.SALARIO, EMP.DEPT_NO 
,DEPT.DNOMBRE, DEPT.DEPT_NO
from EMP
INNER JOIN DEPT
ON EMP.DEPT_NO=DEPT.DEPT_NO
where EMP.SALARIO >=300000;

--Mostrar todos los nombres de Hospital con sus nombres de salas
--correspondientes.
select * from HOSPITAL;
select * from SALA;
select HOSPITAL.NOMBRE, SALA.NOMBRE
from HOSPITAL
inner join SALA
on HOSPITAL.HOSPITAL_COD=SALA.HOSPiTAL_COD;

Calcular cuántos trabajadores de la empresa hay en cada ciudad.

select DEPT.LOC,EMP.APELLIDO
count(*) as TRABAJADORES, DEPT.LOC, EMP.APELLIDO
from DEPT 
group by LOC, APELLIDO
on DEPT.DEPT_NO=EMP.DEPT_NO

