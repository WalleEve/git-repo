-- Handled or unhandled exception in procedure

-- inner procedure
CREATE OR REPLACE PROCEDURE TestProcedure01 ( num1 IN NUMBER,num2 IN NUMBER)
IS
BEGIN
DBMS_OUTPUT.PUT_LINE(num1/num2);
EXCEPTION
WHEN zero_divide THEN
DBMS_OUTPUT.PUT_LINE(' num2 cannot be zero');
END;
/

-- outer procedure
CREATE OR REPLACE PROCEDURE TestProcedure02 
IS
BEGIN
TestProcedure(5,0);
EXCEPTION
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE('Please check the program..');
ENd;
/
