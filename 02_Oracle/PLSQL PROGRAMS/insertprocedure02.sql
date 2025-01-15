--write a pl/sql stored procedure to insert a record into result table by using in parameter
CREATE OR REPLACE PROCEDURE insertprocedure(p_number IN NUMBER,p_msg IN VARCHAR2)
IS
BEGIN
IF MOD(p_number,2)=0 AND p_msg='EVEN' THEN
INSERT INTO result values(p_number,p_msg);
DBMS_OUTPUT.PUT_LINE('Transaction Successful.');
ELSIF MOD(p_number,2)=0 AND p_msg='ODD' THEN
DBMS_OUTPUT.PUT_LINE('Transaction canceled..);
DBMS_OUTPUT.PUT_LINE('PLease check the msg The Number is an EVEN number You have entered ODD');
ELSIF MOD(p_number,2)!=0 AND p_msg='ODD'
INSERT INTO result VALUES(p_number,p_msg);
DBMS_OUTPUT.PUT_LINE(' Transaction successful.');
ELSIF MOD(p_number,2) !=0 AND p_msg='EVEN' THEN
DBMS_OUTPUT.PUT_LINE('Transaction canceled..');
DBMS_OUTPUT.PUT_LINE('Please check the msg The number is ODD and you have entered EVEN');
IF p_number=0 THEN
DBMS_OUTPUT.PUT_LINE('Transaction canceled..');
DBMS_OUTPUT.PUT_LINE('Zero Value not allowed');
END IF;
EXCEPTION 
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE('Transaction error!');
END;
