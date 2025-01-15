/* Write a pl/sql cursor program to display all employee name and their salary from Emp table by using cursor for loop */
DECLARE
cursor EmpCursor IS Select * from Emp;
v_Emp EmpCursor%Rowtype;
BEGIn
FOR v_Emp IN EmpCursor
LOOP
DBMS_OUTPUT.PUT_LINE(v_Emp.Ename||' '||v_Emp.Sal);
END LOOP;
END;
/
