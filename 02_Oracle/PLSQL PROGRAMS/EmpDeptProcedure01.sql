-- Write a pl/sql stored procedure for passing deptno as in parameter then return number of employees working in that department from emp table by using out parameter.

CREATE OR REPLACE PROCEDURE Emp_dept_procedure (P_Deptno IN NUMBER,P_Ename OUT VARCHAR2,P_Job OUT VARCHAR2,P_Sal OUT NUMBER,P_Count OUT NUMBER)

AS
CURSOR EmpCursor IS
Select Ename,Job,Sal from Emp
Where Deptno=P_Deptno;
v_Emp Emp%ROWTYPE;
BEGIN
OPEN EmpCursor;
LOOP
FETCH EmpCursor INTO P_Ename,P_Job,P_Sal;
EXIT WHEN EmpCursor%NOTFOUND;
DBMS_OUTPUT.PUT_LINE('Name Of the Employee is: '||P_Ename||' Working as: '||P_Job||' Getting Slary: '||P_Sal);
END LOOP;
Select COUNT(1) INTO P_Count FROM emp
Where Deptno=P_Deptno;
DBMS_OUTPUT.PUT_LINE('Total Number of Employees in the department is: '||P_Count);
END;
/

-- EXECUTING THE CURSOR
DECLARE
v_Ename VARCHAR2(10);
v_Job VARCHAR2(10);
v_Sal NUMBER;
v_Count NUMBER;
BEGIN
Emp_dept_procedure (&deptno,v_Ename,v_Job,v_Sal,v_Count);
END;

