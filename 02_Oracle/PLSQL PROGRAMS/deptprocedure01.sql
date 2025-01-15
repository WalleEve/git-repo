--Write a pl/sql stored procedure for passing deptno as inparameter then return dname,loc from dept table by using out parameter.
CREATE OR REPLACE PROCEDURE DeptProcedure(P_Deptno IN NUMBER,P_Dname OUT VARCHAR2,P_Loc OUT VARCHAR2)
IS
BEGIN
SELECT dname,loc INTO P_Dname,P_LOC FROM DEPT 
WHERE Deptno=P_Deptno;
END;
/

-- Execute the procedure by using bind variable
sql> VARIABLE b_Dname VARCHAR2(10);
sql> VARIABLE b_Loc VARCHAR2(10);
sql> EXEC DeptProcedure(10,b_Dname,b_Loc);
sql> PRINT b_Dname,b_Loc;

-- Execute the procedure by anonymous block
DECLARE
v_Dname VARCHAR2(10);
v_Loc VARCHAR2(10);
BEGIN
DeptProcedure(&Deptno,v_Dname,v_Loc);
DBMS_OUTPUT.PUT_LINE('Name Of the Department is: '||v_Dname||' '||' And Located at: '||v_Loc);
END;
/

