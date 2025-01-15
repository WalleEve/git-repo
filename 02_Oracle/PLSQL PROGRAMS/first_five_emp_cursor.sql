/* Write a plsql program which is used to dispaly 1st five highest salary employee's from emp table by using %rowcount attribute. */ 
DECLARE
CURSOR Emp5Cursor IS Select Ename,Sal From Emp ORDER BY Sal DESC;
v_Ename Emp.Ename%type;
v_Sal Emp.Sal%type;
BEGIN
OPEN Emp5Cursor;
LOOP
FETCH Emp5Cursor INTO v_Ename,V_Sal;
DBMS_OUTPUT.PUT_LINE(v_Ename||' '||v_Sal);
Exit WHEN Emp5Cursor%ROWCOUNT >=5;
END LOOP;
CLOSE Emp5Cursor;
END;
/
