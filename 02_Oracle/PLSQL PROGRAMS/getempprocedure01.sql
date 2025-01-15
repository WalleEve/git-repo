-- Write a pl/sql stored procedure for passing employee name as in parameter then retten of the employee from emp table using out parameter.

CREATE OR REPLACE PROCEDURE getempprocedure (P_Empno IN NUMBER,P_Ename OUT VARCHAR2,P_Sal OUT VARCHAR2)
IS
BEGIN
SELECT Ename,Sal INTO P_Ename,P_Sal From Emp
Where Empno=P_Empno;
END;
/


DECLARE
v_Ename varcahr2(10);
v_Sal number;
BEGIN
getempprocedure(7839,v_Ename,v_Sal);
DBMS_OUTPUT.PUT_LINE(v_Ename||' '||v_Sal);
END;
/
