-- The LIKE operator compares a charecter,string or clob value to a pattern and terurns TRUE  if the value matches the pattern and FALSE if it does not.

-- LIKE OPERATOR in Expression

CREATE OR REPLACE PROCEDURE compare (value VARCHAR2, pattern VARCHAR2)
IS
BEGIN
   IF value LIKE pattern THEN
     DBMS_OUTPUT.PUT_LINE('TRUE');
   ELSE
     DBMS_OUTPUT.PUT_LINE('FALSE');
   END IF;
END;

BEGIN
   compare ('Johnson','J%s_n');
   compare ('Johnson','J%S_N');
END;
/
