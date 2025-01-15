-- NULL value in Equal Comparison
DECLARE
  a NUMBER :=NULL;
  b NUMBER :=NULL;
BEGIN
  IF (a = b) THEN  -- yields NULL  not true
	DBMS_OUTPUT.PUT_LINE (' a= b '); -- not run
  ELSIF (a != b ) THEN  -- yields NULL , not true
	DBMS_OUTPUT.PUT_LINE(' a != b '); -- not run
  ELSE
	DBMS_OUTPUT.PUT_LINE(' Can''t tell if two NULLs are equal ');
  END IF;
END;
/
