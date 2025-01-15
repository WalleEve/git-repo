-- Procedure

CREATE OR REPLACE PROCEDURE mybonusProcedure 
IS
CURSOR DeptCursor IS Select Deptno From Dept;
BEGIN
FOR r_groupbonus IN DeptCursor 
LOOP
UPDATE Emp
SET Sal=Sal*0.5 
WHERE Deptno=r_groupbonus.Deptno;
DBMS_OUTPUT.PUT_LINE('The bonus information is '||r_groupbonus.deptno);
END LOOP;
END mybonusProcedure;
/
