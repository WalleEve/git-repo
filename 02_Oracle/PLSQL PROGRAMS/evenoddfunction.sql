-- Write a pl/sql stored function for passing no as parameter then return a message either even or odd nased on passed number..
CREATE OR REPLACE FUNCTION evenoddfunction (F_num1 NUMBER)
RETURN VARCHAR2
IS
BEGIN
IF MOD(F_num1,2)=0 THEN
RETURN 'EVEN';
else 
RETURN 'ODD';
END IF
END;
/

-- Execution function using select statement
sql> Select evenoddfunction(12) FROM dual;

-- Execution function using annonymous block
DECLARE
v_result varchar2(10);
BEGIN
v_result :=evenoddfunction(&num1);
DBMS_OUTPUT.PUT_LINE(v_result);
END;
/

