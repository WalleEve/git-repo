-- Improving Readability with parantheses
DECLARE
a INTEGER :=2**2*3**2;
b INTEGER :=(2**2)*(3**2);
BEGIN
DBMS_OUTPUT.PUT_LINE(' a= '||TO_CHAR(a));
DBMS_OUTPUT.PUT_LINE(' b= '||TO_CHAR(b));
END;
/
