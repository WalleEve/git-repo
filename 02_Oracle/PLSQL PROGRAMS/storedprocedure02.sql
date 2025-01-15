-- Write a pl/sql stored procedure for passing deptno as a parameter from emp table then display employee details from emp table based passed deptno

CREATE OR REPLACE PROCEDURE DeptnoProcedure(P_Deptno Number)
AS
CURSOR EmpCursor IS Select * from Emp
Where Deptno=P_Deptno;
v_Emp Emp%ROWTYPE;

BEGIN
OPEN EmpCursor;
LOOP
FETCH EmpCursor INTO V_Emp;
EXIT WHEN EmpCursor%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(v_Emp.Ename|| ' '||v_Emp.Sal);
END LOOP;
CLOSE EmpCursor;
END;
/
