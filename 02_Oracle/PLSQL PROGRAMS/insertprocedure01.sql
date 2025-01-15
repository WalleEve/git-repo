-- Write a pl/sql stored procedure to insert a record into dept table by using in parameter  
CREATE OR REPLACE PROCEDURE DeptProcedure (P_Deptno IN NUMBER,P_Dname  IN VARCHAR2,P_Loc IN VARCHAR2)
IS 
BEGIN
INSERT INTO dept VALUES(P_Deptno,P_Dname,P_Loc);
DBMS_OUTPUT.PUT_LINE('One new record is inserted ');
END ;
/
