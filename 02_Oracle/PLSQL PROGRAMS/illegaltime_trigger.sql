-- Creating Trigger for control the SQL DML statements to modify the tables on Time line

CREATE OR REPLACE TRIGGER illegaltime
BEFORE INSERT OR UPDATE OR DELETE
ON reg
DECLARE
v_time NUMBER;
BEGIN
v_time :=TO_CHAR(SYSDATE,'HH24');
IF v_time NOT BETWEEN 10 AND 17 
THEN
RAISE_APPLICATION_ERROR (-20011,'Illegal Intrusion Not besiness hours...');
END IF;
END;
/
