/* write a plsql cursor program to dispaly all the employee's and their salary from the emp table by using %found attribute */
DECLARE

CURSOR EmpCursor IS Select * From Emp;
v_Emp Emp%ROWTYPE;
BEGIN
OPEN EmpCursor;
Fetch EmpCursor INTO v_Emp;
While (EmpCursor%Found) 
LOOP
DBMS_OUTPUT.PUT_LINE(v_Emp.Ename||' '||v_Emp.Sal);
FETCH EmpCursor INTO v_Emp;
END LOOP;
Close EmpCursor;
END;
/
