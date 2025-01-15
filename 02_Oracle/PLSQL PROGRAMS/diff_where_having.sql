/* Difference Between HAHING and WHERE clause
  HAVING specifies a search conditon for a GROUP or an AGGREGATE function used in SELECT statement. The WHERE clause specifies the
  criteria which individual records  must meet to be selected by a query. It can be used without the GROUP by clause. The HAVING clause
  cannot be used without the GROUP BY clause.
  . The WHERE clause selects rows before GROUPPING. The HAVING clause selects rows after GROUPPING.
  . The WHERE clause cannot contain aggregate functions. The HAVING clause can contain aggregate function.
*/

sql> SELECT deptno,SUM(saL) FROM emp GROUP BY deptno;

/* output: 
 DEPTNO   SUM(SAL)
---------- ----------
        30       9400
        20      10875
        10       8750
*/

sql> SELECT deptno,SUM(sal) FROM emp WHERE deptno !=10 GROUP BY deptno;

/* output:
 DEPTNO   SUM(SAL)
---------- ----------
        30       9400
        20      10875
*/

sql> SELECT deptno,SUM(sal) FROM emp WHERE deptno !=10 GROUP BY deptno HAVING SUM(sal) <10000;

/* output:
  DEPTNO   SUM(SAL)
---------- ----------
        30       9400
*/

