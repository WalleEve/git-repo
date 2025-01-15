-- Trigger example
CREATE OR REPLACE  TRIGGER weekendcheck
AFTER INSERT OR UPDATE OR DELETE
ON Emp
DECLARE
v weekDay VARCHAR2(100);
BEGIN
v_weekDay := TO_CHAR(SYSDATE,'DY');
IF v_weekDay ='SAT' OR v_weekDay='SUN' THNE
RAISE_APPLICATION_ERROR(-20010 , ' An illegal Intrusion into the system was detected');
END IF;
END;
/
