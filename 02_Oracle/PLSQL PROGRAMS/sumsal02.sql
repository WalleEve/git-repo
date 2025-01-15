/* Sum of Slary */
DECLARE
v_Total number :=0;
BEGIN
DBMS_OUTPUT.PUT_LINE(RPAD('Sal',10)||RPAD('Total',10));
FOR v_Sal IN Select Sal From Emp
LOOP
v_Total :=v_Total+NVl(v_Sal.Sal,0);
DBMS_OUTPUT.PUT_LINE(RPAD(v_Sal.Sal,10)||RPAD(v_Total,10));
END LOOP;
DBMS_OUTPUT.PUT_LINE('Total Salary is: '||v_Total);
END;
/
