/* Write a  pl/sql program to display 5th record fro Emp table by using cursor for loop */
DECLARE
cursor EmpCursor IS Select * from Emp;
/*v_Emp EmpCursor%ROWTYPE;*/
BEGIN
FOR v_Emp IN EmpCursor
LOOP
IF EmpCursor%ROWCOUNT=5 THEN 
DBMS_OUTPUT.PUT_LINE(v_Emp.Ename|| ' '||v_Emp.Job);
END IF;
END LOOP;
END;
/

 
