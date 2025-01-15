/* Write a plsql cursor program to diaplay 5th record from emp table by using %rowcounbt attributes */
DECLARE
CURSOR EmpCursor IS Select * from Emp;
v_Emp Emp%ROWTYPE;
BEGIN
OPEN EmpCursor;
LOOP
FETCH EmpCursor INTO v_Emp;
EXIT WHEN EmpCursor%NOTFOUND;
IF EmpCursor%ROWCOUNT=5 THEN
DBMS_OUTPUT.PUT_LINE(v_Emp.Ename,v_Emp.Job.v_Emp.Sal);
END IF;
END LOOP;
END;
/
