-- Write a pl/sql stored function for passing department number as in parameter from the dept table and then return dname,location from the dept table by using out parameters.

CREATE OR REPLACE FUNCTION deptfunction01 (f_deptno NUMBER,f_dname OUT VARCHAR2,f_loc OUT VARCHAR2)
RETURN VARCHAR2
IS
BEGIN
Select Dname,Loc INTO f_dname,f_loc From Dept Where Deptno=f_Deptno;
RETURN f_dname;
END;
/

--executing the deptfunction using annonymous block
DECLARE
v_Dname varchar2(10);
v_loc varchar2(10);
v_det varchar2(10);
BEGIN
v_dept :=deptfunction01(&Deptno,v_dname,v_loc);
DBMS_OUTPUT.PUT_LINE(v_Dname||' '||v_loc);
END;

-- or
sql> VERIABLE v_Dname varchar2(10);
sql> VARIABLE v_Loc varchar2(10);
sql> VARIABLE v_Dept varchar2(10);
BEGIN
:v_Dept  :=deptfunction01 (&Deptno,:v_Dname,:v_Loc);
END;

sql> PRINT v_Dname,v_Loc;
