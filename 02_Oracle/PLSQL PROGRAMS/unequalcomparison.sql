-- NULL value in unequal comparison
DECLARE
  x NUMBER :=5;
  y NUMBER :=NULL;
BEGIN
  IF x != y THEN -- yields NULL Not TRUE
    DBMS_OUTPUT.PUT_LINE('x != y'); -- not run
  ELSIF x=y THEN -- also yields NULL
    DBMS_OUTPUT.PUT_LINE('x=y');
  ELSE
    DBMS_OUTPUT.PUT_LINE(' Can''t tell if x and y are equal or not. ');
  END IF;
END;
/

Output:
Can't tell if x and y are equal or not.
