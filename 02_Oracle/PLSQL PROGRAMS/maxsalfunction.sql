-- Create a function for retivr max of sal from emp table
CREATE OR REPLACE FUNCTION maxsalfunction
RETURN NUMBER
IS
v_maxsal NUMBER(10);
BEGIN
SELECT MAX(sal) INTO v_maxsal FROM emp;
RETURN v_maxsal;
END;

--Featching the return value of the function by select statement
sql> SELECT maxsalfunction FROM dual;





