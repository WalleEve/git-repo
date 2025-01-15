/* This is use as cursor without declaring the cursor we can declare a cursor in the for loop directly */
BEGIN
FOR v_Emp IN (Select * from Emp)
LOOP
DBMS_OUTPUT.PUT_LINE(v_EMp.Ename||' '||v_Emp.Job||' '||v_Emp.Sal);
END LOOP;
END;
/
