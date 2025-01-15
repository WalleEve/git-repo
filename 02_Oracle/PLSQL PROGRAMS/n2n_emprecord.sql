-- Program to get the nth number of rows for emp table 

DECLARE
v_Emp Emp%ROWTYPE;
v_count NUMBER :=&rows_number;

CURSOR EmpCursor IS Select Ename,Sal From Emp ;

BEGIN
FOR v_Emp IN EmpCursor
LOOP
DBMS_OUTPUT.PUT_LINE(v_Emp.Ename||' '||v_Emp.Sal);
EXIT WHEN EmpCursor%ROWCOUNT =v_count;
END LOOP;
END;


-- Program to get n to n number of records from emp table.

DECLARE
CURSOR EmpCursor IS Select * from Emp;
v_Emp Emp%ROWTYPE;
v_range1  NUMBER :=&range_from;
v_range2 NUMBER :=&range_to;
BEGIN
FOR v_Emp IN EmpCursor
LOOP
IF EmpCursor%ROWCOUNT=v_range1 THEN
DBMS_OUTPUT.PUT_LINE(v_Emp.Ename);
v_range1 :=v_range1+1;
EXIT When EmpCursor%ROWCOUNT=v_range2;
END IF;
END LOOP;
END;



