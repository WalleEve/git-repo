-- Operator PRECEDENCE 
DECLARE
  salary NUMBER :=60000;
  commission NUMBER :=0.10;
BEGIN
-- Division has higher precedence than addition:
  DBMS_OUTPUT.PUT_LINE('5+12/4 = '||TO_CHAR(5+12/4));
  DBMS_OUTPUT.PUT_LINE('12/4+5 = '||TO_CHAR(12/4+5));
-- Parantheses override default operator precedence:
  DBMS_OUTPUT.PUT_LINE('8+6/2= '||TO_CHAR(8+6/2));
  DBMS_OUTPUT.PUT_LINE('(8+6)/2 = '||TO_CHAR((8+6)/2));
-- Most deeply nested operator is evaluated first:
  DBMS_OUTPUT.PUT_LINE('100+(20/5+(7-3)) = '||TO_CHAR(100+(20/5+(7-3))));
-- Parentheses evewn when unnecessary improve readability:

  DBMS_OUTPUT.PUT_LINE('(aslary*0.05)+(commission*0.05)= '||TO_CHAR((salary*0.05)+(commission*0.05)));
  DBMS_OUTPUT.PUT_LINE(' salary*0.05+commission*0.05 = '||TO_CHAR(salary*0.05+commission*0.05));
END;
/
