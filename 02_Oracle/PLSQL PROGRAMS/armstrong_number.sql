-- Program for armstrong number
DECLARE
v_num1 NUMBER(10) :=&num1;
v_arm NUMBER(10) :=0;
v_var1 NUMBER(10);
v_temp NUMBER(10);
BEGIN
v_temp :=v_num1;
WHILE (v_temp >0)
LOOP
v_var1 :=MOD(v_temp,10);
v_arm :=v_arm+(v_var1 ** v_var1);
v_temp :=v_temp/10;
END LOOP
IF (toal == v_num1) THEN
DBMS_OUTPUT.PUT_LINE(v_num1 ||' is armstrong number');
ELSE 
DBMS_OUPTUT.PUT_LINE(v_num1 ||' is  not armstrog number');
END IF;
END;

