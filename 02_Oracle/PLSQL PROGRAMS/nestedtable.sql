-- Write a pl/sql program which is used to transfer all employee name from emp table into nested table and also display ccontent from nested table.

DECLARE
TYPE EmpTable IS TABLE OF VARCHAR2(10)
INDEX BY BINARY_INTEGER;
v_Emptable Emptable :=Emptable();
CURSOR EmpCursor IS Select Ename From emp;
--v_num1 NUMBER(10) :=1;
BEGIN
FOR v_Ename IN Empcursor
LOOP
v_Emptable.extend;
v_Emptable(MyIndex) :=v_Ename.Ename;
MyIndex :=MyIndex+1;
END LOOP;
FOR MyIndex IN v_EmpTable.FIRST..v_EmpTable.LAST
LOOP
DBMS_OUTPUT.PUT_LINE(v_EmpTable(v_Ename));
END LOOP;
END;
/
