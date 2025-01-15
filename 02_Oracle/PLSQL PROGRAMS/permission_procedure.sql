-- Granting  EXECUTING permission on PROCEURE to other users
CREATE OR REPLACE PROCEDURE EmpProcedure(P_Empno NUMBER)
AUTHID current_user
IS
v_Ename VARCHAR2(10);
v_Sal NUMBER(10);
BEGIN
SELECT Ename,Sal INTO v_Ename,v_Sal From Emp
WHERE Empno=P_Empno;
EXCEPTION
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE('Please Check The Employee number..');
END;
/


-- granting EXECUTE permission  to scott user
sql> GRANT EXECUTE ON EmpCursor TO SCOTT;
