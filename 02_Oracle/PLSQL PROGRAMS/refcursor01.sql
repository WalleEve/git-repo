/ *ref cursor*/
DECLARE
TYPE EmpRefCursor IS REF CURSOR;
v_Emprefcursor EmpRefCursor;
v_Emp Emp%ROWTYPE;
BEGIN
OPEN v_Emprefcursor FOR 
Select * from Emp;
LOOP
FETCH v_Emprefcursor INTO v_Emp;
EXIT WHEN v_Emprefcursor%NOTFOUND;
DBMS_OUTPUT.PUT_LINE('Employee Number '||TO_CHAR(v_Emprefcursor%ROWCOUNT,'09')||' : '||v_Emp.Ename);
END LOOP;
CLOSE v_Emprefcursor;
END;
/
