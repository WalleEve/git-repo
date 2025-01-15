-- Expression With nested Parentheses
DECLARE
a INTEGER :=((1+2)*(3+7))/7;
BEGIN
DBMS_OUTPUT.PUT_LINE('a = '||TO_CHAR(a));
END;
/
