/* %rowcout always returns number of records fetched from the cursor */
DECLARE
CURSOR EmpCursor IS Select Ename,Sal From Emp;
v_Ename Emp.Ename%type;
v_Sal Emp.Sal%type;
BEGIN
OPEN EmpCursor;
LOOP
FETCH EmpCursor INTO v_Ename,v_Sal;
EXIT WHEN EmpCursor%NOTFOUND;
END LOOP;
DBMS_OUTPUT.PUT_LINE('The Total number of records fetched from the Cursor is: '||EmpCursor%rowcount);
CLOSE EmpCursor;
END;


 
