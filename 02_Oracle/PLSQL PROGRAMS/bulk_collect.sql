-- Bulk collect clause
--Cursor degrades performace because cursor internally uses record by record process.Where as bulk collect clause improves performance because whenever we are using bulk collect clause oracle server selects columns data at a time on storing collection.

--syntax
SELECT * BULK COLLECT INTO collection_name FROM tablename WHERE conditions.
-- This clause is used in executable section of PL/SQL Bolck

DECLARE
   TYPE t1 IS TABLE OF VARCHAR2(20) 
   INDEX BY BINARY_INTEGER;
   v_t1 t1;
BEGIN
   SELECT ename BULK COLLECT INTO v_t1 FROM emp;
   FOR i IN v_t1.FIRST..v_t1.LAST
   LOOP
      DBMS_OUTPUT.PUT_LINE(v_t1(i));
   END LOOP;
END;
/
