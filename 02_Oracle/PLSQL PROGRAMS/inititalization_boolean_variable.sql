-- initialization the BOOLEAN variable done to NULL by default assigns it the literal value FALSE compares it to the literal value TRUE and assigns it the value of a BOOLEAN expression.
--Assigning value to BOOLEAN variable
DECLARE
  done BOOLEAN; --Initial value is NULL  by default
  counter NUMBER :=0;
BEGIN
  done :=FALSE; --assign literal value
WHILE done != TRUE  --compare to literal value 
LOOP
  counter :=counter+1;
  done :=(counter >500);  -- Assign value of BOOLEAN expression
  DBMS_OUTPUT.PUT_LINE(done);
END LOOP;
END;
/



  1  DECLARE
  2  v_ename VARCHAR2(10);
  3  v_empno NUMBER :=&empno;
  4  v_sal NUMBER;
  5  v_status BOOLEAN :=&conformation;
  6  BEGIN
  7  IF v_status =TRUE THEN
  8  SELECT ename,sal INTO v_ename,v_sal FROM emp WHERE empno=v_empno;
  9  DBMS_OUTPUT.PUT_LINE(v_ename||' '||v_sal);
 10  ELSIF v_status =FALSE THEN
 11  DBMS_OUTPUT.PUT_LINE('Please check the status..');
 12  END IF;
 13* ENd;
