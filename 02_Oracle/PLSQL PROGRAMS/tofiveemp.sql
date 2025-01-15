--CURSOR TO Get the top five paid employee in the organization
-- Using Simple LOOP
DECLARE
CURSOR EmpCursor IS
SELECT Ename,Job,Sal FROM Emp ORDER BY Sal DESC;
v_Ename VARCHAR2(10);
v_Job VARCHAR2(10);
v_Sal NUMBER(10);
BEGIN
OPEN EmpCursor;
LOOP
FETCH EmpCursor INTO v_Ename,v_Job,v_Sal;
EXIT WHEN EmpCursor%ROWCOUNT=6;
DBMS_OUTPUT.PUT_LINE(v_Ename||' '||v_Job||' '||v_Sal);
END LOOP;
CLOSE EmpCursor;
END;
/

-- Using FOR LOOP 
DECLARE
CURSOR EmpCursor IS
SELECT Ename,Job,Sal FROM Emp ORDER BY Sal DESC;
v_Ename VARChAR2(10);
v_Job VARCHAR2(10);
v_Sal NUMBER(10);
BEGIN
OPEN EmpCursor;
FOR i IN 1..5
LOOP
FETCH EmpCursor INTO v_Ename,v_Job,v_Sal;
EXIT WHEN EmpCursor%NOTFOUNT ;
DBMS_OUTPUT.PUT_LINE(v_Ename||' '||v_Job||' '||v_Sal);
END LOOP; 
CLOSE EmpCursor;
END;
