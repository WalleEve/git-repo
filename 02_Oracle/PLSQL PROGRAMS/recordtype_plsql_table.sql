-- Record datatype (%rowtype) using in pl/sql table
DECLARE
 TYPE emptable IS TABLE OF emp%ROWTYPE
 INDEX BY BINARY_INTEGER;
 v_emptable emptable;
 x NUMBER(10);
BEGIN
 SELECT * BULK COLLECT  INTO v_emptable FROM emp;
 x :=1;
 LOOP
  DBMS_OUTPUT.PUT_LINE(v_emptable(x).ename||' '||v_emptable(x).Job||v_emptable(x).sal);
  x :=v_emptable.NEXT(x)
  EXIT WHEN x IS NULL;
 END LOOP;
END;

-- example 

DECLARE
 TYPE emptable IS TABLE OF emp%ROWTYPE
 INDEX BY BINARY_INTEGER;
 v_emptable emptable;
BEGIN
 SELECT * BULK COLLECT INTO v_emptable FROM emp;
 
FOR i IN v_emptable.FIRST..v_emptable.LAST
 LOOP
   DBMS_OUTPUT.PUT_LINE(RPAD(v_emptable(i).Ename,10)||' '||RPAD(v_emptable(i).Job,10)||RPAD(v_emptable(i).sal,10));
 END LOOP;
END;
  
