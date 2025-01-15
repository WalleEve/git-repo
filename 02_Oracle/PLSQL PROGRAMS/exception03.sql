-- Exception03
DECLARE
v_Empno VARCHAR2(4) :='&Empno';
v_Ename VARCHAR2(10) :='&Ename';
v_Deptno VARCHAR2(2) :='&Deptno';
BEGIN
INSERT INTO Emp(Empno,Ename,Deptno) VALUES (v_Empno,v_Ename,v_job) ;
EXCEPTION
WHEN INVALID_NUMBER THEN
DBMS_OUTPUT.PUT_LINE('Given Empno or Deptno Is INVALID Please Check..');
END;
/
