-- Controling Evaluation order with parentheses
DECLARE
a INTEGER :=1+2**2;
b INTEGER :=(1+2)**2;
BEGIN
DBMS_OUTPUT.PUT_LINE(' a= '||TO_CHAR(a));
DBMS_PUTPUT.PUT_LINE(' b= '||TO_CHAR(b));
END;
/
