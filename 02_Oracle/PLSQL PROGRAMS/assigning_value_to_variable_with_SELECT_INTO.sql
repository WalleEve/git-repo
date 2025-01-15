-- uses a SELECT INTO statement to assign to the variable bonus the value that is 10% of the salary of the employee whose employee_id is 7839.

--Assigning values to variable with SELECT INTO statement

DECLARE
  bonus NUMBER(8,2);
BEGIN
  SELECT sal*0.10 INTO bonus
  FROM Emp         -- here i am using emp table 
  WHERE empno=7839;
  
  DBMS_OUTPUT.PUT_LINE('bonus = '||TO_CHAR(bonus));
END;
/

 
