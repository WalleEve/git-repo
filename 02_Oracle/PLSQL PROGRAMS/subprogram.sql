--  and subprogram with same name inthe same scope

CREATE PROCEDURE echo AS
x NUMBER :=0;
BEGIN
	DECLARE
	
	x NUMBER :=5;
	BEGIN
	DBMS_OUTPUT.PUT_LINE('x = '||x);
	DBMS_OUPTUT.PUT_LINE('echo.x = '||echo.x);
	END;
END;

BEGIN
echo;
END;



 CREATE PROCEDURE echo1
  2  IS
  3  x NUMBER :=5;
  4  BEGIN
  5     DECLARE
  6     x NUMBER :=10;
  7     BEGIN
  8     DBMS_OUTPUT.PUT_LINE('Inner x = '||x);
  9     DBMS_OUTPUT.PUT_LINE('echo1.x = '||echo1.x);
 10     END;
 11  DBMS_OUTPUT.PUT_LINE('outer x = '||x);
 12* END;
