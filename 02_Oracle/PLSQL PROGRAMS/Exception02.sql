--Exception02
DECLARE
v_Emp Emp%ROWTYPE;
v_Sal Emp.Sal%TYPE :=&Sal;
BEGIN
Select * INTO v_Emp From Emp
WHERE Sal=v_Sal;
DBMS_OUTPUT.PUT_LINE(v_Emp.Ename||' '||v_Emp.Job||' '||v_Emp.Sal);
EXCEPTION
WHEN TOO_MANY_ROWS THEN
DBMS_OUTPUT.PUT_LINE('Output of the program is returning more than one row ...');
DBMS_OUTPUT.PUT_LINE('To Get More than one row you have to use cursor..');
END;
/

