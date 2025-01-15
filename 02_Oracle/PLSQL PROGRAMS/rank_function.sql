/* RANK () FUNCTION
In Oracle PL/SQL, RANK() function is abuilt in analytic function which is used to rank a record within a group of rows.
Its return type is number and serves for both aggredate and analytic purpose in SQL.

used as an Aggregate function:
RANK (expression) WITHIN GROUP (ORDER BY expression [ASC | DESC ] NULLS [FIRST | LAST ] )

used as an Analytic function:
RANK () OVER ( PARTITION BY Expression ORDER BY expression)
*/
// The SQl query demonstrates analytic behaviour or RANK() function. It ranks the slary of the employees working in the same department

sql> SELECT deptno,empno,ename,RANK() OVER (PARTITION BY deptno ORDER BY sal DESC) rank FROM emp;

sql> Select E.Ename,E.Job,E.Sal,R.rank From Emp E ,(Select empno, DENSE_RANK() OVER (ORDER BY Sal DESC) rank From Emp) R
     WHERE E.Empno=R.Empno AND R.rank =3


//Aggregate Example 
// The following example calculates the rank of a hypothetical employee in the sample table employees with a salary of $15500 and commission of 5%:

sql> SELECT RANK(15500,.05) WITHIN GROUP (ORDER BY salary ,Commission_pct) RANK FROM employees;
sql> SELECT RANK (15000) WITHIN GROUP (ORDER BY sal DESC) rank  FROM employees;



