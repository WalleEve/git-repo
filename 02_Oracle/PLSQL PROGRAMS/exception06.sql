-- EXCETION 
e_Empexit EXCEPTION;
v_count NUMBER(2);
v_Salsum number(6);
PRAGMA EXCEPTION_INIT(e_Empexit,-2292);
v_Empno Emp.Empno%TYPE :=&Empno;
BEGIN

