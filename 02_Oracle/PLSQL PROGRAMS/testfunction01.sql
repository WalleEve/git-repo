-- Funcion
CREATE OR REPLACE FUNCTION testfunction01 (a varchar2)
RETURN VARCHAR2
IS
BEGIN
RETURN a;
END;
/

-- Function Execution
--using select statemnt
sql> Select testfunction01('Sabeeha') From Dual;

-- unsig annonymous block
DECLARE
z varchar2(10);
BEGIN
z :=testFunction01('Hi Sabeeha');
DBMS_OUTPUT.PUT_LINE(z);
END;
/
