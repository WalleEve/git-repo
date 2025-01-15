-- Concatination operator
DECLARE
  x VARCHAR2(10) := 'suit';
  y VARCHAR2(10) := 'case';
BEGIN
  DBMS_OUTPUT.PUT_LINE(x||y);
END;
/

--The concatination operator ignores null operands 

BEGIN
DBMS_OUTPUT.PUT_LINE('apple'||NULL||NULL||'sauce');
END;
