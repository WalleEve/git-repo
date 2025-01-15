/* %isopen attribute return boolean value true/false .This attribute returns true when corsor is already open ,it returns false when cursor is not open. */
DECLARE
CURSOR EmpCursor IS Select * from Emp;
v_Emp Emp%ROWTYPE;
BEGIN
IF  NOT EmpCursor%ISOPEN THEN
OPEN EmpCursor;
END IF;
LOOP
FETCh EmpCursor INTO v_Emp;
EXIT WHEN EmpCursor%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(v_Emp.Ename||' '||v_Emp.Sal);
END LOOP;
CLOSE EmpCursor;
END;
 
