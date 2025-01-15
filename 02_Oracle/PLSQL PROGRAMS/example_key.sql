-- Example
DECLARE
 TYPE t1 IS TABLE OF VARChAR2(10)
 INDEX BY BINARY_INTEGER;
 v_t1 t1;
 x VARCHAR2(10);
BEGIN
 v_t1 ('a') :='SAYED';
 v_t1 ('b') :='SABEEHA';
 v_t1 ('c') :='ZAARA';
 v_t1 ('d') :='MILEY';
 x:='a';
LOOP
 DBMS_OUTPUT.PUT_LINE(v_t1(x));
 x :=v_t1.NEXT(x);
 EXIT WHEN x IS NULL;
END LOOP;
END;
