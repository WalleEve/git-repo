-- Exception04
DECLARE
v_Num1 NUMBER;
BEGIN
v_num1 :='&Givenum1'+'&givenum2';
DBMS_OUTPUT.PUT_LINE('The Result of the operation is: '||v_num1);
EXCEPTION
WHEN VALUE_ERROR THEN
DBMS_OUTPUT.PUT_LINE('Please check - There is a source of invalid value in your input or operator');
END;
/
