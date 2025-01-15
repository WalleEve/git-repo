-- EXCEPTION01 

DECLARE
v_Empno Emp.Empno%TYPE :=&Empno;
v_Ename Emp.Ename%TYPE;
v_Job Emp.Job%TYPE;
v_Sal Emp.Sal%TYPE;
BEGIN
SELECT Ename,Job,Sal INTO v_Ename,v_Job,v_Sal FROM emp WHERE Empno=v_Empno;
DBMS_OUTPUT.PUT_LINE('Name of the employee is '||v_Ename ||' working as '||v_Job||' Getting salary '||v_Sal);
EXCEPTION
WHEN NO_DATA_FOUND THEN
DBMS_OUTPUT.PUT_LINE('Please Check The Employee Number...!');
END;
/
