-- passes the variable now_sal to the procedure adjust_salary. The procedure assigns a value to the corresponding formal parameter ,sal.Because sal is an IN OUT parameter,the variable new_sal retains the assigned value after the procedure finishes running

CREATE PROCEDURE adjust_salary (
  empno NUMBER,
  sal IN OUT NUMBER,
  adjustment NUMBER
  )
IS
emp_salary NUMBER(8,2);
BEGIN
sal := sal + adjustment;
END;

BEGIN
  SELECT sal  INTO emp_salary 
  FROM emp
  WHERE empno = 7839;
  
  DBMS_OUTPUT.PUT_LINE (' Before invoking procedure emp_salary: '||emp_salary);
  adjust_salary (7839,emp_salary,1000);
  DBMS_OUTPUT.PUT_LINE(' After invoking procedure , emp_salary: '||emp_salary);
END;
/

-- Creating procedure in SQL 
SQL> ed
Wrote file afiedt.buf

  1  CREATE PROCEDURE adjust_salary (
  2  empno NUMBER,
  3  sal IN OUT NUMBER,
  4  adjustment NUMBER
  5  )
  6  IS
  7  emp_salary NUMBER(8,2);
  8  BEGIN
  9  sal :=sal+adjustment;
 10* END;
 11  /

Procedure created.


-- PL/SQl Block for featching the above procedure by using emp table..

SQL> ed
Wrote file afiedt.buf

  1  DECLARE
  2  v_empno NUMBER :=&empno;
  3  emp_salary NUMBER(8,2);
  4  BEGIN
  5  SELECT sal INTO emp_salary
  6  FROM emp
  7  WHERE empno=v_empno;
  8  DBMS_OUTPUT.PUT_LINE('Before Invoking procedure emp_salary: '||emp_salary);
  --calling procedure with actual parameter // here emp_salary goes to procedure block and process as sal parameter 
  9  adjust_salary (v_empno,emp_salary,0.50*emp_salary); 

 10  DBMS_OUTPUT.PUT_LINE('After Invoking procedure emp_salary: '||emp_salary);
 11* END;
SQL> /
Enter value for empno: 7839 
Before Invoking procedure emp_salary: 5000
After Invoking procedure emp_salary: 7500

PL/SQL procedure successfully completed.

