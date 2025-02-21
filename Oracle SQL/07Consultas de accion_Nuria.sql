--Dar de alta con fecha actual al empleado José Escriche Barrera
--como programador perteneciente al departamento de producción.
--Tendrá un salario base de 70000 pts/mes y no cobrará comisión. 
select * from EMP;
insert into EMP (EMP_NO,APELLIDO, DEPT_NO,SALARIO, COMISION) 
values 
((select MAX(EMP_NO) + 1 from EMP),'Escriche Barrera',40, 70000,0);

--Se quiere dar de alta un departamento de informática situado en 
--Fuenlabrada (Madrid).
select * from DEPT;
insert into DEPT (DEPT_NO, DNOMBRE,LOC)
values
((select MAX(dept_NO) + 10 from dept), 'INFORMATICA','FUENLABRADA');
--CUANDO ES SOLO UN DATO LO QUE BORRASA = PERO CUANDO ES MAS DE UNO IN
DELETE FROM DEPT WHERE DEPT_NO IN (51,61);
insert into DEPT (DEPT_NO, DNOMBRE,LOC)
values
((select MAX(dept_NO) + 10 from dept), 'INFORMATICA','FUENLABRADA');
--El departamento de ventas, por motivos peseteros, se traslada a Teruel, 
--realizar dicha modificación.
update DEPT set LOC='TERUEL'
--actualiza las tabla dept en la columna loc y pon teruel
WHERE LOC='BARCELONA'
--donde pone barcelona
--En el departamento anterior (ventas), se dan de alta dos empleados: 
--Julián Romeral y Luis Alonso.  Su salario base es el menor que cobre un
--empleado, y cobrarán una comisión del 15% de dicho salario.
select * from EMP;
insert into EMP (EMP_NO,APELLIDO, DEPT_NO,SALARIO, COMISION) 
values 
((select MAX(EMP_NO) + 1 from EMP),'Luis Alonso',30, 70000,0);




