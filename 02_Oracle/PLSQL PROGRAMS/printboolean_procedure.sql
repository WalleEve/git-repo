-- Procedure Prints BOOLEAN variable
CREATE OR REPLACE PROCEDURE print_boolean  (b_name VARCHAR2,b_value BOOLEAN)
IS
BEGIN
  IF b_values IS NULL THEN
    DBMS_OUTPUT.PUT_LINE(b_name||' =NULL ');
  ELSIF b_values=TRUE  THEN
    DBMS_OUTPUT.PUT_LINE(b_name||' =TRUE ');
  ELSE 
    DBMS_OUTPUT.PUT_LINE(b_name||' =FALSE ');
  END IF;
END;
/
 
