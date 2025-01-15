/* %FOUND AND %NOTFOUND return the boolean value either true or false */
DECLARE
v_Empno number :=&Empno;
CURSOR EmpCursor IS Select * From Emp
Where Empno=v_Empno;
v_Emp Emp%ROWTYPE;
BEGIN
OPEN EmpCursor;
FETCH EmpCursor INTO v_Emp;
IF EmpCursor%FOUND THEN
DBMS_OUTPUT.PUT_LINE(' Hi You are looking for the Employee '||v_Emp.Empno||'''s Details ... ');
DBMS_OUTPUT.PUT_LINE(' Name of the employee is '||v_Emp.Ename);
DBMS_OUTPUT.PUT_LINE(' And Working As '||v_Emp.Job);
DBMS_OUTPUT.PUT_LINE(' Getting salary '||v_Emp.Sal);
ELSIF EmpCursor%NOTFOUND THEN
DBMS_OUTPUT.PUT_LINE('Please Check The Employee number!');
DBMS_oUTPUT.PUT_lINE(v_Empno||' is not available in database.');
END IF;
CLOSE EmpCursor;
END;
/

