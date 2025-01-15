/*Write pl/sql program to display even no of records from emp table by using rowcount attribute.*/
DECLARE
CURSOR EvenCursor IS Select Ename,Sal From Emp;
v_ename varchar2(10);
v_sal number(10);
BEGIN
open EvenCursor;
LOOP
FETCH EvenCursor INTO v_ename,v_sal;
EXIT WHEN EvenCursor%NOTFOUND;
IF MOD(EnenCursoe%Rowcount,2)=0 THEN
DBMS_OUTPUT.PUT_LINE(v_ename||' '||v_sal);
END IF;
END LOOP;
Close EvenCursor;
END;
/
