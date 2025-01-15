-- Program for factorial of a number
DECLARE
v_num1 NUMBER(10) :=&num1;
v_fact NUMBER :=1;
BEGIN
FOR i IN REVERSE 1..v_num1
LOOP
v_fact :=v_fact*i;
END LOOP;
DBMS_OUTPUT.PUT_LINE(v_fact);
END;

