DECLARE 
v_errorCode NUMBER(6);
v_errorMessage varchar2(100);
BEGIN
INSERT INTO acer_achool values(&srno,'&edu_type',&duration,&seat);
EXCEPTION
WHEN OTHERS THEN
v_errCode :=SQLCODE;
v_errorMessage :=SQLERRM;
DBMS_OUTPUT.PUT_LINE('The error code traced is: '||v_errCode);
DBMS_OUTPUT.PUT_LINE('The error message traced is: '||v_errorMessage);
END;
/
