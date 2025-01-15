-- Write a pl/sql stored procedure for passinfg emp no as a parameter from emp table and display name of the employee and his salary
CREATE OR REPLACE PROCEDURE EmpPro(P_Empno number)
AS
v_Ename VARCHAR2(10);
v_Sal NUMBER(10);
BEGIN
SELECT ENAME,SAL INTO v_Ename,v_Sal From Emp
Where Empno=P_Empno;
DBMS_OUTPUT.PUT_LINE(v_Ename||' '||v_Sal);
END;
/

