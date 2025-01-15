-- Declaring Same Identifier in Different Units
DECLARE
CREATE PROCEDURE p
IS
x VARCHAR2(2);
BEGIN
x :='a'; --Assign the value a to x
DBMS _OUTPUT.PUT_LINE ('In Procedure p, x= '||x);
END;

CREATE PROCEDURE q
IS
x VARCHAR2(2);
BEGIN
x :='b'; -- Assign the value b to x
DBMS_OUTPUT.PUT_LINE('In Procedure q, x= '||x);
END;


BEGIN
p;
q;
END;
/
