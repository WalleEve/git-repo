--procedure ex1
CREATE OR REPLACE PROCEDURE GetEnameSalJob (p_Empno IN Emp.Empno%TYPE)
AS
v_Ename Emp.Ename%TYPE;
v_Job Emp.Job%TYPE;
v_Sal Emp.Sal%TYPE;
BEGIN
Select Ename,Job,Sal INTO v_Ename,v_Job,v_Sal From Emp
Where Empno=v_Empno;
DBMS_OUTPUT.PUT_LINE('The Details of employee: '||v_Empno);
DBMS_OUTPUT.PUT_LINE('The name of the given employee number is: '||v_Ename);
DBMS_OUTPUT.PUT_LINE('The job of the employee is: '||v_job);
DBMS_OUTPUT.PUT_LINE('The salary of the employee is: '||v_Sal);
END GetEnmaeSalJob;
/

--procedure ex2
CREATE OR REPLACE PROCEDURE EmpInsert
(
p_Empno Emp.Empno%TYPE,
p_Ename Emp.Ename%TYPE,
p_Sal Emp.Sal%TYPE;
p_Deptno Emp.Deptno%TYPE;
p_Job Emp.Job%TYPE;
p_Comm Emp.Comm%TYPE;
p_Hiredate Emp.Hiredate%TYPE,
p_Mgr Emp.Mgr%TYPE
)
AS
BEGIN
INSERT INTO Emp (Empno,Ename,Sal,Deptno,Job,Comm,Hiredate,Mgr) 
VALUES (p_Empno,p_Ename,p_Sal,p_Deptno,p_Job,p_Comm,p_Hiredate,p_Mgr);
COMMIT;
EXCEPTION
WHEN DUP_VALUE_ON_INDEX THEN
RAISE _APPLICATION_ERROR(-20001,'Employee already exit');
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE('-20011',SQLERRM);
END EmpInsert;
/

--Calling the above procedure..
sql> EXECUTE EmpInsert(1241,'SAYED',5000,40,ANALYST,NULL,SYSDATE,7839);
