-- Write a pl/sql stored function for passing employee number as a parameter from emp table then delete that record and also return deleted no of records number.

CREATE OR REPLACE FUNCTION deletefunction(f_Empno NUMBER)
RETURN NUMBER
IS 
v_count number(10);
BEGIN
DELETE * From Emp Where Empno=f_Empno;
v_count :=SQL%ROWCOUNT;
RETURN v_count;
END;
/

-- Execution of deletefunction
DECLARE
v_count number(10);
BEGIN
v_count :=deletefunction(&empno);
DBMS_OUTPUT.PUT_LINE(v_count);
END;
