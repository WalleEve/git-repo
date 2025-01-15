-- Write a pl/sql program to transfer all employees name from emp table into index by table and also display content from index by table
DECLARE
TYPE tablet1 TABLE OF VARCHAR2(10) INDEX BY BINARY_INTEGER;
v_tablet1 tablet1;
CURSOR empcursor IS SELECT ename FROM emp;
m NUMBER(10) :=1;
BEGIN
OPEN empcursor;
LOOP
 FETCH empcursor INTO v_tablet1(m);
 EXIT WHEN empcursor%NOTFOUND;
 m :=m+1;
END LOOP;
CLOSE empcursor;
FOR i IN v_tablet1_FIRST..v_tablet1_LAST
LOOP
DBMS_OUTPUT.PUT_LINE(v_tablet1(i));
END LOOP;
END;
/


-- test

SQL>

  1  DECLARE
  2     TYPE ename_table IS  TABLE OF VARCHAR2(20) INDEX BY BINARY_INTEGER;
  3     v_ename_table ename_table;
  4     CURSOR empcursor IS SELECT ename FROM emp;
  5     v_num NUMBER(10) :=1;
  6     v_count NUMBER;
  7  BEGIN
  8     OPEN empcursor;
  9     LOOP
 10       FETCH empcursor INTO v_ename_table(v_num);
 11       EXIT WHEN empcursor%NOTFOUND;
 12       v_count :=empcursor%ROWCOUNT;
 13       v_num :=v_num+1;
 14     END LOOP;
 15     FOR i IN 1..v_count
 16       LOOP
 17         DBMS_OUTPUT.PUT_LINE(v_ename_table(i));
 18       END LOOP;
 19* END;



-- Output: 
SQL> /
SMITH
ALLEN
WARD
JONES
MARTIN
BLAKE
CLARK
SCOTT
KING
TURNER
ADAMS
JAMES
FORD
MILLER

PL/SQL procedure successfully completed.

