/* Write a pl/sql parameterized cursor for passing job is as parameters from emp table display the employee working as clerk or 
   analyst and also display output statically based on following format
   Employee working as clerk
	SMIT
	MILLER
	KING
	.
	.
Employee working as analyst
	SCOTT
	FORD
	.
	.
*/

DECLARE
  2  CURSOR EmpCursor(p_job varchar2)
  3  IS
  4  Select *  From Emp
  5  WHERE Job =p_job;
  6  v_Emp Emp%ROWTYPE;
  7  BEGIN
  8  OPEN EmpCursor('CLERK');
  9  DBMS_OUTPUT.PUT_LINE('Employee working as CLERK ..');
 10  LOOP
 11  FETCH EmpCursor INTO v_Emp;
 12  EXIT WHEN EmpCursor%NOTFOUND;
 13  DBMS_OUTPUT.PUT_LINE(v_Emp.Ename|| ' '||v_Emp.Job);
 14  END LOOP;
 15  CLOSE EmpCursor;
 16  OPEN EmpCursor('ANALYST');
 17  DBMS_OUTPUT.PUT_LINE('Employees Working as ANALYST');
 18  LOOP
 19  FETCH EmpCursor INTO v_Emp;
 20  EXIT WHEN EmpCursor%NOTFOUND;
 21  DBMS_OUTPUT.PUT_LINE(v_Emp.Ename||' '||v_Emp.job);
 22  END LOOP;
 23  CLOSE EmpCursor;
 24* END;
SQL> /
