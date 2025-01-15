--Program for reverse a number like 25 to 52

DECLARE
v_num1 number(10) :=&num1;
v_rev number :=0;
BEGIN
WHILE (v_num1>0)
LOOP
v_rev :=v_rev*10+MOD(v_num1,10);
v_num1 :=v_num1/10;
END LOOP;
DBMS_OUTPUT.PUT_LINE(v_rev);
END;

-- It's output can be like a triangle 
DECLARE
v_num1 NUMBER(10) :=&num1;
v_rev number :=0;
BEGIN
WHILE (v_num1>0)
LOOP
v_rev :=v_rev*10 + MOD(v_num1,10);
DBMS_OUTPUT.PUT_LINE(v_rev);
v_num1 :=v_num1/10;
END LOOP;
END;

-- If the num1 value is negative then 

DECLARE
v_num1 number(10) :=&num1;
v_rev number :=0;
BEGIN
--This section for positive number(v_num1)..
WHILE (v_num1>0)
LOOP
v_rev :=v_rev*10+MOD(v_num1,10);
v_num1 :=v_num1/10;
DBMS_OUTPUT.PUT_LINE(v_rev);
END LOOP;
-- This section for nagative number(-v_num1)..

WHILE (v_num1 <0)
LOOP
v_rev :=(v_rev*10) - MOD(v_num1,10);
v_num1 :=v_num1/10;
DBMS_OUTPUT.PUT_LINE(v_rev);
END LOOP;
END;



