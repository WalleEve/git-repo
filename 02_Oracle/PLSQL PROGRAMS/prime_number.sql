--Program for prime number
DECLARE
v_num NUMBER :=&num;
BEGIN
FOR i IN 1..v_num
LOOP
IF i IN(3,5,7) THEN
DBMS_OUTPUT.PUT_LINE('These are the known prime number: '||i);
END IF;
IF i NOT IN (3,5,7) THEN
IF MOD(i,3)=0 OR MOD(i,6)=0 OR MOD(i,9)=0 THEN
NULL;
ELSIF MOD(i,2)=0 OR MOD(i,4)=0 OR MOD(i,8)=0 THEN
NULL:
ELSIF MOD(i,5)=0 OR MOD(i,10)=0 THEN
NULL;
ELSIF MOD(i,7)=0 THEN
NULL;
ELSE
DBMS_OUPTUT.PUT_LINE('The prime number is: '||i);
END IF;
END IF;
END LOOP;
END;
