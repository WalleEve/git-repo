--# LAG and LEAD Analytic Functions 
/* 
The ALG and LEAD analytical functions were introduced in 8.1.6 to give access to multiple rows
within a table, wothout the need for a self-join.
*/

--# Setup 

-- DROP TABLE EMP PURGE; 

CREATE TABLE EMP (
empno   NUMBER(4) CONSTRAINT pk_emp PRIMARY KEY,
ename   VARCHAR2(10),
job     VARCHAR2(9),
mgr     NUMBER(4),
hiredate    DATE,
sal     NUMBER(7, 2),
comm    NUMBER(7, 2),
deptno  NUMBER(2)
);


INSERT INTO emp VALUES (7369,'SMITH','CLERK',7902,to_date('17-12-1980','dd-mm-yyyy'),800,NULL,20);
INSERT INTO emp VALUES (7499,'ALLEN','SALESMAN',7698,to_date('20-2-1981','dd-mm-yyyy'),1600,300,30);
INSERT INTO emp VALUES (7521,'WARD','SALESMAN',7698,to_date('22-2-1981','dd-mm-yyyy'),1250,500,30);
INSERT INTO emp VALUES (7566,'JONES','MANAGER',7839,to_date('2-4-1981','dd-mm-yyyy'),2975,NULL,20);
INSERT INTO emp VALUES (7654,'MARTIN','SALESMAN',7698,to_date('28-9-1981','dd-mm-yyyy'),1250,1400,30);
INSERT INTO emp VALUES (7698,'BLAKE','MANAGER',7839,to_date('1-5-1981','dd-mm-yyyy'),2850,NULL,30);
INSERT INTO emp VALUES (7782,'CLARK','MANAGER',7839,to_date('9-6-1981','dd-mm-yyyy'),2450,NULL,10);
INSERT INTO emp VALUES (7788,'SCOTT','ANALYST',7566,to_date('13-JUL-87','dd-mm-rr')-85,3000,NULL,20);
INSERT INTO emp VALUES (7839,'KING','PRESIDENT',NULL,to_date('17-11-1981','dd-mm-yyyy'),5000,NULL,10);
INSERT INTO emp VALUES (7844,'TURNER','SALESMAN',7698,to_date('8-9-1981','dd-mm-yyyy'),1500,0,30);
INSERT INTO emp VALUES (7876,'ADAMS','CLERK',7788,to_date('13-JUL-87', 'dd-mm-rr')-51,1100,NULL,20);
INSERT INTO emp VALUES (7900,'JAMES','CLERK',7698,to_date('3-12-1981','dd-mm-yyyy'),950,NULL,30);
INSERT INTO emp VALUES (7902,'FORD','ANALYST',7566,to_date('3-12-1981','dd-mm-yyyy'),3000,NULL,20);
INSERT INTO emp VALUES (7934,'MILLER','CLERK',7782,to_date('23-1-1982','dd-mm-yyyy'),1300,NULL,10);
COMMIT;

--# LAG 
/*
The LAG function is used to access data from a previous row. The following query returns the salary
from the previous row to calculate the difference between the salary of the current row and that of the 
previous row. Notice that the ORDER BY of the LAG function is used to order the data by salary.

*/

SELECT empno,
    ename,
    job, 
    sal,
    LAG(sal, 1, 0) OVER (ORDER BY sal) as sal_prev,
    sal - LAG(sal, 1, 0) OVER (ORDER BY sal) as sal_diff
FROM emp;



SELECT deptno,
    empno,
    ename,
    job,
    sal,
    LAG(sal, 1, 0) OVER (PARTITION BY deptno ORDER BY sal) as sal_prev
FROM emp;

--# LEAD 
/*
The LEAD function is used to return data from rows further down the result set. The following query
returns the salary from the next row to calculate the difference between the salary of the current row
and the following row.
*/

SELECT empno,
    ename,
    job,
    sal,
    LEAD(sal, 1, 0) OVER (ORDER BY sal) as sal_next,
    LEAD(sal, 1, 0) OVER (ORDER BY sal) -  sal as sal_diff
FROM emp;


SELECT deptno,
    empno,
    ename,
    job,
    sal,
    LEAD(sal, 1, 0) OVER (PARTITION BY deptno ORDER BY sal) AS sal_next 
FROM emp;






