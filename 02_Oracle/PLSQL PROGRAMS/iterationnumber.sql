-- This is an iteration condition . enter a number from keyboard if it is not zero then print this is a natural number else print this is wrong number 
DECLERE
v_num NUMBER :=num;
BEGIN
FI v_num >0 THEN
DBMS_OUTPUT.PUT_LINE(v_num||' This is a natural number');
ELSE
DBMS_OUTPUT.PUT_LINE('This is wrong number');
EXIT WHEN v_num >100;
END IF;
END;

