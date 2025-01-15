/*sum of Sal */
Declare
cursor EmpCursor IS Select Sal From Emp;
v_Sal Emp.Sal%type;
v_Total number :=0;
BEGIn
DBMS_OUTPUT.PUT_LINE(RPAD('Sal',10)||RPAD('Total_Sal',10));
OPEN EmpCursor;
LOOP
FETCH EmpCursor INTO v_Sal;
EXIT WHEN EmpCursor%NOTFOUND;
v_Total :=v_Total+NVL(Sal,0);
DBMS_OUPTUT.PUT_LINE(RPAD(v_Sal,10)||RPAD(v_Total,10));
END LOOP;
DBMS_OUTPUT.PUT_LINE('Total Salary is: '||v_Total);
END;
/
