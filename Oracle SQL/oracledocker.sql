--- COMENTARIOS
/*
    varias lineas
    PODEMOS TENER TODAS LAS CONSULTAS QUE DESEEMOS
    NO ES NECESARIO BORRARLAS
    EN EL EDITOR INDICAREMOS QUE CONSULTA, LINEA O SELECCION 
    QUEREMOS EJECUTAR
    PARA EJECUTAR CTRL+ ENTER EN WINDOWS ALT + ENTER
    NO HAY DIFERENCIA MAYUSCULAS DE MINISCULAS EN LAS CONSULTAS
    LAS CONSULTAS FINALIZAN CON ;

*/
select * from EMP;
select * from DEPT;
select DEPT_NO, DNOMBRE, LOC from DEPT;

--ORDENAR REGISTROS order by columna
select * from EMP ORDER BY APELLIDO desc;
--FILTRADO DE REGISTROS
-- PARA FILTRAR UTILIZAMOS LA PALABRA where
OPERADORES DE COMPARACION
> MAYOR
>= MAYOR O IGUAL
< MENOR
<= MENOR O IGUAL
=IGUAL
<> DISTINTO
TODO LO QUE NO SEA UN NUMERO SE ESCRIBE ENTRE COMILLLAS SIMPLES PARA LA COMPRACIÓN
ORACLE DIFERENCIA MAYUSCULAS DE MINUSCULAS EN LOS STRING
/*
select * from EMP where DEPT_NO=10;
-- mostrar todos los empleados cuyo oficioo dsea director
select * from EMP where OFICIO='DIRECTOR';
select * from EMP where OFICIO='director';
/*
OPERADORES RELACIONABLES
PERMITEN PREGUNTAR POR MAS DE UN FILTRO EN UNA MISMA CONSULTA
and TODAS LAS CONDICIONES DEBEN CUMPLIRSE
or MUESTRA DATOS DE CADA CONDICION
not PROHIBIDO , NO LO DEBEMOS UTILIZAR, NIEGA UNA CONDICION
*/
--mostrar todos los empleados del departamento 10 y 20
select *from EMP where DEPT_NO=10 and DEPT_NO=20;
--mostrar todos los empleados cuyo EMP_NO este entre 7800 y 7900;
select * from EMP where EMP_NO>=7800 and EMP_NO<= 7900;
--Mostrar todo los empleados que NO sean vendedores
select * from EMP where not OFICIO= 'VENDEDOR';
select * from EMP where OFICIO<> 'VENDEDOR';

--EXISTEN OTROS TIPO DE OPERADORES PARA FILTRAR
--OPERADOR BETWEEN: BUSCA ENTRE UN RANGO Y DEVUELVE LOS VALORES 
--INCLUSIVE DLE RANGO
--Mostar los empleados cuyo salaro este enre 318000 y 399999
select * from EMP where SALARIO between 318000 and 390000
select * from emp where SALARIO >= 318000 and SALARIO <=390000;
__OPERADOR IN
BUSCA EN UN MISMO CAMPO MULTIPLES VALORES DE IGUALDAD
--Mostrar todos los empleados del departamento 10 y 20
-- CAMPO IN (VALOR1, VALOR2, VALOR3)
select * from EMP where DEPT_NO=10 or DEPT_NO=20 or DEPT_NO=30
DEPT_NO=55 or DEPT_NO=66 or DEPT_NO=88;
select * from EMP where DEPT_NO= in (10, 20,30, 55,66,88);
OPERADOR NOT IN
--Muestra los contrarios al operador IN
-- Mostar todos los empleados que no esten en el departamento 10 ni el 20
select * from EMP where DEPT_NO NOT in (10,20);
--OPERADOR LIKE
SE UTILIZA PARA BUSCAR COINCIDENCIAS EN TEXTOS (STRING, VARCHAR)
__ BUSCADORES
__UTILIZA UNA SERIE DE CARACTERES ESPECIALES(SOLO SIRVE UNO)
--? busca un digito en el texto
-- _representa un caracter cualquiera
--%busca cualquier caracter y cualquier longitud
-- Mostrar todos los empleados cuyo apellido commience por la letra S
select * from EMP where apellido like 's';
select * from EMP where apellido like 's%';
-- Mostrar todos los empleados cuyo apellido commience por la letra S y finalice con S
select * from EMP where apellido like 's%a';
--Mostar todos los empleados cuyo apellido sea de 4 letras
select * from EMP where apellido like '____';
--CLAUSULA DISTINCT
--NOS PERMITE QUITAR REPETIDOS DE UNA CONSULTA select
--en realidad , se utiliza con poco campos
-- Mostrar los oficios de los empleados
select distinct OFICIO from EMP;
--campos calculados
--Un campo calculado es una columna que no existe en una tabla 
--pero se genera a partir de otra columna
--OPERADORES MATEMATICOS : *,+;/,-
--TODO CAMPO CALCULADO DEBE TENER UN ALIAS SIEMPRE
--LOS ALIAS SIN ESPACIOS
--Mostrar el apellido y el salario total (salario+comision) de todos los empleados.
select APELLIDO,(SALARIO+ COMISION) as TOTAL from EMP;
-- los campos calculados no se pueden filtrar con where
-- un where solamente se utiliza para filtrar datos de la tabla
-- si deseamos filtrar sobre un campo calculado, debemos hacerlo 
--con el mismo calculo
select APELLIDO, (SALARIO *COMISION) as TOTAL FROM EMP where TOTAL >=;
select APELLIDO, (SALARIO *COMISION) as TOTAL FROM EMP order by TOTAL asc;






