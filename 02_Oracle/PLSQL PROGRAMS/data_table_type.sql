-- write a pl/sql program which stores next 10 days into index by table and also display content of index by table 
DECLARE
   TYPE dtable  IS TABLE OF date
   INDEX BY BINARY_INTEGER;
   v_dtable dtable;
BEGIN
   FOR MyIndex 1..10
   LOOP
     v_dtable(MyIndex) :=sysdate+MyIndex;
     --SELECT sysdate INTO v_dtable(MyIndex) From Dual; 
   END LOOP;
   FOR MyIndex IN v_dtable.FIRST..v_dtable.LAST
   LOOP
     DBMS_OUPTUT.PUT_LINE(v_dtable(MyIndex));
   END LOOP;
END;


-- DECLARE
  2  v_today DATE;
  3  v_nextday DATE;
  4  BEGIN
  5  Select SYSDATE INTO v_today From Dual;
  6  FOR i IN 1..5
  7  LOOP
  8  v_nextday :=v_today; --It can be like (v_nextday :=v_today+i)
  9  v_today :=v_nextday+1;
 10  DBMS_OUTPUT.PUT_LINE('next day  is: '||v_nextday);
 11  END LOOP;
 12* END;
