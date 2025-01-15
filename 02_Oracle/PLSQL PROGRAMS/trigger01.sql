--TRIGGER
CREATE OR REPLACE TRIGGER weekebndcheck
AFTER INSERT OR UPDATE OR DELETE
ON Emp
DECLARE
v_Weekday VARCAHR2(10);
BEGIN
v_weekday :=TO_CHAR(SYSDATE,'DY');
IF v_weekday ='SAT'OR v_weekday='SUN' THEN
RAISE_APPLICATION_ERROR(20010,'An illegal Intrusion in to the syatem was detected..');
END IF;
END;
 
