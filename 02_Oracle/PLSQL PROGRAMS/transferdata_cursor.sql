/* Using cursor we can also transfer data from one oracle table into another oracle table */
DECLARE
CURSOR EmpCursor IS Select * form Emp ORDER BY SAL &order;
v_Emp Emp%ROWTYPE;
v_id Number;
BEGIN
OPEN EmpCursor;
LOOP
FETCH EmpCursor INTO v_Emp;
EXIT WHEN EmpCursor%ROWCOUNT=&rows;
v_id :=EmpCursor%Rowcount;
INSERT INTO TERGET VALUES (v_id,v_Emp.Ename,v_Emp.Job,v_Emp.Sal);
END LOOP;
CLOSE EmpCursor;
END;
/
