/* cursor with parameter */

DECLARE
Cursor EmpCursor (P_Deptno Number)
IS 
Select * From Emp Where Deptno=P_Deptno;
v_Emp Emp%ROWTYPE;
BEGIN
OPEN EmpCursor(10);
LOOP
FETCH EmpCursor INTO v_Emp;
EXIT WHEN EmpCursor%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(v_Emp.Ename||' '||v_Emp.Job||' '||v_Emp.Sal);
END LOOP;
END;
/
