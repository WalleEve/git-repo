-- Procedure with out mode parameter 
CREATE OR REPLACE PROCEDURE inoutprocedure01 (a IN INT,b OUT INT)
IS
BEGIN
b :=a*a;
END;
/

DECLARE
result number;
BEGIN
inoutprocedure (5,result);
DBMS_OUTPUT.PUT_LINE(result);
END;
/
